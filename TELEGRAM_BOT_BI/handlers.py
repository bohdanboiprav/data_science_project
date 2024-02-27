import asyncio
import logging
import datetime
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart, Command, ExceptionMessageFilter
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
# from aiogram.types import MenuButtonCommands
from aiogram.utils.markdown import hbold
from magic_filter import F

from conf.config import settings
# from aiogram.utils.callback_data import CallbackData
# from keyboards.stock import product_markup

from database.db import async_select_one, async_select_all

dp = Dispatcher()
bot = Bot(token=settings.BOT_TOKEN)


class StockCallback(CallbackData, prefix="stock_tracker"):
    company: str
    stock_price: float
    day_range: str
    pe_ratio: float
    week_range: str


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command("stock_tracker"))
async def command_start_handler(message: Message) -> None:
    query = """SELECT *
                FROM stock_data
                WHERE DATE_TRUNC('minutes', report_timestamp) = (SELECT MAX(DATE_TRUNC('minutes', report_timestamp)) FROM stock_data)
            """
    stock_data = await async_select_all(query)
    await message.answer("""Hi!\nSend me any type of message to start.\nOr just send /webview""",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [InlineKeyboardButton(text=x[2],
                                                       callback_data=StockCallback(company=x[2],
                                                                                   stock_price=x[3], day_range=x[4],
                                                                                   pe_ratio=x[5],
                                                                                   week_range=x[6]).pack()
                                                       ) for x in stock_data]]))


@dp.message(Command("other_tracker"))
async def echo_handler(message: types.Message) -> None:
    query = """SELECT
                report_date,
                cases - LAG(cases, 1, 0) OVER (ORDER BY report_date) AS daily_cases,
                deaths - LAG(deaths, 1, 0) OVER (ORDER BY report_date) AS daily_deaths,
                recovered - LAG(recovered, 1, 0) OVER (ORDER BY report_date) AS daily_recovered
                FROM covid_cases
                ORDER BY report_date desc
                limit 1"""
    cases = await async_select_one(query)
    if not cases:
        await message.answer("No data found")
    reply_string = f"COVID-19 Data on {cases[0]}\n🦠Cases: {cases[1]}\n☠️Deaths: {cases[2]}\n🏥Recovered: {cases[3]}"
    await message.answer(reply_string)


@dp.callback_query(StockCallback.filter())
async def language_callback(query: CallbackQuery, callback_data: StockCallback):
    await query.message.edit_text(
        text=f"{callback_data.company}: {callback_data.stock_price}\n📈Day Range: {callback_data.day_range}\n📊PE Ratio: {callback_data.pe_ratio}\n📉52 Week Range: {callback_data.week_range}")


# , reply_markup=None

@dp.message()
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"I'm not sure what you meant.\n\nPlease check the bot's description or use the '/help' command to see its available functionalities and commands")

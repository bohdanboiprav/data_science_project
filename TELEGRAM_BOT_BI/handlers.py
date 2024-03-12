import asyncio
import logging
import datetime
import sys
from random import randint

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart, Command, ExceptionMessageFilter
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
# from aiogram.types import MenuButtonCommands
from aiogram.utils.markdown import hbold
from magic_filter import F

from conf.config import settings
# from aiogram.utils.callback_data import CallbackData
# from keyboards.stock import product_markup

from database.db import async_select_one, async_select_all
from keyboards.other import get_keyboard_other, OtherCallback, get_keyboard_other_return, OtherCallbackReturn
from keyboards.stock import get_keyboard_stock, get_keyboard_stock_return, StockCallback, StockCallbackReturn

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command("stock_tracker"))
async def command_start_handler(message: Message) -> None:
    query = """SELECT *
                FROM stock_data
                WHERE DATE_TRUNC('minutes', report_timestamp) = (SELECT MAX(DATE_TRUNC('minutes', report_timestamp)) FROM stock_data)
            """
    global stock_data
    stock_data = await async_select_all(query)

    await message.answer("""Use the buttons below to check the stock prices.""",
                         reply_markup=get_keyboard_stock([x[2:] for x in stock_data]))


@dp.callback_query(StockCallback.filter())
async def stock_callback(query: CallbackQuery, callback_data: StockCallback):
    await query.message.edit_text(
        f"{callback_data.company}: {callback_data.stock_price}\n📈Day Range: {callback_data.day_range}\n📊PE Ratio: {callback_data.pe_ratio}\n📉52 Week Range: {callback_data.week_range}",
        reply_markup=get_keyboard_stock_return())


@dp.callback_query(StockCallbackReturn.filter())
async def stock_callback_return(query: CallbackQuery, callback_data: StockCallbackReturn):
    if stock_data:
        await query.message.edit_text("""Use the buttons below to check the stock prices.""",
                                      reply_markup=get_keyboard_stock([x[2:] for x in stock_data]))
    else:
        await query.message.edit_text("No stock data found")


@dp.message(Command("other_trackers"))
async def other_handler(message: types.Message) -> None:
    await message.answer("Please select want information you want to get", reply_markup=get_keyboard_other())


@dp.callback_query(OtherCallback.filter())
async def other_callback(query: CallbackQuery, callback_data: OtherCallback):
    if callback_data.action == "covid_cases":
        sql_query = """SELECT
                    report_date,
                    cases - LAG(cases, 1, 0) OVER (ORDER BY report_date) AS daily_cases,
                    deaths - LAG(deaths, 1, 0) OVER (ORDER BY report_date) AS daily_deaths,
                    recovered - LAG(recovered, 1, 0) OVER (ORDER BY report_date) AS daily_recovered
                    FROM covid_cases
                    ORDER BY report_date desc
                    limit 1"""
        cases = await async_select_one(sql_query)
        reply_string = f"COVID-19 Data on {cases[0]}\n🦠Cases: {cases[1]}\n☠️Deaths: {cases[2]}\n🏥Recovered: {cases[3]}"
        await query.message.edit_text(reply_string, reply_markup=get_keyboard_other_return())


@dp.callback_query(OtherCallbackReturn.filter())
async def stock_callback_return(query: CallbackQuery, callback_data: OtherCallbackReturn):
    await query.message.edit_text("Please select want information you want to get", reply_markup=get_keyboard_other())


@dp.message(Command("help"))
async def other_handler(message: types.Message) -> None:
    await message.answer("""Here is the list of commands you can use:\n\n 
    /start - To start the bot\n
    /stock_tracker - To get the stock prices\n
    /other_trackers - To get the other trackers list\n
    /help - To get the list of commands\n
    """)


@dp.message()
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"I'm not sure what you meant.\n\nPlease check the bot's description or use the '/help' command to see its available functionalities and commands")

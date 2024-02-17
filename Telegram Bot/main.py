import requests
from bs4 import BeautifulSoup
from config import settings

#covid cases
data_request = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(data_request.content, 'html.parser')
data_out = soup.find_all('div', class_='maincounter-number')
data_out = [data_out.find('span').text.strip() for data_out in data_out]

text = f"🦠Cases: {data_out[0]}\n☠️Deaths: {data_out[1]}\n🏥Recovered: {data_out[2]}"
print(data_out)
requests.post(f"https://api.telegram.org/bot{settings.TELEGRAM_API_KEY}/sendMessage?text={text}&chat_id=997060203")



# tsla stock
data_request = requests.get('https://www.marketwatch.com/investing/stock/tsla')
soup = BeautifulSoup(data_request.content, 'html.parser')

stock_price = soup.find('bg-quote', class_='value')
day_range = soup.find('span', class_='range kv__primary')
pe_ratio = soup.find('li', class_='kv__item')
week_range = soup.find('span', class_='range kv__item')

text = f"⚡TSLA: {stock_price}\n📈Day Range: {day_range}\n📊PE Ratio: {pe_ratio}\n📉52 Week Range: {week_range}"

requests.post(f"https://api.telegram.org/bot{settings.TELEGRAM_API_KEY}/sendMessage?text={text}&chat_id=997060203")

print(stock_price, day_range, pe_ratio, week_range)


# amzn stock
data_request = requests.get('https://www.marketwatch.com/investing/stock/amzn')
soup = BeautifulSoup(data_request.content, 'html.parser')

stock_price = soup.find('bg-quote', class_='value')
day_range = soup.find('span', class_='range kv__primary')
pe_ratio = soup.find('li', class_='kv__item')
week_range = soup.find('span', class_='range kv__item')

text = f"📦AMZN: {stock_price}\n📈Day Range: {day_range}\n📊PE Ratio: {pe_ratio}\n📉52 Week Range: {week_range}"

requests.post(f"https://api.telegram.org/bot{settings.TELEGRAM_API_KEY}/sendMessage?text={text}&chat_id=997060203")

print(stock_price, day_range, pe_ratio, week_range)


# google stock
data_request = requests.get('https://www.marketwatch.com/investing/stock/googl')
soup = BeautifulSoup(data_request.content, 'html.parser')

stock_price = soup.find('bg-quote', class_='value')
day_range = soup.find('span', class_='range kv__primary')
pe_ratio = soup.find('li', class_='kv__item')
week_range = soup.find('span', class_='range kv__item')

text = f"🔍GOOGL: {stock_price}\n📈Day Range: {day_range}\n📊PE Ratio: {pe_ratio}\n📉52 Week Range: {week_range}"

requests.post(f"https://api.telegram.org/bot{settings.TELEGRAM_API_KEY}/sendMessage?text={text}&chat_id=997060203")

print(stock_price, day_range, pe_ratio, week_range)


# aapl stock
data_request = requests.get('https://www.marketwatch.com/investing/stock/aapl')
soup = BeautifulSoup(data_request.content, 'html.parser')

stock_price = soup.find('bg-quote', class_='value')
day_range = soup.find('span', class_='range kv__primary')
pe_ratio = soup.find('li', class_='kv__item')
week_range = soup.find('span', class_='range kv__item')

text = f"🍏AAPL: {stock_price}\n📈Day Range: {day_range}\n📊PE Ratio: {pe_ratio}\n📉52 Week Range: {week_range}"

requests.post(f"https://api.telegram.org/bot{settings.TELEGRAM_API_KEY}/sendMessage?text={text}&chat_id=997060203")

print(stock_price, day_range, pe_ratio, week_range)


# msft stock
data_request = requests.get('https://www.marketwatch.com/investing/stock/msft')
soup = BeautifulSoup(data_request.content, 'html.parser')

stock_price = soup.find('bg-quote', class_='value')
day_range = soup.find('span', class_='range kv__primary')
pe_ratio = soup.find('li', class_='kv__item')
week_range = soup.find('span', class_='range kv__item')

text = f"💻MSFT: {stock_price}\n📈Day Range: {day_range}\n📊PE Ratio: {pe_ratio}\n📉52 Week Range: {week_range}"

requests.post(f"https://api.telegram.org/bot{settings.TELEGRAM_API_KEY}/sendMessage?text={text}&chat_id=997060203")

print(stock_price, day_range, pe_ratio, week_range)


import requests
from bs4 import BeautifulSoup
from config import settings

# # Covid cases
# data_request = requests.get('https://www.worldometers.info/coronavirus/')
# soup = BeautifulSoup(data_request.content, 'html.parser')
# data_out = soup.find_all('div', class_='maincounter-number')
# data_out = [data_out.find('span').text.strip() for data_out in data_out]
#
# text = f"🦠Cases: {data_out[0]}\n☠️Deaths: {data_out[1]}\n🏥Recovered: {data_out[2]}"
# requests.post(f"https://api.telegram.org/bot{settings.TELEGRAM_API_KEY}/sendMessage?text={text}&chat_id=997060203")
#
# mapping_dict = {
#     'TSLA': 'https://www.marketwatch.com/investing/stock/tsla',
#     'AMZN': 'https://www.marketwatch.com/investing/stock/amzn',
#     'GOOGL': 'https://www.marketwatch.com/investing/stock/googl',
#     'AAPL': 'https://www.marketwatch.com/investing/stock/aapl',
#     'MSFT': 'https://www.marketwatch.com/investing/stock/msft'
# }


def get_stock_price(stock_name: str, stock_link: str) -> None:
    data_request = requests.get(stock_link)
    soup = BeautifulSoup(data_request.content, 'html.parser')
    stock_price = soup.find('h2', class_='intraday__price').find('bg-quote', class_='value').text.strip()
    day_range = soup.find_all('span', class_='primary')[7].text.strip()
    pe_ratio = soup.find_all('span', class_='primary')[14].text.strip()
    week_range = soup.find_all('span', class_='primary')[8].text.strip()
    text = f"{stock_name}: {stock_price}\n📈Day Range: {day_range}\n📊PE Ratio: {pe_ratio}\n📉52 Week Range: {week_range}"

    requests.post(f"https://api.telegram.org/bot{settings.TELEGRAM_API_KEY}/sendMessage?text={text}&chat_id=997060203")


# get_stock_price('⚡TSLA', mapping_dict['TSLA'])
# get_stock_price('📦AMZN', mapping_dict['AMZN'])
# get_stock_price('🔍GOOGL', mapping_dict['GOOGL'])
# get_stock_price('🍏AAPL', mapping_dict['AAPL'])
# get_stock_price('💻MSFT', mapping_dict['MSFT'])

#crypto price code

mapping_dict = {
    'BTCUSD': 'https://finance.yahoo.com/quote/BTC-USD',
    'ETHUSD': 'https://finance.yahoo.com/quote/ETH-USD',
    'XRPUSD': 'https://finance.yahoo.com/quote/XRP-USD',
    'SOLUSD': 'https://finance.yahoo.com/quote/SOL-USD',
    'DOGEUSD': 'https://finance.yahoo.com/quote/DOGE-USD'
}


def get_crypto_price(crypto_name: str, crypto_link: str) -> None:
    data_request = requests.get(crypto_link)
    soup = BeautifulSoup(data_request.content, 'html.parser')
    crypto_price = soup.find('div', class_='D(ib) Va(m) Maw(65%) Ov(h)').find("fin-streamer", class_="Fw(b) Fz(36px) Mb(-4px) D(ib)").text.strip()
    day_range = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[2].text.strip()
    week_range = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[3].text.strip()
    price_increase = soup.find('div', class_='D(ib) Mend(20px)').find("fin-streamer", class_="Fw(500) Pstart(8px) Fz(24px)").text.strip()
    text = f"{crypto_name}: {crypto_price}\n⚖️Day Range: {day_range}\n📊Week Range: {week_range}\n📈Price Increase: {price_increase}"
    requests.post(f"https://api.telegram.org/bot{settings.TELEGRAM_API_KEY}/sendMessage?text={text}&chat_id=997060203")


get_crypto_price('🪙BTC', mapping_dict['BTCUSD'])
get_crypto_price('🔷ETH', mapping_dict['ETHUSD'])
get_crypto_price('🌊XRP', mapping_dict['XRPUSD'])
get_crypto_price('☀️SOL', mapping_dict['SOLUSD'])
get_crypto_price('🐕DOGE', mapping_dict['DOGEUSD'])


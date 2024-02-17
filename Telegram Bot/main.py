import requests
from bs4 import BeautifulSoup
from config import settings

# Covid cases
data_request = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(data_request.content, 'html.parser')
data_out = soup.find_all('div', class_='maincounter-number')
data_out = [data_out.find('span').text.strip() for data_out in data_out]

text = f"🦠Cases: {data_out[0]}\n☠️Deaths: {data_out[1]}\n🏥Recovered: {data_out[2]}"
print(data_out)


# requests.post(f"https://api.telegram.org/bot{settings.TELEGRAM_API_KEY}/sendMessage?text={text}&chat_id=997060203")

mapping_dict = {
    'TSLA': 'https://www.marketwatch.com/investing/stock/tsla',
    'AMZN': 'https://www.marketwatch.com/investing/stock/amzn',
    'GOOGL': 'https://www.marketwatch.com/investing/stock/googl',
    'AAPL': 'https://www.marketwatch.com/investing/stock/aapl',
    'MSFT': 'https://www.marketwatch.com/investing/stock/msft'
}


def get_stock_price(stock_name: str, stock_link: str) -> None:
    data_request = requests.get(stock_link)
    soup = BeautifulSoup(data_request.content, 'html.parser')
    stock_price = soup.find('h2', class_='intraday__price').find('bg-quote', class_='value').text.strip()
    day_range = soup.find_all('span', class_='primary')[7].text.strip()
    pe_ratio = soup.find_all('span', class_='primary')[14].text.strip()
    week_range = soup.find_all('span', class_='primary')[8].text.strip()
    text = f"{stock_name}: {stock_price}\n📈Day Range: {day_range}\n📊PE Ratio: {pe_ratio}\n📉52 Week Range: {week_range}"

    requests.post(f"https://api.telegram.org/bot{settings.TELEGRAM_API_KEY}/sendMessage?text={text}&chat_id=997060203")


get_stock_price('⚡TSLA', mapping_dict['TSLA'])
get_stock_price('📦AMZN', mapping_dict['AMZN'])
get_stock_price('🔍GOOGL', mapping_dict['GOOGL'])
get_stock_price('🍏AAPL', mapping_dict['AAPL'])
get_stock_price('💻MSFT', mapping_dict['MSFT'])

import requests
from bs4 import BeautifulSoup
from config import settings


def covid_cases_data():
    data_request = requests.get('https://www.worldometers.info/coronavirus/')
    soup = BeautifulSoup(data_request.content, 'html.parser')
    data_out = soup.find_all('div', class_='maincounter-number')
    data_out = [data_out.find('span').text.strip() for data_out in data_out]
    return f"🦠Cases: {data_out[0]}\n☠️Deaths: {data_out[1]}\n🏥Recovered: {data_out[2]}"


stock_mapping_dict = {
    'TSLA': 'https://www.marketwatch.com/investing/stock/tsla',
    'AMZN': 'https://www.marketwatch.com/investing/stock/amzn',
    'GOOGL': 'https://www.marketwatch.com/investing/stock/googl',
    'AAPL': 'https://www.marketwatch.com/investing/stock/aapl',
    'MSFT': 'https://www.marketwatch.com/investing/stock/msft'
}


def get_stock_price(stock_name: str, stock_link: str):
    data_request = requests.get(stock_link)
    soup = BeautifulSoup(data_request.content, 'html.parser')
    stock_price = soup.find('h2', class_='intraday__price').find('bg-quote', class_='value').text.strip()
    day_range = soup.find_all('span', class_='primary')[7].text.strip()
    pe_ratio = soup.find_all('span', class_='primary')[14].text.strip()
    week_range = soup.find_all('span', class_='primary')[8].text.strip()
    return f"{stock_name}: {stock_price}\n📈Day Range: {day_range}\n📊PE Ratio: {pe_ratio}\n📉52 Week Range: {week_range}"


mapped_services = {
    'Covid': covid_cases_data(),
    'Stock TSLA': get_stock_price('⚡TSLA', stock_mapping_dict['TSLA']),
    'Stock AMZN': get_stock_price('📦AMZN', stock_mapping_dict['AMZN']),
    'Stock GOOGL': get_stock_price('🔍GOOGL', stock_mapping_dict['GOOGL']),
    'Stock AAPL': get_stock_price('🍏AAPL', stock_mapping_dict['AAPL']),
}


def lambda_handler(event, context):
    chat_id = json.loads(event['body'])
    chat_id = chat_id['message']['chat']['id']
    service_type = chat_id['message']['text']
    text = mapped_services[service_type]
    requests.post(
        f"https://api.telegram.org/bot6777180102:AAF1TyJw-PfVunfKiIlckiY6v911NV44mfQ/sendMessage?text={text}&chat_id={chat_id}")
    return {
        'statusCode': 200,
        'body': json.dumps('Done')
    }

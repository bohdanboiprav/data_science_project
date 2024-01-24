import requests
from bs4 import BeautifulSoup

from config import settings

data_request = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(data_request.content, 'html.parser')
data_out = soup.find_all('div', class_='maincounter-number')
data_out = [data_out.find('span').text.strip() for data_out in data_out]

text = f"🦠Cases: {data_out[0]}\n☠️Deaths: {data_out[1]}\n🏥Recovered: {data_out[2]}"
requests.post(f"https://api.telegram.org/bot{settings.KEY}/sendMessage?text={text}&chat_id=997060203")
print(data_out)

import requests
from bs4 import BeautifulSoup
import fake_useragent


user = fake_useragent.UserAgent().random

session = requests.Session()
auth_link = 'https://br-analytics.ru/account/login_check'
data1 = {
	"_username": "kibyakov98@mail.ru",
	"_password": "Durosa_159357",
	"_remember_me": "on"
}

data2 = {
	"type": "messages",
	"ext": "csv",
	"themeId": "12505867",
	"reportType": "messages",
	"tsf": "1681160400",
	"tst": "1681505999",
	"sort": "time_create"
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'
}
# https://br-analytics.ru/ajax/export/?tsf=1681160400&tst=1681505999


response_page = session.post(auth_link, data=data1, headers=header)


# def get_export(url):
#     
#     response_export = session.post(url, headers=header, data=data2)
#     return response_page, response_export

def get_html(url, params=None):
    r = session.get(url, params=params, headers=header)
    
    return r.content

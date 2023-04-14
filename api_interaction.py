from pprint import pprint
import requests
import db_interaction as db
from models import Date, Project, Source
from datetime import datetime as dt
from config import API_TOKEN
from bs4 import BeautifulSoup

URL = r'https://stat-api.br-analytics.ru/v1/statistic/'

theme_id = '12505867'

date_from = dt.strptime(r'2022-12-04 00:00:00', r'%Y-%m-%d %H:%M:%S')
date_to = dt.now()

# project = Project(
#         theme_id=theme_id,
#         name='Peptid PRO',
#     )

# db.add_to_db(project)

params = {
    'themeId': theme_id,
    'token': API_TOKEN,
    'timeFrom': int(date_from.timestamp()),
    'timeTo': int(date_to.timestamp()),
    'params[size]': 999999,
    'filter[fm][1]': 'on',
}

class API:
    def __init__(self, url: str) -> None:
        self.url = url

    def get(self, url:str, params: dict = params):
        content = []
        response = requests.get(url=self.url + url, params=params)
        content.append(response.json())
        return content
        

api = API(url=URL)


def get_page():
    response = requests.get('https://br-analytics.ru/report/12505867?tsf=1681160400&tst=1681505999&page=1')
    soup = BeautifulSoup(response.text, 'lxml')
    pprint(soup)



# def get_authors():
#     data = api.get(url='/authorsstat/')
#     pprint(data)

# def get_tophubs():
#     data = api.get_tophubs(params=params)

#     for s in data[0]['data']['top_hubs']:
#         source = Source(
#             name=s['name'],
#             num_of_msgs=s['msgs'],
#             percent=s['percent'],
#             project_id=project.id,
#             project_sources=project,
#         )
#         db.add_to_db(source)
#         for d, content in s['histogram'].items():
#             date = Date(
#                 source_id=source.id,
#                 date=dt.utcfromtimestamp(int(d)),
#                 num_of_msgs=content['msgs'],
#                 tone_neutral=content['tone']['neutral'],
#                 tone_positive=content['tone']['positive'],
#                 tone_negative=content['tone']['negative'],
#                 source_dates = source,
#             )
#             db.add_to_db(date)
#     print('Done')

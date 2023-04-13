from pprint import pprint
import requests
import time
from config import API_TOKEN
from datetime import datetime as dt
from models import Project, Source
import db_interaction as db
# from pprint import pprint

URL = r'https://stat-api.br-analytics.ru/v1/statistic/'


class API:
    def __init__(self, url: str) -> None:
        self.url = url
        
    def get(self, params: dict = None):
        content = []
        response = requests.get(url=self.url, params=params)
        content.append(response.json())
        return content


if __name__ == '__main__':
    while True: 

        date_from = dt.strptime(r'2023-04-07 00:00:00', r'%Y-%m-%d %H:%M:%S')
        date_to = dt.now()

        api = API(url=URL + '/tophubs/')
        
        params = {
            'themeId': '12543742',
            'token': API_TOKEN,
            'timeFrom': int(date_from.timestamp()),
            'timeTo': int(date_to.timestamp()),
            'params[size]': 100,
        }
        
        data = api.get(params=params)
        project = Project(
            theme_id='12543742',
            name='Peptid PRO',
        )
        db.add_to_db(project)
        
        for s in data[0]['data']['top_hubs']:
            source = Source(
                name=s['name'],
                num_of_msgs=s['msgs'],
                percent=s['percent'],
                project_id=project.id
            )
            db.add_to_db(source)
        
        db.close_session()
        pprint(data)
        
        time.sleep(1800)
    
        
    
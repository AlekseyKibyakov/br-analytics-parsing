from pprint import pprint
import requests
import time
from config import API_TOKEN
from datetime import datetime as dt
# from pprint import pprint


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

        api = API(r'https://stat-api.br-analytics.ru/v1/statistic/erstat/')
        
        params = {
            'themeId': '12543742',
            'token': API_TOKEN,
            'timeFrom': int(date_from.timestamp()),
            'timeTo': int(date_to.timestamp()),
            # 'params[size]': 5,
        }
        
        data = api.get(params=params)
        pprint(data)
        
        time.sleep(21600)
    
        
    
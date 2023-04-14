import json
from pprint import pprint
import time
from db_interaction import close_session, commit_session
import api_interaction
import html_parsing as html
# from pprint import pprint

if __name__ == '__main__':
    while True:
        # print(html.get_export('https://br-analytics.ru/ajax/export/?tsf=1681160400&tst=1681505999'))
        with open('page.json', 'wb') as f:
            f.write(html.get_html('https://br-analytics.ru/exports/list/?tsf=1681160400&tst=1681505999'))  
        time.sleep(1111)

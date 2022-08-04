import os
import requests
import random
from bs4 import BeautifulSoup
import time
class Parser:

    def __init__(self):
        self.estetica = 'https://yandex.ru/referats/?t=astronomy+geology+gyroscope+literature+marketing+mathematics+music+polit+agrobiologia+law+psychology+geography+physics+philosophy+chemistry+estetica&s='

    def _create_link(self):
        to_return = self.estetica + str(random.randint(10000, 99999))
        return to_return

    def _get_response(self):
        link = self._create_link()
        req = requests.get(link)
        soup = BeautifulSoup(req.text, 'html.parser')
        done_article = soup.find('div', {'class': 'referats__text'})
        return done_article


def do_git():
    os.system('git commit -a -m "test"')
    os.system('git push')


def do_all():
    parser = Parser()
    exit_text = parser._get_response()
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(str(exit_text))
    do_git()


while 1:
   try:
       do_all()
   except Exception as ex:
       print(ex)
       continue
   time.sleep(3)

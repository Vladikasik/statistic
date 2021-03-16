import os
import requests
import random
from bs4 import BeautifulSoup
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
        print(done_article)


def do_git():
    os.system('git commit -a -m "test"')
    os.system('git push')


# parser = Parser()
# parser._get_response()
do_git()

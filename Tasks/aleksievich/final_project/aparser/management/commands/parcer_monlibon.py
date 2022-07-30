# from gettext import Catalog
# from pydoc import text
import requests
from bs4 import BeautifulSoup as BS
import datetime

from django.core.management.base import BaseCommand
from aparser.models import Product


headler = {
    'Host': 'www.ml-auto.by',
    'Referer': 'https://www.ml-auto.by/search/preload/?article=K2056c3',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}



def get_html(url):
    r = requests.get(url, headers=headler)
    return r

def get_content(r):
    soup = BS(r, 'html.parser')
    return soup

def get_product(soup):
#    catalog = []
    i = 0

    for k in soup:

        brend = soup.findAll('a', class_='fancy_inline droppeda danger-hover-link brand-search')[i].text.strip()
        cross = soup.findAll('a', style="font-size: 14px")[i].text.strip()
        quantity = soup.findAll('div', class_='col-4 col-sm-2 col-lg-1 text-center m-auto')[i].text.strip()
        cost = soup.findAll('span', class_='old_PriceLevel')[i].text.strip()
        
        try:
            p = Product.objects.get(cross=cross)
            p.brend = brend
            p.quantity = quantity
            p.cost = cost
            p.parsing_date = datetime.datetime.now()
        except Product.DoesNotExist:
            p = Product(
                article = 'k2056c3',
                brend = brend,
                cross = cross,
                quantity = quantity,
                cost = cost,
                parsing_date = datetime.datetime.now(),
            ).save()
        print(f'product {p}')
        i+=1
    return 



        # if article != '':
        #     catalog.append({
        #             'brend': brend,
        #             'article': article,
        #             'quantity': quantity,
        #             'cost': cost,
        #     })
        # i+=1
    # return catalog


class Command(BaseCommand):
    help = 'Парсинг Momlibon'
    def handle(*args, **options):
        URL = f'https://www.ml-auto.by/search/number/?article=K2056c3&brand=FENOX&ajax=true'
        r = get_html(URL)
        soup = get_content(r.text)
        get_product(soup)



#         URL = f'https://www.ml-auto.by/search/number/?article=k1956&brand=FENOX&ajax=true'
#         r = get_html(URL)
#         soup = get_pages_count(r)
#         data = get_content(soup)
# #        data.extend(get_content(soup))
#         time.sleep(1)



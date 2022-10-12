from bs4 import BeautifulSoup
import requests
import pandas as pd

def moreexchange():
    page = requests.get("""https://www.moreexchange.cl/tipo-de-cambio-de-divisas-more-exchange/""")
    soup = BeautifulSoup (page.text, 'html.parser')
    tables = soup.find_all('table')
    return tables[0]

def cambiossuiza():
    page = requests.get("""https://www.desarrollaonline.com/guinazu/index.php?suc=1""")
    soup = BeautifulSoup (page.text, 'html.parser')
    tables = soup.find_all('table')
    print(tables)
    return tables[0]



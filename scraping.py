from bs4 import BeautifulSoup
import requests
import pandas as pd

def moreexchange():
    page = requests.get("""https://www.moreexchange.cl/tipo-de-cambio-de-divisas-more-exchange/%27""")
    soup = BeautifulSoup (page.text, 'html.parser')
    tables = soup.find_all('table')
    return tables[0]


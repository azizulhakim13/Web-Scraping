from bs4 import BeautifulSoup
import requests
import csv

html_text = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population').text

soup = BeautifulSoup(html_text, 'lxml')
tables = soup.find_all('tr')
row = soup.find('tr')
for table in tables:
    if 'Rank' in row:
        print(row)

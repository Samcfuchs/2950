from bs4 import BeautifulSoup
import re
import pandas as pd

in_filename = "web/AUDL_team_stats.html"
out_filename = "data/team_data_1.csv"

f = open(in_filename, 'r').read()
soup = BeautifulSoup(f, 'lxml')

table = soup.find('table', class_='views-table')
headers = table.find('thead').find_all('th')

def parse_headers(th):
    text = th.get_text()
    if text is None:
        text = th.find('a').get_text()
    return text.strip()

headers = list(map(parse_headers, headers))

rows = table.find('tbody').find_all('tr')

parse_row = lambda row: [d.get_text().strip() for d in row.find_all('td')]
data = map(parse_row, rows)

df = pd.DataFrame(data, columns=headers)

df.to_csv(out_filename)

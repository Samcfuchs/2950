from bs4 import BeautifulSoup
import re
import pandas as pd

in_filename = "web/players/AUDL_player_stats_0.html"
out_filename = "data/player_data.csv"

f = open(in_filename, 'r').read()
soup = BeautifulSoup(f, 'lxml') 
f.close()

single_player = soup.find_all('tr', class_ = "views-field-tooltip-row")

stat_names = soup.find_all('tr', class_ = "views-label2-tooltip-row-0")
for name in stat_names:
    print(name.find('a').get_text())
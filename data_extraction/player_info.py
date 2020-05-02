from bs4 import BeautifulSoup
import re
import pandas as pd

in_filename = "web/players/AUDL_player_info.html"
out_filename = "data/player_info.csv"

f = open(in_filename, "r").read()
soup = BeautifulSoup(f, "lxml")
f.close()

general = soup.find("ul", class_= "views-fluid-grid-list").find_all("li")
results = {}
for li in general :
    name = li.find("div", class_="views-field-player-field-player-display-name").find("span").get_text()
    number = li.find("div", class_="views-field-player-field-jersey-number").find("span").get_text()
    results[name] = number

from bs4 import BeautifulSoup
import re
import pandas as pd

team_column = []
player_name = []

out_filename = "data/player_info.csv"
teams = pd.read_csv("data/teams.csv")
for team in teams['link']:

    in_filename = "web/players" + team + ".html"


    f = open(in_filename, "r").read()
    soup = BeautifulSoup(f, "lxml")

    general = soup.find("ul", class_= "views-fluid-grid-list")
    general = general.find_all("li")
    for li in general :
        name = li.find("div", class_="views-field-player-field-player-display-name").find("span").get_text()

        player_name.append(name)

        team_column.append(team)

data = [team_column, player_name]

df = pd.DataFrame(data)
df.to_csv(out_filename)

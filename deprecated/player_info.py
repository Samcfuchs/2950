from bs4 import BeautifulSoup
import re
import pandas as pd

# Parses the roster from each individual team page first.
# This script is deprecated, use roster_parser instead.

team_column = []
player_name = []

out_filename = "data/player_info.csv"
teams = pd.read_csv("data/teams.csv")
for team in teams['link']:

    in_filename = "web/players" + team + ".html"



    f = open(in_filename, "r").read()
    soup = BeautifulSoup(f, "lxml")

    general = soup.find("ul", class_= "views-fluid-grid-list")

    if general is None:
        continue

    general = general.find_all("li")
    for li in general :
        name = li.find("div", class_="views-field-player-field-player-display-name").find("span").get_text()

        print(name)

        player_name.append(name)

        team_column.append(team[1:])

df = pd.DataFrame({"Team": team_column, "Player": player_name})
df.to_csv(out_filename)

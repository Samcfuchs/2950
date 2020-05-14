from bs4 import BeautifulSoup
import re
import pandas as pd
import sys

# Run fetch_data.get_rosters() first
# Parses the weekly roster posts to extract teams and their players

in_filename = "web/rosters_w/week_{}.html"
out_filename = "data/rosters.csv"

def get_players(node):
    lines = str(r).split("<br/>")

    players = []
    for p in lines:
        name = p.strip()
        name = re.sub("<.*>", "", name)
        name = name.replace("\u00A0", "")
        name = name.strip("*")
        if len(name) and "Inactive" not in name:
            players.append(name)
    
    return players

team_info = pd.read_csv("data/teams.csv", index_col=0)
translator = {k.lower():v[1:] for k,v in zip(team_info.team, team_info.link)}

data = []
for week in range(1,10):
    f = open(in_filename.format(week), 'r', encoding='utf-8').read()
    soup = BeautifulSoup(f, 'lxml')

    content = soup.find('section', id='main-content').find('div', id='content')

    t = str(content)
    pattern = re.compile(r"\*\*Questionable to play</em></p>\n((.|\n)*)<p>\n?<u><strong>MATCHUPS", re.MULTILINE)
    results = re.search(pattern, t)

    if results:
        t = results.group(1)
        content = BeautifulSoup(t, 'lxml')
        teams = content.find_all('h2')
        rosters = content.find_all('p')

        for t,r in zip(teams, rosters):
            players = get_players(r)
            team = translator[t.text.lower()]
            rows = [{'Team':team, 'Player':p} for p in players]
            data += rows

    else:
        print(f"Regex failed. Text for week {week} must be different")
        print(t)
        break

df = pd.DataFrame(data)
df = df.drop_duplicates().reset_index(drop=True)
df.to_csv(out_filename, encoding='utf-8')

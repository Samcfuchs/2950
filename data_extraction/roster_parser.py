from bs4 import BeautifulSoup
import re
import pandas as pd
import sys

in_filename = "web/rosters_w/week1.html"
out_filename = "data/rosters.csv"

def get_players(node):
    players = str(r).split("<br/>")
    players = map(lambda p: p.strip(), players)
    players = map(lambda p: re.sub("<.*>","", p), players)
    players = map(lambda p: p.strip("*"), players)
    return list(players)

team_info = pd.read_csv("data/teams.csv", index_col=0)
translator = {k:v[1:] for k,v in zip(team_info.team, team_info.link)}

f = open(in_filename, 'r').read()
soup = BeautifulSoup(f, 'lxml')

content = soup.find('section', id='main-content').find('div', id='content')

t = str(content)
pattern = re.compile(r"\*\*Questionable to play</em></p>\n((.|\n)*)<p>\n<u><strong>MATCHUPS", re.MULTILINE)
results = re.search(pattern, t)

if results:
    t = results.group(1)
    content = BeautifulSoup(t, 'lxml')
    teams = content.find_all('h2')
    rosters = content.find_all('p')

    data = []
    for t,r in zip(teams, rosters):
        players = get_players(r)
        team = translator[t.text]
        rows = [{'Team':team, 'Player':p} for p in players]
        data += rows
    
    df = pd.DataFrame(data)
    df.to_csv(out_filename)

else:
    print("Regex failed. Text on this page must be different")

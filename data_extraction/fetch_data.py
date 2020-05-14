import requests
import time
import pandas as pd

user_agent = {'User-Agent': 'Mozilla/5.0'}

def write_html(url, filename):
    r = requests.get(url, headers=user_agent)
    r.raise_for_status()

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(r.text)

# Fetch team statistics
def get_team_stats():
    url = "https://theaudl.com/stats/team?year=2"
    filename = "web/AUDL_team_stats.html"
    
    write_html(url, filename)


# Get team listing page
def get_team_page():
    url = "https://theaudl.com/league/teams"
    filename = "web/teams.html"

    write_html(url, filename)

# Get individual stats tables for 2019
def get_player_stats():
    for n in range(23):
        url = f"https://theaudl.com/stats/player-season?page={n}"
        filename = f"web/player_stats/page_{n}.html"
        
        write_html(url, filename)

# Fetch weekly roster blog posts
def get_rosters():
    url = "https://www.theaudl.com/league/news/2019-audl-active-rosters-week-{n}"
    filename = "web/rosters_w/week_{n}.html"
    
    for n in range(1,10):
        print(n)
        write_html(url.format(n=n), filename.format(n=n))

get_rosters()

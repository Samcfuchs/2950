import requests
import time

user_agent = {'User-Agent': 'Mozilla/5.0'}

team_data_params = [
    "https://theaudl.com/stats/team?year=2",
    "web/AUDL_team_stats.html"
]

player_data_params = [
    "https://theaudl.com/stats/player-season?page={n}",
    "web/players/AUDL_player_stats_{n}.html"
]

def write_html(url, filename):
    r = requests.get(url, headers=user_agent)
    r.raise_for_status()

    with open(filename, 'w') as f:
        f.write(r.text)

#write_html(*team_data_params)

for page in range(1,2):
    time.sleep(1)
    write_html(*list(map(lambda s: s.format(n=page), player_data_params)))

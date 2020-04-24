import requests
import time

user_agent = {'User-Agent': 'Mozilla/5.0'}

team_data_params = [
    "https://theaudl.com/stats/team?year=2",
    "web/AUDL_team_stats.html"
]

player_data_params = [
    "https://theaudl.com/stats/players-all-time?page={n}",
    "web/players/AUDL_player_stats_{n}.html"
]

def write_html(url, filename):
    r = requests.get(url, headers=user_agent)
    r.raise_for_status()

    with open(filename, 'w') as f:
        f.write(r.text)

# Fetch team statistics
def get_team_stats():
    write_html(*team_data_params)

# Fetch all-time player statistics
def get_alltime_player_stats():
    for page in range(0,77):
        time.sleep(1)
        url = player_data_params[0].format(n=page)
        filename = player_data_params[1].format(n=page)
        write_html(url, filename)

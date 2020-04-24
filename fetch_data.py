import requests
import time

user_agent = {'User-Agent': 'Mozilla/5.0'}

def write_html(url, filename):
    r = requests.get(url, headers=user_agent)
    r.raise_for_status()

    with open(filename, 'w') as f:
        f.write(r.text)

# Fetch team statistics
def get_team_stats():
    url = "https://theaudl.com/stats/team?year=2",
    filename = "web/AUDL_team_stats.html"
    
    write_html(url, filename)

# Fetch all-time player statistics
def get_alltime_player_stats():
    base_url = "https://theaudl.com/stats/players-all-time?page={n}"
    base_filename = "web/players/AUDL_player_stats_{n}.html"
    
    for page in range(0,77):
        time.sleep(1)
        url = base_url.format(n=page)
        filename = base_filename.format(n=page)
        write_html(url, filename)

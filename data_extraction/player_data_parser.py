from bs4 import BeautifulSoup
import re
import pandas as pd

# Parses individual player statistics
# Run fetch_data.get_player_stats() first.

all_the_data = []
for n in range(0,23):
    in_filename = "web/player_stats/page_" + str(n) + ".html"

    f = open(in_filename, 'r', encoding='utf-8').read()
    soup = BeautifulSoup(f, 'lxml')

    if n ==0:
        stat_names = soup.find_all('th', class_ = "views-label2-tooltip-row-0")
        headers = ['PLAYER']
        for entry in stat_names:
            stat_name = entry.get_text()
            if stat_name is None:
                stat_name = entry.find('a').get_text()
            headers.append(stat_name[1:].strip())


    all_players = soup.find_all('tr', class_ = "views-field-tooltip-row")
    for single_player in all_players:
        single_player_data = []
        stats = single_player.find_all('td')
        for stat in stats:
            stat_value = stat.get_text()
            if stat_value is None:
                stat_value = stat.find('a').get_text().strip()
            single_player_data.append(stat_value[1:].strip())
        all_the_data.append(single_player_data)

player_stats_df = pd.DataFrame(all_the_data, columns = headers)

player_stats_df.to_csv("data/player_stats.csv", encoding='utf-8')



from bs4 import BeautifulSoup
import pandas as pd

# Parses team names from team listing page.
# Generates a listing of team names and their abbreviated representations
# Run fetch_data.get_team_page() first.

in_filename = "web/teams.html"
out_filename = "data/teams.csv"

f = open(in_filename, 'r').read()
soup = BeautifulSoup(f, 'lxml')

table = soup.find('table', class_='league-team-table-pg')

nodes = table.find_all('td')

def parse_cell(td):
    return {
        'team': td.find('figcaption').get_text(),
        'link': td.find('a')['href']
    }

data = map(parse_cell, nodes)

df = pd.DataFrame(data)
df.to_csv(out_filename)

from bs4 import BeautifulSoup
import re
import pandas as pd

in_filename = "web/AUDL_team_stats.html"
out_filename = "data/team_stats.csv"

f = open(in_filename, 'r').read()
soup = BeautifulSoup(f, 'lxml')

# Select the whole table
table = soup.find('table', class_='views-table')

# Get a list of table headers
headers = table.find('thead').find_all('th')

# Gets the name of the table header for each th element
def parse_headers(th):
    text = th.get_text()
    if text is None:
        text = th.find('a').get_text()
    return text.strip()

# Apply the parse_headers function to the table
headers = list(map(parse_headers, headers))

# Get all the table rows
rows = table.find('tbody').find_all('tr')

# parse_row is a function to get a list of strings from each row
parse_row = lambda row: [d.get_text().strip() for d in row.find_all('td')]

# Apply that function to all the rows
data = map(parse_row, rows)

# Convert the data into a dataframe, use the headers as column names
df = pd.DataFrame(list(data), columns=headers)

# Export dataframe to a csv
df.to_csv(out_filename)

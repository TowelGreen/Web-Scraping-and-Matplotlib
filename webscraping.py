import re
from bs4 import BeautifulSoup
import requests
import csv

source=requests.get('https://www.basketball-reference.com/players/a/antetgi01.html').text
soup=BeautifulSoup(source,'lxml')

csv_file=open('data_scrape.csv','w')
csv_writer= csv.writer(csv_file)
csv_writer.writerow(['Age','Team','Lg','Pos','G','GS','MP','FG','FGA','FG%','3P','3PA','3P%','2P','2PA'	,'2P%','eFG%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS'])

data=soup.find('tbody')
rows = data.find_all('tr')
for row in rows:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    print (cols)
    csv_writer.writerows([cols])




csv_file.close()



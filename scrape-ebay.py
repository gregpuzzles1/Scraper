from bs4 import BeautifulSoup
import requests
from bs4.diagnose import diagnose
print "Success"

#url = 'http://my.ebay.com/ws/eBayISAPI.dll?MyEbay&gbh=1&CurrentPage=MyeBayAllSelling&ssPageName=STRK:ME:LNLK:MESX'

data = open("testing-sheriff.html").read()
diagnose (data)

"""response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser") #.encode('utf-8')
#print soup.prettify()
#print soup
table = soup.find('table', attrs={'id': 'v4-My_47_82_tab_0'})
#print table

for row in table.findAll('tr'):
    for cell in row.findAll('td'):
        print cell.text"""
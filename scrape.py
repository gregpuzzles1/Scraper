from bs4 import BeautifulSoup
import requests
print "Success"

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser") #.encode('utf-8')
#print soup.prettify()
#print soup
table = soup.find('table', attrs={'class': 'collapse shadow BCSDTable'})
#print table

for row in table.findAll('tr'):
    for cell in row.findAll('td'):
        print cell.text
import webbrowser
import os

f = open("data.csv", 'r')
data = f.readlines()
lines = len(data)
for line in range(0, lines):
    line = data[line].split(',')
    amazon_link = line[1]

    new = 2

    url = amazon_link

    webbrowser.open(url, new=new)

    os.system('pause')



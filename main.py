import data, functions

usr = data.user()

from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup


try:
    html = urlopen("https://www.fasteconomicnews.com/fx_calendar.aspx")
except HTTPError as e:
    print("The url couldn't be found!")
try:
    bs = BeautifulSoup(html.read(), 'html.parser')
    links = bs.findAll('a')
except AttributeError as e:
    print("Elemento não econtrado!")

functions.print_list(links)

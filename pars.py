import requests
from bs4 import BeautifulSoup as BS

max_page  = 6
pages     = []

for x in range(1, max_page + 1):
	pages.append( requests.get('https://stopgame.ru/review/new/stopchoice/p' + str(x) ) )

for r in pages:
	html  = BS(r.content, 'html.parser')

	for el in html.select('.lent-block'):
		title = el.select('.lent-title > a')
		print( title[0].text )
import requests
from lxml import html

ps = str(input('\nWhat problem are you on? '))

url = ('http://www.projecteuler.net/problem=' + ps)
print('\nGET: ',url)

r = requests.get(url)
tree = html.fromstring(r.content)

problemName = tree.xpath('//*[@id="content"]/h2/text()')
problem1 = tree.xpath('//*[@id="content"]/div[3]/p[1]/text()')
problem2 = tree.xpath('//*[@id="content"]/div[3]/p[2]/text()')
problem3 = tree.xpath('//*[@id="content"]/div[3]/p[3]/text()')


print('\n\n',problemName,'\n\n',problem1,'\n',problem2)
if len(str(problem3)) > 2:
	print('',problem3)
print('\n')

#parser 

import requests
from bs4 import BeautifulSoup


URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
HOST = 'https://auto.ria.com'

#get source code of page 
def get_html(url,params=None):
	r=requests.get(url,headers=HEADERS,params = params)
	return r
#parse html
def get_content(html):
	soup = BeautifulSoup(html, 'html.parser') #html parser is type of document for parsing 
	items = soup.find_all('div',class_='proposition') #get all elements with class_name 'proposition'
	cars=[]
	objects=[]
	for item in items:
		cars.append({
			'title':item.find('h3',class_='proposition_name').get_text(strip=True), #parsing of text
			})
	links = soup.find_all('div',class_='proposition_equip') #find element div to parse links
	for link in links:
		objects.append(link.find('a',href=True).get('href')) #find links


	print(cars)
	print(objects,"\n")


#get data 
def parse():
	#get html 
	html = get_html(URL)
	#if we got content
	if html.status_code == 200:
		get_content(html.text)

	else:
		print("Error :'html status_code doesn't equal to 200' ")


parse()

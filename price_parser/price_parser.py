import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime 


headers = ({
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,'
				  'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
					  'AppleWebKit/537.36(KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
      })


URL = 'https://www.eldorado.ru/'
#specify main URL


def get_html(page):
	"""receiving information from page"""
	url = (f'https://www.eldorado.ru/c/kholodilniki/f/no-frost-v-holodilnoy'
		   f'-kamere/no-frost-v-morozilnoy-kamere/?f_p=15000:40000&page={page}')
	#specify the page with the configured filters, where the page number is replaced with '{page}'
	response = requests.get(url, headers=headers)
	return response.text


def check_content(html):
	"""Функция выполняет проверку на наличие интересующего контента при переключении страницы"""
	soup = BeautifulSoup(html, 'html.parser')
	contain_items = soup.find('h1', class_='_2RRdG7U')
	
	if contain_items.get_text() == ('Холодильники с No Frost (ноу фрост) в холодильной'
									' камере с No Frost (ноу фрост) в морозильной камере'):
	#validation based on the keyword that is displayed on the page
		return True
	else:
		return False


def get_items(html):
	"""Получение информации с элемента"""
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('div', class_='_39MI3A8')
	#insert tag type and element's class name
	list_items = []

	for item in items:
		list_items.append(
			{
			'price': item.find('span', class_='Q35hFri hlL-W8I').get_text(),
			'name': item.find('a', class_ = '_32Sm557').get_text(),
			'link': URL+item.find('a', class_ = '_32Sm557').get('href'),

			}
		)
	return list_items


def parse():
	"""main cycle"""
	with open('parse.csv', 'a', ) as file:
		writer = csv.writer(file, delimiter=';')
		writer.writerow(['Название холодильника', 'Цена', 'Ссылка', datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
	
	page = 1
	html = get_html(page)
	while check_content(html):
		html = get_html(page)
		list_items = get_items(html)
		with open('parse.csv', 'a', ) as file:
			for item in list_items:
				writer = csv.writer(file, delimiter=';')
				writer.writerow([item['name'], item['price'], item['link']])
				page +=1
		

if __name__ == '__main__':
	parse()


  
	




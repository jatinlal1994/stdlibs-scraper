import os

from requests import get
from lxml import html

def getMaxPages(url):
	page = get(url).text
	page_tree = html.fromstring(page)
	max_pages = page_tree.cssselect('.pagination-item')[-2]
	max_pages = max_pages.text_content().lstrip().rstrip()
	return max_pages

def getProductsFromSearch(url):
	links = []
	page = get(url).text
	page_tree = html.fromstring(page)
	products = page_tree.cssselect('.product-link')

	for product in products:
		links.append(getRelativeUrl(product.get('href')))

	file_name = url.split('/')[4]

	file = open('/Users/jatinlal/pph/jewelry/jewelry/files/' + file_name + '.txt', 'a')
	for link in links:
		file.write(link + '\n')
	file.close()

def getUrlsForCategory(category):
	max_pages = getMaxPages(getRelativeUrl(category))

	file_name = category.split('/')[4]

	for n in range(int(max_pages)):
		print("Scraping " + str((n + 1)) + " page from " + str(max_pages) + " pages for " + file_name)
		getProductsFromSearch('https://www.1stdibs.com/jewelry/' + file_name + '/?page=' + str(n))

def getRelativeUrl(url):
	return 'https://www.1stdibs.com' + url
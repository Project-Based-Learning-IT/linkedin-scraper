from selenium import webdriver
from parsel import Selector
import csv

urlArray = []
chromedriver = '/home/sid/Downloads/chromedriver_linux64/chromedriver'

_DRIVER_CHROME = webdriver.Chrome(chromedriver)

_DRIVER_CHROME.get('https://www.linkedin.com/uas/login')

elementID = _DRIVER_CHROME.find_element_by_id('username')
elementID.send_keys('maatsisipbl@gmail.com')

elementID = _DRIVER_CHROME.find_element_by_id('password')
elementID.send_keys('project@123')

elementID.submit()

for i in range(1, 100):
	_DRIVER_CHROME.get('https://www.linkedin.com/search/results/people/?origin=FACETED_SEARCH&page={}&schoolFilter=%5B%22246006%22%5D&sid=b33'.format(i))
	selector = Selector(text=_DRIVER_CHROME.page_source)
	urls = selector.xpath('//a[@class="app-aware-link" and @aria-hidden="false"]/@href').extract()
	for i in range(0, len(urls)):
		urls[i] = urls[i].split('?')[0]

	urlArray.extend(urls)

print(urlArray)

with open('profile_urls.csv', 'w', encoding='UTF8', newline='') as f:
	writer = csv.writer(f)
	
	for url in urlArray:
		writer.writerow([url])
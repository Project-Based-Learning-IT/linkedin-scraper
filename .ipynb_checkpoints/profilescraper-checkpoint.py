# Given the profile urls scrape skills and other info

from selenium import webdriver
from parsel import Selector
import time
import pathlib

#------------------------------------- MAKING CONNECTION-------------------------------------
chromedriver = str(pathlib.Path().resolve())+'/chromedriverMac' 
#Put your chromedriver.exe into current directory as MAC and windows have different system path

_DRIVER_CHROME = webdriver.Chrome(chromedriver)

_DRIVER_CHROME.get('https://www.linkedin.com/uas/login')

elementID = _DRIVER_CHROME.find_element_by_id('username')
elementID.send_keys('maatsisipbl@gmail.com')

elementID = _DRIVER_CHROME.find_element_by_id('password')
elementID.send_keys('project@123')

elementID.submit()
# time.sleep(30) # to solve CAPTCHA

#------------------------------------- GET LIST OF URLS-------------------------------------
def readUrls(DATA_FILE):
	urls = ''
    with open(DATA_FILE,'r') as f:
        urls = f.read()
	
	url_list = urls.split('\n')
	url_list = [url + '/' for url in url_list]
	print(f'Total urls - {len(url_list)}')
	print(f'First url is {url_list[0]}')
	print(f'Last url is {url_list[-1]}')
	return url_list

url_file = 'profile_urls.csv'
urls = readUrls(url_file)

#----------------------------------- SCRAPE PROFILES-------------------------------------
#Enter Start and End ids to scrape
start = 0 #0 based indexing
end = 1 #0 based indexing

filenames = [f'{start}_{end}_atharva',f'{start}_{end}_mayank',f'{start}_{end}_siddhant',f'{start}_{end}_siddesh']

filename = filenames[0]
"""
SCROLL_PAUSE_TIME = 2
# Get scroll height
last_height = int(_DRIVER_CHROME.execute_script("return document.body.scrollHeight"))

for profile in range(start,end):

	url = urls[profile]
	print('dd')
	_DRIVER_CHROME.get(url)
	# sleep(5)

	# _DRIVER_CHROME.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	for i in range(1, last_height, 120):
		_DRIVER_CHROME.execute_script("window.scrollTo(0, {});".format(i))
		time.sleep(1)

		time.sleep(SCROLL_PAUSE_TIME)

		# Calculate new scroll height and compare with last scroll height
		new_height = _DRIVER_CHROME.execute_script(
			"return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height

		selector = Selector(text=_DRIVER_CHROME.page_source)

		# Use xpath to extract the exact class containing the profile name
		name = selector.xpath(
			'//*[starts-with(@class, "text-heading-xlarge")]/text()').extract_first()
		if name:
			name = name.strip()

		# locate link to expand skills
		show_more_skills_button = _DRIVER_CHROME.find_element_by_class_name("pv-skills-section__chevron-icon")
		# expand
		# show_more_skills_button.click()
		_DRIVER_CHROME.execute_script("arguments[0].click();", show_more_skills_button)

		skills = _DRIVER_CHROME.find_elements_by_xpath(
			"//*[starts-with(@class,'pv-skill-category-entity__name-text')]")

		# create skills set
		skill_set = []
		for skill in skills:
			skill_set.append(skill.text)
		
		profile = []
		profile.append(name)
		profile.append(skill_set)
		with open(filename, 'a') as p:
			p.write(profile)
		time.sleep(60)
	_DRIVER_CHROME.close()
"""

def linkedin_scrape(linkedin_urls,filename):
	SCROLL_PAUSE_TIME = 2

	# Get scroll height
	last_height = int(_DRIVER_CHROME.execute_script("return document.body.scrollHeight"))
	profiles = []
	for url in linkedin_urls:

		_DRIVER_CHROME.get(url)
		# sleep(5)

		# _DRIVER_CHROME.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		for i in range(1, last_height, 120): 
			_DRIVER_CHROME.execute_script("window.scrollTo(0, {});".format(i))
			time.sleep(1)

		time.sleep(SCROLL_PAUSE_TIME)

		# Calculate new scroll height and compare with last scroll height
		new_height = _DRIVER_CHROME.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height

		selector = Selector(text=_DRIVER_CHROME.page_source)

		# Use xpath to extract the exact class containing the profile name
		name = selector.xpath('//*[starts-with(@class, "text-heading-xlarge")]/text()').extract_first()
		if name:
			name = name.strip()

		# position = selector.xpath('//*[starts-with(@class, "text-body-medium")]/text()').extract_first()
		# headline = ""
		# company = ""

		# if position:
		# 	headline = position.strip()
		# 	company = headline[headline.find('at')+3:]
		# 	position = position.strip()
		# 	position = position[0:position.find(' at ')]

		#locate link to expand skills
		show_more_skills_button = _DRIVER_CHROME.find_element_by_class_name("pv-skills-section__chevron-icon")
		#expand
		# show_more_skills_button.click()
		_DRIVER_CHROME.execute_script("arguments[0].click();", show_more_skills_button)

		skills = _DRIVER_CHROME.find_elements_by_xpath("//*[starts-with(@class,'pv-skill-category-entity__name-text')]")

		#create skills set
		skill_set = []
		for skill in skills:
			# print(skill.text)
			skill_set.append(skill.text)

		profiles.append([name, skill_set])
		with open(filename, 'a') as p:
			p.write(profiles)

		print(f'{len(profiles)}: {name}, {url}, {skill_set}')
		time.sleep(60)
	return profiles
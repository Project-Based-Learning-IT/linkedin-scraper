# Given the profile urls scrape skills and other info

from selenium import webdriver
from parsel import Selector
import time
import pathlib
import json
import os

#------------------------------------- MAKING CONNECTION-------------------------------------
chromedriver = str(pathlib.Path().resolve())+'/chromedriver.exe' 
#Put your chromedriver.exe into current directory as MAC and windows have different system path

_DRIVER_CHROME = webdriver.Chrome(chromedriver)

_DRIVER_CHROME.get('https://www.linkedin.com/uas/login')

elementID = _DRIVER_CHROME.find_element_by_id('username')
elementID.send_keys('maatsisipbl@gmail.com')

elementID = _DRIVER_CHROME.find_element_by_id('password')
elementID.send_keys('project@123')

elementID.submit()
#CHANGE - if captcha occurs
# time.sleep(30) # to solve CAPTCHA 

#------------------------------------- GET LIST OF URLS-------------------------------------
def readUrls(DATA_FILE):        
	f = open(DATA_FILE)
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
#------ BOOKEEPING for next iteration ------- #CHANGE
#				ATHARVA
#		 Start - 10		End - ?
#		------------------------
#				MAYANK
#		 Start - 0		End - ?
#		------------------------
#				SIDHESH
#		 Start - 0		End - ?
#		------------------------ 
#				SIDHANT
#		 Start - 0		End - ?
#---------------------------------------------

#CHANGE
#Enter Start and End ids to scrape
start = 300 #0 based indexing
end = 320 #0 based indexing

filenames = ['atharva','mayank','siddhant','siddesh']

filename = filenames[1] + '.json' #CHANGE

def linkedin_scrape(linkedin_urls,filename):
	SCROLL_PAUSE_TIME = 2

	# Get scroll height
	last_height = int(_DRIVER_CHROME.execute_script("return document.body.scrollHeight"))
	profiles = {}
	for p in range(start,end):
		url = linkedin_urls[p]
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

		profiles[name] = skill_set
		print(profiles)

		try:
			file = open(filename)
			data = json.load(file)
			file.close()
			data.append(profiles)
			file = open(filename,'w')
			json.dump(data,file)
			file.close()			
		except:
			file = open(filename,'w')
			json.dump(profiles,file)
			file.close()

		time.sleep(30)
	_DRIVER_CHROME.close()
	return 0

linkedin_scrape(urls,filename)

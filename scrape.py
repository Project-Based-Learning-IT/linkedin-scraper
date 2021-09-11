# Given the profile urls scrape skills and other info

from selenium import webdriver
from parsel import Selector
import time

chromedriver = "/home/sid/Downloads/chromedriver_linux64/chromedriver"

_DRIVER_CHROME = webdriver.Chrome(chromedriver)

_DRIVER_CHROME.get('https://www.linkedin.com/uas/login')

elementID = _DRIVER_CHROME.find_element_by_id('username')
elementID.send_keys('maatsisipbl@gmail.com')

elementID = _DRIVER_CHROME.find_element_by_id('password')
elementID.send_keys('project@123')

elementID.submit()

def linkedin_scrape(linkedin_urls):
	SCROLL_PAUSE_TIME = 5

	# Get scroll height
	last_height = _DRIVER_CHROME.execute_script("return document.body.scrollHeight")
	profiles = []
	for url in linkedin_urls:

		_DRIVER_CHROME.get(url)
		# sleep(5)

		_DRIVER_CHROME.execute_script("window.scrollTo(0, document.body.scrollHeight);")
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

		position = selector.xpath('//*[starts-with(@class, "text-body-medium")]/text()').extract_first()
		headline = ""
		company = ""

		if position:
			headline = position.strip()
			company = headline[headline.find('at')+3:]
			position = position.strip()
			position = position[0:position.find(' at ')]

		#locate link to expand skills
		show_more_skills_button = _DRIVER_CHROME.find_element_by_class_name("pv-skills-section__chevron-icon")
		#expand
		show_more_skills_button.click()

		skills = _DRIVER_CHROME.find_elements_by_xpath("//*[starts-with(@class,'pv-skill-category-entity__name-text')]")

		#create skills set
		skill_set = []
		for skill in skills:
			# print(skill.text)
			skill_set.append(skill.text)

		profiles.append([name, headline, position, company, url])
		print(f'{len(profiles)}: {name}, {headline}, {position}, {company}, {url}, {skill_set}')
	return profiles

urls = ['https://www.linkedin.com/in/siddhesh-kothadi/']
linkedin_scrape(urls)
# _DRIVER_CHROME.get(urls[0])

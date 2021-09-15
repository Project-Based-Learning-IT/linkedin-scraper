# linkedin-scraper
### Main project Project Partner 
- [App Design Figma](https://www.figma.com/file/P2RAquKIxdMTbwwkzilvIn/Dating-APP-Template-with-Micro-Interaction-Community)
 - [ Process Flow Diagram Figma](https://www.figma.com/file/Bp0wCsUnWjYWc3G77kJl9Q/CollegeSpace) 
 
 ## Tech stack used
 - Selenium
 - Beautiful Soup
 
 ## Warning
 - Use a dummy account as linkedin doesn't allow multiple profile visits using a automation tool. 
 - Your account might get restricted or blocked
 - You might be asked to verify your identity using government ID when your account is restricted.
 
## Guide
- For chrome driver error add chrome driver folder to path using windows environment variable
### Fields to scrape using scraper.py (Scrolling and clicking):
-  Name
-  Skills
#### Scraped data is stored in csv format in `{your_name}.csv`
#### To change the parameters for your execution search `#CHANGE` to see all the places change is necessary in file `scraper.py`. 
#### Add email and password for login in code.

### Fields to scrape using Scraper.ipynb:
- Everything about is profile quickly fetched in a csv

#### [VIIT College Students and Alumnis search page](https://www.linkedin.com/search/results/people/?origin=FACETED_SEARCH&page=2&schoolFilter=%5B%22246006%22%5D) URL is used to generate profile urls using profile_url_scraper.py and then run scraper.py or scraper.ipynb



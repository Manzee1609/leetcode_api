#import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
def get_leetcode_details(username):
    
    url = "https://www.leetcode.com/"+username+"/"
    driver = webdriver.Chrome('./chromedriver', chrome_options=options)
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    
    realName = soup.find('div', {'class': 'realname__30kg'})
    userName = soup.find('div', {'class': 'username__o7KX'})
    points = soup.find_all('span', {'class': 'css-vsyzx3-SimpleBadge'})
    contestRating = soup.find_all('div', {'class': 'css-57pydk'})
    ranking = soup.find_all('div', {'class': 'css-x9b7oa'})
    problems_solved = soup.find('div', {'class': 'total-solved-count__2El1 css-57pydk'})
    acceptance = soup.find('div', {'size': '108'})
    levels = soup.find_all('span', {'class': 'difficulty-ac-count__jhZm'} )
    submissions = soup.find_all('div', {'class': 'ant-card-head-title'})
    driver.close()
    
    return {'Real Name': realName.text,
            'Username': userName.text,
            'Points': points[0].text,
            'Problems': points[1].text,
            'TestCases': points[2].text,
            'Reputation': points[3].text,
            'Contest Rating': contestRating[0].text,
            'Problems Solved': contestRating[1].text,
            'Ranking': ranking[0].text,
            'Attended': ranking[1].text,
            'Problems Solved': problems_solved.text, 
            'Acceptance': acceptance.text.split('%')[0], 
            'Easy': levels[0].text, 
            'Medium': levels[1].text, 
            'Hard': levels[2].text,
            'Submissions': submissions[3].text.split(' ')[0]
            }
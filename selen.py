import selenium
from selenium import webdriver

url = 'http://www.the-numbers.com/movie/budgets/all'

firefox = webdriver.Firefox()

firefox.get(url)









# import requests
# from bs4 import BeautifulSoup
# import re
# from pprint import pprint
# import pandas as pd
# import html5lib


# url = 'http://www.the-numbers.com/movie/budgets/all'
# response = requests.get(url)
# page_html = response.text


# soup = BeautifulSoup(page_html, "lxml")


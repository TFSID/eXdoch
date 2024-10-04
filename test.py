import os
import json

# from utils.selenium_cookies_management import import_cookies
# from selenium import webdriver
from module.driver import run_firefox
from dotenv import load_dotenv
from utils.selenium_cookies_management import import_cookies

load_dotenv()
driver = run_firefox()
import_cookies(driver,os.getenv("COOKIES_PATH"))
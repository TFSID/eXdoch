import os

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()
from module.JS_Selectors.GoogleSelectors import LoginButton as GoogleLoginButton
from module.driver import run_firefox
from utils import selenium_execute_js

from utils.selenium_cookies_management import import_cookies

js_execute = selenium_execute_js.execute
js_click = selenium_execute_js.click

def login(driver: webdriver, username: str, password: str):
    url = 'https://www.google.com/'
    print("input username: " + username)
    print("input password: " + password)
    print("[*] Opening webdriver")
    try:
        driver.get(url)
        try:
            js_click(driver,GoogleLoginButton)
            print("executing javascript")
        except Exception as e:
            print(f"Error executing javascript: {e}")
        print("run firefox successfully")
    except Exception as e:
        print(f"Error opening URL: {e}")

def login_with_cookies(driver: webdriver):
    session = import_cookies(driver,os.getenv("COOKIES_PATH"))
    url = "https://www.expireddomains.net/"
    print("[*] requests url")
    try:
        session.get(url)
        with open("preview.html", "w") as f:
            f.write(driver.page_source)
            print("write preview.html successfully")
        print(session.get(url))
        print("run firefox successfully")
    except Exception as e:
        print(f"Error opening URL: {e}")

driver = run_firefox
# login(driver, "Tefos", "1234")
login_with_cookies(driver)

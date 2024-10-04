import json
import os
import requests
from selenium import webdriver

def add_cookies(driver: webdriver, key: str, value: str):
    cookie = f'{"name": "{key}", "value": "{value}"}'
    return driver.add_cookie(cookie)

def add_cookies_with_file(driver: webdriver, filename: str):
    return driver.add_cookie(filename)

def read_cookie(COOKIES_PATH:str):
    with open(COOKIES_PATH, 'r') as file:
        cookies = json.load(file)
        print(cookies)
        return cookies

    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    response = session.get(url)

def import_cookies(driver: webdriver,COOKIES_PATH:str):
    # Assume the path to the cookies.json file is 'cookies.json'
    with open(COOKIES_PATH, 'r') as file:
        try:
            cookies = read_cookie(COOKIES_PATH)
            print("[+] cookies found")
            session = requests.Session()
            cookies = json.load(file)
            for cookie in cookies:
                a = cookie['name']
                b = cookie['value']
                print(f'[+] {a} added to session')
                print(f'[+] {b} added to session')
                session.cookies.set(cookie['name'], cookie['value'])
            return session
        except Exception as e:
            print(f'Error reading cookies: {e}')
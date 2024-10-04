from selenium import webdriver
# funcs == js script to be executed
def execute(driver:webdriver,funcs:str):
    return driver.execute_script(f'return {funcs}')

def click(driver:webdriver,funcs:str):
    return driver.execute_script(f'return {funcs}.click()')
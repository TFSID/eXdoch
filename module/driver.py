import sys
from selenium import webdriver
def run_firefox():
    options = webdriver.FirefoxOptions()
    # options.add_argument('-headless')
    options.add_argument('-allow-host')
    options.accept_insecure_certs = True
    options.set_preference('geo.prompt.testing', True)
    options.set_preference('geo.prompt.testing.allow', False)
    options.set_preference('javascript.enabled', True)



    try:
        driver = webdriver.Firefox(options=options)
    except Exception as err:
        # ic(driver)
        sys.exit(f'[!] Failed to run firefox {err}')

    return driver


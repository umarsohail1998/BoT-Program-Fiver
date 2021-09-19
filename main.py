import os
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# function to open browser
def get_browser():
    os.environ['WDM_LOG_LEVEL'] = '0'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-blink-features')
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    wait = WebDriverWait(driver, 45)
    return driver, wait


# opening the site in browser
driver, wait = get_browser()
driver.get('http://149.248.20.234:25500/login.php?referrer=/dashboard.php')

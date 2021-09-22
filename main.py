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

user_name = "admin"
user_password = "xcadmin"
s = 1
ep = 6
url = "https://srv1.streamsology.net:8443/series/darrellmills/Kv66ULdfPX/22995.mkv"





driver, wait = get_browser()
driver.get('http://149.248.20.234:25500/login.php')


wait.until(ec.presence_of_element_located((By.NAME, 'username'))).send_keys(user_name)
wait.until(ec.presence_of_element_located((By.NAME, 'password'))).send_keys(user_password)
wait.until(ec.presence_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
# driver.get("http://149.248.20.234:25500/serie.php")
driver.get("http://149.248.20.234:25500/episode.php?sid=1")

driver.implicitly_wait(3)

driver.find_element_by_id("season_num").send_keys(s)
driver.find_element_by_id("episode").send_keys(ep)
driver.find_element_by_id('select2-tmdb_search-container').click()

# issue here.....
options = driver.find_element_by_id('select2-tmdb_search-results')
options[len(options)-1].click()

driver.find_element_by_id("stream_source").send_keys(url)
driver.find_element_by_name("Next").click()
driver.find_element_by_name("Next").click()
driver.find_element_by_name("Next").click()
driver.find_element_by_name('submit_stream').click()

# driver.find_element_by_name("password").send_keys(user_password)
# driver.find_element_by_xpath("//button[@type='submit']").click()
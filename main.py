import os
import pandas as pd
from time import * 
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import Extractdata

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

def extract_series_from_web_table(lt):
    Series_dict = {}
    for x in lt:
        data = list(x.text.split(' '))
        length = len(data)-6
        val = data[0]
        S_name = ' '.join(data[1:length])
        Series_dict[S_name] = val
    return Series_dict


def Add_serie(driver, name):
    goto = 'http://149.248.20.234:25500/serie.php'
    driver.get(goto)
    driver.find_element_by_id('title').send_keys(name)
    # driver.implicitly_wait(3)    
    driver.find_element_by_link_text("Next").click()
    driver.find_element_by_link_text("Previous").click()
    sleep(1)
    
    driver.find_element_by_id('select2-tmdb_search-container').click()        
    html_list = driver.find_element_by_id("select2-tmdb_search-results")
    html_list.find_elements_by_tag_name("li")[1].click()

    sleep(2)
    driver.find_element_by_xpath('//*[@id="stream-details"]/div/div/div[4]/div/span/span[1]/span/ul').click()
    driver.find_element_by_id('select2-bouquets-results').click()
    
    driver.find_element_by_link_text("Next").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="movie-information"]/ul/li[2]/input').click()
    

def Add_series_to_web(driver, web, local):
    # print(web, local)
    for x in local:
        if x not in web:
            Add_serie(driver, x) 
            driver.implicitly_wait(3)
            

def find_All_Series(driver):
    d = {}    
    lt = driver.find_elements_by_xpath("//*[@id='datatable-streampage']/tbody/tr")
    d.update(extract_series_from_web_table(lt))
    return d

    





user_name = "admin"
user_password = "xcadmin"
s = 1
ep = 6
url = "https://srv1.streamsology.net:8443/series/darrellmills/Kv66ULdfPX/22995.mkv"
web_Srs_dict = 0

driver, wait = get_browser()
driver.get('http://149.248.20.234:25500/login.php')
driver.maximize_window()

wait.until(ec.presence_of_element_located((By.NAME, 'username'))).send_keys(user_name)
wait.until(ec.presence_of_element_located((By.NAME, 'password'))).send_keys(user_password)
wait.until(ec.presence_of_element_located((By.XPATH, "//button[@type='submit']"))).click()


driver.get("http://149.248.20.234:25500/series.php")
sleep(2)
web_Srs_dict = find_All_Series()

file_record = Extractdata.getData()
file_Series_name = file_record.keys()
Add_series_to_web(driver, web_Srs_dict.keys(), file_Series_name)

driver.get("http://149.248.20.234:25500/series.php")
driver.close()


# for x, y in record.items():
#     for i in y:
#         print(x, i['S#'], i['EP#'])


# driver.get("http://149.248.20.234:25500/episode.php?sid=1")

# driver.implicitly_wait(3)

# driver.find_element_by_id("season_num").send_keys(s)
# driver.find_element_by_id("episode").send_keys(ep)


# driver.find_element_by_id('select2-tmdb_search-container').click()

# # tmp = driver.find_element_by_id("select2-tmdb_search-results")
# # for x in tmp:
# #     print(x.get_attribute('innerHTML'))

# html_list = driver.find_element_by_id("select2-tmdb_search-results")
# html_list.find_elements_by_tag_name("li")[-1].click()

# driver.find_element_by_id("stream_source").send_keys(url)

# driver.find_element_by_link_text("Next").click()
# driver.find_element_by_link_text("Next").click()
# driver.find_element_by_link_text("Next").click()

# source = driver.find_element_by_link_text("Main Server")
# target = driver.find_element_by_link_text("Stream Source")

# action_chains = ActionChains(driver)
# action_chains.drag_and_drop(source, target).perform()

# driver.find_element_by_name('submit_stream').click()
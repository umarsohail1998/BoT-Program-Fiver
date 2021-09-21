import time
from selenium import webdriver
from selenium.webdriver import ActionChains

# Your Xtream account details
user_name = "admin"
user_password = "xcadmin"



# Definitions for Selenium, don't change them

driver = webdriver.Chrome('\Program Files/chromedriver')
Xtream_home = "http://149.248.20.234:25500/login.php"
login_button = "//button[@type='submit']"
subMenu_Vod = "//html/body/header/div[2]/div/div/ul/li[5]"
manage_series ="/html/body/header/div[2]/div/div/ul/li[5]/ul/li[1]/ul/li[5]"
manage_series ="/html/body/header/div[2]/div/div/ul/li[5]/ul/li[1]/ul/li[5]"




# Xtream Log in
def login():
    # Open Xtream on Chrome Driver
    driver.get(Xtream_home)
    time.sleep(2)

    # Log in
    user = driver.find_element_by_name("username")
    user.send_keys(user_name)
    time.sleep(2)
    pas = driver.find_element_by_name("password")
    pas.send_keys(user_password)
    time.sleep(2)
    driver.find_element_by_xpath(login_button).click()
    time.sleep(2)

#Select VOD and then select manage series

def goto_manage_series():
    vod = driver.find_element_by_xpath(subMenu_Vod)
    man_ser = driver.find_element_by_xpath(manage_series)

    actions = ActionChains(driver)
    actions.move_to_element(vod).move_to_element(man_ser).click().perform()

login()
goto_manage_series()
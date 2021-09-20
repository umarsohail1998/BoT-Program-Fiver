import time
from selenium import webdriver


# Your Xtream account details
user_name = "admin"
user_password = "xcadmin"



# Definitions for Selenium, don't change them

driver = webdriver.Chrome('\Program Files/chromedriver')
Xtream_home = "http://149.248.20.234:25500/login.php"
login_button = "//button[@type='submit']"





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




login()

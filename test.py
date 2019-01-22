from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("https://justyouand.me/login")
assert "login" in driver.title
elemU = driver.find_element_by_name("username")
elemP = driver.find_element_by_name("password")
elemSub = driver.find_element_by_id("loginBtn")

elemU.send_keys("username")
# time.sleep(0.3)
elemP.send_keys("password")
# time.sleep(0.3)
elemSub.submit()

loader = driver.find_element_by_class_name('loader').get_attribute('style')

if loader == 'display: none;':
    # time.sleep(0.3)
    elemSearch = driver.find_element_by_id('search_btn')
    elemSearch.click()

search = driver.find_element_by_id('search')

search.send_keys('bad boys ')

# elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("https://justyouand.me/login")
assert "login" in driver.title
elemU = driver.find_element_by_name("username")
elemP = driver.find_element_by_name("password")
elemSub = driver.find_element_by_id("loginBtn")

elemU.send_keys("rogerndaba")
# time.sleep(0.3)
elemP.send_keys("rootroot2%")
# time.sleep(0.3)
elemSub.submit()

assert "home" in driver.title

# print(driver.execute_script("return document.readyState"))

loader = driver.find_element_by_class_name('loader').get_attribute('style')

if loader == 'display: none;':
    # time.sleep(0.3)
    elemSearch = driver.find_element_by_id('search_btn')
    elemSearch.click()
search = driver.find_element_by_id('search')


search.send_keys('bad boys ')

driver.execute_script('''window.open("http://bings.com","_blank");''')
time.sleep(1)
driver.switch_to_window(driver.window_handles[1])
search = driver.find_element_by_id('sb_form_q')
search.send_keys('history of python')
search.send_keys(Keys.RETURN)
# driver.get('https://github.com/login')
assert "No results found." not in driver.page_source
# driver.quit()

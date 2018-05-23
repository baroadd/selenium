from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://viza.io/signup")
elm = driver.find_elements_by_tag_name('input')

for i in elm:
    if(i.get_attribute('name') != '' and i.get_attribute('type') != 'hidden'):
        driver.find_element_by_name(i.get_attribute('name')).send_keys('aaa')
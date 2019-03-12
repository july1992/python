from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.126.com/'
driver.get(base_url)
time.sleep(5)
# driver.switch_to_frame('//*[@id="x-URS-iframe1552355264449.2908"]')
# driver.find_element_by_name('email').send_keys('sss')
# driver.find_element_by_name('password').send_keys('sadad')

driver.find_element(By.NAME('email'))
# driver.find_element_by_xpath('//*[@id="auto-id-1552357575647"]')
# driver.find_element_by_id('login_button').click()
time.sleep(5)
driver.quit()
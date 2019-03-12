from selenium import webdriver
import time

driver = webdriver.Chrome()
base_url = 'https://mail.qq.com/'
driver.get(base_url)
time.sleep(5)
driver.switch_to_frame('login_frame')
driver.find_element_by_name('u').send_keys('sss')
driver.find_element_by_name('p').send_keys('sadad')
# driver.find_element_by_id('login_button').click()

# driver.quit()
# coding=utf-8
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

url = 'https://mail.qq.com/'

login_text = '登录'

account = 'aaa'

pwd = 'bbb'


def login():
    driver = webdriver.Chrome()
    driver.get(url)
    # time.sleep(5)
    # driver.switch_to.frame("login_frame")


if __name__ == '__main__':
    login()

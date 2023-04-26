from pyvirtualdisplay import Display
display = Display(visible=0, size=(2000, 2000))
display.start()
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from random import randint
import random
import string


options = uc.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--load-extension=./buster')
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
id_generator()
driver = uc.Chrome(version_main = 112 ,options=options)
driver.set_window_size(2000, 2000)
wait = WebDriverWait(driver, 30)

driver.get("https://tech.amwaly.com/blog/29134/%D8%A3%D9%81%D8%B6%D9%84-%D8%A3%D8%AC%D9%87%D8%B2%D8%A9-apple-iphone-%D9%84%D9%84%D8%B4%D8%B1%D8%A7%D8%A1-%D9%81%D9%8A-%D8%B9%D8%A7%D9%85-2023")
time.sleep(30)

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

driver.get("https://mirex.cc/?ref=mahmoudfahmi")
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main__screen"]/div/div[2]/div[1]/a'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/div/div/form/div[1]/input'))).send_keys(id_generator(5))
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/div/div/form/div[2]/input'))).send_keys(id_generator(5)+"@gmail.com")
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/div/div/form/div[3]/input'))).send_keys("zxcasdqwe12")
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/div/div/form/div[4]/input'))).send_keys("zxcasdqwe12")
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/div/div/form/div[5]/button'))).click()
time.sleep(10)

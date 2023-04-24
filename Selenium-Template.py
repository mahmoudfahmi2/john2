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

options = uc.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--load-extension=./buster')
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
randomchar = (random_with_N_digits(9))
driver = uc.Chrome(version_main = 112 ,options=options)
driver.set_window_size(2000, 2000)
wait = WebDriverWait(driver, 30)

driver.get("https://millioner-but.ru/?ref=675059")
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div[1]/form/input'))).send_keys("P"+str(randomchar))
driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']"))
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]'))).click()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='recaptcha challenge expires in two minutes']"))
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[4]'))).click()
driver.switch_to.default_content()
time.sleep(15)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div[1]/form/button'))).click()
time.sleep(5)

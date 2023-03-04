from pyvirtualdisplay import Display
display = Display(visible=0, size=(2000, 2000))
display.start()
import undetected_chromedriver as uc
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
driver = uc.Chrome(version_main = 110 ,options=options)
driver.set_window_size(2000, 2000)
wait = WebDriverWait(driver, 30)
driver.get("https://cuty.io/fetchrewards")
try:
  time.sleep(20)
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-button"]'))).click()
  time.sleep(5)
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-button"]'))).click()
  time.sleep(5)
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-button"]'))).click()
  time.sleep(5)
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-button"]'))).click()
  time.sleep(5)
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-button"]'))).click()
except:
  time.sleep(10)
  driver.save_screenshot('screenie.png')
  driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='recaptcha challenge expires in two minutes']"))
  wait.until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div/div/div[4]'))).click()
  time.sleep(10)
  driver.save_screenshot('screenie.png')
  try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-button"]'))).click()
  except:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div/div/div[4]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-button"]'))).click()
  time.sleep(5)
  driver.save_screenshot('screenie.png')

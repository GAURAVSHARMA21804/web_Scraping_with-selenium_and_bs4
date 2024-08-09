from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=18GH7ZDODC7UD&sprefix=l%2Caps%2C256&ref=nb_sb_ss_ts-doa-p_1_1")
elem = driver.find_element(By.CLASS_NAME,"puis-card-container")
print(elem.get_attribute("outerHTML"))


time.sleep(10)
driver.close()
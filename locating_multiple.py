from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=18GH7ZDODC7UD&sprefix=l%2Caps%2C256&ref=nb_sb_ss_ts-doa-p_1_1")
    elems = driver.find_elements(By.CLASS_NAME,"puis-card-container")
    # print(elems.get_attribute("outerHTML"))
    print(f"{len(elems)} items found")
    for elem in elems:
        print(elem.text)


    time.sleep(10)
driver.close()
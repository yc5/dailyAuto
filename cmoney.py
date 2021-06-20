import sys
import time
from decouple import config
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--window-size=1280,720')
chrome_options.add_argument('--headless')
account_email = config('CMONEY_USERNAME')
account_password = config('CMONEY_PW')

t = time.localtime()
current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print("start:", current_time)

print("=== run cmoney ===")
try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.cmoney.tw/member/login/?url=https%3A%2F%2Fwww.cmoney.tw%2Fmember%2Fbonus%2Fdefault.aspx%3Fifr%3D1")

    print("input account_email")
    input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.ID, "account"))
        )
    input.send_keys(account_email)

    print("input account_password")
    input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.ID, "pw"))
        )
    input.send_keys(account_password)

    print("click submit")
    input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[type=submit]"))
        )
    input.click()
except:
    print(sys.exc_info())

time.sleep(10)

t = time.localtime()
current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print("end:", current_time)

driver.quit()
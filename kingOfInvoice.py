import sys
import time
from decouple import Config, config
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--window-size=250,1000')
chrome_options.add_argument('--headless')
# account_email = config('CMONEY_USERNAME')
# account_password = config('CMONEY_PW')
KING_TOKEN = config('KING_TOKEN')

t = time.localtime()
current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print("start:", current_time)

print("=== run kingOfInvoice ===")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.money.com.tw/sleepearly?access_token="+KING_TOKEN+"&os=android")

try:
    print("checking reward modal ...")
    checkInModal = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "rewardModal"))
        )
    print("click closeBtn")
    closeBtn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#rewardModal .close"))
        )
    closeBtn.click()
except:
    print(sys.exc_info())
    print("reward modal doesn't show")

try:
    print("checking sign in modal ...")
    checkInModal = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "checkInModal"))
        )
    print("click closeBtn")
    closeBtn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#checkInModal .close"))
        )
    closeBtn.click()
except:
    print(sys.exc_info())
    print("sign in modal doesn't show")

try:
    print("click regBtn")
    regBtn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#sleepEarlyBtn.btn.btn-yellow-filled"))
        )
    regBtn.click()

    print("click OKBTN")
    OKBTN = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#check_in_form3 #sleepEarlyBtn.OKBTN"))
        )
    OKBTN.click()
except:
    print(sys.exc_info())

time.sleep(10)

t = time.localtime()
current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print("end:", current_time)

driver.quit()
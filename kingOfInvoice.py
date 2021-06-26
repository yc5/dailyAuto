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
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")
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
    print("checking 獎勵Modal ...")
    checkInModal = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "rewardModal"))
        )
    print("click closeBtn using JS")
    driver.execute_script("$('#rewardModal').modal('hide')")
except:
    print("獎勵Modal doesn't show")
    print(sys.exc_info())
finally:
    time.sleep(5)

try:
    print("checking  打卡成功Modal ...")
    checkInModal = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "checkInModal"))
        )
    print("打卡成功")
    print("click closeBtn using JS")
    driver.execute_script("$('#checkInModal').modal('hide')")
except:
    print("打卡成功Modal doesn't show")
    print(sys.exc_info())
finally:
    time.sleep(5)

try:
    print("click 報名按鈕")
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
    print("button not clickable")
    print(sys.exc_info())
finally:
    time.sleep(5)

btn_text = driver.execute_script("return $('#sleepEarlyBtn').text();")
print(btn_text)

t = time.localtime()
current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print("end:", current_time)

driver.quit()
import time
from decouple import config
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# mobile
chrome_options = Options()
chrome_options.add_argument("--window-size=600,1000")
chrome_options.add_argument("--headless")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1"
)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://login.yahoo.com/m/?.intl=tw&.lang=zh-Hant-TW&.src=twmobi&.done=https%3A%2F%2Ftw.yahoo.com%2Fmember"
)

tmp = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "login-username"))
)
tmp.send_keys(config("YAHOO_EMAIL") + Keys.ENTER)
time.sleep(1)
tmp = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "login-passwd"))
)
tmp.send_keys(config("YAHOO_PW") + Keys.ENTER)

time.sleep(2)
print("T:", driver.get_cookie("T")["value"])
print("Y:", driver.get_cookie("Y")["value"])
driver.quit()

import sys
import time
from decouple import config
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--window-size=1280,720')
chrome_options.add_argument('--headless')
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")
YAHOO_T = sys.argv[1]
YAHOO_Y = sys.argv[2]

# line notify
token = config('KING_LINE_NOTIFY_TOKEN')
url = 'https://notify-api.line.me/api/notify'
headers = {'Authorization': 'Bearer ' + token}
msg = ''

t = time.localtime()
current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print("start:", current_time)

print("=== run yahoo ===")
try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://mail.yahoo.com/")
    print("setting cookie ...")

    driver.add_cookie({"name": "T", "value": YAHOO_T})
    driver.add_cookie({"name": "Y", "value": YAHOO_Y})
    print("redirect to yahoo mail ...")
    driver.get("https://mail.yahoo.com/")

    print("getting ybarAccountMenuOpener ...")
    personal_info = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, "ybarAccountMenuOpener"))
    )
    print("Hello,", personal_info.get_attribute('textContent').strip())
    msg += "Yahoo! " + personal_info.get_attribute('textContent').strip()

except:
    print(sys.exc_info())

for i in range(5):
    if "d/folders" in driver.current_url:
        break
    print("current_url:", driver.current_url)
    time.sleep(5)

print("current_url:", driver.current_url)

time.sleep(5)
try:
    print("=== click top ten ===")
    driver.get(
        "https://tw.search.yahoo.com/search?p=%E5%88%BA%E5%88%BA%E6%98%9F&fr=yfp-search-sa")
    print("setting cookie ...")

    driver.add_cookie({"name": "T", "value": YAHOO_T})
    driver.add_cookie({"name": "Y", "value": YAHOO_Y})
    print("redirect to yahoo index ...")
    driver.get(
        "https://tw.search.yahoo.com/search?p=%E5%88%BA%E5%88%BA%E6%98%9F&fr=yfp-search-sa")

    txt = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".trendingNow a"))
    )
    print("click", txt.get_attribute('textContent').strip(), "...")
    msg += "\nClick " + txt.get_attribute('textContent').strip()
    txt.click()
    time.sleep(5)
    txt = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".trendingNow a"))
    )
    print("click", txt.get_attribute('textContent').strip(), "...")
    msg += "\nClick " + txt.get_attribute('textContent').strip()
    txt.click()
    time.sleep(5)
except:
    print(sys.exc_info())


# line notify
data = {'message': msg}
r = requests.post(url, data=data, headers=headers)

t = time.localtime()
current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print("end:", current_time)
driver.quit()

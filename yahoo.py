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
chrome_options.add_argument("--window-size=1280,720")
chrome_options.add_argument("--headless")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
)
YAHOO_T = sys.argv[1]
YAHOO_Y = sys.argv[2]

# line notify
token = config("KING_LINE_NOTIFY_TOKEN")
url = "https://notify-api.line.me/api/notify"
headers = {"Authorization": "Bearer " + token}
msg = ""

t = time.localtime()
current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print("start:", current_time)

print("=== run yahoo ===")
try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://mail.yahoo.com/")
    print("setting cookie ...")

    driver.add_cookie({"name": "T", "value": YAHOO_T, "domain": "yahoo.com"})
    driver.add_cookie({"name": "Y", "value": YAHOO_Y, "domain": "yahoo.com"})
    print("redirect to yahoo mail ...")
    driver.get("https://mail.yahoo.com/")

    print("getting ybarAccountMenuOpener ...")
    personal_info = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "ybarAccountMenuOpener"))
    )
    print("Hello,", personal_info.get_attribute("textContent").strip())
    msg += "Yahoo! " + personal_info.get_attribute("textContent").strip()

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
        "https://tw.search.yahoo.com/search?p=%E5%88%BA%E5%88%BA%E6%98%9F&fr=yfp-search-sa"
    )
    print("setting cookie ...")

    driver.add_cookie({"name": "T", "value": YAHOO_T})
    driver.add_cookie({"name": "Y", "value": YAHOO_Y})
    print("redirect to yahoo index ...")
    driver.get(
        "https://tw.search.yahoo.com/search?p=%E5%88%BA%E5%88%BA%E6%98%9F&fr=yfp-search-sa"
    )

    txt = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".trendingNow a"))
    )
    print("click", txt.get_attribute("textContent").strip(), "...")
    msg += "\nclick " + txt.get_attribute("textContent").strip()
    txt.click()
    time.sleep(5)
    txt = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".trendingNow a"))
    )
    print("click", txt.get_attribute("textContent").strip(), "...")
    msg += "\nClick " + txt.get_attribute("textContent").strip()
    txt.click()
    time.sleep(5)
except:
    print(sys.exc_info())
finally:
    driver.quit()

# click eight news
chrome_options = Options()
chrome_options.add_argument("--window-size=600,1000")
chrome_options.add_argument("--headless")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1"
)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tw.yahoo.com/member")
driver.add_cookie({"name": "T", "value": YAHOO_T, "domain": "yahoo.com"})
driver.add_cookie({"name": "Y", "value": YAHOO_Y, "domain": "yahoo.com"})

url_challenges_info_api = "https://tw.yahoo.com/_td-hl/api/resource/LoyaltyService.challenges?bkt=tw-fp-mweb-tts3-part2-bucket&contentType=null&device=smartphone&ecma=default&feature=always%2CnewBreakingNews%2CadFeedback%2CoathPlayer%2CuseDefaultNavigation%2CuseNTKCanonical%2Ctts3&intl=tw&lang=zh-Hant-TW&page=membercenter&pageType=undefined&partner=none&period=day&prid=988irr5hcl6bf&region=TW&site=fp&subCategory=null&tz=Asia%2FTaipei&ver=3.2.4345&returnMeta=true"
current_execution_times = driver.execute_async_script(
    "var callback = arguments[arguments.length-1]; return fetch('"
    + url_challenges_info_api
    + "').then((e) => e.json()) .then((json) => { let currentExecutionTimes = 0; json.data.challenges.forEach((e) => { if (e.defaultActionType == 'read_article') currentExecutionTimes = e.currentExecutionTimes; }); return currentExecutionTimes; }) .then(callback) .catch(callback);"
)
print("current_execution_times", current_execution_times)
msg += "\ncurrent_execution_times " + str(current_execution_times)

driver.get("https://tw.news.yahoo.com")
links_news = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#ntk-list a"))
)
list_links_news = []
for x in links_news:
    list_links_news.append(x.get_attribute("href"))

for x in range(8 - current_execution_times):
    driver.get(list_links_news[x])
    time.sleep(2)

    news_title = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "header > h1"))
    )
    news_title = news_title.get_attribute("textContent").strip()
    print("get", x + 1, news_title)
    msg += "\nget " + str(x + 1) + " " + news_title

    driver.execute_script("window.scrollTo(0, 2000);")
    time.sleep(2)
    try:
        btn_skip = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".skip-button"))
        )
        btn_skip.click()
        print("click", x + 1, "skip button")
    except:
        pass

    driver.execute_script("window.scrollTo(0, 2000);")
    time.sleep(1)
    driver.execute_script(
        "window.scrollTo(0, document.querySelector('#postArticle').offsetTop);"
    )
    btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".challenge-target > button"))
    )
    btn.click()
    time.sleep(2)

# Shopping-start
driver.get("https://tw.buy.yahoo.com/rushbuy")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
try:
    btn_checkin = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[class^=CheckInButton]"))
    )
    btn_checkin.click()
except:
    print("there is no btn_checkin")

# line notify
data = {"message": msg}
r = requests.post(url, data=data, headers=headers)

t = time.localtime()
current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print("end:", current_time)
driver.quit()

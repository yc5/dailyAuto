# dailyAuto

Automate several daily routine tasks with Python Selenium.

使用 Python Selenium 技術，自動化完成每日重複性工作。

目前支援項目包含：
- Yahoo!奇摩好朋友計畫：電子信箱每日簽到、點擊十大熱門搜尋、閱讀新聞、購物中心 找阿虎任務
- 發票集點王每日打卡簽到
- Cmoney每日登入理財寶購物金回饋


## Setting up .env file

```
CMONEY_USERNAME="0900000000"
CMONEY_PW="PASSWORD"

YAHOO_EMAIL="EMAIL_ADDRESS"
YAHOO_PW="PASSWORD"
YAHOO_T="TOKEN_AF_D_SK_KT_KU"
YAHOO_Y="TOKEN_V_L_P_IZ_R_INTL"

KING_TOKEN="TOKEN_32"
```


## Setup Chrome

1. ```wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb```
2. ```sudo apt install ./google-chrome-stable_current_amd64.deb```


## Setup ChromeDriver

1. Download it from https://chromedriver.chromium.org/ .
2. `sudo unzip chromedriver_linux64.zip -d /usr/local/bin`


## Command Line Arguments

```python yahoo.py COOKIE_YAHOO_T COOKIE_YAHOO_Y```

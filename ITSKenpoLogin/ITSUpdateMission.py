#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Required
- requests (必須)
- pillow (可選)
Info
- author : "Simon"
- email  : ""
- date   : "2018.4.6"
'''
import requests
from datetime import date
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re
import time
import logging


url = 'https://its-kenpo.mhweb.jp/mission/record/save'
# リクエストヘッダーを作成
agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
headers = {
    "Host": "its-kenpo.mhweb.jp",
    "Referer": url,
    'User-Agent': agent,
}

def update(session, token):
    postdata = {
            'method': 'POST',
            '__token': token,
            'data[syear]': date.today().year,
            'data[smonth]': date.today().month,
            'data[sday]': date.today().day,
            'data[plans][17]': '3',
            'x': '46',
            'y': '11'
        }

    logging.info('Begin Update Mission')
    page = session.post(url, verify=False, data=postdata, headers=headers)
    if page.stauts_code == 200:
        logging.info('Update Mission Success')
    else:
        logging.info('Update Mission Failed.Code:' + page.status_code)

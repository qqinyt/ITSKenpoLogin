#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Required
- requests 
- date
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
import json
import random
import logging

url = 'https://its-kenpo.mhweb.jp/security_code'

# リクエストヘッダーを作成
agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
headers = {
    "Host": "its-kenpo.mhweb.jp",
    "Referer": url,
    'User-Agent': agent,
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
}

def view(session, token, security_code):
    postdata = {
        '_method':'POST',
        '__token':token,
        'data[UserTunable][section]':'',
        'data[UserTunable][security_code]':security_code
        }

    logging.info('Begin Verify Security Code.')
    page = session.get(url, headers = headers, verify=False)
    if page.status_code == 200:
        logging.info('Verify Security Code Success.')
        page = session.post(url, headers = headers, data = postdata, verify=False)

        if page.status_code == 200:
            #医療費明細
            urlmeisai = 'https://its-kenpo.mhweb.jp/meisai/iryouhi/show'
            session.get(urlmeisai, headers = headers, verify=False)

            time.sleep(random.randint(3, 5))

            #ジェネリック医薬品
            session.get('https://its-kenpo.mhweb.jp/meisai/generic/show', headers = headers , verify=False)
       
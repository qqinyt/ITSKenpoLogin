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
import json

url = 'https://its-kenpo.mhweb.jp/vital/'
# リクエストヘッダーを作成
agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
headers = {
    "Host": "its-kenpo.mhweb.jp",
    "Referer": url,
    'User-Agent': agent,
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With':'XMLHttpRequest'
}

def update(session, token):
    headers['X-CSRF-TOKEN'] = token
    before_ymd = {
        'before_ymd':date.today().isoformat()
        }
    postdata = {
            '__token': token,
            'year': date.today().year,
            'month': date.today().month,
            'day': date.today().day,
            'data':json.dumps(before_ymd),
            'UserWeight':'',
            'UserHighPressure':'130',
            'UserLowPressure':'89',
            'UserTargetSteps':'7856',
            'modelDisplayYm':''
        }

    page = session.post('https://its-kenpo.mhweb.jp/vital/updateVitalData', verify=False, data=json.dumps(postdata), headers=headers)
    print(page.status_code)

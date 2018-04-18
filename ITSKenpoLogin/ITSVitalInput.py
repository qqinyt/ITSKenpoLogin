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
import random
import logging

# リクエストヘッダーを作成
agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
headers = {
    "Host": "its-kenpo.mhweb.jp",
    "Referer": 'https://its-kenpo.mhweb.jp/vital/',
    'User-Agent': agent,
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With':'XMLHttpRequest'
}

#歩数
def getTargetSteps():
    return random.randint(3000, 15000)
#高血圧
def getHighPressure():
    return random.randint(110,130)
#低血圧
def getLowPressure():
    return random.randint(70,90)

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
            'UserHighPressure':getHighPressure(),
            'UserLowPressure':getLowPressure(),
            'UserTargetSteps':getTargetSteps(),
            'modelDisplayYm':''
        }

    logging.info('Begin Update Vital.')
    page = session.post('https://its-kenpo.mhweb.jp/vital/updateVitalData', verify=False, data=json.dumps(postdata), headers=headers)
    if page.status_code == 200:
        logging.info('Update Vital Success.')
    else:
        logging.info('Update Vital Failed.Code:' + page.status_code)


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
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re
import time
import ITSUpdateMission
import ITSVitalInput

url = 'https://its-kenpo-oauth.mhweb.jp/oauth/login?response_type=code&client_id=NTQxMDI4ZjY3Y2E3ZTNh&redirect_uri=https%3A%2F%2Fits-kenpo.mhweb.jp%2Flogin%2Fcallback'
_token = ''

# リクエストヘッダーを作成
agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
headers = {
    #"Host": "its-kenpo-oauth.mhweb.jp", これは認証用ホスト、認証成功したらホストはits-kenpo.mhweb.jpに変わる、セットしたらずっとこれのまま、ログイン失敗する
    "Referer": url,
    'User-Agent': agent,
}

# cookie情報をロードする
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
   print("Cookie is not loaded")

# token情報をロードする
def get_token():
    index_page = session.get(url, headers=headers, verify=False)
    html = index_page.text
    pattern = r'name="token" type="hidden" value="(.*?)"'
    tokens = re.findall(pattern, html)
   
    return tokens[0]

# ログインする
def login(kigou, bangou, password):
    if len(kigou) == 0 :
        print("kigou is Empty.")
        return False
    elif len(bangou) == 0:
        print("bangou is Empty.")
        return False
    elif len(password) == 0:
        print ("password is Empty")
        return False

    _token = get_token()
    postdata = {
            '_method': 'POST',
            'token': _token,
            'data[User][kigou]': kigou,
            'data[User][bangou]': bangou,
            'data[User][password]': password,
            'x': '46',
            'y': '11'
        }

    headers['Origin'] = 'https://its-kenpo-oauth.mhweb.jp'
    headers['Upgrade-Insecure-Requests'] = '1'

    login_page = session.post(url, verify=False, data=postdata, headers=headers)

    if login_page.status_code == 200 :
        pattern = r'name="__token" content="(.*?)"'
        globals()['_token'] = re.findall(pattern, login_page.text)[0]
        session.cookies.save()
        return True

    return False

# ログアウトする
def logout():
    session.get('https://its-kenpo.mhweb.jp/logout', headers = headers)

#if __name__ == '__main__':
#        if login('','', '') == True:
#           TSUpdateMission.update(session, _token)
#           ITSVitalInput.update(session, _token)

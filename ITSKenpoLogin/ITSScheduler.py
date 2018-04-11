#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Required
Info
- author : "Simon"
- email  : ""
- date   : "2018.4.6"
'''
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import ITSKenpoLogin
import ITSVitalInput
import ITSUpdateMission
import ITSView
import time
import random
import logging
import xml.sax
import os
from LoginInfo import LoginInfo
import MailSender

premonth = 0
logging.basicConfig(filename = 'logger.log', level = logging.INFO, format= '%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s')

logininfo = LoginInfo()

#Job
def job():
    try:
        if ITSKenpoLogin.login(logininfo.kigou,logininfo.bangou,logininfo.password) == True:
            time.sleep(random.randint(3,10))
            ITSUpdateMission.update(ITSKenpoLogin.session, ITSKenpoLogin._token)
            time.sleep(random.randint(5,10))
            ITSVitalInput.update(ITSKenpoLogin.session, ITSKenpoLogin._token)
            time.sleep(random.randint(5,10))

            if globals()['premonth'] != datetime.today().month:
                ITSView.view(ITSKenpoLogin.session, ITSKenpoLogin._token, logininfo.securitycode)
                globals()['premonth'] = datetime.today().month
                time.sleep(random.randint(5,10))

            ITSKenpoLogin.logout()
    except Exception as ex:
        if len(logininfo.mailaddress) != 0 and len(logininfo.mailaddress) != 0:
            MailSender.send(logininfo.mailaddress, logininfo.mailpassword, str(ex))

        logging.error(str(ex))

if __name__ == '__main__':
        if os.path.exists("login.xml"):
            # XMLReader作成
            parser = xml.sax.make_parser()
            # turn off namepsaces
            parser.setFeature(xml.sax.handler.feature_namespaces, 0)
             # ContextHandler
            parser.setContentHandler(logininfo)
            parser.parse("login.xml")

            # スケジュール作成
            sched = BlockingScheduler()
            sched.add_job(job,'cron', day='*', hour='10')
            sched.start()

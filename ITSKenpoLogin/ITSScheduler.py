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
import time
import random

#Job
def job():
    if ITSKenpoLogin.login('','','') == True:
        time.sleep(random.randint(3,10))
        ITSUpdateMission.update(ITSKenpoLogin.session, ITSKenpoLogin._token)
        time.sleep(random.randint(5,10))
        ITSVitalInput.update(ITSKenpoLogin.session, ITSKenpoLogin._token)
        time.sleep(random.randint(5,10))
        ITSKenpoLogin.logout()

try:
    input = raw_input
except:
    pass

if __name__ == '__main__':
        sched = BlockingScheduler()
        sched.add_job(job,'cron', day='*', hour='10')
        sched.start()
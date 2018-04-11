#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Required
- xml.sax
Info
- author : "Simon"
- email  : ""
- date   : "2018.4.11"
'''
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

def create_message(addr, body):
    msg =MIMEText(body)
    msg['Subject'] = "エラー発生"
    msg['From'] = addr
    msg['To'] = addr
    msg['Date'] = formatdate()
    return msg

def send(mail, password, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(mail, password)
    smtpobj.sendmail(mail, mail, create_message(mail, msg).as_string())
    smtpobj.close()
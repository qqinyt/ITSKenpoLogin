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
import xml.sax

class LoginInfo(xml.sax.ContentHandler):
    """description of class"""
    def __init__(self, *args, **kwargs):
        self.kigou = '' # 記号
        self.bangou = '' # 番号
        self.password = '' # パスワード
        self.securitycode = '' # セキュリティコード
        self.mailaddress = '' # メールアドレス
        self.mailpassword = '' # メールパスワード

    def startElement(self, name, attrs):
        self.tag = name

    def endElement(self, name):
        self.tag = ""

    def characters(self, content):
        if self.tag =='kigou':
            self.kigou = content
        elif self.tag == 'bangou':
            self.bangou = content
        elif self.tag  == 'password':
            self.password = content
        elif self.tag == 'securitycode':
            self.securitycode = content
        elif self.tag == 'mailaddress':
            self.mailaddress = content
        elif self.tag == 'mailpassword':
            self.mailpassword = content
        

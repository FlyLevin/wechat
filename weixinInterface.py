#coding:UTF-8

import hashlib
import web
import lxml
import time
import os
import urllib2, json
from lxml import etree

class WeixinInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.tamplates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):

        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr

        #token
        token = "flylevin"

        #directory
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()

        #sha1 encode

        # if the request from wechat, return echostr
        if hashcode == signature:
            return echostr
        else:
            return "Hello"

    def POST(self):
        str_xml = web.data()
        xml = etree.fromstring(str_xml)

        # get the information
        content = xml.find("Content").text
        msgType = xml.find("MsgType").text
        fromUser = xml.find("FromUserName").text
        toUser = xml.find("ToUserName").text

        return self.render.reply_text(fromUser, toUser, int(time.time()), u"Hello what you just said is:"+content)

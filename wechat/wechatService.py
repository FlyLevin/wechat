# -*- coding:utf-8 -*-
import time
from wechatUtil import MessageUtil
from wechatReply import TextReply
from config import *


class WechatService(object):
    """process request"""
    @staticmethod
    def processRequest(request):
        """process different message types.

        :param request: post request message
        :return: None
        """
        requestMap = MessageUtil.parseXml(request)
        fromUserName = requestMap.get(u'FromUserName')
        toUserName = requestMap.get(u'ToUserName')
        createTime = requestMap.get(u'CreateTime')
        msgType = requestMap.get(u'MsgType')
        msgId = requestMap.get(u'MsgId')

        textReply = TextReply()
        textReply.setToUserName(fromUserName)
        textReply.setFromUserName(toUserName)
        textReply.setCreateTime(time.time())
        textReply.setMsgType(RESP_MESSAGE_TYPE_TEXT)

        if msgType == REQ_MESSAGE_TYPE_TEXT:
            content = requestMap.get('Content').decode('utf-8')
            respContent = u'您发送的是文本消息: ' + content
        elif msgType == REQ_MESSAGE_TYPE_IMAGE:
            respContent = u'您发送的是图片消息！'
        elif msgType == REQ_MESSAGE_TYPE_VOICE:
            respContent = u'您发送的是语音消息！'
        elif msgType == REQ_MESSAGE_TYPE_VIDEO:
            respContent = u'您发送的是视频消息！'
        elif msgType == REQ_MESSAGE_TYPE_LOCATION:
            respContent = u'您发送的是地理位置消息！'
        elif msgType == REQ_MESSAGE_TYPE_LINK:
            respContent = u'您发送的是链接消息！'
        elif msgType == REQ_MESSAGE_TYPE_EVENT:
            eventType = requestMap.get(u'Event')
            if eventType == EVENT_TYPE_SUBSCRIBE:
                respContent = u'^_^谢谢您的关注!'
            elif eventType == EVENT_TYPE_UNSUBSCRIBE:
                pass
            elif eventType == EVENT_TYPE_SCAN:
                # TODO
                pass
            elif eventType == EVENT_TYPE_LOCATION:
                # TODO
                pass
            elif eventType == EVENT_TYPE_CLICK:
                # TODO
                pass

        print textReply

        textReply.setContent(respContent)
        respXml = MessageUtil.class2xml(textReply)

        return respXml

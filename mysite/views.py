# -*- coding: utf-8 -*-
# version 1.0 test the reply function in django

# author: Levin

from django.http import HttpResponse
import hashlib
import time
import os
import urllib2,json
from lxml import etree
from django.views.generic.base import View
from django.shortcuts import render, render_to_response
class WeixinInterfaceView(View):
	def get(self, request):
		#get the request content
		signature = request.GET.get('signature', None)
		timestamp = request.GET.get('timestamp', None)
		nonce = request.GET.get('nonce', None)
		echostr = request.GET.get('echostr', None)
		
		#token yourself
		token = 'flylevin'
		
		tmpList = [token, timestamp, nonce]
		tmpList.sort()
		tmpstr = '%s%s%s' % tuple(tmpList)
		#sha1 encode method
		tmpstr = hashlib.sha1(tmpstr).hexdigest()
		
		if tmpstr == signature:
			return render(request, 'get.html', {'str': echostr},
			content_type='text/plain')
			
	def post(self, request):
		str_xml = request.body.decode('utf-8')
		xml = etree.fromstring(str_xml)
		
		toUserName = xml.find('ToUserName').text
		fromUserName = xml.find('FromUserName').text
		createTime = xml.find('CreateTime').text
		msgType = xml.find('MsgType').text
		content = xml.find('Content').text
		msgId = xml.find('MsgId').text
                print msgType, content
		return render_to_response('reply_text.xml', {'toUserName': fromUserName, 'fromUserName': toUserName, 'createTime': time.time(), 'msgType': msgType, 'content': content,})	

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import View
from .wechatUtil import checkSignature
from .wechatService import wechatService


class WechatInterfaceView(View):

    def get(self, request):
        echostr = request.GET.get(u'echostr', None)
        if checkSignature(request):
            return HttpResponse(echostr)

    def post(self, request):
        return HttpResponse(wechatService.processRequest(request))

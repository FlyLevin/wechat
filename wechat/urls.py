from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from wechat import views


urlpatterns = patterns('',
    url(r'^$', csrf_exempt(views.WechatInterfaceView.as_view())),
)

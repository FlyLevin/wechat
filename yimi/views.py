# -*- coding:utf-8 -*-

import sys  
import StringIO  
  
from django.http import HttpResponse  
def syncdb(request):  
    #重定向标准输出重定向到内存的字符串缓冲(由StringIO模块提供)  
    saveout = sys.stdout  
    log_out = StringIO.StringIO()    
    sys.stdout = log_out   
    #利用django提供的命令行工具来执行“manage.py syncdb”  
    from django.core.management import execute_from_command_line  
    execute_from_command_line(["manage.py", "syncdb", "--noinput --v 3"])  
    #获得“manage.py syncdb”的执行输出结果，并展示在页面  
    result = log_out.getvalue()  
    sys.stdout = saveout  
    return HttpResponse(result.replace("\n","<br/>")) 

def migratedb(request):
    #重定向标准输出重定向到内存的字符串缓冲(由StringIO模块提供)  
    saveout = sys.stdout
    log_out = StringIO.StringIO()
    sys.stdout = log_out
    #利用django提供的命令行工具来执行“manage.py syncdb”  
    from django.core.management import execute_from_command_line
    execute_from_command_line(["manage.py", "migrate", "--noinput"]) 
    #获得“manage.py syncdb”的执行输出结果，并展示在页面  
    result = log_out.getvalue()
    sys.stdout = saveout
    return HttpResponse(result.replace("\n","<br/>"))


def createUser(request):
    from django.contrib.auth.models import User
    User.objects.create_user('admin', 'admin@123.com', 'dlovew2009')
    return HttpResponse('Success')

def createCacheTable(request):
    import os, subprocess
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    Manage = os.path.join(BASE_DIR, 'manage.py')
    CMD = 'ls -al '+Manage
    Handle = subprocess.call(CMD, shell=True)
    return HttpResponse(Handle)

# coding: UTF-8
import os

import sae
from yimi import wsgi

import sae from sae.ext.shell import ShellMiddleware

def app():
    manage = os.getcwd() + '/manage.py'
    os.system("python manage shell")

application = sae.create_wsgi_app(ShellMiddleware(app))
#application = sae.create_wsgi_app(wsgi.application)

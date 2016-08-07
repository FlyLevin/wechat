# coding: UTF-8
import os

import sae
#from yimi import wsgi

from sae.ext.shell import ShellMiddleware

def app(environ, start_response):

    status = '200 OK' 
    response_headers = [('Content-type', 'text/plain')] 
    start_response(status, response_headers)
    return ["Hello, world!"]

application = sae.create_wsgi_app(ShellMiddleware(app))
#application = sae.create_wsgi_app(wsgi.application)

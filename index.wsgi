# coding: UTF-8
import os

import sae
from mysite import wsgi

application = sae.create_wsgi_app(wsgi.application)

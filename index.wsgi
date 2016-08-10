# coding: UTF-8
import os

import sae
from yimi import wsgi

application = sae.create_wsgi_app(wsgi.application)

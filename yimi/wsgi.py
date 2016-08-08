#!/usr/bin/env python
#coding:utf8

import os
import sys
reload(sys)

#import django
#django.setup()

sys.setdefaultencoding('utf-8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yimi.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

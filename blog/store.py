#! coding:utf-8

import itertools 
import sae.storage
from datetime import datetime
from os.path import basename, splitext
from sae.const import APP_NAME
from django.conf import settings
from django.core.files.storage import Storage
from django.utils.http import urlquote

class SaeStorage(Storage):
    """
    SAE Storage
    """
    def __init__(self, domain = None, app = None):
        if app is None:
            app = APP_NAME
        if domain is None:
            domain = settings.SAE_STORAGE_DOMAIN
        self.domain = domain
        self.base_url = "%s-%s.stor.sinaapp.com/"% (app, self.domain)
        self.client = sae.storage.Client()

    def _open(self, name, mode='rb'):
        raise sae.storage.PermissionDeniedError('Not allow to do this')

    def _save(self, name, content):
        name = self.get_available_name(name)
        data = ''.join(content.chunks())
        ob = sae.storage.Object(data)
        return self.client.put(self.domain, name, ob)

    def delete(self, name):
        return self.delete(self.domain, name)

    def exists(self, name):
        return name in [ob['name'] for ob in self.client.list(self.domain)]

    def listdir(self, path):
        return [ob['name'] for ob in self.client.list(self.domain)]

    def path(self, name):
        return self.url

    def size(self, name):
        ob = self.client.stat(self.domain, name)
        return ob['length']

    def url(self, name):
        url = self.client.url(self.domain, name)
        return url.replace(urlquote(self.base_url), '')

    def accessed_time(self, name):
        ob = self.client.stat(self.domain, name)
        return datetime.fromtimestamp(ob['datetime'])

    def modified_time(self, name):
        return self.created_time()

    def get_available_name(self, name):
        count = itertools.count(1)
        while name in (ob['name'] for ob in self.client.list(self.domain)):
            file_root, file_ext = splitext(basename(name))
            name = '%s_%s%s' % (file_root, count.next(), file_ext)
        return name



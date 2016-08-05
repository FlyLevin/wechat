from config import *

import hashlib
from lxml import etree


def checkSignature(request):
    """check signature.

    :param request: get method
    :return: if success return True else False
    """
    signature = request.GET.get(u'signature', None)
    timestamp = request.GET.get(u'timestamp', None)
    nonce = request.GET.get(u'nonce', None)
    token = TOKEN 

    tmplist = [token, timestamp, nonce]
    tmplist.sort()
    tmpstr = '%s%s%s' % tuple(tmplist)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()

    if tmpstr == signature:
        return True
    else:
        return False

class MessageUtil(object):
    @staticmethod
    def parseXml(request):
        """parse request post xml message.

        :param request: post request
        :return: dict of xml message
        """
        raw_xml = request.body.decode(u'UTF-8')
        xmlstr = etree.fromstring(raw_xml)
        dict_xml = {}
        for child in xmlstr:
            dict_xml[child.tag] = child.text.encode(u'UTF-8')    # note
        return dict_xml



    @staticmethod
    def class2xml(obj):
        """convert reply message class to xml.

        :param obj: reply message class' object
        :return: xml of the object
        """
        root = etree.Element(u'xml')
        for key, value in vars(obj).items():
            if key in MESSAGETYPE:
                tmproot = etree.SubElement(root, key)
                if key == u'Articles':    # solve Article, it's special
                    for eachArticle in value:
                        etree.SubElement(tmproot, u'item')
                        for tmpkey, tmpvalue in vars(eachArticle).items():
                            tmpkey_ele = etree.SubElement(tmproot, tmpkey)
                            tmpkey_ele.text = etree.CDATA(unicode(tmpvalue))
                else:
                    for tmpkey, tmpvalue in vars(obj.__getattribute__(key)).items():
                        tmpkey_ele = etree.SubElement(tmproot, tmpkey)
                    if u'time' in tmpkey.lower() or u'count' in tmpkey.lower():
                        tmpkey_ele.text = unicode(tmpvalue)
                    else:    # CDATA tag for str
                        tmpkey_ele.text = etree.CDATA(unicode(tmpvalue))
            else:
                if u'time' in key.lower() or u'count' in key.lower():
                    etree.SubElement(root, key).text = unicode(value)
                else:
                    etree.SubElement(root, key).text = etree.CDATA(unicode(value))

        return etree.tostring(root, pretty_print=True, xml_declaration=False, encoding=u'utf-8')

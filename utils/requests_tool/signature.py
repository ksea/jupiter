#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/1  15:10
# @Author  : tzy
# @FileName: signature.py
"""
    Description:
        
"""
import base64
import hashlib
import hmac
import time
import urllib.parse
from hashlib import sha1


def md5_code(**kwargs):
    if kwargs.get('json'):
        json_test1 = kwargs.get('json').encode('utf-8')
        content_md5 = hashlib.md5(json_test1)
        content_md5_64 = base64.b64encode(content_md5.digest()).decode('utf-8')
        print("content_md5_64:" + content_md5_64)
    else:
        content_md5_64 = ''

    return content_md5_64


def cononical_resource(content_md5_64, **kwargs):

    if kwargs.get('json'):
        # cononical_string = "%s\n%s\n%s\n%d\n%s" % (kws.get('method') + content_md5_64 + kws.get('Content-Type')
        # + kws.get('expires') + kws.get('path'))
        cononical_string = kwargs.get('method') + "\n" + content_md5_64 + \
                           "\n" + kwargs.get('Content-Type') + "\n" + kwargs.get('expires') + "\n" + kwargs.get('path')

    else:
        # cononical_string = "%s\n\n\n%d\n%s" % (kws.get('method'), kws.get('expires'), kws.get('path'))
        cononical_string = kwargs.get('method') + "\n" + "\n" + "\n" + kwargs.get('expires') + "\n" + kwargs.get('path')
        # print('+++++path:+++++' + kws.get('path'))

    return cononical_string


def time_expires(num):
    # 1、本地时间
    local_time = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
    # print(local_time)

    # 1、 当前时间戳
    time_now = time.time()
    expires = time_now + num * 600
    # print(int(expires))
    # print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime(expires)))

    return int(expires)


def signature(accesskey_id_test, accesskey_screat_test, host_test, **kwargs):
    # 计算  content
    # print(kws)
    content_md5_64 = md5_code(**kwargs)
    # print('content_md5_64:' + content_md5_64)

    # 计算canonical_string:
    cononical_string = cononical_resource(content_md5_64, **kwargs)
    # print('cononical_string:' + cononical_string)

    # 计算signature
    cononical_string_test = cononical_string.encode('utf-8')
    hash_sha1 = hmac.new(accesskey_screat_test.encode('utf-8'), cononical_string_test, sha1).digest()
    signature_test = base64.b64encode(hash_sha1).decode('utf-8')
    print('signature_test:' + signature_test)

    s = urllib.parse.quote(signature_test)
    # print("-----s-----:" + s)

    # return signature_test
    return s
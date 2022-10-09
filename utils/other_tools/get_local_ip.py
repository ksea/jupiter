#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/9  14:52
# @Author  : tzy
# @FileName: get_local_ip.py
"""
    Description:
        
"""
import socket


def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    _s = None
    try:
        _s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _s.connect(('8.8.8.8', 80))
        host = _s.getsockname()[0]
    finally:
        _s.close()

    return host

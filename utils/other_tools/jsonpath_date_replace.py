#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/9  15:34
# @Author  : tzy
# @FileName: jsonpath_date_replace.py
"""
    Description:
        
"""


def jsonpath_replace(change_data, key_name, data_switch=None):
    """处理jsonpath数据"""
    _new_data = key_name + ''
    for i in change_data:
        if i == '$':
            pass
        elif data_switch is None and i == "data":
            _new_data += '.data'
        elif i[0] == '[' and i[-1] == ']':
            _new_data += "[" + i[1:-1] + "]"
        else:
            _new_data += '[' + '"' + i + '"' + "]"
    return _new_data


if __name__ == '__main__':
    jsonpath_replace(change_data=['$', 'data', 'id'], key_name='self.__yaml_case')

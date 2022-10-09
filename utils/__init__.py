#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/9  14:46
# @Author  : tzy
# @FileName: __init__.py
"""
    Description:
        
"""

from utils.read_files_tools.yaml_handler import GetYamlData
from common.setting import ensure_path_sep
from utils.other_tools.models import Config

_data = GetYamlData(ensure_path_sep("\\common\\config.yaml")).get_yaml_data()
config = Config(**_data)
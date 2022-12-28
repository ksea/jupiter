#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022-12-02 11:40:18


import allure
import pytest
from utils.read_files_tools.get_yaml_data_analysis import GetTestCase
from utils.assertion.assert_handler import Assert
from utils.requests_tool.request_handler import RequestHandler
from utils.read_files_tools.regular_handler import regular
from utils.requests_tool.teardown_handler import TearDownHandler


case_id = ['biz_portal_content_01']
TestData = GetTestCase.case_data(case_id)
re_data = regular(str(TestData))


@allure.epic("biz-portal-api")
@allure.feature("Taurus")
class TestTaurus:

    @allure.story("课程")
    @pytest.mark.parametrize('in_data', eval(re_data), ids=[i['detail'] for i in TestData])
    def test_taurus(self, in_data, case_skip):
        """
        :param :
        :return:
        """
        res = RequestHandler(in_data).http_request()
        TearDownHandler(res).teardown_handle()
        Assert(in_data['assert_data']).assert_equality(response_data=res.response_data,
                                                       sql_data=res.sql_data, status_code=res.status_code)


if __name__ == '__main__':
    pytest.main(['test_taurus.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])

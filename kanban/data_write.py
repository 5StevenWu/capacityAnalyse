#!/usr/bin/env python3

import os, sys
from datetime import datetime, timedelta

ret = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ret)
# print("环境变量信息:%s" % sys)

from kanban.data_req import kanban_req
from kanban.data7 import day7 as dayseven
from kanban.data_ana import realtimebalance




def week():
    '''
    :return:
    '''
    day = datetime.now().strftime("%Y-%m-%d")
    rightday = datetime.now() + timedelta(days=-3)
    # 必须是周一  非周一适量调整timedelta
    print("本周一是:", rightday.strftime("%Y-%m-%d"))
    return dayseven(rightday)


day7 = week()

req_lst = []


def req_all():
    for d in range(len(day7) - 1):  # 从上上周日开始循环
        # print(day7[d+1])
        #if day7[d + 1] == '2021-08-29':
            # print("开始进行%s的数据处理" % str(day7[d + 1]), str(day7[d]))  # 默认day为前一天
        one_day_data = kanban_req(day7[d + 1])  # 爬取数据
        # print(one_day_data)
        one_day_data = realtimebalance(one_day_data, day7[d + 1], day7[d])  # 解析数据
        req_lst.append({day7[d + 1]: one_day_data})  # 添加到列表
    return req_lst


if __name__ == '__main__':
    print("\r\n\r\n")
    print("爬取解析最终总结果:\t%s" % str(req_all()))
    # print(2)

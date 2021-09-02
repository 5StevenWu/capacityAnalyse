#!/usr/bin/env python3

from kanban.data_req import kanban_req
from kanban.data7 import day7
from datetime import datetime, timedelta


def week():
    '''
    :return:
    '''
    day = datetime.now().strftime("%Y-%m-%d")
    rightday = datetime.now() + timedelta(days=-3)
    # 必须是周一  非周一适量调整timedelta
    print("本周一是:", rightday.strftime("%Y-%m-%d"))
    return day7(rightday)


day7 = week()

req_all = []


def req_all():
    for d in day7:
        one_day_data = kanban_req(day=d)
        req_all.append(one_day_data)
    return req_all


print(req_all)

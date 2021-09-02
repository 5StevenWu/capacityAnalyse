#!/usr/bin/env python3

# 爬取单天数据信息
# {'LoadbalanceData': [588, '1.04%', 61, '13.17%', 50, '21.10%', 60, '0.00%'], 'samecoverdata': [1099, 1577, 896, '56.82%', 612, '55.69%', 2790, '99.10%']}

from datetime import datetime, timedelta

def  day7(rightday):

    lastsunday=(rightday + timedelta(days=-8)).strftime("%Y-%m-%d")
    monday = (rightday + timedelta(days=-7)).strftime("%Y-%m-%d")
    tuesday = (rightday + timedelta(days=-6)).strftime("%Y-%m-%d")
    wednesday = (rightday + timedelta(days=-5)).strftime("%Y-%m-%d")
    thursday = (rightday + timedelta(days=-4)).strftime("%Y-%m-%d")
    friday = (rightday + timedelta(days=-3)).strftime("%Y-%m-%d")
    saturday = (rightday + timedelta(days=-2)).strftime("%Y-%m-%d")
    sunday = (rightday + timedelta(days=-1)).strftime("%Y-%m-%d")

    week = [lastsunday,monday, tuesday, wednesday, thursday, friday, saturday, sunday]
    print(week)
    return week

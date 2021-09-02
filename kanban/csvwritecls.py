#!/usr/bin/env python3

# 爬取单天数据信息
# {'LoadbalanceData': [588, '1.04%', 61, '13.17%', 50, '21.10%', 60, '0.00%'], 'samecoverdata': [1099, 1577, 896, '56.82%', 612, '55.69%', 2790, '99.10%']}

from datetime import datetime, timedelta

day = datetime.now().strftime("%Y-%m-%d")
yday = datetime.now() + timedelta(days=-1)

monday = datetime.now() + timedelta(days=-7)
tuesday = datetime.now() + timedelta(days=-6)
wednesday = datetime.now() + timedelta(days=-5)
thursday = datetime.now() + timedelta(days=-4)
friday = datetime.now() + timedelta(days=-3)
saturday = datetime.now() + timedelta(days=-2)
sunday = datetime.now() + timedelta(days=-1)
print(day, yday)

#!/usr/bin/env python3

import pandas as pd
from kanban.data_writeF import req_all
# df = pd.
# all_data = [{'2021-10-11': {'LoadbalanceData': [74, '0.26%', 0, '0.00%', 0, '0.00%', 0, '0.00%'],
#                             'samecoverdata': [1039, 1065, 1034, '97.09%', 623, '59.96%', 2602, '98.69%']}}, {
#                 '2021-10-12': {'LoadbalanceData': [115, '0.23%', 6, '5.56%', 0, '0.00%', 9, '100.00%'],
#                                'samecoverdata': [1646, 2263, 2154, '95.18%', 1274, '77.40%', 5366, '99.25%']}}, {
#                 '2021-10-13': {'LoadbalanceData': [564, '0.94%', 103, '21.50%', 4, '0.00%', 177, '93.22%'],
#                                'samecoverdata': [1898, 2364, 2182, '92.30%', 1369, '72.13%', 5721, '96.45%']}}, {
#                 '2021-10-14': {'LoadbalanceData': [459, '0.77%', 74, '17.75%', 69, '1150.00%', 121, '90.91%'],
#                                'samecoverdata': [2134, 2494, 2280, '91.42%', 1478, '69.26%', 6064, '96.24%']}}, {
#                 '2021-10-15': {'LoadbalanceData': [482, '0.81%', 61, '14.63%', 46, '44.66%', 97, '97.94%'],
#                                'samecoverdata': [2254, 2715, 2494, '91.86%', 1601, '71.03%', 6746, '95.23%']}}, {
#                 '2021-10-16': {'LoadbalanceData': [494, '0.83%', 71, '16.32%', 32, '43.24%', 98, '100.00%'],
#                                'samecoverdata': [2251, 2701, 2508, '92.85%', 1617, '71.83%', 6726, '96.21%']}}, {
#                 '2021-10-17': {'LoadbalanceData': [484, '0.82%', 65, '15.93%', 43, '70.49%', 97, '97.94%'],
#                                'samecoverdata': [2236, 2619, 2411, '92.06%', 1611, '72.05%', 6494, '96.35%']}}]
all_data=req_all()

def alldataana(all_data):
    for one in all_data:
        for day, data in one.items():
            # print(day, data)
            print(',' + str(day), end='')
            for _, d in data.items():
                # print(d)
                for i in d:
                    print(',' + str(i), end='')
                # print()
            print("\r")


if __name__ == '__main__':
    alldataana(all_data)

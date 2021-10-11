#!/usr/bin/env python3

import pandas as pd


# df = pd.
all_data =[{'2021-10-04': {'LoadbalanceData': [117, '0.48%', 0, '0.00%', 0, '0.00%', 0, '0.00%'], 'samecoverdata': [934, 0, 0, '0.00%', 609, '65.20%', 0, '0.00%']}}, {'2021-10-05': {'LoadbalanceData': [101, '2.20%', 0, '0.00%', 0, '0.00%', 0, '0.00%'], 'samecoverdata': [807, 0, 0, '0.00%', 525, '65.06%', 0, '0.00%']}}, {'2021-10-06': {'LoadbalanceData': [87, '1.90%', 0, '0.00%', 0, '0.00%', 0, '0.00%'], 'samecoverdata': [729, 0, 0, '0.00%', 495, '67.90%', 0, '0.00%']}}, {'2021-10-07': {'LoadbalanceData': [85, '1.86%', 1, '1.08%', 0, '0.00%', 0, '0.00%'], 'samecoverdata': [650, 0, 0, '0.00%', 436, '67.08%', 0, '0.00%']}}, {'2021-10-08': {'LoadbalanceData': [60, '1.31%', 0, '0.00%', 0, '0.00%', 0, '0.00%'], 'samecoverdata': [677, 1116, 1113, '99.73%', 611, '90.25%', 2847, '100.00%']}}, {'2021-10-09': {'LoadbalanceData': [66, '1.44%', 0, '0.00%', 0, '0.00%', 0, '0.00%'], 'samecoverdata': [636, 1024, 986, '96.29%', 563, '88.52%', 2546, '100.00%']}}, {'2021-10-10': {'LoadbalanceData': [75, '1.64%', 0, '0.00%', 0, '0.00%', 0, '0.00%'], 'samecoverdata': [961, 1075, 1040, '96.74%', 614, '63.89%', 2711, '97.60%']}}]

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

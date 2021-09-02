#!/usr/bin/env python3


def realtimebalance(res, updatetime, beforeDay):
    LoadbalanceDataCount_Y = res.get("LoadbalanceDataCount_Y")
    SamecoverDataCount = res.get("SamecoverDataCount")

    everydaydata_dic = {}

    unbalances = 0
    unbalances_one = 0
    adjusteds = 0
    finished = 0
    alllogs = 0
    samecoverxiaoqus_one = 0
    condit3 = 0
    unbalances_1 = 0
    unbalances_1_y = 0
    successlogs = 0
    for S in SamecoverDataCount:
        # print("初始数据",S)
        if S.get("updatetime") == updatetime:
            # print("当天数据", S)
            unbalances_one += S.get("unbalances_one")
            unbalances += S.get("unbalances")
            adjusteds += S.get("adjusteds")
            finished += S.get("finished")
            alllogs += S.get("alllogs")
            unbalances_1 += S.get("unbalances_1")
            samecoverxiaoqus_one += S.get("samecoverxiaoqus_one")
            successlogs += S.get("successlogs")
        elif S.get("updatetime") == beforeDay:
            unbalances_1_y += S.get("unbalances_1")

    finishedRate = finished / unbalances_1_y  # 垂直均衡闭环(闭环占比)
    daylogs_successRate = successlogs / alllogs  # 垂直面均衡工单执行情况(成功率)

    # 对应前端垂直平面第一行8条数据
    print(unbalances_one, "%.2f%%" % (unbalances_one / samecoverxiaoqus_one * 100),
          adjusteds, "%.2f%%" % (adjusteds / unbalances * 100),
          finished, "%.2f%%" % (finishedRate * 100),
          alllogs, "%.2f%%" % (daylogs_successRate * 100),
          )
    loadbalancedata = {"LoadbalanceData": [unbalances_one, "%.2f%%" % (unbalances_one / samecoverxiaoqus_one * 100),
                                           adjusteds, "%.2f%%" % (adjusteds / unbalances * 100),
                                           finished, "%.2f%%" % (finishedRate * 100),
                                           alllogs, "%.2f%%" % (daylogs_successRate * 100), ]}
    everydaydata_dic.update(loadbalancedata)

    countxiaoqu = 0
    countlimit = 0
    countyx = 0
    countlogs = 0
    countsuccesslogs = 0
    countback = 0
    countadjust = 0

    for L in LoadbalanceDataCount_Y:
        if L.get("updatetime") == updatetime:
            # print(L)
            countxiaoqu += L.get("countxiaoqu")
            countlimit += L.get("countlimit")
            countyx += L.get("countyx")
            countlogs += L.get("countlogs")
            countsuccesslogs += L.get("countsuccesslogs")
            countback += L.get("countback")
            countadjust += L.get("countadjust")
        # print(L.get("countxiaoqu"))

    print(
        "水平面均衡优化高负荷小区数\t", countxiaoqu,
        "\n邻区对数\t", countadjust,

        "\n水平面均衡回调\t", countback,
        "\n回调占比\t", "%.2f%%" % (countback / countadjust * 100),

        "\n水平面均衡有效情况\t", countyx,
        "\n有效率\t", "%.2f%%" % (countyx / countxiaoqu * 100),

        "\n水平面均衡工单执行情况\t", countlogs,
        "\n成功率\t", "%.2f%%" % (countsuccesslogs / countlogs * 100),

    )
    samecoverdata = {
        "samecoverdata": [countxiaoqu, countadjust, countback, "%.2f%%" % (countback / countadjust * 100), countyx,
                          "%.2f%%" % (countyx / countxiaoqu * 100), countlogs,
                          "%.2f%%" % (countsuccesslogs / countlogs * 100), ]}
    everydaydata_dic.update(samecoverdata)
    return everydaydata_dic


if __name__ == '__main__':
    res = {'LoadbalanceDataCount_Y': [
        {'countxiaoqu': 418, 'countlimit': 0, 'countyx': 149, 'countadjust': 647, 'countlogs': 759,
         'countsuccesslogs': 756,
         'city': '咸宁市', 'updatetime': '2021-08-29', 'countback': 49, 'id': 1221},
        {'countxiaoqu': 129, 'countlimit': 0, 'countyx': 110, 'countadjust': 218, 'countlogs': 469,
         'countsuccesslogs': 469,
         'city': '宜昌市', 'updatetime': '2021-08-29', 'countback': 197, 'id': 1222},
        {'countxiaoqu': 33, 'countlimit': 0, 'countyx': 25, 'countadjust': 44, 'countlogs': 95, 'countsuccesslogs': 95,
         'city': '恩施州', 'updatetime': '2021-08-29', 'countback': 41, 'id': 1223},
        {'countxiaoqu': 1, 'countlimit': 0, 'countyx': 0, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
         'city': '恩施市', 'updatetime': '2021-08-29', 'countback': 0, 'id': 1224},
        {'countxiaoqu': 205, 'countlimit': 0, 'countyx': 180, 'countadjust': 361, 'countlogs': 759,
         'countsuccesslogs': 758,
         'city': '武汉市', 'updatetime': '2021-08-29', 'countback': 331, 'id': 1225},
        {'countxiaoqu': 2, 'countlimit': 0, 'countyx': 0, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
         'city': '江汉市', 'updatetime': '2021-08-29', 'countback': 0, 'id': 1226},
        {'countxiaoqu': 1, 'countlimit': 0, 'countyx': 0, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
         'city': '潜江市', 'updatetime': '2021-08-29', 'countback': 0, 'id': 1227},
        {'countxiaoqu': 1, 'countlimit': 0, 'countyx': 1, 'countadjust': 2, 'countlogs': 4, 'countsuccesslogs': 4,
         'city': '荆州市', 'updatetime': '2021-08-29', 'countback': 2, 'id': 1228},
        {'countxiaoqu': 86, 'countlimit': 0, 'countyx': 77, 'countadjust': 132, 'countlogs': 272,
         'countsuccesslogs': 272,
         'city': '荆门市', 'updatetime': '2021-08-29', 'countback': 119, 'id': 1229},
        {'countxiaoqu': 176, 'countlimit': 0, 'countyx': 31, 'countadjust': 109, 'countlogs': 289,
         'countsuccesslogs': 268,
         'city': '鄂州市', 'updatetime': '2021-08-29', 'countback': 102, 'id': 1230},
        {'countxiaoqu': 47, 'countlimit': 0, 'countyx': 39, 'countadjust': 64, 'countlogs': 143,
         'countsuccesslogs': 143,
         'city': '随州市', 'updatetime': '2021-08-29', 'countback': 55, 'id': 1231},
        {'countxiaoqu': 445, 'countlimit': 0, 'countyx': 147, 'countadjust': 625, 'countlogs': 667,
         'countsuccesslogs': 667,
         'city': '咸宁市', 'updatetime': '2021-08-30', 'countback': 4, 'id': 1236},
        {'countxiaoqu': 2, 'countlimit': 0, 'countyx': 0, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
         'city': '天门市', 'updatetime': '2021-08-30', 'countback': 0, 'id': 1237},
        {'countxiaoqu': 1, 'countlimit': 0, 'countyx': 0, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
         'city': '孝感市', 'updatetime': '2021-08-30', 'countback': 0, 'id': 1238},
        {'countxiaoqu': 196, 'countlimit': 0, 'countyx': 164, 'countadjust': 261, 'countlogs': 525,
         'countsuccesslogs': 524,
         'city': '宜昌市', 'updatetime': '2021-08-30', 'countback': 230, 'id': 1239},
        {'countxiaoqu': 54, 'countlimit': 0, 'countyx': 39, 'countadjust': 74, 'countlogs': 157,
         'countsuccesslogs': 157,
         'city': '恩施州', 'updatetime': '2021-08-30', 'countback': 59, 'id': 1240},
        {'countxiaoqu': 1, 'countlimit': 0, 'countyx': 1, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
         'city': '恩施市', 'updatetime': '2021-08-30', 'countback': 0, 'id': 1241},
        {'countxiaoqu': 195, 'countlimit': 0, 'countyx': 174, 'countadjust': 306, 'countlogs': 680,
         'countsuccesslogs': 679,
         'city': '武汉市', 'updatetime': '2021-08-30', 'countback': 260, 'id': 1242},
        {'countxiaoqu': 11, 'countlimit': 0, 'countyx': 0, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
         'city': '江汉市', 'updatetime': '2021-08-30', 'countback': 0, 'id': 1243},
        {'countxiaoqu': 1, 'countlimit': 0, 'countyx': 0, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
         'city': '潜江市', 'updatetime': '2021-08-30', 'countback': 0, 'id': 1244},
        {'countxiaoqu': 118, 'countlimit': 0, 'countyx': 99, 'countadjust': 150, 'countlogs': 309,
         'countsuccesslogs': 309,
         'city': '荆门市', 'updatetime': '2021-08-30', 'countback': 133, 'id': 1245},
        {'countxiaoqu': 83, 'countlimit': 0, 'countyx': 67, 'countadjust': 113, 'countlogs': 229,
         'countsuccesslogs': 229,
         'city': '襄阳市', 'updatetime': '2021-08-30', 'countback': 84, 'id': 1246},
        {'countxiaoqu': 530, 'countlimit': 0, 'countyx': 99, 'countadjust': 253, 'countlogs': 675,
         'countsuccesslogs': 566,
         'city': '鄂州市', 'updatetime': '2021-08-30', 'countback': 173, 'id': 1247},
        {'countxiaoqu': 61, 'countlimit': 0, 'countyx': 53, 'countadjust': 93, 'countlogs': 200,
         'countsuccesslogs': 200,
         'city': '随州市', 'updatetime': '2021-08-30', 'countback': 87, 'id': 1248}], 'SamecoverDataCount': [
        {'unbalances': 33, 'adjusteds': 20, 'finished': 15, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 20, 'successlogs': 0, 'unbalances_1': 23, 'samecoverxiaoqus': 1703, 'unbalances_one': 46,
         'samecoverxiaoqus_one': 3055, 'countyx_1': 0, 'city': '咸宁市', 'updatetime': '2021-08-28', 'id': 1519},
        {'unbalances': 55, 'adjusteds': 51, 'finished': 38, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 48, 'successlogs': 8, 'unbalances_1': 52, 'samecoverxiaoqus': 4447, 'unbalances_one': 59,
         'samecoverxiaoqus_one': 6035, 'countyx_1': 0, 'city': '荆州市', 'updatetime': '2021-08-28', 'id': 1520},
        {'unbalances': 92, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 2542, 'unbalances_one': 96,
         'samecoverxiaoqus_one': 4514,
         'countyx_1': 0, 'city': '十堰市', 'updatetime': '2021-08-28', 'id': 1521},
        {'unbalances': 2, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 1831, 'unbalances_one': 0,
         'samecoverxiaoqus_one': 3850,
         'countyx_1': 0, 'city': '孝感市', 'updatetime': '2021-08-28', 'id': 1522},
        {'unbalances': 41, 'adjusteds': 0, 'finished': 13, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 21, 'samecoverxiaoqus': 2272, 'unbalances_one': 51,
         'samecoverxiaoqus_one': 4979,
         'countyx_1': 0, 'city': '宜昌市', 'updatetime': '2021-08-28', 'id': 1523},
        {'unbalances': 27, 'adjusteds': 0, 'finished': 14, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 21, 'samecoverxiaoqus': 1329, 'unbalances_one': 38,
         'samecoverxiaoqus_one': 3074,
         'countyx_1': 0, 'city': '恩施州', 'updatetime': '2021-08-28', 'id': 1524},
        {'unbalances': 77, 'adjusteds': 0, 'finished': 20, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 40, 'samecoverxiaoqus': 9729, 'unbalances_one': 144,
         'samecoverxiaoqus_one': 14947, 'countyx_1': 0, 'city': '武汉市', 'updatetime': '2021-08-28', 'id': 1525},
        {'unbalances': 23, 'adjusteds': 0, 'finished': 27, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 34, 'samecoverxiaoqus': 1273, 'unbalances_one': 27,
         'samecoverxiaoqus_one': 3057,
         'countyx_1': 0, 'city': '荆门市', 'updatetime': '2021-08-28', 'id': 1526},
        {'unbalances': 51, 'adjusteds': 0, 'finished': 16, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 31, 'samecoverxiaoqus': 2553, 'unbalances_one': 63,
         'samecoverxiaoqus_one': 5314,
         'countyx_1': 0, 'city': '襄阳市', 'updatetime': '2021-08-28', 'id': 1527},
        {'unbalances': 5, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 725, 'unbalances_one': 5,
         'samecoverxiaoqus_one': 1150,
         'countyx_1': 0, 'city': '鄂州市', 'updatetime': '2021-08-28', 'id': 1528},
        {'unbalances': 24, 'adjusteds': 0, 'finished': 7, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 15, 'samecoverxiaoqus': 938, 'unbalances_one': 18,
         'samecoverxiaoqus_one': 2068,
         'countyx_1': 0, 'city': '随州市', 'updatetime': '2021-08-28', 'id': 1529},
        {'unbalances': 3, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 2129, 'unbalances_one': 3,
         'samecoverxiaoqus_one': 4477,
         'countyx_1': 0, 'city': '黄冈市', 'updatetime': '2021-08-28', 'id': 1530},
        {'unbalances': 1, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 1150, 'unbalances_one': 1,
         'samecoverxiaoqus_one': 2358,
         'countyx_1': 0, 'city': '黄石市', 'updatetime': '2021-08-28', 'id': 1531},
        {'unbalances': 36, 'adjusteds': 28, 'finished': 12, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 28, 'successlogs': 0, 'unbalances_1': 20, 'samecoverxiaoqus': 1693, 'unbalances_one': 44,
         'samecoverxiaoqus_one': 3054, 'countyx_1': 0, 'city': '咸宁市', 'updatetime': '2021-08-29', 'id': 1534},
        {'unbalances': 34, 'adjusteds': 33, 'finished': 38, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 32, 'successlogs': 0, 'unbalances_1': 51, 'samecoverxiaoqus': 4431, 'unbalances_one': 47,
         'samecoverxiaoqus_one': 6036, 'countyx_1': 0, 'city': '荆州市', 'updatetime': '2021-08-29', 'id': 1535},
        {'unbalances': 85, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 2540, 'unbalances_one': 85,
         'samecoverxiaoqus_one': 4517,
         'countyx_1': 0, 'city': '十堰市', 'updatetime': '2021-08-29', 'id': 1536},
        {'unbalances': 3, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 1842, 'unbalances_one': 3,
         'samecoverxiaoqus_one': 3850,
         'countyx_1': 0, 'city': '孝感市', 'updatetime': '2021-08-29', 'id': 1537},
        {'unbalances': 42, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 2260, 'unbalances_one': 55,
         'samecoverxiaoqus_one': 4980,
         'countyx_1': 0, 'city': '宜昌市', 'updatetime': '2021-08-29', 'id': 1538},
        {'unbalances': 24, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 1320, 'unbalances_one': 29,
         'samecoverxiaoqus_one': 3074,
         'countyx_1': 0, 'city': '恩施州', 'updatetime': '2021-08-29', 'id': 1539},
        {'unbalances': 96, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 9645, 'unbalances_one': 156,
         'samecoverxiaoqus_one': 14953, 'countyx_1': 0, 'city': '武汉市', 'updatetime': '2021-08-29', 'id': 1540},
        {'unbalances': 32, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 1267, 'unbalances_one': 38,
         'samecoverxiaoqus_one': 3057,
         'countyx_1': 0, 'city': '荆门市', 'updatetime': '2021-08-29', 'id': 1541},
        {'unbalances': 73, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 2533, 'unbalances_one': 93,
         'samecoverxiaoqus_one': 5312,
         'countyx_1': 0, 'city': '襄阳市', 'updatetime': '2021-08-29', 'id': 1542},
        {'unbalances': 13, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 723, 'unbalances_one': 14,
         'samecoverxiaoqus_one': 1150,
         'countyx_1': 0, 'city': '鄂州市', 'updatetime': '2021-08-29', 'id': 1543},
        {'unbalances': 24, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 931, 'unbalances_one': 24,
         'samecoverxiaoqus_one': 2068,
         'countyx_1': 0, 'city': '随州市', 'updatetime': '2021-08-29', 'id': 1544},
        {'unbalances': 1, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 2098, 'unbalances_one': 0,
         'samecoverxiaoqus_one': 4476,
         'countyx_1': 0, 'city': '黄冈市', 'updatetime': '2021-08-29', 'id': 1545},
        {'unbalances': 37, 'adjusteds': 25, 'finished': 17, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 25, 'successlogs': 0, 'unbalances_1': 28, 'samecoverxiaoqus': 1701, 'unbalances_one': 40,
         'samecoverxiaoqus_one': 3055, 'countyx_1': 0, 'city': '咸宁市', 'updatetime': '2021-08-30', 'id': 1549},
        {'unbalances': 57, 'adjusteds': 54, 'finished': 24, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 16, 'successlogs': 16, 'unbalances_1': 33, 'samecoverxiaoqus': 4470, 'unbalances_one': 56,
         'samecoverxiaoqus_one': 6035, 'countyx_1': 0, 'city': '荆州市', 'updatetime': '2021-08-30', 'id': 1550},
        {'unbalances': 102, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 2537, 'unbalances_one': 108,
         'samecoverxiaoqus_one': 4515,
         'countyx_1': 0, 'city': '十堰市', 'updatetime': '2021-08-30', 'id': 1551},
        {'unbalances': 2, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 1870, 'unbalances_one': 2,
         'samecoverxiaoqus_one': 3850,
         'countyx_1': 0, 'city': '孝感市', 'updatetime': '2021-08-30', 'id': 1552},
        {'unbalances': 39, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 2275, 'unbalances_one': 53,
         'samecoverxiaoqus_one': 4982,
         'countyx_1': 0, 'city': '宜昌市', 'updatetime': '2021-08-30', 'id': 1553},
        {'unbalances': 34, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 1331, 'unbalances_one': 36,
         'samecoverxiaoqus_one': 3074,
         'countyx_1': 0, 'city': '恩施州', 'updatetime': '2021-08-30', 'id': 1554},
        {'unbalances': 96, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 9757, 'unbalances_one': 138,
         'samecoverxiaoqus_one': 14943, 'countyx_1': 0, 'city': '武汉市', 'updatetime': '2021-08-30', 'id': 1555},
        {'unbalances': 30, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 1298, 'unbalances_one': 36,
         'samecoverxiaoqus_one': 3057,
         'countyx_1': 0, 'city': '荆门市', 'updatetime': '2021-08-30', 'id': 1556},
        {'unbalances': 60, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 2559, 'unbalances_one': 74,
         'samecoverxiaoqus_one': 5317,
         'countyx_1': 0, 'city': '襄阳市', 'updatetime': '2021-08-30', 'id': 1557},
        {'unbalances': 15, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 729, 'unbalances_one': 16,
         'samecoverxiaoqus_one': 1150,
         'countyx_1': 0, 'city': '鄂州市', 'updatetime': '2021-08-30', 'id': 1558},
        {'unbalances': 25, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 931, 'unbalances_one': 20,
         'samecoverxiaoqus_one': 2068,
         'countyx_1': 0, 'city': '随州市', 'updatetime': '2021-08-30', 'id': 1559},
        {'unbalances': 3, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 2135, 'unbalances_one': 1,
         'samecoverxiaoqus_one': 4476,
         'countyx_1': 0, 'city': '黄冈市', 'updatetime': '2021-08-30', 'id': 1560},
        {'unbalances': 1, 'adjusteds': 0, 'finished': 0, 'condit1': None, 'condit2': None, 'condit3': None,
         'alllogs': 0,
         'successlogs': 0, 'unbalances_1': 0, 'samecoverxiaoqus': 1158, 'unbalances_one': 0,
         'samecoverxiaoqus_one': 2358,
         'countyx_1': 0, 'city': '黄石市', 'updatetime': '2021-08-30', 'id': 1561}]}

    updatetime = "2021-08-29"
    beforeDay = "2021-08-28"
    everyday_dic = realtimebalance(res, updatetime, beforeDay)
    print(everyday_dic)
    """
    {'LoadbalanceData': [580, '0.99%', 79, '15.77%', 41, '57.75%', 41, '39.02%'], 
    'samecoverdata': [1698, 1875, 1030, '54.93%', 843, '49.65%', 3442, '96.78%']}

    """

{'countxiaoqu': 418, 'countlimit': 0, 'countyx': 149, 'countadjust': 647, 'countlogs': 759, 'countsuccesslogs': 756,
 'city': '咸宁市', 'updatetime': '2021-08-29', 'countback': 49, 'id': 1221}
{'countxiaoqu': 129, 'countlimit': 0, 'countyx': 110, 'countadjust': 218, 'countlogs': 469, 'countsuccesslogs': 469,
 'city': '宜昌市', 'updatetime': '2021-08-29', 'countback': 197, 'id': 1222}
{'countxiaoqu': 33, 'countlimit': 0, 'countyx': 25, 'countadjust': 44, 'countlogs': 95, 'countsuccesslogs': 95,
 'city': '恩施州', 'updatetime': '2021-08-29', 'countback': 41, 'id': 1223}
{'countxiaoqu': 1, 'countlimit': 0, 'countyx': 0, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
 'city': '恩施市', 'updatetime': '2021-08-29', 'countback': 0, 'id': 1224}
{'countxiaoqu': 205, 'countlimit': 0, 'countyx': 180, 'countadjust': 361, 'countlogs': 759, 'countsuccesslogs': 758,
 'city': '武汉市', 'updatetime': '2021-08-29', 'countback': 331, 'id': 1225}
{'countxiaoqu': 2, 'countlimit': 0, 'countyx': 0, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
 'city': '江汉市', 'updatetime': '2021-08-29', 'countback': 0, 'id': 1226}
{'countxiaoqu': 1, 'countlimit': 0, 'countyx': 0, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
 'city': '潜江市', 'updatetime': '2021-08-29', 'countback': 0, 'id': 1227}
{'countxiaoqu': 1, 'countlimit': 0, 'countyx': 1, 'countadjust': 2, 'countlogs': 4, 'countsuccesslogs': 4,
 'city': '荆州市', 'updatetime': '2021-08-29', 'countback': 2, 'id': 1228}
{'countxiaoqu': 86, 'countlimit': 0, 'countyx': 77, 'countadjust': 132, 'countlogs': 272, 'countsuccesslogs': 272,
 'city': '荆门市', 'updatetime': '2021-08-29', 'countback': 119, 'id': 1229}
{'countxiaoqu': 176, 'countlimit': 0, 'countyx': 31, 'countadjust': 109, 'countlogs': 289, 'countsuccesslogs': 268,
 'city': '鄂州市', 'updatetime': '2021-08-29', 'countback': 102, 'id': 1230}
{'countxiaoqu': 47, 'countlimit': 0, 'countyx': 39, 'countadjust': 64, 'countlogs': 143, 'countsuccesslogs': 143,
 'city': '随州市', 'updatetime': '2021-08-29', 'countback': 55, 'id': 1231}
{'countxiaoqu': 445, 'countlimit': 0, 'countyx': 147, 'countadjust': 625, 'countlogs': 667, 'countsuccesslogs': 667,
 'city': '咸宁市', 'updatetime': '2021-08-30', 'countback': 4, 'id': 1236}
{'countxiaoqu': 2, 'countlimit': 0, 'countyx': 0, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
 'city': '天门市', 'updatetime': '2021-08-30', 'countback': 0, 'id': 1237}
{'countxiaoqu': 1, 'countlimit': 0, 'countyx': 0, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
 'city': '孝感市', 'updatetime': '2021-08-30', 'countback': 0, 'id': 1238}
{'countxiaoqu': 196, 'countlimit': 0, 'countyx': 164, 'countadjust': 261, 'countlogs': 525, 'countsuccesslogs': 524,
 'city': '宜昌市', 'updatetime': '2021-08-30', 'countback': 230, 'id': 1239}
{'countxiaoqu': 54, 'countlimit': 0, 'countyx': 39, 'countadjust': 74, 'countlogs': 157, 'countsuccesslogs': 157,
 'city': '恩施州', 'updatetime': '2021-08-30', 'countback': 59, 'id': 1240}
{'countxiaoqu': 1, 'countlimit': 0, 'countyx': 1, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
 'city': '恩施市', 'updatetime': '2021-08-30', 'countback': 0, 'id': 1241}
{'countxiaoqu': 195, 'countlimit': 0, 'countyx': 174, 'countadjust': 306, 'countlogs': 680, 'countsuccesslogs': 679,
 'city': '武汉市', 'updatetime': '2021-08-30', 'countback': 260, 'id': 1242}
{'countxiaoqu': 11, 'countlimit': 0, 'countyx': 0, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
 'city': '江汉市', 'updatetime': '2021-08-30', 'countback': 0, 'id': 1243}
{'countxiaoqu': 1, 'countlimit': 0, 'countyx': 0, 'countadjust': 0, 'countlogs': 0, 'countsuccesslogs': 0,
 'city': '潜江市', 'updatetime': '2021-08-30', 'countback': 0, 'id': 1244}
{'countxiaoqu': 118, 'countlimit': 0, 'countyx': 99, 'countadjust': 150, 'countlogs': 309, 'countsuccesslogs': 309,
 'city': '荆门市', 'updatetime': '2021-08-30', 'countback': 133, 'id': 1245}
{'countxiaoqu': 83, 'countlimit': 0, 'countyx': 67, 'countadjust': 113, 'countlogs': 229, 'countsuccesslogs': 229,
 'city': '襄阳市', 'updatetime': '2021-08-30', 'countback': 84, 'id': 1246}
{'countxiaoqu': 530, 'countlimit': 0, 'countyx': 99, 'countadjust': 253, 'countlogs': 675, 'countsuccesslogs': 566,
 'city': '鄂州市', 'updatetime': '2021-08-30', 'countback': 173, 'id': 1247}
{'countxiaoqu': 61, 'countlimit': 0, 'countyx': 53, 'countadjust': 93, 'countlogs': 200, 'countsuccesslogs': 200,
 'city': '随州市', 'updatetime': '2021-08-30', 'countback': 87, 'id': 1248}

# Process finished with exit code 0

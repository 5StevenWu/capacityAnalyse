import requests
import json

url = r"http://10.25.225.89:8089/carrier/sameCover/interface/countBalances"


# day = "2021-08-30"


def kanban_req(day, url):
    params = {
        "day": day,
        "city": "",
    }
    res = requests.post(url, params).text
    res = json.loads(res)
    return res
# print(res)
# LoadbalanceDataCount_Y = res.get("LoadbalanceDataCount_Y")
# SamecoverDataCount = res.get("SamecoverDataCount")

import pyperclip
import time
from selenium.webdriver.common.keys import Keys
# 变量:1.复制工单号,
# 固定:1.粘贴, 搜索  复制粘贴提交 (录制鼠标轨迹)

# 工单号文件名
gongdanfile = 'gongdan.txt'
# 每条复制粘贴间隔
s = 4


def cvgongdan():
    with open(gongdanfile, mode='r', encoding='utf8') as file:
        print(file)
        # print(file.readline())
        # print(file.readlines())
        # print(file.read())
        for everyline in file.readlines():
            print("复制间隔%ss,当前剪切板内容:%s" % (s, everyline), end='')
            pyperclip.copy(everyline.replace('\n', '').replace('\r', ''))

            time.sleep(s)


def selinum_test(selenium=None):
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=r'C:\Users\hsingpu\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get("http://www.baidu.com/")
    element = driver.find_element_by_id('kw')
    element.clear()
    element.send_keys('hanxin48694648')
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.CONTROL,'c')	#复制CTRL+C
    element.send_keys(Keys.CONTROL,'x')	#剪切CTRL+X
    element.send_keys(Keys.CONTROL,'v')#
    element.click()  # 光标向下

    # element.send_keys(Keys.ENTER)  # 回车
    time.sleep(4)

if __name__ == '__main__':
    # niubi().lihai()
    # cvgongdan()
    selinum_test()
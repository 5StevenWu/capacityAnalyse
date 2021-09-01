with open(r"C:\Users\hsingpu\Documents\WeChat Files\windfishing\FileStorage\File\2021-08\new9.csv", mode='r',
          encoding='gbk') as oldfile:
    nfile=open(r"C:\Users\hsingpu\Documents\WeChat Files\windfishing\FileStorage\File\2021-08\new92.csv", mode='a',
              encoding='utf-8')
    for line in oldfile.readlines():
        print(line)
        nfile.write(line)
    # for l in oldfile.readline():
    nfile.close()
    #         nfile.writelines(line)

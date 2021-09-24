with open("daihuifu.log", mode='r', encoding='utf-8') as f:
    with open('f.log',mode='w',encoding='utf-8') as f2:
        for line in f.readlines():

            # print(line)
            if 'HB' in line:
                # print(line)
                fname = line.split(' ')[1]
                fname=fname.strip('\r\n')
                f2.write(fname+',')
                # print(fname,',',end='')


            if "offset" in line:
                lin = line.split(" ")
                # print(lin)
                block = lin[7]
                offset = lin[9]
                f2.write(str(block)+str(offset))
            # print(str(fname)   , block, offset)

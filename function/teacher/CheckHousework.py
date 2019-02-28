from Data import Data

def checkHousework():
    while True:
        print('1.查看已发布的作业')
        print('2.发布新的作业')
        print('0.返回')
        choose = input()
        if choose == '1':
            PublishedHousework()
        elif choose == '2':
            PubulishHousework()
        elif choose == '0':
            break
        else:
            print('输出错误请重新选择')
            print('***********************')



def PublishedHousework():
    rs = Data.readFile('publishhousework')
    for i in rs:
        print(i[0] + '   ' + i[1] + '\n')

def PubulishHousework():
    date = 1
    key = input('是否第一次发布作业')
    if key == '1':
        rs = Data.readFilewhilenull('publishhousework')
    else:
        rs = Data.readFile('publishhousework')
        for i in rs:
            date = int(i[0])
        date += 1
    content = input('请输入你的作业内容')
    Data.addItem('publishhousework', str(date))
    Data.addItem('publishhousework', content)
    Data.addItem('publishhousework', '\n')
    for i in range(20):
        Data.addItem('第'+str(date)+'次作业', '学号'+str(i))
        Data.addItem('第'+str(date)+'次作业', str(0))
        Data.addItem('第'+str(date)+'次作业', '\n')
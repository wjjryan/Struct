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
    content = input('请输入你的作业内容')
    rs = Data.readFile('publishhousework')
    for i in rs:
        date = i[0]
    date += 1
    Data.addItem('publishhousework', date)
    Data.addItem('publishhousework', content)
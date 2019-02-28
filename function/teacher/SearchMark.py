from Data import Data

def searchMark():
    while True:
        print('1.查看所有学生的所有作业的成绩')
        print('2.查看所有学生的某次作业的成绩')
        print('3.查看某次作业没有成绩的学生')
        print('0.返回')
        choose = input()
        if choose == '1':
            AllMark()
        elif choose == '2':
            OnceMark()
        elif choose == '3':
            NoMark()
        elif choose == '0':
            break
        else:
            print('输出错误请重新选择')
            print('***********************')


def AllMark():
    rs =Data.readFile('publishhousework')
    for i in rs :
        rs2 = Data.readFile('第' + i[0] + '次作业')
        print('第' + i[0] + '次作业')
        print(rs2)

def OnceMark():
    MarkNum = input('请输出所需查询的作业号')
    rs = Data.readFile('第' + str(MarkNum) + '次作业')
    print(rs)

def NoMark():
    MarkNum = input('请输出所需查询的作业号')
    rs = Data.readFile('第' + str(MarkNum) + '次作业')
    for i in rs:
        if i[1] == '0':
            print(i[0] + '\n')



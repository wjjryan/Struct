from Data import Data

def searchOnceMark(num):
    while True:
        MarkNum = input('请输入你要查询的成绩的作业号')
        rs =Data.readFile(MarkNum)
        for i in rs:
            if i[0] == num:
                print(i[1])
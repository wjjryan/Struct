from Data import Data

def inputAndCorrectMark():
    while True:
        print('请输入相应序号选择所需的功能')
        print('1.录入或修改成绩')
        print('0.返回')
        choose = input()
        if choose == '1':
            InputOrCorrectMark()
        elif choose == '0':
            break
        else:
            print('输出错误请重新选择')
            print('***********************')



def InputOrCorrectMark():
    while True:
        MarkNum = input('请输入所需要录入成绩作业的作业号')
        rs = Data.readFile('第' + str(MarkNum) + '次作业')
        print('该次作业所有同学的成绩'+'\n')
        print(rs)
        student = input('请输入所需要录入成绩学生的学号')
        Mark    = input('请输入成绩')
        oncemark = ['学号'+str(student), Mark]
        for i in rs:
            if i[0] == oncemark[0]:
                i[1] = oncemark[1]
        Data.rewriteFile('第'+str(MarkNum)+'次作业',rs)
        key = input('是否继续输入成绩(1继续，0退出)')
        if key == '0':
            break
"""def CorrectMark():
    student = input('请输入所需要修改成绩学生的学号')
    MarkNum = input('请输入所需要修改成绩作业的作业号')
    Mark    = input('请输入成绩')
    rs = Data.readFile('第'+str(MarkNum)+'次作业')
    rs[student+1][1] = Mark
    Data.rewriteFile(MarkNum, ['学号', '成绩'])
    for i in rs:
        for j in i:
            Data.addItem(MarkNum, j)"""

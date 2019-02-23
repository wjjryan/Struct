def inputAndCorrectMark():
    while True:
        print('请输入相应序号选择所需的功能')
        print('1.录入成绩')
        print('2.修改成绩')
        print('0.返回')
        choose = input()
        if choose == '1':
            InputMark()
        elif choose == '2':
            CorrectMark()
        elif choose == '0':
            break
    else:
            print('输出错误请重新选择')
            print('***********************')



def InputMark():
    while True:
        student = input('请输入所需要录入成绩学生的学号')
        MarkNum = input('请输入所需要录入成绩作业的作业号')

def CorrectMark():
    student = input('请输入所需要修改成绩学生的学号')
    MarkNum = input('请输入所需要修改成绩作业的作业号')
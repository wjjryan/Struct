from function.teacher import TeacherFunctionChoose
from Data import Data

def TeacherLogin():
    while True:
        key = 0
        account  = input('请输入你的工号')
        password = input('请输入你的密码')
        k = print('输入0返回')
        if k == '0':
            break
        re = Data.readFile('TeacherInformation')
        for i in re:
            print(i[1])
            if account == i[2] and password == i[3]:
                key = 1
        if key == 1:
            TeacherFunctionChoose.teacherFunctionChoose()
            break
        else:
            print('工号或密码错误请重新输入')
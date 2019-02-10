from function.teacher import TeacherFunctionChoose
def TeacherLogin():
    while True:
        account  = input('请输入你的工号')
        password = input('请输入你的密码')
        if account == '' and password == '':
            TeacherFunctionChoose.teacherFunctionChoose()
            break
        else:
            print('工号或密码错误请重新输入')
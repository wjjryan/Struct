from function.teacher import TeacherRegister,TeacherLogin
def teacherLogin():
    while True:
        print('1.注册')
        print('2.登录')
        choose = input()
        if choose == '1':
            TeacherRegister.teacherRegister()
            break
        elif choose == '2':
            TeacherLogin.TeacherLogin()
            break
        else:
            print('输出错误请重新选择')
            print('***********************')

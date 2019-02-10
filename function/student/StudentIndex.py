from function.student import StudentLogin,StudentRegister
def teacherLogin():
    while True:
        print('1.注册')
        print('2.登录')
        choose = input()
        if choose == '1':
            StudentLogin.studentLogin()
            break
        elif choose == '2':
            StudentRegister.studentregister()
            break
        else:
            print('输出错误请重新选择')
            print('***********************')

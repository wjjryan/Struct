def studentLogin():
    while True:
        account  = input('请输入你的学号')
        password = input('请输入你的密码')
        if account == '' and password == '':
            break
        else:
            print('学号或密码错误请重新输入')
from action import TeacherLogin,StudentLogin

print('作业管理系统')
while True:
    print('请选择你的登录方式(输入序号以选择)：')
    print('1.老师')
    print('2.学生')
    choose = input()
    if choose == '1':
        TeacherLogin()
    elif choose == '2':
        StudentLogin()
    else:
        print('输入错误请重新选择')

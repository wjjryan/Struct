from function.student import StudentLogin
from function.teacher import TeacherIndex

print('作业管理系统')
while True:
    print('请选择你的登录方式(输入序号以选择)：')
    print('1.老师')
    print('2.学生')
    print('0.返回')
    choose = input()
    if choose == '1':
        TeacherIndex.teacherLogin()
    elif choose == '2':
        StudentLogin.studentLogin()
    elif choose == '0':
        print('欢迎再次使用')
        break
    else:
        print('输入错误请重新选择')
        print('***********************')
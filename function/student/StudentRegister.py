from Data import Data

def studentregister():
    name     = input('请输入你的姓名')
    Class    = input('请输入你所在的班级')
    number   = input("请输入你的学号：")
    password = input("请输入你的密码：")
    studentinformation = [name, Class, number, password]
    for i in studentinformation:
        Data.addItem('TeacherInformation', i)
    Data.addItem('TeacherInformation', '\n')
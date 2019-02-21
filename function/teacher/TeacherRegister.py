from Data import Data
def teacherLogin():
    name     = input('请输入你的姓名')
    subject  = input('请输入你所任教的科目')
    number   = input("请输入你的工号：")
    password = input("请输入你的密码：")
    teacherinformation = [name, subject, number, password]
    Data.addItem('TeacherInformation', teacherinformation)
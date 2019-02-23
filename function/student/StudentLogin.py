from Data import Data
from function.student import StudentFunctionChoose,SearchAllMark,SearchOnceMark,SearchTotalANDAverage
def studentLogin():
    while True:
        account  = input('请输入你的学号')
        password = input('请输入你的密码')
        re = Data.readFile('StudentInformation')
        for i in re:
            print(i[1])
            if account == i[2] and password == i[3]:
                key = 1
        if key == 1:
            StudentFunctionChoose.studentFunctionChoose(account)
            break
        else:
            print('学号或密码错误请重新输入')
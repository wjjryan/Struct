from function.teacher import CheckHousework,InputAndCorrectMark,SearchMark

def teacherFunctionChoose():
    A ='从文件中读取'
    print('你好'+ A +'老师，欢迎使用作业管理系统')
    while True:
        print('1.查看已发布的作业或创建新作业')
        print('2.录入成绩或更改成绩')
        print('3.查看成绩')
        print('0.返回')
        choose = input()
        if choose == '1':
            CheckHousework.checkHousework()
        elif choose == '2':
            InputAndCorrectMark.inputAndCorrectMark()
        elif choose == '3':
            SearchMark.searchMark()
        elif choose == '0':
            break
        else:
            print('输出错误请重新选择')
            print('***********************')
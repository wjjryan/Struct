from function.student import SearchAllMark, SearchOnceMark, SearchTotalANDAverage

def studentFunctionChoose():
    A = '从文件中读取'
    print('你好' + A + '同学，欢迎使用作业管理系统')
    while True:
        print('1.查看自己所有作业的成绩')
        print('2.查看自己某次作业的成绩')
        print('3.统计自己的作业的总分和平均分')
        choose = input()
        if choose == '1':
            SearchAllMark.searchAllMark()
            break
        elif choose == '2':
            SearchOnceMark.searchOnceMark()
            break
        elif choose == '3':
            SearchTotalANDAverage.searchTotalAndAverage()
            break
        else:
            print('输出错误请重新选择')
            print('***********************')
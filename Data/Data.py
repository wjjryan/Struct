import  os
def creatFile(filename):
    os.chdir('/Volumes/data/PycharmProject/Struct/Data')
    fileobject = open(filename, 'w')
    fileobject.close()

def readFile(filename):
    rs = []
    os.chdir('/Volumes/data/PycharmProject/Struct/Data')
    fileoject = open(filename, 'r')
    line = fileoject.readline().strip()
    while line:
        linestr = line.split(',')
        rs.append(linestr)
        line = fileoject.readline().strip()
    return rs
def addItem(filename,item):
    os.chdir('/Volumes/data/PycharmProject/Struct/Data')
    fileobject = open(filename, 'a')
    if item != '\n':
        fileobject.write(item + ',')
    else:
        fileobject.write(item)
    fileobject.close()


def rewriteFile(filename,item):
    s = ''
    os.chdir('/Volumes/data/PycharmProject/Struct/Data')
    fileobject = open(filename, 'w')
    for i in item:
        for j in i:
            if j != s.strip():
                print(str(j+','))
                fileobject.write(j + ',')
        fileobject.write('\n')
    fileobject.close()

def readFilewhilenull(filename):
    rs = []
    os.chdir('/Volumes/data/PycharmProject/Struct/Data')
    fileoject = open(filename, 'a+')
    line = fileoject.readline().strip()
    while line:
        linestr = line.split(',')
        rs.append(linestr)
        line = fileoject.readline().strip()

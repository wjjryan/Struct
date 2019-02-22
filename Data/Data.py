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
def creatFile(filename):
    fileobject = open(filename, 'w')
    fileobject.close()

def readFile(filename):
    fileoject = open(filename, 'r')
    return fileoject.read()
def addItem(filename,item):
    fileobject = open(filename, 'a')
    fileobject.write(item)
    fileobject.close()
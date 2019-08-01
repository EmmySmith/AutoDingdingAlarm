#coding:utf-8
import os

def getBugCount():
    with open('../common/count.txt', 'r+', encoding='UTF-8') as f:
        size = os.path.getsize()
        if size == 0:
            f.write(5)
        else:
            count = f.readline('../common/count.txt');
            print(count)
            f.close();
            return int(count)

def updateBugCount(newCount):
    with open('../common/count.txt', 'r+') as f:
        f.write(str(newCount))
        f.flush()
        f.seek(0)
        f.close()
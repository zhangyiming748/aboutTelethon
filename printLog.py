#用来记录下载多媒体的日志
from datetime import datetime


def writeLog(photoid, name):
    #打开文件
    with open('log.md', 'a') as f:
        #刷新缓冲区
        f.flush()
        #打印到控制台
        print('downloading:\t' + str(photoid) + '\tin\t ' + str(name) + '\t')
        #记录到文件
        b = str('downloading:\t' + str(photoid) + '\tin\t' + str(name) + '\t')
        f.write(b)


def before(index):
    with open('log.md', 'a') as f:
        f.flush()
        before = datetime.now()
        print('This Request begin at\t' + str(before))
        a = str(str(index) + ' This Request begin at\t' + str(before) + '\t')
        f.write(a)


def after():
    with open('log.md', 'a') as f:
        f.flush()
        after = datetime.now()
        print('The Request end at\t' + str((after)))
        c = str('The Request end at\t' + str((after)) + '\n')
        f.write(c)


if __name__ == '__main__':
    pass

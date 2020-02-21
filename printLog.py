from datetime import datetime


def writeLog(photoid, name):
    with open('log.md', 'a') as f:
        f.flush()
        print('downloading:\t' + str(photoid) + '\tin\t ' + str(name) + '\t')
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



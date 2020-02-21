from GetSetMessages import *
from time import sleep
def daozhang():
    url="https://t.me/daozhangqiandaoqun"
    text = "/checkin@baipiaodaozhang_bot"
    sgend(url,text)
    sleep(2)
    receive(url,10)

def suying():
    url="https://t.me/suying678"
    text="/checkin@suying_bot"
    send(url,text)
    sleep(2)
    receive(url,10)

if __name__ == '__main__':
    daozhang()
    suying()
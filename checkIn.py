# 针对机器人签到群组实现自动化
from GetSetMessages import *
from time import sleep


def daozhang():
    url = "https://t.me/daozhangqiandaoqun"
    text = "/checkin@baipiaodaozhang_bot"
    send(url, text)
    sleep(1)
    receive(url, 10)


def suying():
    url = "https://t.me/suying678"
    text = "/checkin@suying_bot"
    send(url, text)
    sleep(1)
    receive(url, 10)


if __name__ == '__main__':
    daozhang()
    suying()

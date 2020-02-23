# 用于超时判断,如果某次循环(下载)超过时间限制则跳过,目前未使用
import eventlet
import time


def limit():
    eventlet.monkey_patch()
    with eventlet.Timeout(2, False):
        print("in time")
    print("times up")

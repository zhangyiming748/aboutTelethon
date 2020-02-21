import eventlet
import time
def limit():
    eventlet.monkey_patch()
    with eventlet.Timeout(2,False):
        print("in time")
    print("times up")
eventlet.monkey_patch()

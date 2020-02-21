import eventlet
import time
def aa():
    eventlet.monkey_patch()
    with eventlet.Timeout(2, False):
        time.sleep(3)
        print("in 3")
    print("out")
def bb():
    eventlet.monkey_patch()
    if eventlet.Timeout(2, False):
        time.sleep(3)
        print("in 3")
    else:
        print("out")
if __name__ == '__main__':
    aa()
    bb()
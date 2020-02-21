import eventlet
import
import time
eventlet.monkey_patch()
if eventlet.Timeout(2,False):
    time.sleep(1)
    print('r')
else:print('aa')

import zmq
import time
context = zmq.Context()

#sub = context.socket(zmq.SUB)
#sub.connect("ipc://first")
#sub.setsockopt(zmq.SUBSCRIBE, '')

pub = context.socket(zmq.PUB)
pub.bind("tcp://192.168.1.10:5556")

while True:
    print 'beginpub_sub'
    pub.send("FIRST") 
    print 'sendpub_sub'
    time.sleep(1)
    #msg = sub.recv()
    #print 'pub_sub msg={}'.format(msg)
    print 'pub_sub'

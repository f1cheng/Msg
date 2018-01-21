import zmq
import time
context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.bind('tcp://*:5556')

while True:
    print 'beginpub_sub'
    pub.send("FIRST") 
    print 'sendpub_sub FIRST'
    time.sleep(1)



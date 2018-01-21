import zmq
import time
context = zmq.Context()
sub = context.socket(zmq.SUB)
sub.connect('tcp://192.168.1.10:5556')
sub.setsockopt(zmq.SUBSCRIBE, '')

pub = context.socket(zmq.PUB)
pub.bind("tcp://*:5557")


while True:
    print 'begin t recv'
    msg = sub.recv()
    print 'recvd  recv'
    print 'msg in pub={}'.format(msg)
    pub.send('FIRST')
    print 'msg in pub send={}'.format(msg)



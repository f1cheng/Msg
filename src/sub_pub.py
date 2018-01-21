import zmq
import time
context = zmq.Context()

sub = context.socket(zmq.SUB)
sub.connect("tcp://192.168.1.10:5556")
sub.setsockopt(zmq.SUBSCRIBE, '')
sub.setsockopt(zmq.SUBSCRIBE, "FIRST")

#pub = context.socket(zmq.PUB)
#pub.bind("ipc://first")

while True:
    print 'begin t recv'
    msg = sub.recv()
    print 'recvd  recv'
    print 'msg in sub_pub={}'.format(msg)
    time.sleep(1)
    #pub.send(msg)

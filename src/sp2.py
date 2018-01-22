import zmq
import time
context = zmq.Context()

sub = context.socket(zmq.SUB)
sub.connect("tcp://192.168.1.10:5556")
sub.setsockopt(zmq.SUBSCRIBE, "FIRST")
sub.setsockopt(zmq.LINGER, 0)

pub = context.socket(zmq.PUB)
pub.bind("ipc://first")
while True:
    print 'sub ready to recv'
    msg = sub.recv()
    print 'sub recveived={}'.format(msg)
    time.sleep(1)
    pub.send(msg)
    print 'pub send={}'.format(msg)

import zmq
import time
context = zmq.Context()
sub = context.socket(zmq.SUB)
sub.connect("tcp://192.168.1.10:5557")
sub.setsockopt(zmq.SUBSCRIBE, '')

while True:
    print 'beginpub_sub'
    time.sleep(1)
    msg = sub.recv()
    print 'rec pub_sub msg={}'.format(msg)



import zmq
import time
context = zmq.Context()

sub = context.socket(zmq.SUB)
sub.connect("ipc://first")
sub.setsockopt(zmq.SUBSCRIBE, '')

pub = context.socket(zmq.PUB)
pub.bind("tcp://192.168.1.10:5556")
#below sleep is required also peer side sub needs be started firstly 
#Put sleep before the first send. Give subscriber time to subscribe.
#A publisher doesn't wait for subscribers. If no sub, the the msg is lost.
time.sleep(1)
#what is other way to avoid the issue. by syncing? how to?
while True:
    print 'pub ready to send'
    pub.send("FIRST....") 
    print 'sent FIRST....'
    time.sleep(1)
    msg = sub.recv()
    print 'sub received msg={}'.format(msg)

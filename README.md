# Msg
```
ID + Payload
```

# big-endian
```
big endian(most significant value) stored first(at lowest storage adress)  
```
# reliable msg
```
1. TCP ACK mechanism
```

# ZeroMQ
```
1. models
2. lock less pipe
3. inproc
4. ipc
5. tcp
```

# message queue types
```
1. message queue with fix length structure, message content is fully filled
e.g: struct msg_q{int msg_type; char buf[400];}
2. pingpong msg queue
将一个队列=》生产者队列和消费者两队列 通过指针交换位置，达到减少锁的目的。
条件：当消费者对消费队列取完后，需要互换两消息队列的指针，讲生产者的队列=》消费者；消费者的队列变为生产者。
```

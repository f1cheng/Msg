# Msg
ID + Payload

# 消息队列  
```  
将一个队列=》生产者队列和消费者两队列 通过指针交换位置，达到减少锁的目的。
条件：当消费者对消费队列取完后，需要互换两消息队列的指针，讲生产者的队列=》消费者；消费者的队列变为生产者。
```  

# big-endian  

big endian(most significant value) stored first(at lowest storage adress)  

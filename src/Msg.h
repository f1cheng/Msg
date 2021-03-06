#ifndef _MSG_H_
#define _MSG_H_
typedef struct MsgHeader
{
  unsigned int id;
} MsgHeader;

typedef struct Msg
{
  MsgHeader header;
  int payload;//memcpy(&msg->payload, &orignal_data, size-headerSize);(char buf[])
} Msg;

template <typename Payload, unsigned id = 0>
class CMsg
{
public:
  const static ID = id;
  CMsg(int size);
  CMsg(void *msg);
  ~CMsg();
  void send(void);
protected:
  Payload *payLoad;
  void *msg;
};

typedef CMsg<NotifyType, 0x100> StartupNotificationMsg;
typedef CMsg<ReadyType, 0x101> StartupReadyMsg;
//class Service;
class ServiceStartup;
std::map<int, Func> handlers;
==addHandler(handle1);
==addHandler(handle2);
auto func = bind(&ServiceStartup::handleNotif, _1, _2);//bind(&xxx, this, _2);
handlers.insert(std::pair<int, Func>(StartupNotificationMsg::ID, func);
//func(service, msg);

handlers.find(id) != handlers.end();
std::map<int, Func>::iterator iter = handlers.find(id);
if (iter != handlers.end())
  (*iter).send->handleMsg(msg);

StartupReadyResMsg resp(ack_id);
resp.send();

//shared memory shm_open, mmap
/* 1. receiving shared buffer for each process(push/pop location of global message allocating offset)
 * 2. global shared memory pool(fixed size) for messages
 */
 
                
#endif

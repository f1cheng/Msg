#ifndef _MSG_H_
#define _MSG_H_
typedef struct MsgHeader
{
  unsigned int id;
} MsgHeader;

typedef struct Msg
{
  MsgHeader header;
  int payload;
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

#endif

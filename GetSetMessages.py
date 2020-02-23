# 发送和接收消息功能代码
import connect
from telethon.tl.functions.messages import GetHistoryRequest
from telethon import TelegramClient, sync
from telethon import *
import persional
import socks


def send(link, msg):
    client = connect.Connect()
    entity = client.get_entity(link)
    client.send_message(entity, msg)
    connect.disConnect(client)


def receive(link, limit):
    client = connect.Connect()
    entity = client.get_entity(link)
    posts = client(
        GetHistoryRequest(peer=entity, limit=limit, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0,
                          hash=0))
    index = 0
    for i in posts.messages:
        with open('GetMsg.md', 'a', encoding="utf-8", errors='ignore') as f:
            f.write("\n")
            f.flush()
            count = str(index + 1)
            f.write(count)
            f.write(" ")
            print(i.message)
            f.write(str(i.message))
            # f.write("\n")
            index += 1
    connect.disConnect(client)


if __name__ == '__main__':
    url = "https://t.me/testAnything"
    text = "早上好"
    send(link=url, msg=text)

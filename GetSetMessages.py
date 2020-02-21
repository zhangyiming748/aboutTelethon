from telethon import TelegramClient, sync
import pathlib
from datetime import datetime
import time
import Personal_info as pinfo
# import channelList
import channelList
import socks  # 如果你不需要通过代理连接Telegram，可以删掉这一行
import random
import utils
import connect
import eventlet  # 添加时间限制,防止无法连接的内容导致程序异常退出
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import InputMessagesFilterEmpty, InputMessagesFilterPhotos, InputMessagesFilterVideo, \
    InputMessagesFilterPhotoVideo, InputMessagesFilterDocument, InputMessagesFilterUrl, InputMessagesFilterGif, \
    InputMessagesFilterVoice, InputMessagesFilterMusic, InputMessagesFilterChatPhotos, InputMessagesFilterPhoneCalls, \
    InputMessagesFilterRoundVoice, InputMessagesFilterRoundVideo, InputMessagesFilterMyMentions, \
    InputMessagesFilterGeo, InputMessagesFilterContacts




def send(link, message):
    client=connect.Connect()
    entity = client.get_entity(link)
    client.send_message(entity=entity, message=message)
    connect.disConnect(client)

def receive(link, limit):
    client=connect.Connect()
    entity = client.get_entity(link)
    posts = client(GetHistoryRequest(peer=entity, limit=limit, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
    index = 0
    for i in posts.messages:

        with open('GetMsg.md', 'a',encoding="utf-8",errors = 'ignore') as f:

            f.write("\n")
            f.flush()
            count = str(index+1)
            f.write(count)
            f.write(" ")

            print(i.message)
            f.write(str(i.message))
            #f.write("\n")
            index+=1
    connect.disConnect(client)


if __name__ == '__main__':

    strToSent = '''
  Message was too long. Current maximum length is 4096 UTF-8 characters (caused by SendMessageRequest)'''
    #test.send(channelList.Windows, strToSent)
    link =channelList.Windows
    #send(link=link,message=strToSent)
    receive(link=channelList.Windows,limit=10)

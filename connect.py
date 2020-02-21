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
import eventlet  # 添加时间限制,防止无法连接的内容导致程序异常退出
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import InputMessagesFilterEmpty, InputMessagesFilterPhotos, InputMessagesFilterVideo, \
    InputMessagesFilterPhotoVideo, InputMessagesFilterDocument, InputMessagesFilterUrl, InputMessagesFilterGif, \
    InputMessagesFilterVoice, InputMessagesFilterMusic, InputMessagesFilterChatPhotos, InputMessagesFilterPhoneCalls, \
    InputMessagesFilterRoundVoice, InputMessagesFilterRoundVideo, InputMessagesFilterMyMentions, \
    InputMessagesFilterGeo, InputMessagesFilterContacts


def Connect():
    # my api_id
    api_id = pinfo.getId()
    # my api_hash
    api_hash = pinfo.getHash()
    # my proxy
    proxy = (socks.SOCKS5, '127.0.0.1', 1080)
    # proxy = (socks.PROXY_TYPE_HTTP, '127.0.0.1', 1080)
    print("connecting...")
    client = TelegramClient('my_session', api_id=api_id, api_hash=api_hash, proxy=proxy).start()
    print("connected!")
    return client


def disConnect(client):
    client.disconnect()
    print("disConnect,Done")

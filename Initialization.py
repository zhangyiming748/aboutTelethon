# 原始功能代码防止意外
from telethon import TelegramClient, sync
import pathlib
from datetime import datetime
import time

import socks  # 如果你不需要通过代理连接Telegram，可以删掉这一行
from telethon.tl.types import InputMessagesFilterEmpty, InputMessagesFilterPhotos, InputMessagesFilterVideo, \
    InputMessagesFilterPhotoVideo, InputMessagesFilterDocument, InputMessagesFilterUrl, InputMessagesFilterGif, \
    InputMessagesFilterVoice, InputMessagesFilterMusic, InputMessagesFilterChatPhotos, InputMessagesFilterPhoneCalls, \
    InputMessagesFilterRoundVoice, InputMessagesFilterRoundVideo, InputMessagesFilterMyMentions, \
    InputMessagesFilterGeo, InputMessagesFilterContacts


def function():
    api_id = 1062870
    api_hash = '52be17f4c38ba6e92a9236ccf2e38c49'
    proxy = (socks.SOCKS5, '127.0.0.1', 1080)
    # proxy = (socks.PROXY_TYPE_HTTP, '127.0.0.1', 1080)
    client = TelegramClient('my_session', api_id=api_id, api_hash=api_hash, proxy=proxy).start()
    url = "https://t.me/testAnything"
    text = "早"
    entity = client.get_entity(url)
    print(client)
    client.send_message(entity=entity, message=text)
    print("3")
    client.disconnect()


if __name__ == '__main__':
    function()

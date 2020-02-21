from telethon import TelegramClient, sync
import Personal_info as pinfo

import socks  # 如果你不需要通过代理连接Telegram，可以删掉这一行


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

import persional
import socks
from telethon import TelegramClient, sync


def Connect():
    # my api_id
    api_id = persional.getId()
    # my api_hash
    api_hash = persional.getHash()
    # my proxy
    proxy = (socks.HTTP, '127.0.0.1', 1087)
    # proxy = (socks.SOCKS5, '127.0.0.1', 1086)
    print("connecting...")
    client = TelegramClient('my_session', api_id=api_id, api_hash=api_hash, proxy=proxy).start()
    print("connected!")
    return client


def disConnect(client):
    client.disconnect()
    print("disConnect,Done")


if __name__ == '__main__':
    Connect()
    print("连接成功")
    disConnect(Connect())
    print("断开连接")

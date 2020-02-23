# 建立/断开连接代码
import persional
import socks
from telethon import TelegramClient, sync


def Connect():
    # 机器人id
    api_id = persional.getId()
    # 机器人Hash
    api_hash = persional.getHash()
    # 需要代理用这个
    proxy = (socks.SOCKS5, '127.0.0.1', 1080)
    # proxy = (socks.PROXY_TYPE_HTTP, '127.0.0.1', 1080)
    print("connecting...")
    # 建立连接
    client = TelegramClient('my_session', api_id=api_id, api_hash=api_hash, proxy=proxy).start()
    print("connected!")
    print(client)
    # 函数返回此时的链接
    return client


def disConnect(client):
    # 断开已经建立的连接
    client.disconnect()
    print("disConnect,Done")


if __name__ == '__main__':
    Connect()
    # print("connected!")
    disConnect(Connect())
    # print("disconnected!")

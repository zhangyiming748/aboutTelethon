# 建立/断开连接代码
import persional as p
import socks
from telethon import TelegramClient, sync


def Connect():
    # 机器人id
    api_id = p.getId()
    # 机器人Hash
    api_hash = p.getHash()
    # 需要代理用这个
    proxy = (socks.SOCKS5, '127.0.0.1', 1089)
    #proxy = (socks.PROXY_TYPE_HTTP, '127.0.0.1', 12321)
    # my proxy
    # proxy = (base.socks.HTTP, '127.0.0.1', 12333)
    # proxy = (socks.SOCKS5, '127.0.0.1', 1086)
    print("connecting...")
    # 建立连接
    client = TelegramClient('my_session', api_id=api_id, api_hash=api_id, proxy=proxy).start()
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

    disConnect(Connect())

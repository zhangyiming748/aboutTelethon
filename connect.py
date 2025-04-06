# Telegram客户端连接管理模块
# 该模块提供了与Telegram服务器建立连接和断开连接的基本功能

import persional as p
import socks
from telethon import TelegramClient, sync

def Connect():
    """
    建立与Telegram服务器的连接
    
    Returns:
        TelegramClient: 已建立连接的Telegram客户端实例
        
    说明:
        - 使用persional模块中的API凭证(ID和Hash)
        - 默认使用SOCKS5代理（127.0.0.1:1089）
        - 会话文件保存为'my_session'
    """
    # 从persional模块获取API凭证
    api_id = p.getId()     # Telegram应用的API ID
    api_hash = p.getHash() # Telegram应用的API Hash
    
    # 配置代理设置
    # SOCKS5代理配置，用于突破网络限制
    proxy = (socks.SOCKS5, '127.0.0.1', 1089)
    
    # 其他可选的代理配置（已注释）
    #proxy = (socks.PROXY_TYPE_HTTP, '127.0.0.1', 12321)
    #proxy = (base.socks.HTTP, '127.0.0.1', 12333)
    #proxy = (socks.SOCKS5, '127.0.0.1', 1086)
    
    print("connecting...")
    # 创建并启动Telegram客户端
    # my_session: 会话文件名，用于保存登录状态
    client = TelegramClient('my_session', api_id=api_id, api_hash=api_id, proxy=proxy).start()
    print("connected!")
    print(client)
    return client

def disConnect(client):
    """
    断开与Telegram服务器的连接
    
    Args:
        client (TelegramClient): 要断开连接的Telegram客户端实例
    """
    client.disconnect()
    print("disConnect,Done")

if __name__ == '__main__':
    # 测试连接功能
    Connect()
    # 测试断开连接功能
    disConnect(Connect())

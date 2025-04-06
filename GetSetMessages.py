# Telegram消息收发模块
# 该模块提供了发送消息和获取历史消息的功能

import connect
from telethon.tl.functions.messages import GetHistoryRequest, GetStickerSetRequest


def send(link, msg):
    """
    向指定的Telegram频道或用户发送消息
    
    Args:
        link (str): Telegram频道或用户的链接
        msg (str): 要发送的消息内容
    
    说明:
        - 自动建立连接并在发送后断开
        - 支持发送文本、Markdown格式的消息
    """
    client = connect.Connect()
    entity = client.get_entity(link)
    client.send_message(entity, msg)
    connect.disConnect(client)


def receive(link, limit):
    """
    获取指定Telegram频道或用户的历史消息
    
    Args:
        link (str): Telegram频道或用户的链接
        limit (int): 要获取的消息数量
    
    说明:
        - 获取的消息会按时间倒序排列
        - 消息内容会保存到GetMsg.md文件中
        - 每条消息前会添加序号
    """
    client = connect.Connect()
    entity = client.get_entity(link)
    # 使用GetHistoryRequest获取历史消息
    posts = client(
        GetHistoryRequest(
            peer=entity,      # 目标对象
            limit=limit,      # 消息数量限制
            offset_date=None, # 时间偏移
            offset_id=0,      # 消息ID偏移
            max_id=0,         # 最大消息ID
            min_id=0,         # 最小消息ID
            add_offset=0,     # 额外偏移量
            hash=0            # 消息hash
        ))
    
    # 遍历并保存消息
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
            index += 1
    connect.disConnect(client)

def GetSticker(link, limit):
    """
    获取贴纸集信息（未完成的功能）
    
    Args:
        link (str): 贴纸集链接
        limit (int): 数量限制
    """
    client = connect.Connect()
    entity = client.get_entity(link)
    posts = client(
        GetStickerSetRequest()
    )

if __name__ == '__main__':
    # 测试代码
    url = "https://t.me/testAnything"
    text = "早上好"
    long = '''不知道这个好不好使 完整代码已经发给你们了
    使用时注意别侵权'''
    md = '''
    |星期|时间|
    |:---:|:---:|
    |1|2|
    |3|4|
    '''
    # 测试发送不同类型的消息
    send(link=url, msg=md)
    # 测试接收消息
    receive(url, 5)

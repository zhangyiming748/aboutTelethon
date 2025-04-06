# Telegram媒体文件下载模块
# 该模块提供了下载Telegram频道中各种类型媒体文件的功能
# 支持下载图片、GIF动图、视频和文档

'''
可用的消息过滤器类型：
InputMessagesFilterEmpty: 无过滤
InputMessagesFilterPhotos: 仅图片
InputMessagesFilterVideo: 仅视频
InputMessagesFilterPhotoVideo: 图片和视频
InputMessagesFilterDocument: 文档
InputMessagesFilterUrl: URL链接
InputMessagesFilterGif: GIF动图
InputMessagesFilterVoice: 语音消息
InputMessagesFilterMusic: 音乐文件
InputMessagesFilterChatPhotos: 聊天图片
InputMessagesFilterPhoneCalls: 通话记录
InputMessagesFilterRoundVoice: 语音消息（圆形界面）
InputMessagesFilterRoundVideo: 视频消息（圆形界面）
InputMessagesFilterMyMentions: 提及我的消息
InputMessagesFilterGeo: 地理位置
InputMessagesFilterContacts: 联系人
'''

from connect import *
from url2name import *
from rootPath import *
from telethon.tl.types import *
from printLog import *


def getPicture(link):
    """
    下载指定Telegram频道中的所有图片
    
    Args:
        link (str): Telegram频道链接
    
    说明:
        - 使用InputMessagesFilterPhotos过滤器仅获取图片
        - 图片保存在 [频道名]/Picture 目录下
        - 文件名使用消息ID命名
        - 下载过程会记录日志
    """
    # 建立连接
    client = Connect()
    # 获取频道名称
    name = url2name(link)
    # 指定下载目录前缀
    path = root + name + '\\Picture'
    # 获取信息 过滤器过滤图片
    photos = client.get_messages(link, None, filter=InputMessagesFilterPhotos)
    index = 0
    # 遍历图片
    for photo in photos:
        # 为log.md添加每行前缀
        index = index + 1
        # 拼接文件名
        filename = path + '\\' + str(photo.id) + '.jpg'
        # 调用写日志
        before(index)
        # 调用写日志
        writeLog(photo.id, name)
        # 下载文件核心代码
        client.download_media(photo, filename)
        # 调用写日志
        after()
    # 断开连接
    disConnect(client)


def getGif(link):
    """
    下载指定Telegram频道中的所有GIF动图
    
    Args:
        link (str): Telegram频道链接
    
    说明:
        - 使用InputMessagesFilterGif过滤器仅获取GIF
        - GIF保存在 [频道名]/GIF 目录下
        - 文件以MP4格式保存
    """
    client = Connect()
    name = url2name(link)
    path = root + name + '\\GIF'
    GIFs = client.get_messages(link, None, filter=InputMessagesFilterGif)
    index = 0
    for GIF in GIFs:
        index = index + 1
        filename = path + '\\' + str(GIF.id) + '.mp4'
        before(index)
        writeLog(GIF.id, name)
        client.download_media(GIF, filename)
        after()
    disConnect(client)


def getVideo(link):
    """
    下载指定Telegram频道中的所有视频
    
    Args:
        link (str): Telegram频道链接
    
    说明:
        - 使用InputMessagesFilterVideo过滤器仅获取视频
        - 视频保存在 [频道名]/Video 目录下
    """
    client = Connect()
    name = url2name(link)
    path = root + name + '\\Video'
    Videos = client.get_messages(link, None, filter=InputMessagesFilterVideo)
    index = 0
    for Video in Videos:
        index = index + 1
        filename = path + '\\' + str(Video.id) + '.mp4'
        before(index)
        writeLog(Video.id, name)
        client.download_media(Video, filename)
        after()
    disConnect(client)


def getDoc(link):
    """
    下载指定Telegram频道中的所有文档
    
    Args:
        link (str): Telegram频道链接
    
    说明:
        - 使用InputMessagesFilterDocument过滤器仅获取文档
        - 文档保存在 [频道名]/Document 目录下
        - 默认保存为HTML格式
    """
    client = Connect()
    name = url2name(link)
    path = root + name + '\\Document'
    Docs = client.get_messages(link, None, filter=InputMessagesFilterDocument)
    index = 0
    for Doc in Docs:
        index = index + 1
        filename = path + '\\' + str(Doc.id) + '.html'
        before(index)
        writeLog(Doc.id, name)
        client.download_media(Doc, filename)
        after()
    disConnect(client)


def getPictureOnMAC(link):
    """
    为macOS系统优化的图片下载函数
    
    Args:
        link (str): Telegram频道链接
    
    说明:
        - 功能与getPicture相同
        - 使用macOS风格的路径分隔符
        - 文件保存在 ./[频道名]/Picture 目录下
    """
    # 建立连接
    client = Connect()
    # 获取频道名称
    name = url2name(link)
    # 指定下载目录前缀
    path = root + name + '/Picture'  # ./testAnything/Picture
    # 获取信息 过滤器过滤图片
    photos = client.get_messages(link, None, filter=InputMessagesFilterPhotos)
    index = 0
    # 遍历图片
    for photo in photos:
        # 为log.md添加每行前缀
        index = index + 1
        # 拼接文件名
        filename = path + '/' + str(photo.id) + '.jpg'
        print("filename = " + filename)
        # 调用写日志
        before(index)
        # 调用写日志
        writeLog(photo.id, name)
        # 下载文件核心代码
        client.download_media(photo, filename)
        # 调用写日志
        after()
    # 断开连接
    disConnect(client)


if __name__ == '__main__':
    # 测试代码
    # getPicture(link=channelList.zukong)
    getPictureOnMAC(link="https://t.me/testAnything")
    # getVideo(link=channelList.zukong)
    # getPicture(link=channelList.OnlyDeviant)

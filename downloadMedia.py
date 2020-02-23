# 下载多媒体文件代码
'''
过滤器
InputMessagesFilterEmpty, InputMessagesFilterPhotos, InputMessagesFilterVideo, \
    InputMessagesFilterPhotoVideo, InputMessagesFilterDocument, InputMessagesFilterUrl, InputMessagesFilterGif, \
    InputMessagesFilterVoice, InputMessagesFilterMusic, InputMessagesFilterChatPhotos, InputMessagesFilterPhoneCalls, \
    InputMessagesFilterRoundVoice, InputMessagesFilterRoundVideo, InputMessagesFilterMyMentions, \
    InputMessagesFilterGeo, InputMessagesFilterContacts
'''
from connect import *
from url2name import *
from rootPath import *
from telethon.tl.types import *
from printLog import *


def getPicture(link):
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


if __name__ == '__main__':
    # getPicture(link=channelList.zukong)
    getPicture(link="https://t.me/sizukon")
    # getVideo(link=channelList.zukong)
    # getPicture(link=channelList.OnlyDeviant)

from url2name import *
import rootPath
from printLog import *
from connect import *
from telethon.tl.types import InputMessagesFilterEmpty, InputMessagesFilterPhotos, InputMessagesFilterVideo, \
    InputMessagesFilterPhotoVideo, InputMessagesFilterDocument, InputMessagesFilterUrl, InputMessagesFilterGif, \
    InputMessagesFilterVoice, InputMessagesFilterMusic, InputMessagesFilterChatPhotos, InputMessagesFilterPhoneCalls, \
    InputMessagesFilterRoundVoice, InputMessagesFilterRoundVideo, InputMessagesFilterMyMentions, \
    InputMessagesFilterGeo, InputMessagesFilterContacts
from telethon.tl.types import InputMessagesFilterEmpty

def getPicture(link):
    client = Connect()
    name = url2name(link)
    path = rootPath.root + name + '\\Picture'
    photos = client.get_messages(link, None, filter=InputMessagesFilterPhotos)
    index = 0
    for photo in photos:
        index = index + 1
        filename = path + '\\' + str(photo.id) + '.jpg'
        before(index)
        writeLog(photo.id, name)
        client.download_media(photo, filename)
        after()
    disConnect(client)


def getGif(link):
    client = Connect()
    name = url2name(link)
    path = rootPath.root + name + '\\GIF'
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
    path = rootPath.root + name + '\\Video'
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
    path = rootPath.root + name + '\\Document'
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


def getChatPhotos(link):
    client = Connect()
    name = url2name(link)
    path = rootPath.root + name + '\\ChatPhoto'
    ChatPhotos = client.get_messages(link, None, filter=InputMessagesFilterChatPhotos)
    index = 0
    for ChatPhoto in ChatPhotos:
        index = index + 1
        filename = path + '\\' + str(ChatPhoto.id) + '.png'
        time.sleep(2)
        before(index)
        writeLog(ChatPhoto.id, name)
        client.download_media(ChatPhoto, filename)
        after()
    disConnect(client)


if __name__ == '__main__':
    #getPicture(link=channelList.zukong)
    #getGif(link=channelList.zukong)
    #getVideo(link=channelList.zukong)
    getDoc(link=channelList.huangwen)
    #getPicture(link=channelList.OnlyDeviant)

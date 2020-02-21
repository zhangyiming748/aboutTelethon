from telethon import TelegramClient, sync
import pathlib
from datetime import datetime
import time
import Personal_info as pinfo
# import channelList
import channelList
import socks  # 如果你不需要通过代理连接Telegram，可以删掉这一行
import random
import utils
import eventlet  # 添加时间限制,防止无法连接的内容导致程序异常退出
from telethon.tl.types import InputMessagesFilterEmpty, InputMessagesFilterPhotos, InputMessagesFilterVideo, \
    InputMessagesFilterPhotoVideo, InputMessagesFilterDocument, InputMessagesFilterUrl, InputMessagesFilterGif, \
    InputMessagesFilterVoice, InputMessagesFilterMusic, InputMessagesFilterChatPhotos, InputMessagesFilterPhoneCalls, \
    InputMessagesFilterRoundVoice, InputMessagesFilterRoundVideo, InputMessagesFilterMyMentions, \
    InputMessagesFilterGeo, InputMessagesFilterContacts


class TelegramDownload(object):
    def __init__(self):
        # my api_id
        api_id = pinfo.getId()
        # my api_hash
        api_hash = pinfo.getHash()
        # my proxy
        # proxy = (socks.SOCKS5, '127.0.0.1', 1080)
        proxy = (socks.PROXY_TYPE_HTTP, '127.0.0.1', 1080)
        self.client = TelegramClient('my_session', api_id=api_id, api_hash=api_hash, proxy=proxy).start()
        self.BasePATH = 'C:\\Users\\Zen\\Downloads\\TelegramDownload\\'
        print('program running on \n' + self.BasePATH)

    # def getGroupList(self):
    #     for dialog in self.client.get_dialogs(limit=10):
    #         print(utils.get_display_name(dialog.entity), dialog.draft.message)
    def getPhoto(self, channel_link):
        # 频道名
        channelNames = channel_link.split('/')
        # path=/home/zen/downloadfile/channelName/picture
        path = self.BasePATH + channelNames[3] + '\\picture'
        photos = self.client.get_messages(channel_link, None, filter=InputMessagesFilterPhotos)
        index = 0
        with open('log.md', 'a') as f:
            for photo in photos:
                f.flush()
                index += 1
                times = str(str(index) + '. ')
                f.write(times)
                # /home/zen/downloadfile/channelName/picture/photo.id.jpg
                filename = path + '\\' + str(photo.id) + '.jpg'
                finalname = pathlib.Path(filename)
                if finalname.exists():
                    filename = str(random.randint(1, 200)) + filename
                    self.client.download_media(photo, filename)
                    print(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    line = str(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    f.write(line)
                else:
                    before = datetime.now()
                    print('This Request begin at\t' + str(before))
                    a = str('This Request begin at\t' + str(before) + '\t')
                    f.write(a)
                    print('downloading:\t' + str(photo.id) + '\tin\t ' + str(channelNames[3]) + '\t')
                    b = str('downloading:\t' + str(photo.id) + '\tin\t' + str(channelNames[3]) + '\t')
                    f.write(b)
                    self.client.download_media(photo, filename)
                    after = datetime.now()
                    print('The Request Spend\t' + str((after - before).microseconds) + ' `ms\n')
                    c = str('The Request Spend\t' + str((after - before).microseconds) + '`ms\n')
                    f.write(c)
            self.client.disconnect()
            print('Done.')

    def getVideo(self, channel_link):
        channelNames = channel_link.split('/')
        # path=/home/zen/downloadfile/channelName/picture
        path = self.BasePATH + channelNames[3] + '\\video'
        videos = self.client.get_messages(channel_link, None, filter=InputMessagesFilterVideo)
        index = 0
        with open('log.md', 'a') as f:
            for video in videos:
                f.flush()
                index += 1
                times = str(str(index) + '. ')
                f.write(times)
                # /home/zen/downloadfile/channelName/picture/photo.id.jpg
                filename = path + '\\' + str(video.id) + '.mp4'
                finalname = pathlib.Path(filename)
                if finalname.exists():
                    filename = str(random.randint(1, 200)) + filename
                    self.client.download_media(video, filename)
                    print(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    line = str(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    f.write(line)
                else:
                    before = datetime.now()
                    print('This Request begin at\t' + str(before))
                    a = str('This Request begin at\t' + str(before) + '\t')
                    f.write(a)
                    print('downloading:\t' + str(video.id) + '\tin\t ' + str(channelNames[3]) + '\t')
                    b = str('downloading:\t' + str(video.id) + '\tin\t' + str(channelNames[3]) + '\t')
                    f.write(b)
                    self.client.download_media(video, filename)
                    after = datetime.now()
                    print('The Request Spend\t' + str((after - before).microseconds) + ' `ms\n')
                    c = str('The Request Spend\t' + str((after - before).microseconds) + '`ms\n')
                    f.write(c)
            self.client.disconnect()
            print('Done.')

    def getPhotoVideo(self, channel_link):
        channelNames = channel_link.split('/')
        # path=/home/zen/downloadfile/channelName/picture
        path = self.BasePATH + channelNames[3] + '\\PV'
        PVs = self.client.get_messages(channel_link, None, filter=InputMessagesFilterPhotoVideo)
        index = 0
        with open('log.md', 'a') as f:
            for PV in PVs:
                f.flush()
                index += 1
                times = str(str(index) + '. ')
                f.write(times)
                # /home/zen/downloadfile/channelName/picture/photo.id.jpg
                filename = path + '\\' + str(PV.id) + '.jpg'
                finalname = pathlib.Path(filename)
                if finalname.exists():
                    line = str(filename + '\talready exist\tPASS On ' + str(datetime.now()) + '\n')
                    f.write(line)
                else:
                    before = datetime.now()
                    print('This Request begin at\t' + str(before))
                    a = str('This Request begin at\t' + str(before) + '\t')
                    f.write(a)
                    print('downloading:\t' + str(PV.id) + '\tin\t ' + str(channelNames[3]) + '\t')
                    b = str('downloading:\t' + str(PV.id) + '\tin\t' + str(channelNames[3]) + '\t')
                    f.write(b)
                    self.client.download_media(PV, filename)
                    after = datetime.now()
                    print('The Request Spend\t' + str((after - before).microseconds) + ' `ms\n')
                    c = str('The Request Spend\t' + str((after - before).microseconds) + '`ms\n')
                    f.write(c)
            self.client.disconnect()
            print('Done.')

    def getAudio(self, channel_link):
        channelNames = channel_link.split('/')
        path = self.BasePATH + channelNames[3] + '\\Audio'
        Audios = self.client.get_messages(channel_link, None, filter=InputMessagesFilterMusic)
        index = 0
        with open('log.md', 'a')as f:
            for Audio in Audios:
                f.flush()
                index += 1
                times = str(str(index) + '. ')
                f.write(times)
                filename = path + '\\' + str(Audio.id) + '.mp3'
                finalname = pathlib.Path(filename)
                if finalname.exists():
                    line = str(filename + '\talready exist\tPASS On ' + str(datetime.now()) + '\n')
                else:
                    before = datetime.now()
                    print('This Request begin at\t' + str(before))
                    a = str('This Request begin at\t' + str(before) + '\t')
                    f.write(a)
                    print('downloading:\t' + str(Audio.id) + '\tin\t ' + str(channelNames[3]) + '\t')
                    b = str('downloading:\t' + str(Audio.id) + '\tin\t' + str(channelNames[3]) + '\t')
                    f.write(b)
                    self.client.download_media(Audio, filename)
                    after = datetime.now()
                    print('The Request Spend\t' + str((after - before).microseconds) + ' `ms\n')
                    c = str('The Request Spend\t' + str((after - before).microseconds) + '`ms\n')
                    f.write(c)
            self.client.disconnect()
            print('Done.')

    def getGif(self, channel_link):
        channelNames = channel_link.split('/')
        # path=/home/zen/downloadfile/channelName/picture
        path = self.BasePATH + channelNames[3] + '\\Gif'
        Gifs = self.client.get_messages(channel_link, None, filter=InputMessagesFilterGif)
        index = 0
        with open('log.md', 'a') as f:
            for Gif in Gifs:
                f.flush()
                index += 1
                times = str(str(index) + '. ')
                f.write(times)
                # /home/zen/downloadfile/channelName/picture/photo.id.jpg
                filename = path + '\\' + str(Gif.id) + '.mp4'
                finalname = pathlib.Path(filename)
                if finalname.exists():
                    filename = str(random.randint(1, 200)) + filename
                    self.client.download_media(Gif, filename)
                    print(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    line = str(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    f.write(line)
                else:
                    before = datetime.now()
                    print('This Request begin at\t' + str(before))
                    a = str('This Request begin at\t' + str(before) + '\t')
                    f.write(a)
                    print('downloading:\t' + str(Gif.id) + '\tin\t ' + str(channelNames[3]) + '\t')
                    b = str('downloading:\t' + str(Gif.id) + '\tin\t' + str(channelNames[3]) + '\t')
                    f.write(b)

                    self.client.download_media(Gif, filename)
                    after = datetime.now()
                    print('The Request Spend\t' + str((after - before).microseconds) + ' `ms\n')
                    c = str('The Request Spend\t' + str((after - before).microseconds) + '`ms\n')
                    f.write(c)
            self.client.disconnect()
            print('Done.')

    def getDoc(self, channel_link):
        channelNames = channel_link.split('/')
        # path=/home/zen/downloadfile/channelName/picture
        path = self.BasePATH + channelNames[3] + '\\TXT'
        TXTs = self.client.get_messages(channel_link, None, filter=InputMessagesFilterDocument)
        index = 0
        with open('log.md', 'a') as f:
            for TXT in TXTs:
                f.flush()
                index += 1
                times = str(str(index) + '. ')
                f.write(times)
                # /home/zen/downloadfile/channelName/picture/photo.id.jpg
                filename = path + '\\' + str(TXT.id) + '.txt'
                finalname = pathlib.Path(filename)
                if finalname.exists():
                    filename = str(random.randint(1, 200)) + filename
                    self.client.download_media(TXT, filename)
                    print(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    line = str(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    f.write(line)
                else:
                    before = datetime.now()
                    print('This Request begin at\t' + str(before))
                    a = str('This Request begin at\t' + str(before) + '\t')
                    f.write(a)
                    print('downloading:\t' + str(TXT.id) + '\tin\t ' + str(channelNames[3]) + '\t')
                    b = str('downloading:\t' + str(TXT.id) + '\tin\t' + str(channelNames[3]) + '\t')
                    f.write(b)
                    self.client.download_media(TXT, filename)
                    after = datetime.now()
                    print('The Request Spend\t' + str((after - before).microseconds) + ' `ms\n')
                    c = str('The Request Spend\t' + str((after - before).microseconds) + '`ms\n')
                    f.write(c)
            self.client.disconnect()
            print('Done.')
    def getPhotoAll(self, channel_link):
        channelNames = channel_link.split('/')
        channelName = channelNames[3]
        path = self.BasePATH + channelName + '\\picture'
        photos = self.client.get_messages(channel_link, None, filter=InputMessagesFilterPhotos)
        index = 0
        with open('log.md', 'a') as f:
            for photo in photos:
                eventlet.monkey_patch()  # 必须加这条代码
                with eventlet.Timeout(1000, False):  # 设置超时时间为2秒
                    f.flush()
                    index += 1
                    times = str(str(index) + '. ')
                    f.write(times)
                    filename = path + '\\' + str(photo.id) + '.jpg'
                    finalname = pathlib.Path(filename)
                    print(finalname)
                    before = datetime.now()
                    print('This Request begin at\t' + str(before))
                    a = str('This Request begin at\t' + str(before) + '\t')
                    f.write(a)
                    print('downloading:\t' + str(photo.id) + '\tin\t ' + str(channelNames[3]) + '\t')
                    b = str('downloading:\t' + str(photo.id) + '\tin\t' + str(channelNames[3]) + '\t')
                    f.write(b)
                    self.client.download_media(photo, filename)
                    print('try to download')
                    after = datetime.now()
                    print('The Request Spend\t' + str((after - before).microseconds) + ' `ms\n')
                    c = str('The Request Spend\t' + str((after - before).microseconds) + '`ms\n')
                    f.write(c)
                print("times up!")
            self.client.disconnect()
            print('Done.')

    def getPhotoInTime(self, channel_link):
        channelNames = channel_link.split('/')
        channelName = channelNames[3]
        path = self.BasePATH + channelName + '\\picture'
        photos = self.client.get_messages(channel_link, None, filter=InputMessagesFilterPhotos)
        index = 0
        with open('log.md', 'a') as f:
            for photo in photos:
                f.flush()
                index += 1
                times = str(str(index) + '. ')
                f.write(times)
                filename = path + '\\' + str(photo.id) + '.jpg'
                finalname = pathlib.Path(filename)
                if finalname.exists():
                    # firstname = filename.split('.')
                    # print(firstname)
                    # filename = firstname[0] + 'ReName.jpg'
                    # print('重命名之后的文件名是' + filename)
                    # with eventlet.Timeout(5, False):
                    # self.client.download_media(photo, filename)
                    # print('try to download')
                    # print(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    # line = str(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    # f.write(line)
                    print("can not download in times,pass!\n")
                    line = str(filename + '\talready exist\n')
                    f.write(line)
                    continue
                before = datetime.now()
                print('This Request begin at\t' + str(before))
                a = str('This Request begin at\t' + str(before) + '\t')
                f.write(a)
                print('downloading:\t' + str(photo.id) + '\tin\t ' + str(channelNames[3]) + '\t')
                b = str('downloading:\t' + str(photo.id) + '\tin\t' + str(channelNames[3]) + '\t')
                f.write(b)
                eventlet.monkey_patch()
                with eventlet.Timeout(10, False):
                    self.client.download_media(photo, filename)
                    print('try to download')
                    after = datetime.now()
                    print('The Request Spend\t' + str((after - before).microseconds) + ' `ms\n')
                    c = str('The Request Spend\t' + str((after - before).microseconds) + '`ms\n')
                    f.write(c)
                    print("download in times")

                print("times up!")

            self.client.disconnect()
            print('Done.')

    def getGifInTime(self, channel_link):
        channelNames = channel_link.split('/')
        channelName = channelNames[3]
        path = self.BasePATH + channelName + '\\gif'
        gifs = self.client.get_messages(channel_link, None, filter=InputMessagesFilterGif)
        index = 0
        with open('log.md', 'a') as f:
            for gif in gifs:
                f.flush()
                index += 1
                times = str(str(index) + '. ')
                f.write(times)
                filename = path + '\\' + str(gif.id) + '.mp4'
                finalname = pathlib.Path(filename)
                if finalname.exists():
                    # firstname = filename.split('.')
                    # print(firstname)
                    # filename = firstname[0] + 'ReName.jpg'
                    # print('重命名之后的文件名是' + filename)
                    # with eventlet.Timeout(5, False):
                    # self.client.download_media(photo, filename)
                    # print('try to download')
                    # print(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    # line = str(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    # f.write(line)
                    print("can not download in times,pass!\n")
                    line = str(filename + '\talready exist\n')
                    f.write(line)
                    continue
                before = datetime.now()
                print('This Request begin at\t' + str(before))
                a = str('This Request begin at\t' + str(before) + '\t')
                f.write(a)
                print('downloading:\t' + str(gif.id) + '\tin\t ' + str(channelNames[3]) + '\t')
                b = str('downloading:\t' + str(gif.id) + '\tin\t' + str(channelNames[3]) + '\t')
                f.write(b)
                eventlet.monkey_patch()
                if eventlet.Timeout(10, False):
                    self.client.download_media(gif, filename)
                    print('try to download')
                    after = datetime.now()
                    print('The Request Spend\t' + str((after - before).microseconds) + ' `ms\n')
                    c = str('The Request Spend\t' + str((after - before).microseconds) + '`ms\n')
                    f.write(c)
                else:
                    print("can not download in times,pass!")

            self.client.disconnect()
            print('Done.')

    def getVideoInTime(self, channel_link):
        channelNames = channel_link.split('/')
        channelName = channelNames[3]
        path = self.BasePATH + channelName + '\\video'
        videos = self.client.get_messages(channel_link, None, filter=InputMessagesFilterVideo)
        index = 0
        with open('log.md', 'a') as f:
            for video in videos:
                f.flush()
                index += 1
                times = str(str(index) + '. ')
                f.write(times)
                filename = path + '\\' + str(video.id) + '.mp4'
                finalname = pathlib.Path(filename)
                if finalname.exists():
                    # firstname = filename.split('.')
                    # print(firstname)
                    # filename = firstname[0] + 'ReName.jpg'
                    # print('重命名之后的文件名是' + filename)
                    # with eventlet.Timeout(5, False):
                    # self.client.download_media(photo, filename)
                    # print('try to download')
                    # print(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    # line = str(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    # f.write(line)
                    print("can not download in times,pass!\n")
                    line = str(filename + '\talready exist\n')
                    f.write(line)
                    continue
                before = datetime.now()
                print('This Request begin at\t' + str(before))
                a = str('This Request begin at\t' + str(before) + '\t')
                f.write(a)
                print('downloading:\t' + str(video.id) + '\tin\t ' + str(channelNames[3]) + '\t')
                b = str('downloading:\t' + str(video.id) + '\tin\t' + str(channelNames[3]) + '\t')
                f.write(b)
                eventlet.monkey_patch()
                if eventlet.Timeout(10, False):
                    self.client.download_media(video, filename)
                    print('try to download')
                    after = datetime.now()
                    print('The Request Spend\t' + str((after - before).microseconds) + ' `ms\n')
                    c = str('The Request Spend\t' + str((after - before).microseconds) + '`ms\n')
                    f.write(c)
                else:
                    print("can not download in times,pass!")

            self.client.disconnect()
            print('Done.')

    def getDocumentInTime(self, channel_link):
        channelNames = channel_link.split('/')
        channelName = channelNames[3]
        path = self.BasePATH + channelName + '\\document'
        documents = self.client.get_messages(channel_link, None, filter=InputMessagesFilterDocument)
        index = 0
        with open('log.md', 'a') as f:
            for document in documents:
                f.flush()
                index += 1
                times = str(str(index) + '. ')
                f.write(times)
                filename = path + '\\' + str(document.id) + '.txt'
                finalname = pathlib.Path(filename)
                if finalname.exists():
                    # firstname = filename.split('.')
                    # print(firstname)
                    # filename = firstname[0] + 'ReName.jpg'
                    # print('重命名之后的文件名是' + filename)
                    # with eventlet.Timeout(5, False):
                    # self.client.download_media(photo, filename)
                    # print('try to download')
                    # print(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    # line = str(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    # f.write(line)
                    print("can not download in times,pass!\n")
                    line = str(filename + '\talready exist\n')
                    f.write(line)
                    continue
                before = datetime.now()
                print('This Request begin at\t' + str(before))
                a = str('This Request begin at\t' + str(before) + '\t')
                f.write(a)
                print('downloading:\t' + str(document.id) + '\tin\t ' + str(channelNames[3]) + '\t')
                b = str('downloading:\t' + str(document.id) + '\tin\t' + str(channelNames[3]) + '\t')
                f.write(b)
                eventlet.monkey_patch()
                with eventlet.Timeout(10, False):
                    self.client.download_media(document, filename)
                    print('try to download')
                    after = datetime.now()
                    print('The Request Spend\t' + str((after - before).microseconds) + ' `ms\n')
                    c = str('The Request Spend\t' + str((after - before).microseconds) + '`ms\n')
                    f.write(c)

                print("can not download in times,pass!")

            self.client.disconnect()
            print('Done.')

    def getVoiceInTime(self, channel_link):
        channelNames = channel_link.split('/')
        channelName = channelNames[3]
        path = self.BasePATH + channelName + '\\document'
        voices = self.client.get_messages(channel_link, None, filter=InputMessagesFilterVoice)
        index = 0
        with open('log.md', 'a') as f:
            for voice in voices:
                f.flush()
                index += 1
                times = str(str(index) + '. ')
                f.write(times)
                filename = path + '\\' + str(voice.id) + '.mp3'
                finalname = pathlib.Path(filename)
                if finalname.exists():
                    # firstname = filename.split('.')
                    # print(firstname)
                    # filename = firstname[0] + 'ReName.jpg'
                    # print('重命名之后的文件名是' + filename)
                    # with eventlet.Timeout(5, False):
                    # self.client.download_media(photo, filename)
                    # print('try to download')
                    # print(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    # line = str(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    # f.write(line)
                    print("can not download in times,pass!\n")
                    line = str(filename + '\talready exist\n')
                    f.write(line)
                    continue
                before = datetime.now()
                print('This Request begin at\t' + str(before))
                a = str('This Request begin at\t' + str(before) + '\t')
                f.write(a)
                print('downloading:\t' + str(voice.id) + '\tin\t ' + str(channelNames[3]) + '\t')
                b = str('downloading:\t' + str(voice.id) + '\tin\t' + str(channelNames[3]) + '\t')
                f.write(b)
                eventlet.monkey_patch()
                if eventlet.Timeout(10, False):
                    self.client.download_media(voice, filename)
                    print('try to download')
                    after = datetime.now()
                    print('The Request Spend\t' + str((after - before).microseconds) + ' `ms\n')
                    c = str('The Request Spend\t' + str((after - before).microseconds) + '`ms\n')
                    f.write(c)
                else:
                    print("can not download in times,pass!")

            self.client.disconnect()
            print('Done.')

    def getMusicInTime(self, channel_link):
        channelNames = channel_link.split('/')
        channelName = channelNames[3]
        path = self.BasePATH + channelName + '\\music'
        musics = self.client.get_messages(channel_link, None, filter=InputMessagesFilterMusic)
        index = 0
        with open('log.md', 'a') as f:
            for music in musics:
                f.flush()
                index += 1
                times = str(str(index) + '. ')
                f.write(times)
                filename = path + '\\' + str(music.id) + '.mp3'
                finalname = pathlib.Path(filename)
                if finalname.exists():
                    # firstname = filename.split('.')
                    # print(firstname)
                    # filename = firstname[0] + 'ReName.jpg'
                    # print('重命名之后的文件名是' + filename)
                    # with eventlet.Timeout(5, False):
                    # self.client.download_media(photo, filename)
                    # print('try to download')
                    # print(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    # line = str(filename + '\talready exist\trename to ' + str(filename) + '\n')
                    # f.write(line)
                    print("can not download in times,pass!\n")
                    line = str(filename + '\talready exist\n')
                    f.write(line)
                    continue
                before = datetime.now()
                print('This Request begin at\t' + str(before))
                a = str('This Request begin at\t' + str(before) + '\t')
                f.write(a)
                print('downloading:\t' + str(music.id) + '\tin\t ' + str(channelNames[3]) + '\t')
                b = str('downloading:\t' + str(music.id) + '\tin\t' + str(channelNames[3]) + '\t')
                f.write(b)
                eventlet.monkey_patch()
                if eventlet.Timeout(10, False):
                    self.client.download_media(music, filename)
                    print('try to download')
                    after = datetime.now()
                    print('The Request Spend\t' + str((after - before).microseconds) + ' `ms\n')
                    c = str('The Request Spend\t' + str((after - before).microseconds) + '`ms\n')
                    f.write(c)
                else:
                    print("can not download in times,pass!")

            self.client.disconnect()
            print('Done.')


if __name__ == '__main__':
    pic = TelegramDownload()
    # pic.getPhotoInTime(channelList.alilisi)
    # pic.getDocumentInTime(channelList.xiaoshuo)
    pic.getPhotoAll(channelList.alilisi)

from telethon import TelegramClient, sync
import pathlib
from datetime import datetime
import time
import Personal_info as pinfo
import channelList
import socks  # 如果你不需要通过代理连接Telegram，可以删掉这一行
from telethon.tl.types import InputMessagesFilterEmpty, InputMessagesFilterPhotos, InputMessagesFilterVideo, \
    InputMessagesFilterPhotoVideo, InputMessagesFilterDocument, InputMessagesFilterUrl, InputMessagesFilterGif, \
    InputMessagesFilterVoice, InputMessagesFilterMusic, InputMessagesFilterChatPhotos, InputMessagesFilterPhoneCalls, \
    InputMessagesFilterRoundVoice, InputMessagesFilterRoundVideo, InputMessagesFilterMyMentions, \
    InputMessagesFilterGeo, InputMessagesFilterContacts


class TelegramDownload(object):
    def __init__(self):
        # my api_id
        # api_id = 1062870
        api_id = pinfo.getId()
        # my api_hash
        api_hash = pinfo.getHash()
        # my proxy
        proxy = (socks.SOCKS5, '127.0.0.1', 1086)
        # proxy = (socks.PROXY_TYPE_HTTP, '127.0.0.1', 1080)
        self.client = TelegramClient('my_session', api_id=api_id, api_hash=api_hash, proxy=proxy).start()
        self.BasePATH = '/Users/zen/Documents/DownloadFile/'

    def getPhoto(self, channel_link):
        # 频道名
        channelNames = channel_link.split('/')
        # path=/home/zen/downloadfile/channelName/picture
        path = self.BasePATH + channelNames[3] + '/picture'
        photos = self.client.get_messages(channel_link, None, filter=InputMessagesFilterPhotos)
        index = 0
        with open('log.md', 'a') as f:
            for photo in photos:
                f.flush()
                index += 1
                times = str(str(index) + '. ')
                f.write(times)
                # /home/zen/downloadfile/channelName/picture/photo.id.jpg
                filename = path + '/' + str(photo.id) + '.jpg'
                finalname = pathlib.Path(filename)
                if finalname.exists():
                    line = str(filename + '\talready exist\tPASS On ' + str(datetime.now()) + '\n')
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
                    line = str(filename + '\talready exist\tPASS On ' + str(datetime.now()) + '\n')
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
                    line = str(filename + '\talready exist\tPASS On ' + str(datetime.now()) + '\n')
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


if __name__ == '__main__':
    pic = TelegramDownload()
    pic.getPhoto(channelList.Futanariporn)

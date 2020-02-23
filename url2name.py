# 解析群组链接中的群组名
def url2name(link):
    channelNames = link.split('/')
    return channelNames[3]

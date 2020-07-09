# 解析群组链接中的群组名
# 从url中提取频道名
def url2name(link):
    channelNames = link.split('/')
    return channelNames[3]
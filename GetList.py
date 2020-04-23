from connect import *
from url2name import *
from rootPath import *
from telethon.tl.types import *
from saveToFile import *
from printLog import *


# 获取频道信息

def getList(client):
    responses = client.iter_dialogs(10000)
    if responses is not None:
        for response in responses:
            if isinstance(response.entity ,tuple([Channel, Chat])):
                print(response.entity)
                res = response.entity
                print(res.id)
                saveFile("text.txt",str(response))


if __name__ == '__main__':
    client = Connect()
    getList(client)
    disConnect(client)

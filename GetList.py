from connect import *
from url2name import *
from rootPath import *
from telethon.tl.types import *
from saveToFile import *
from printLog import *
from openpyxl import Workbook
from openpyxl import Workbook

# 获取频道信息

def getList(client):
    wb = Workbook()
    print(wb)
    ws = wb.active
    print(ws)
    ws.append(['频道id', '频道名称', '频道链接'])
    responses = client.iter_dialogs(10000)
    if responses is not None:
        for response in responses:
            if isinstance(response.entity, Channel):
                # if isinstance(response.entity, tuple([Channel, Chat])):
                print(response.entity)
                res = response.entity
                print(res.username)
                id= res.id
                name=res.title
                link =str('https://t.me/'+name)
                line = [id,name,link]
                ws.append(line)
                saveFile("text.txt", str(res))
    wb.save('balances.xlsx')


if __name__ == '__main__':
    client = Connect()
    getList(client)
    disConnect(client)

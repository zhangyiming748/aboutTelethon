# Telegram贴纸包下载模块
# 该模块提供了自动下载完整贴纸包的功能
# 使用异步操作和事件监听实现自动化下载

# 必要的依赖包
# pip3 install telethon
# pip3 install PySocks

import asyncio
import logging
import os
from collections import defaultdict
import connect
from telethon.errors import MessageNotModifiedError
from telethon import TelegramClient
from telethon import events
from telethon.tl.types import DocumentAttributeSticker, DocumentAttributeFilename
from telethon.tl.functions.messages import GetStickerSetRequest

# 配置日志记录
logging.basicConfig(level=logging.INFO)
# 创建Telegram客户端实例
client = connect.Connect()

target=''

def find_instance(items, class_or_tuple):
    """
    在列表中查找指定类型的第一个实例
    
    Args:
        items: 要搜索的列表
        class_or_tuple: 要查找的类型
    
    Returns:
        找到的实例或None
    """
    for item in items:
        if isinstance(item, class_or_tuple):
            return item
    return None


@client.on(events.NewMessage(chats='me'))
async def on_sticker(event):
    """
    处理新消息事件的异步函数
    当用户发送贴纸时，自动下载整个贴纸包
    
    Args:
        event: 新消息事件对象
    """
    # 检查消息是否包含贴纸
    if not event.message.sticker:
        return
    
    sticker = event.message.sticker
    sticker_attrib = find_instance(sticker.attributes, DocumentAttributeSticker)
    
    # 检查贴纸是否属于贴纸包
    if not sticker_attrib.stickerset:
        await event.raeply('That sticker is not part of a pack')
        return

    # 获取贴纸包信息
    sticker_set = await client(GetStickerSetRequest(sticker_attrib.stickerset))
    pack_file = os.path.join(sticker_set.set.short_name, 'pack.txt')
    if os.path.isfile(pack_file):
        os.remove(pack_file)

    # 构建贴纸表情映射
    # 将每个贴纸ID与其对应的表情关联
    emojis = defaultdict(str)
    for pack in sticker_set.packs:
        for document_id in pack.documents:
            emojis[document_id] += pack.emoticon

    async def download(sticker, emojis, path, file):
        """
        下载单个贴纸的异步函数
        
        Args:
            sticker: 贴纸对象
            emojis: 表情映射字典
            path: 保存路径
            file: 文件名
        """
        prefix ='/Users/zen/Pictures/Sticker/'
        target=prefix
        await client.download_media(sticker, file=os.path.join(prefix,path, file))

        # 记录贴纸信息到pack.txt
        with open(pack_file, 'a') as f:
            f.write(f'{emojis[sticker.id]} {file}\n')

    # 创建所有贴纸的下载任务
    pending_tasks = [
        asyncio.ensure_future(
            download(document, emojis, sticker_set.set.short_name, f'{i:03d}.webp')
        ) for i, document in enumerate(sticker_set.documents)
    ]

    # 显示下载进度
    status_msg = await event.reply(f'Downloading {sticker_set.set.count} sticker(s) to ./{sticker_set.set.short_name}...')
    num_tasks = len(pending_tasks)

    # 监控下载进度
    while 1:
        done, pending_tasks = await asyncio.wait(pending_tasks, timeout=2.5,
            return_when=asyncio.FIRST_COMPLETED)
        try:
            await status_msg.edit(
                f'Downloaded {num_tasks - len(pending_tasks)}/{sticker_set.set.count}')
        except MessageNotModifiedError:
            pass
        if not pending_tasks:
            break
    
    # 完成下载
    await status_msg.edit('Done')
    await asyncio.sleep(3)
    await status_msg.delete()

print('Send stickers to yourself to download sticker packs\t'+'save to' + target)
# 运行客户端直到断开连接
client.run_until_disconnected()
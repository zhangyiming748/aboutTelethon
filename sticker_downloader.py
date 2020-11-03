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

logging.basicConfig(level=logging.INFO)
# client = TelegramClient("user", 6, "eb06d4abfb49dc3eeb1aeb98ae0f581e").start()
client = connect.Connect()

target=''
def find_instance(items, class_or_tuple):
    for item in items:
        if isinstance(item, class_or_tuple):
            return item
    return None


@client.on(events.NewMessage(chats='me'))
async def on_sticker(event):
    if not event.message.sticker:
        return
    sticker = event.message.sticker
    sticker_attrib = find_instance(sticker.attributes, DocumentAttributeSticker)
    if not sticker_attrib.stickerset:
        await event.raeply('That sticker is not part of a pack')
        return

    sticker_set = await client(GetStickerSetRequest(sticker_attrib.stickerset))
    pack_file = os.path.join(sticker_set.set.short_name, 'pack.txt')
    if os.path.isfile(pack_file):
        os.remove(pack_file)

    # Sticker emojis are retrieved as a mapping of
    # <emoji>: <list of document ids that have this emoji>
    # So we need to build a mapping of <document id>: <list of emoji>
    # Thanks, Durov
    emojis = defaultdict(str)
    for pack in sticker_set.packs:
        for document_id in pack.documents:
            emojis[document_id] += pack.emoticon

    async def download(sticker, emojis, path, file):
        prefix ='/Users/zen/Pictures/Sticker/'
        target=prefix
        await client.download_media(sticker, file=os.path.join(prefix,path, file))
        #await client.download_media(sticker, file='./')

        with open(pack_file, 'a') as f:
            f.write(f'{emojis[sticker.id]} {file}\n')

    pending_tasks = [
        asyncio.ensure_future(
            download(document, emojis, sticker_set.set.short_name, f'{i:03d}.webp')
        ) for i, document in enumerate(sticker_set.documents)
    ]

    status_msg = await event.reply(f'Downloading {sticker_set.set.count} sticker(s) to ./{sticker_set.set.short_name}...')
    num_tasks = len(pending_tasks)

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
    await status_msg.edit('Done')
    await asyncio.sleep(3)
    await status_msg.delete()

print('Send stickers to yourself to download sticker packs\t'+'save to' + target)
client.run_until_disconnected()
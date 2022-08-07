from telethon import TelegramClient
import pandas as pd

from scrappers.local_settings import api_id, api_hash


client = TelegramClient('anon', api_id, api_hash)
# Or, as another example:
# client = TelegramClient(
#     'anon',
#     api_id,
#     api_hash,
#     connection=connection.Connection.TcpMTPRandomizedIntermediate,
#     proxy=('mtproxy.example.com', 2002, 'secret')
# )

# Тушёнка и патроны (BorisBurkovChat) has ID -1001121514187


async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    # username = me.username
    # print(username)
    # print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)

    # # You can send messages to yourself...
    # await client.send_message('me', 'Hello, myself!')
    # # ...to some chat ID
    # await client.send_message(-100123456, 'Hello, group!')
    # # ...to your contacts
    # await client.send_message('+34600123123', 'Hello, friend!')
    # # ...or even to any username
    # await client.send_message('username', 'Testing Telethon!')
    #
    # # You can, of course, use markdown in your messages:
    # message = await client.send_message(
    #     'me',
    #     'This message has **bold**, `code`, __italics__ and '
    #     'a [nice website](https://example.com)!',
    #     link_preview=False
    # )
    #
    # # Sending a message returns the sent message object, which you can use
    # print(message.raw_text)
    #
    # # You can reply to messages directly if you have a message object
    # await message.reply('Cool!')
    #
    # # Or send files, songs, documents, albums...
    # await client.send_file('me', '/home/me/Pictures/holidays.jpg')

    # You can print the message history of any chat:
    messages = []
    async for message in client.iter_messages('Тушёнка и патроны (BorisBurkovChat)', limit=10000):
        # You can download media from messages, too!
        # The method will return the path where the file was saved.
        # if message.photo:
        #     path = await message.download_media()
        #     print('File saved to', path)  # printed after download is done
        message_dict = message.to_dict()
        if message.sender is not None:
            message_dict['sender_id'] = message.sender_id
            message_dict['sender_username'] = message.sender.username
        else:
            message_dict['sender_id'] = None
            message_dict['sender_username'] = None
        # message_dict['sender_first_name'] = message.sender.first_name
        # message_dict['sender_last_name'] = message.sender.last_name
        messages.append(message_dict)

    messages_df = pd.DataFrame.from_records(messages)
    messages_df.to_csv("messages.csv")


with client:
    client.loop.run_until_complete(main())

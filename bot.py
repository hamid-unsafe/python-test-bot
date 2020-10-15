from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sync import events
from telethon import functions, types
import telethon

bot_name = 'poster-bot'
API_ID = 1759413
API_HASH = '609e3756b5a95466c9422ab57eea37bb'
BOT_TOKEN = '1345211056:AAFR3DP5XNfHtQWosz2xZkqV9kkpcSJK9fc'

bot = TelegramClient(bot_name, API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage)
async def bot_new_message_handler(event):
  print('new message')
  if(event.raw_text.startswith('/')):
    command = event.raw_text.split('/')[1]
    
    await botCommandRecieved(event, command)
  else:
    await event.respond('default respond')

async def botCommandRecieved(event, command):
  if command == 'start':
    await event.respond('you will get new messages here')

  # set destination channel
  elif command.startswith('setdest'):
    channelId = command.split(' ')[1]

    print('setting dest: ', channelId)

    await event.respond('channel saved')
    
  # add channel command
  elif command.startswith('addchannel'):
    channelId = command.split(' ')[1]

    print('join requerst: ', channelId)

    await event.respond('response')

  else:
    await event.respond('default command response: ' + command)

bot.run_until_disconnected()
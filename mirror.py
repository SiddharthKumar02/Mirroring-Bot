import sys
import time
import telepot
from pprint import pprint

def handle(msg):
    response = bot.getUpdates()
    pprint(response)
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])
    elif content_type == 'photo':
        bot.download_file(msg['photo'][-1]['file_id'], '/home/sid/Pictures/botpic/file(%s).jpg' % chat_id)
        bot.sendPhoto(chat_id, open('/home/sid/Pictures/botpic/file(%s).jpg' % chat_id , 'rb'))

bot = telepot.Bot('315271734:AAHy8Z2AoCFp_V-MZKIVe0dOcbslJScZ6sY')
bot.message_loop(handle)
print ('Listening ...')

while 1:
    time.sleep(10)

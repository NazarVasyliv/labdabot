'''
Отлавливаем сообщение, отлавливаем тип сообщения ( текст, документ,), тип чата и id чата.
Выгружаем с сервера телеграмма файл, обрабатываем и выгружаем обратно пользователю.
'''
import time
import telepot
from telepot.loop import MessageLoop
import wget
import lambdalogic
from lambdalogic import wavelength
import os

telepot.api.set_proxy('https://89.42.133.58:8080')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        bot.sendMessage(chat_id, 'Я жру файлы')
    elif content_type == 'document':
        bot.sendMessage(chat_id, 'На вкус как курица')
        file_id = msg['document']['file_id']
        file_path = bot.getFile(file_id)['file_path']
        file_output_name = file_path[9:]
        url = 'https://api.telegram.org/file/bot' + TOKEN + '/' + file_path
        wget.download(url, '/content')
        file_to_output_location = '/content/' + file_output_name
        path_to_excel = lambdalogic.WL(file_to_output_location, chat_id)
        bot.sendDocument(chat_id, document=open(path_to_excel, 'rb'))
        os.remove(path_to_excel)
        os.remove(file_to_output_location)


TOKEN = '1034981722:AAG2226xw1d4qW23lPaVeeb7fzMfI8ZiHu0'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')
while 1:
    time.sleep(10)

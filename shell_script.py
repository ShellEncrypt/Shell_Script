import telebot
import urllib
import requests
bot = telebot.TeleBot('1769497993:AAHD9qhUtkaq2WZDBo_f9AgfSL2KlDumzLE')

main_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row('🍭 Скрипты 🍭')
main_menu.row('⚙️ Канал ⚙️','💎 Чат 💎')

inline_scripts = telebot.types.InlineKeyboardMarkup(row_width=1)
script_0_0_1=telebot.types.InlineKeyboardButton('💣 Скрипт 0.0.1 💣', callback_data='script_0_0_1')
inline_scripts.add(script_0_0_1)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '🍥 Привет! это бот с скриптами Shell 🏹', reply_markup=main_menu)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.chat.type == 'private':
        if message.text == '🍭 Скрипты 🍭':
            bot.send_message(message.chat.id, "👇 Скрипты: 👇", reply_markup=inline_scripts)
        if message.text == '⚙️ Канал ⚙️':
            bot.send_message(message.chat.id, "@shell_scripts")
        if message.text == '💎 Чат 💎':
            bot.send_message(message.chat.id, "@shell_chat")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'script_0_0_1':
                script='https://github.com/ShellEncrypt/shell_images/blob/main/script.lua?raw=true'
                sc = open('script.lua','wb')
                sc.write(urllib.request.urlopen(script).read())
                sc.close()
                bot.send_chat_action(call.message.chat.id, 'upload_document')
                doc = open('script.lua', 'rb')
                bot.send_document(call.message.chat.id, doc)
    except:
        print("SOME PROBLEM HAPPENED!")

bot.polling()
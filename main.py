import telebot
from telebot import types
from glob import glob
import random




bot=telebot.TeleBot('6313725554:AAFLJwBToHViYcqFKVb2xW_x29RcyAYvNwo')

@bot.message_handler (commands= ["start"])
def start (message):
    chat_id = message.chat.id
    first_name= message.chat.first_name
    markup= types.InlineKeyboardMarkup(row_width= True)
    keyboard1= types.InlineKeyboardButton("отличное", callback_data=1)
    keyboard2 = types.InlineKeyboardButton("хорошое", callback_data=2)
    keyboard3 = types.InlineKeyboardButton("неплохое", callback_data=3)
    keyboard4 = types.InlineKeyboardButton("плохое", callback_data=4)
    markup.add(keyboard1)
    markup.add(keyboard2)
    markup.add(keyboard3)
    markup.add(keyboard4)
    bot.send_message(chat_id, f"Приветик {first_name}! как у тебя настроение?", reply_markup= markup)

@bot.callback_query_handler(func= lambda call:True)
def callback_data(call):
    chat_id= call.message.chat.id
    if call.message:
        if call.data == '1':
            markup = types.InlineKeyboardMarkup(row_width=True)
            keyboard1 = types.InlineKeyboardButton("радость", callback_data=11)
            keyboard2 = types.InlineKeyboardButton("восхищение", callback_data=12)
            keyboard3 = types.InlineKeyboardButton("любовь", callback_data=13)
            markup.add(keyboard1,  keyboard2, keyboard3)
            bot.send_message(chat_id, 'Отлично!!! что ты чувстсвуешь?' ,reply_markup= markup)
        if call.data == '2':
            markup = types.InlineKeyboardMarkup(row_width=True)
            keyboard1 = types.InlineKeyboardButton("Восторг", callback_data=2)
            keyboard2 = types.InlineKeyboardButton("Благодарность", callback_data=22)
            keyboard3 = types.InlineKeyboardButton("любопытство", callback_data=23)
            keyboard4 = types.InlineKeyboardButton("Умиление", callback_data=24)
            keyboard5 = types.InlineKeyboardButton("Гордость", callback_data=25)
            markup.add(keyboard1, keyboard2, keyboard3, keyboard4,keyboard5)
            bot.send_message(chat_id, 'Это классно! что ты чувсствуешь?', reply_markup=markup)
        if call.data == '3':
            markup = types.InlineKeyboardMarkup(row_width=True)
            keyboard1 = types.InlineKeyboardButton("усталость", callback_data=31)
            keyboard2 = types.InlineKeyboardButton("обида", callback_data=32)
            keyboard3 = types.InlineKeyboardButton("разочерование", callback_data=33)
            markup.add(keyboard1, keyboard2, keyboard3)
            bot.send_message(chat_id, 'Кот, что такое?', reply_markup=markup)
        if call.data == '4':
            markup = types.InlineKeyboardMarkup(row_width=True)
            keyboard1 = types.InlineKeyboardButton("грусть", callback_data=41)
            keyboard2 = types.InlineKeyboardButton("стресс", callback_data=42)
            keyboard3 = types.InlineKeyboardButton("гнев", callback_data=43)
            keyboard4 = types.InlineKeyboardButton("раздражение", callback_data=44)
            markup.add(keyboard1, keyboard2, keyboard3, keyboard4)
            bot.send_message(chat_id, 'Котик, что случилось? что такое?', reply_markup=markup)








        if call.data == '11':
            lists = glob('imagesrad/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))
        if call.data == '12':
            lists = glob('vosh/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))
        if call.data == '13':
            lists = glob('love/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))





        if call.data == '21':
            lists = glob('Востор/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))
        if call.data == '22':
            lists = glob('Благодарность/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))
        if call.data == '23':
            lists = glob('Интерес/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))

        if call.data == '24':
            lists = glob('умиление/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))

        if call.data == '25':
            lists = glob('Гордость/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))




        if call.data == '31':
            lists = glob('усталость/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))
        if call.data == '32':
            lists = glob('обида/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))
        if call.data == '32':
            lists = glob('Разочарование/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))

        if call.data == '41':
            lists = glob('грусть/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))

        if call.data == '42':
            lists = glob('стресс/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))

        if call.data == '43':
            lists = glob('гнев/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))

        if call.data == '44':
            lists = glob('раздражение/*')
            picture = random.choice(lists)
            print(picture)
            bot.send_photo(chat_id, photo=open(picture, 'rb'))














bot.polling( none_stop= True)

'''if call.data == '2':
    lists = glob('Востор/*')
    picture = random.choice(lists)
    print(picture)
    bot.send_photo(chat_id, photo=open(picture, 'rb'))'''

















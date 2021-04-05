import telebot
from telebot import types
import sqlite3
import os
bot = telebot.TeleBot('123456789')


try:
    @bot.message_handler(commands=['ready', 'start', '283123'])
    def quest(message):
        if message.text == '/ready':
            con = sqlite3.connect('base.db')
            cur = con.cursor()
            user_id = message.chat.id
            cur.execute("""SELECT user FROM users""")
            allin = cur.fetchall()
            guys = []
            for k in allin:
                guys += [int(k[0])]
            if int(user_id) not in guys:
                cur.execute(f"""INSERT INTO users VALUES({user_id})""")
                con.commit()
                con.close()
                bot.send_message(message.chat.id, "Вы успешно подписались на рассылку!")
            else:
                bot.send_message(message.chat.id, "Вы уже подписаны!")
        elif message.text == '/start':
            bot.send_message(message.chat.id, "Если вы хотите подписаться на нашу рассылку, напишите /ready")

        elif message.text == "/283123":
            rep = bot.send_message(message.chat.id, "Напишите, что хотите отправить другим участникам.")
            bot.register_next_step_handler(rep, repy)


    @bot.message_handler(content_types=['text'])
    def answer(message):
        pass


    def repy(mes):
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        for i in cur.execute("SELECT user FROM users"):
            for j in i:
                bot.send_message(j, mes.text)
        con.close()
    bot.polling()


except:
    os.startfile("D:\xxxx.py")
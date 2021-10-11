import telebot
from settings import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,
                     """Привет!\nНапиши /help для того, чтобы узнать команды.""")


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id,
                     'Список команд:\n\n\nЧтобы узнать расписание уроков на каждый день недели:\n\n/расписание_пн\n/расписание_вт\n/расписание_ср\n/расписание_чт\n/расписание_пт\n/расписание_сб\n\nРасписание звонков:\n\n/звонки')


@bot.message_handler(commands=['расписание_пн'])
def rasp_first(message):
    bot.send_message(message.chat.id,
                     '''Расписание на понедельник:\n1.  -\n2. Алгебра.\n3. Русский язык.\n4. Физика.\n5. История.\n6. Английский язык''')


@bot.message_handler(commands=['расписание_вт'])
def rasp_monday(message):
    bot.send_message(message.chat.id,
                     '''Расписание на вторник:\n1. Физ-ра.\n2. География.\n3. Биология.\n4. Алгебра.\n5. Английский язык.\n6. Химия.''')


@bot.message_handler(commands=['расписание_ср'])
def rasp_tuesday(message):
    bot.send_message(message.chat.id,
                     'Расписание на среду:\n1. Информатика.\n2. Биология.\n3. Физика.\n4. Геометрия.\n5. История.\n6. Алгебра.')


@bot.message_handler(commands=['расписание_чт'])
def rasp_wednesday(message):
    bot.send_message(message.chat.id,
                     '''Расписание на четверг:\n1. Обществознание.\n2. Химия.\n3. Английский язык.\n4. Физ-ра.\n5. Лит-ра.\n6. Русский язык.''')


@bot.message_handler(commands=['расписание_пт'])
def rasp_thursday(message):
    bot.send_message(message.chat.id,
                     'Расписание на пятницу:\n1. Физика.\n2. История.\n3. ОБЖ.\n4. Лит-ра.\n5. Алгебра.\n6. Английский язык.')


@bot.message_handler(commands=['расписание_сб'])
def rasp_friday(message):
    bot.send_message(message.chat.id,
                     '''Расписание на субботу:\n1. Геометрия.\n2. Английския язык.\n3. Физ-ра.\n4. Лит-ра.\n5. Русский язык.\n6. География.''')


@bot.message_handler(commands=['звонки'])
def rasp_saturday(message):
    bot.send_message(message.chat.id,
                     'Расписание звонков:\n\n1 урок: 8:15 - 8:55\n2 урок: 9:15 - 9:55\n3 урок: 10:05 - 10:45\n4 урок: 11:00 - 11:40\nЗавтрак\n5 урок: 12:00 - 12:40\n6 урок: 12:50 - 13:30\n7 урок: 13:40 - 14:20\n8 урок: 14:30 - 15:10')


bot.infinity_polling()

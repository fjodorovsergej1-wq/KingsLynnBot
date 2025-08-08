
import telebot

TOKEN = "8463861931:AAGcekKgRv3HYmroJdkqdsqpYIItP0HQnCk"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Kings Lynn Helper Bot.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

if __name__ == "__main__":
    bot.polling(none_stop=True)

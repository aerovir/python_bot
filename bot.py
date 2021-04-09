from telegram.ext import Updater, CommandHandler

def start_bot(bot, updater):
    print("Hello")

def main():
    updtr = Updater('1785554817:AAGqypuL9ioqX_K5EJQD4OKA5oeOtp3oJls')

    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))

    updtr.start_polling()
    updtr.idle()
    
if __name__ == " __main__":
    main()
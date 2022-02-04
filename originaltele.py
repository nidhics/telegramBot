
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters
import requests

API_KEY="5064827716:AAHKG_OHrt7DBncQaDczJFmmGk4EQethlRs"
updater = Updater(token=API_KEY) 
dispatcher = updater.dispatcher
updater.start_polling()

greeting_list=["hello","hi","hey"]

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, How r u?')

hello_handler = CommandHandler(greeting_list, hello)


dispatcher.add_handler(hello_handler)


def motionD(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='https://www.youtube.com/watch?v=oxmZ9zczptg')

motionD_handler = CommandHandler('motionDEtection', motionD)
dispatcher.add_handler(motionD_handler)


def gamePlay(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='https://editor.p5js.org/nidhigupta.campk12/full/SlWTOyWlU')

motionD_handler = CommandHandler('game', gamePlay)
dispatcher.add_handler(motionD_handler)


def summary(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code==200):
        data = response.json()
        date = data['Date'][:10]
        print(date)
        ans = f"Covid 19 Summary (as of {date}): \n"
        
        print(data['Global'])



        for attribute, value in data['Global'].items():
            # print(attribute, "\n", value)

            if attribute not in ['NewConfirmed', 'NewDeaths', 'NewRecovered']:
                ans += 'Total ' + attribute[5:].lower() + " : " + str(value) + "\n"
                
        ans +="---------------------------------------------------------------\n"
        
        print(data["Countries"][76]["NewConfirmed"])#for india

        dictIndia=dict(data["Countries"][76])
        print(dictIndia.items())


        for attribute, value in dictIndia.items():
            # print(attribute, "\n", value)

            if attribute not in ['ID','Slug','Date','Premium']:
                ans += attribute[:].lower() + " : " + str(value) + "\n"


        

        
        
        print(ans)
        context.bot.send_message(chat_id=update.effective_chat.id, text=ans)

        

    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")

corona_summary_handler = CommandHandler('summary', summary)
dispatcher.add_handler(corona_summary_handler)






def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
    
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


updater.idle()













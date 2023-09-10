import telegram.ext
from dotenv import load_dotenv
import os 


load_dotenv()
TOKEN = os.getenv("TOKEN")


def start(update,context):
    update.message.reply_text("Hello! welcome to tech enthusiasts shubham community")
    
    
def helps(update, context):
    update.message.reply_text(
        """
        Hi there! I'm Telegram bot created by Shubham. Please follow these commands:-
        
        /start - to start the conversation
        /content - Information about Tech Enthusiasts Community
        /contact - Information about contact of Tech Enthusiasts Community
        /help - to get this help menu
        
        I hope this helps:
        """
        
        
        
    )
    
    
def content(update, context):
    update.message.reply_text(
        """
       Tech Enthusiasts is a group of people who love technology and want to share their knowledge with others. if you aré also tech enthusiast then this is right place for you
        """
        
    )
    
def contact(update, context):
    update.message.reply_text(
        """
        * Youtube: https://www.youtube.com/@Tech_Enthusiasts_Shubham
        * Visit my linkedin profile: https://www.linkedin.com/in/shubham-sharma-93944b243/
        """
        
    )
    
def handle_message(update,context):
    update.message.reply_text(f"You said {update.message.text}")
        
        
    
    

            
    
print(TOKEN)

updater = telegram.ext.Updater(TOKEN,use_context=True)
dispatch = updater.dispatcher


dispatch.add_handler(telegram.ext.CommandHandler('start',start))
dispatch.add_handler(telegram.ext.CommandHandler('help',helps))

dispatch.add_handler(telegram.ext.CommandHandler('content',content))

dispatch.add_handler(telegram.ext.CommandHandler('contact',contact))

dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text,handle_message))



updater.start_polling()
updater.idle()


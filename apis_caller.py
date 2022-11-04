"""this is the main file which controls and coordinats all the api calls and its associated functions and media files"""

import os
from time import sleep
import dotenv
dotenv.load_dotenv()
from for_twitter import create_tweet as ta
from for_slack import bot as sa
from for_discord import Discord_bot as da
from for_mail import go_mail as ea
from threading import Thread
text='hiii'
img='C:/Users/grant/OneDrive/Pictures/Screenshots/Screenshot 2022-06-05 101023.png'
def boss_the(text=None,img=None):
     
    #be aware slack mandatory of text and img
    def fun1():
        sa.for_s(os.getenv('SLACK_TOKEN'),
            os.getenv('SLACK_SIGNING_SECRET_'),
            text,
            img)
        #sleep(10)
    fun1()
    def fun2():
        ta.for_t(
            os.getenv('TWITTER_API_KEY'),
            os.getenv('TWITTER_API_SECRET'),
            os.getenv('TWITTER_ACCESS_TOKEN'),
            os.getenv('TWITTER_ACCESS_TOKEN_SECRET'),
            text,img)
   

    #sleep(7)
    def fun3():
    
        da.for_d(os.getenv('DISCORD_TOKEN2'),text,img)
    
    #sleep(5)
    def fun4():
        ea.for_e(text,img)
    #sleep(2)


    a=Thread(target=fun1)
    b=Thread(target=fun2)
    c=Thread(target=fun3)
    d=Thread(target=fun4)
    #a.start()
    #b.start()
    #c.start()
    #d.start()





boss_the(text,img)

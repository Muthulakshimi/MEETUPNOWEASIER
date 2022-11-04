
from instabot import Bot
import os
import dotenv
dotenv.load_dotenv()
bot = Bot()


######  upload a picture #######
try:
    bot.login(username=os.getenv('INSTA_USER_ID'), password=os.getenv('INSTA_PASS'))
    bot.upload_photo('C:/Users/grant/OneDrive/Desktop/aws_hacks/for_insta/cat.png', caption="biscuit eating baby")
except :
   print('Error')
finally:
   bot.logout()
   print('logging out')


######  follow someone #######
#bot.follow("elonmusk")

######  send a message #######
#for i in range(2):
#bot.send_message("Hello from poorvik sent by my code base", ['sanath'])

######  get follower info #######
"""my_followers = bot.get_user_followers("dhavalsays")
for follower in my_followers:
    print(follower)
"""
#bot.unfollow_everyone()
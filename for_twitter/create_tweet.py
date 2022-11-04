import tweepy
#from credentials import keys
def for_t(TWITTER_API_KEY,TWITTER_API_SECRET,TWITTER_ACCESS_TOKEN,TWITTER_ACCESS_TOKEN_SECRET,message=None,img_path=None):
   # img_path='C:/Users/grant/OneDrive/Desktop/aws_hacks/for_twitter/cat.png'
    def api():
        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

        return tweepy.API(auth)


    def tweet(api: tweepy.API, message: str, image_path: str):
        if image_path:
            api.update_status_with_media(message, image_path)
        else:
            api.update_status(message)

        


    
    api = api()
    tweet(api, message,img_path)
    return "Tweeted successfully"
#for_t(keys.api_key,keys.api_secret,keys.access_token,keys.access_token_secret,message="hii")


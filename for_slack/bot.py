
from logging import exception
import slack
import os

from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
#import string
#from datetime import datetime, timedelta
#import time
#from credentials import keys
load_dotenv()

def for_s(SLACK_TOKEN,SLACK_SIGNING_SECRET_,text_f=None,file_f=None):
    app = Flask(__name__)
    slack_event_adapter = SlackEventAdapter(
       SLACK_SIGNING_SECRET_, '/slack/events', app)
    client = slack.WebClient(SLACK_TOKEN)
    #BOT_ID = client.api_call("auth.test")['user_id']
   


   
    client.chat_postMessage(channel='#test',text=text_f)
  
   

    try:
        response = client.files_upload(
            file=file_f,
            initial_comment='This is a granth is back Image',
            channels='#test'
        )
    except exception as e:
        # You will get a Exception if "ok" is False
        assert e.response["ok"] is False
        # str like 'invalid_auth', 'channel_not_found'
        assert e.response["error"]
        print(f"Got an error: {e.response['error']}")

    #end of initial responce
                

    """
    @slack_event_adapter.on('message')
    def message(payload):
        print(payload)
        event = payload.get('event', {})
        channel_id = event.get('channel')
        user_id = event.get('user')
        text = event.get('text')
        client.chat_postMessage(channel=channel_id,text=text)
    """

    @ slack_event_adapter.on('message')
    def message(payload):
        #print(payload)
        event = payload.get('event', {})
        channel_id = event.get('channel')
        user_id = event.get('user')
        text = event.get('text')

        if text == "hi":
            client.chat_postMessage(channel=channel_id,text="Hello")
        if text == "image":
            try:
                response = client.files_upload(
                    file='C:/Users/grant/OneDrive/Desktop/aws_hacks/for_slack/media/cat.png',
                    initial_comment='This is a sample Image',
                    channels=channel_id
                )
            except exception as e:
                # You will get a Exception if "ok" is False
                assert e.response["ok"] is False
                # str like 'invalid_auth', 'channel_not_found'
                assert e.response["error"]
                print(f"Got an error: {e.response['error']}")
        if text == "video":
            try:
                response = client.files_upload(
                    file='/home/pragnakalpdev23/mysite/slack_file_display/sample-mp4-file-small.mp4',
                    # initial_comment='This is a sample video',
                    channels=channel_id
                )
            except Exception as e:
                # You will get a Exception if "ok" is False
                assert e.response["ok"] is False
                # str like 'invalid_auth', 'channel_not_found'
                assert e.response["error"]
                print(f"Got an error: {e.response['error']}")
        if text == "file":
            try:
                response = client.files_upload(
                    file='C:/Users/grant/OneDrive/Desktop/aws_hacks/for_slack/media/certificate for python.pdf',
                    # initial_comment='This is a sample file',
                    channels=channel_id
                )
            except Exception as e:
                # You will get a Exception if "ok" is False
                assert e.response["ok"] is False
                # str like 'invalid_auth', 'channel_not_found'
                assert e.response["error"]
                print(f"Got an error: {e.response['error']}")

        if text == "audio":
            try:
                response = client.files_upload(
                    file='/home/pragnakalpdev23/mysite/slack_file_display/file_example_MP3_700KB.mp3',
                    # initial_comment='This is a sample audio',
                    channels=channel_id
                )
            except Exception as e:
                # You will get a Exception if "ok" is False
                assert e.response["ok"] is False
                # str like 'invalid_auth', 'channel_not_found'
                assert e.response["error"]
                print(f"Got an error: {e.response['error']}")
            

    """
        if f'@{user_id}' not in welcome_messages:
            return

        welcome = welcome_messages[f'@{user_id}'][user_id]
        welcome.completed = True
        welcome.channel = channel_id
        message = welcome.get_message()
        updated_message = client.chat_update(**message)
        welcome.timestamp = updated_message['ts']"""



    app.run(debug=True)
#for_s(os.getenv('SLACK_TOKEN'),os.getenv('SLACK_SIGNING_SECRET_'),'hoo therere','C:/Users/grant/OneDrive/Pictures/Screenshots/Screenshot 2022-06-05 101023.png')
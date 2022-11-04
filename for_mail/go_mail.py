
import os
import smtplib
import imghdr
from email.message import EmailMessage
from time import sleep



import datetime as dt
import os
import dotenv

import json
dotenv.load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_USER')

EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

def for_e(message,img):
    contacts = ['poorvikjaintm@gmail.com', '20is032@gmail.com']

    msg = EmailMessage()
    msg['Subject'] = 'Check out Bronx as a puppy!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts[0]

    #msg.extra_headers = {'X-SMTPAPI': json.dumps({'send_at': time() + 120})}


    msg.set_content(message)

    with open(img, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    msg.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    
    send_time=dt.datetime.today()
    add_time=dt.timedelta(seconds=120)
    final_time=add_time+send_time

    #print(send_time)
    #print((final_time-send_time).seconds)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        #sleep(10)

        smtp.send_message(msg)





    """

    def send_email():
        email_user = 'myemail@gmail.com'
        server = smtplib.SMTP ('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, 'email pass')

        #EMAIL
        message = 'sending this from python!'
        server.sendmail(email_user, email_user, message)
        server.quit()

    send_time = dt.datetime(2018,8,26,3,0,0) # set your sending time in UTC
    time.sleep(send_time.timestamp() - time.time())
    send_email()
    print('email sent')
    If you want to send the email regularly, you can do:

    import datetime as dt
    import time
    import smtplib

    def send_email():
        email_user = 'myemail@gmail.com'
        server = smtplib.SMTP ('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, 'email pass')

        #EMAIL
        message = 'sending this from python!'
        server.sendmail(email_user, email_user, message)
        server.quit()

    def send_email_at(send_time):
        time.sleep(send_time.timestamp() - time.time())
        send_email()
        print('email sent')

    first_email_time = dt.datetime(2018,8,26,3,0,0) # set your sending time in UTC
    interval = dt.timedelta(minutes=2*60) # set the interval for sending the email

    send_time = first_email_time
    while True:
        send_email_at(send_time)
        send_time = send_time + interval


    """
#for_e("hiii",'C:/Users/grant/OneDrive/Pictures/Screenshots/Screenshot 2022-06-05 101023.png')
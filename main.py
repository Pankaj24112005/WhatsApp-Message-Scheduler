# """
# twilio
# datetime module
# time module

# """

# """
# 1-twilio client setup
# 2-user inputs
# 3-scheduling logic
# 4-send message
# """


# step1 install required libraries
from twilio.rest import Client #it use for 
from datetime import datetime, timedelta
import time   # for adding delay

# step2 - twilio credentials
account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)  #useto create a client object to interact with the Twilio API

# step3 - send message function
def send_whatsapp_message(recipient_number,message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',  # Twilio sandbox number for WhatsApp
            body = message_body,
            to = f'whatsapp:{recipient_number}'
        )
        print(f"Message sent successfully! Message SID{message.sid}")
    except Exception as e:
        print('An error occured!')

# step4 - user inputes
name = input("Enter recipients name: ")
recipient_number = input("Enter recipient's WhatsApp number with country code (e.g, +12345): ")
message_body = input(f"Enter the message you want to send to {name}: ")



# step5- parse date/time and calculate delay
date_str = input("Enter the date  to send the message (YYYY-MM-DD): ")
time_str= input("Enter the time to send the message (HH:MM in 24-hour format): ")

# datetime module is used to parse the date and time strings into a datetime object
schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")     #strp means string parse time:- it converts date time into string object formate
current_datetime = datetime.now()  #it gives current date and time

# calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()  #it gives total seconds of time difference

if delay_seconds <=0:
    print("Scheduled time is in the past! Please enter a future date and time.")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}.")

    # wait unitl the cheduled time
    time.sleep(delay_seconds)  #it adds delay for the specified number of seconds

    # send the message:
    send_whatsapp_message(recipient_number,message_body)



#!/usr/bin/python3

import requests, bs4, re, os, smtplib, sys, time
from discord_messenger import DiscordMessenger

#url = 'https://www.instagram.com/asweatyevening/?__a=1'
#url = 'https://www.instagram.com/asweatyevening/'
url = 'https://futurarchives.com/password'
#webook_url = os.environ['WEBHOOK_URL']

try:
    gmail_user = os.environ['GMAIL']
    gmail_password = os.environ['GMAIL_PASSWORD']
    webhook_url = os.environ['WEBHOOK_URL']
except Exception as e:
    print(e)


status_filepath = os.path.join(os.path.dirname(sys.argv[0]), "status.txt")
if not os.path.exists(status_filepath):
    with open(status_filepath, 'w') as infile:
        infile.write("closed")

def update_status_text_file(status):
    os.remove(status_filepath)
    with open(status_filepath, "w") as infile:
        infile.write(status)

with open(status_filepath, "r") as infile:
    if infile.read() == 'closed':
        store_closed = True
    else:
        store_closed = False

regex = r'\[\<.+\>\n\s+(.+)'
locked_string = 'L O A D I N G  .  .  .'
sleep_seconds = 5

while True:
    r = requests.get(url=url)
    soup = bs4.BeautifulSoup(r.text, features="html.parser")

    url_response = str(soup.select('.password__form-heading'))

    # in the case when store opens, loading text is removed and html returns null or '[]'
    if url_response == "[]":
        text = ""
    else:
        text = re.match(regex, url_response).groups()[0].strip()

    # Instanciate Discord Messager class
    bot = DiscordMessenger(webhook_url)

    if text == locked_string:
        if not store_closed: # store was open, but is now closed
            bot.send_store_closed_message() 

            #update text file
            update_status_text_file("closed")
            store_closed = True
    else:
        if store_closed:  # store was closed but is now open
            bot.send_store_open_message()

            # update text file
            update_status_text_file("open")
            store_closed = False

    time.sleep(sleep_seconds)

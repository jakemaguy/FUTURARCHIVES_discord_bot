#!/usr/bin/python3

import requests, bs4, re, os, smtplib, sys
from discord_webhook import DiscordWebhook, DiscordEmbed

#url = 'https://www.instagram.com/asweatyevening/?__a=1'
#url = 'https://www.instagram.com/asweatyevening/'
url = 'https://futurarchives.com/password'
#webook_url = os.environ['WEBHOOK_URL']

if (len(sys.argv) - 1) != 3:
    print("script <gmail_user> <gmail_password> <webhook_url")
    exit(1)
gmail_user = sys.argv[1]
gmail_password = sys.argv[2]
webhook_url = sys.argv[3]


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

payload = {'compression' : '--compressed'}
r = requests.get(url=url)

soup = bs4.BeautifulSoup(r.text, features="html.parser")

url_response = str(soup.select('.password__form-heading'))
text = re.match(regex, url_response).groups()[0].strip()

if text == locked_string:
    if not store_closed:
        webhook = DiscordWebhook(url=webhook_url, username="FUTUR.io")
        embed = DiscordEmbed(title="Store Update", description="Store is closed", color=242424)
        embed.add_embed_field(name="Website Link", value=url)
        embed.set_timestamp()
        webhook.add_embed(embed)
        webhook.execute()
        
        #update text file
        update_status_text_file("closed")
else:
    if store_closed:
        webhook = DiscordWebhook(url=webhook_url, username="FUTUR.io")
        embed = DiscordEmbed(title="Store Update", description="Store is now open", color=242424)
        embed.add_embed_field(name="Website Link", value=url)
        embed.set_timestamp()
        webhook.add_embed(embed)
        webhook.execute()

        # update text file
        update_status_text_file("open")

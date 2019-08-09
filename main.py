#!/usr/bin/python
import requests, bs4, re
from discord_webhook import DiscordWebhook, DiscordEmbed

#url = 'https://www.instagram.com/asweatyevening/?__a=1'
#url = 'https://www.instagram.com/asweatyevening/'
url = 'https://futurarchives.com/password'
webhook_url = 'https://discordapp.com/api/webhooks/609211859031162880/2lwMQfwGZute4hvN8HcBZMgudGy4whPhLRjUvjoIrh97fbO7O4Mtvsg-Fef9QFpw0nJo'


with open("status.txt", "r") as infile:
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
text = re.match(regex, url_response).groups()[0]

if text == 'L O A D I N G  .  .  .':
    """
    webhook = DiscordWebhook(url=webhook_url, username="FUTUR.io")
    embed = DiscordEmbed(title="Store Update", description="Store is closed", color=242424)
    embed.add_embed_field(name="Website Link", value=url)
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()
    """
else:
    """
    webhook = DiscordWebhook(url=webhook_url, username="FUTUR.io")
    embed = DiscordEmbed(title="Store Update", description="Store is now open", color=242424)
    embed.add_embed_field(name="Website Link", value=url)
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()
    """
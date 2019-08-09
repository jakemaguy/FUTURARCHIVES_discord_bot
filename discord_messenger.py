from discord_webhook import DiscordWebhook, DiscordEmbed

class DiscordMessenger:

    def __init__(self, webhook_url):
        self.webhook = DiscordWebhook(url=webhook_url, username="FUTUR.io")
        self.website_url = 'https://futurarchives.com/password'
    
    def send_warning_message(self, message):
        embed = DiscordEmbed(title="Warning Message", description=message, color=242424)
        embed.set_timestamp()
        self.webhook.add_embed(embed)
        self.webhook.execute()
        self.remove_embeds_from_webhook()

    def send_store_open_message(self):
        embed = DiscordEmbed(title="Store Update", description="Store is now open", color=242424)
        embed.add_embed_field(name="Website Link", value=self.website_url)
        embed.set_timestamp()
        self.webhook.add_embed(embed)
        self.webhook.execute()
        self.remove_embeds_from_webhook()

    def send_store_closed_message(self):
        embed = DiscordEmbed(title="Store Update", description="Store is closed", color=242424)
        embed.add_embed_field(name="Website Link", value=self.website_url)
        embed.set_timestamp()
        self.webhook.add_embed(embed)
        self.webhook.execute()
        self.remove_embeds_from_webhook()
    
    def remove_embeds_from_webhook(self):
        for i, embed in enumerate(self.webhook.get_embeds()):
            self.webhook.remove_embed(i)


from discord_webhook import DiscordWebhook, DiscordEmbed


class DiscordMessenger:

    def __init__(self):
        self.webhook = DiscordWebhook(url=webhook_url, username="FUTUR.io")
    
    def send_warning_message(self, message):
        embed = DiscordEmbed(title="Warning Message", description=message, color=9e0310)
        embed.set_timestamp()
        self.webhook.add_embed(embed)
        self.webhook.execute()


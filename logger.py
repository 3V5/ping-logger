import discord
from discord.ext import commands
from discord.ext import tasks
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordWebhook, DiscordEmbed

DiscordID = "" #Your Discord ID
Webhook = "" # Your Discord Webhook
Icon = "" # Webhook Icon URL
token = "" # Your discord token
prefix = "!"
client = commands.Bot(command_prefix=prefix)

@client.event
async def on_message(message):
    async for message in message.channel.history(limit=1):
        if DiscordID in message.content:
            msgcontent = str(message.content)
            msgguild = str(message.guild)
            webhook = DiscordWebhook(url=Webhook, username="Soy Ping Logger")
            embed = DiscordEmbed(title='New Ping!', description='Caused By: '+str(message.author), color=242424)
            embed.set_author(name='Soy Util', url='https://sex.com', icon_url=Icon)
            embed.set_footer(text='New Ping!')
            embed.set_timestamp()
            embed.add_embed_field(name="Message Details: ", value=f"Content: {message.content} \nGuild: {message.guild}\nLink: [click here]({message.jump_url})")
            webhook.add_embed(embed)
            response = webhook.execute()

client.run(token, bot=False)

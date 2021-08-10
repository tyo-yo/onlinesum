import logging
import os

import discord

client = discord.Client()

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)


@client.event
async def on_ready():
    logger.debug("Ready!")
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    logger.debug("on_message()")
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


client.run(os.getenv("DISCORD_API_TOKEN"))

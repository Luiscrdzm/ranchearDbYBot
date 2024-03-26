import discord
from discord.ext import commands,tasks,bridge
import mysql.connector
import os
import json

sql=mysql.connector.connect(
    host="localhost",
    database="stva",
    user="discterminal",
    password="ranchear"
)

Ramireth=bridge.Bot(owner_id=int(os.environ["owner_id"]))

canales=json.load(open("tcanales.json"))

@Ramireth.event
async def on_ready():
    u=Ramireth.get_user(int(os.environ["owner_id"]))
    await u.send("Junciono!")

@Ramireth.bridge_command(is_admin=True)
async def set_terminal_channel(ctx,channel:discord.TextChannel):
    canales[str(ctx.guild.id)]=channel.id
    json.dump(canales,open("tcanales.json","w"))
    await ctx.send(f"Ahora la terminal estara disponible en {channel.mention}")

cursor=sql.cursor()
@Ramireth.event
async def on_message(msg:discord.Message):
    if msg.author.bot:
        return
    if str(msg.guild.id) not in canales.keys():
        return
    if msg.channel.id==canales[str(msg.guild.id)]:
        await msg.add_reaction("✅")
        cursor.execute(str(msg.content))
        response=cursor.fetchall()
        await msg.reply(response)

Ramireth.run(os.environ["ranchear"])
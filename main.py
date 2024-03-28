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

Ramireth=bridge.Bot(owner_id=int(os.environ["owner_id"]),intents=discord.Intents.all())

canales=json.load(open("tcanales.json"))

@Ramireth.event
async def on_ready():
    u=await Ramireth.fetch_user(int(os.environ["owner_id"]))
    await u.send("Junciono!")

@Ramireth.bridge_command(is_admin=True)
async def set_terminal_channel(ctx,channel:discord.TextChannel):
    canales[str(ctx.guild.id)]=channel.id
    json.dump(canales,open("tcanales.json","w"))
    await ctx.reply(f"Ahora la terminal estara disponible en {channel.mention}")

async def terminal_response(tup:list,ch:discord.TextChannel):
    if tup==[]:
        return
    msg=""
    for t in tup:
        if len(msg)+len(str(t))>2000:
            await ch.send(msg)
            msg=""
        msg+=str(t)+"\n"
    if len(msg)>0:
        await ch.send(msg)
    return

@Ramireth.event
async def on_message(msg:discord.Message):
    if msg.author.bot:
        return
    if str(msg.guild.id) not in canales.keys():
        return
    if msg.channel.id==canales[str(msg.guild.id)] and msg.content!="":
        cursor=sql.cursor()
        await msg.add_reaction("🆙")
        cursor.execute(msg.content)
        res=cursor.fetchall()
        await terminal_response(res,msg.channel)
        await msg.remove_reaction("🆙",Ramireth.user)
        cursor.close()

Ramireth.run(os.environ["ranchear"])
import discord
from discord.ext import commands,tasks,bridge
import mysql.connector
import os
import json
import os
from tabulate import tabulate

os.chdir(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists("last_querys"):
    os.mkdir("last_querys")

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
    print("Junciono!")

@Ramireth.bridge_command(is_admin=True)
async def set_terminal_channel(ctx,channel:discord.TextChannel):
    canales[str(ctx.guild.id)]=channel.id
    json.dump(canales,open("tcanales.json","w"))
    await ctx.reply(f"Ahora la terminal estara disponible en {channel.mention}")

async def terminal_response(msg:str,ch:discord.TextChannel):
    if msg=="":
        await ch.send("Set vacio")
        return
    print(os.getcwd())
    with open(f"last_querys/{ch.guild.id}.txt","w") as f:
        f.write(msg)
    f.close()
    await ch.send(file=discord.File(f"last_querys/{ch.guild.id}.txt"))
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
        try:
            cursor.execute(msg.content)
        except mysql.connector.ProgrammingError as er:
            await msg.remove_reaction("🆙",Ramireth.user)
            await msg.add_reaction("❌")
            await msg.reply(f"❌ {er} ❌")
            cursor.close()
            return
        res=str(tabulate(cursor.fetchall(),headers=cursor.column_names,numalign="right",floatfmt=".2f"))
        await terminal_response(res,msg.channel)
        await msg.remove_reaction("🆙",Ramireth.user)
        cursor.close()

Ramireth.run(os.environ["ranchear"])
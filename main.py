import discord
from discord.ext import commands,tasks,bridge
import mysql.connector
import os

sql=mysql.connector.connect(
    host="localhost",
    database="stva",
    user="discterminal",
    password="ranchear"
)

Ramireth=bridge.bot(owner_id=int(os.environ["owner_id"]))

@Ramireth.event
async def on_ready():
    u=Ramireth.get_user(int(os.environ["owner_id"]))
    await u.send("Junciono!")

Ramireth.run(os.environ["ranchear"])
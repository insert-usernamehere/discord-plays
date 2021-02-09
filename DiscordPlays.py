import time
import subprocess
import ctypes
import random
import string
import pyautogui
import pynput
from pynput.mouse import Button, Controller
import discord
from discord.ext import commands
try:
    from key import *
except Exception:
    print("failed to load key.py any attempt to run a session will result in a crash")


client = commands.Bot(command_prefix='.')
ownerid = YOURID
bottoken = 'botid'
#ignore all varibles below this point
dpch = 00000000000000000
botvc = 00000000000000000

#where actual code goes
@client.event
async def on_message(message):
    await client.process_commands(message)
    if (message.channel.id == dpch):
        if message.author.voice and message.author.voice.channel:
            if (message.author.voice.channel == botvc):
                print(message.content + ':' +str(message.author))
                if message.content.lower().startswith("w"):
                    PressAndHoldKey(W, 2)
                if message.content.lower().startswith("a"):
                    PressAndHoldKey(A, 2)
                if message.content.lower().startswith("s"):
                    PressAndHoldKey(S, 2)
                if message.content.lower().startswith("d"):
                    PressAndHoldKey(D, 2)

#Ignore everything past this point
@client.event
async def on_ready():
    print(f'{client.user} is running discord plays')

    
@client.command()
async def start(ctx):
    if ctx.author.id == ownerid:
        if ctx.author.voice and ctx.author.voice.channel:
            global botvc
            botvc = ctx.author.voice.channel
            try:
                await botvc.connect()
                global dpch
                dpch = ctx.channel.id
                await ctx.send("discord plays started any commands sent in this channel will be recorded as a key press")
            except Exception:
                await ctx.send("an error occured, this probably was caused because I'm already in a vc or I can't join one")
        else:
            await ctx.send("you must be in a vc to start discord plays")
        

@client.command()
async def stop(ctx):
    if ctx.author.id == ownerid:
        try:
            await ctx.voice_client.disconnect()
            global dpch
            dpch = 0000000000000000
            await ctx.send("discord plays stopped")
        except Exception:
            await ctx.send("an error occured, this probably was caused because I'm not in a vc")


client.run(bottoken)                

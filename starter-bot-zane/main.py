#Starter Discord bot For Beginner coders!
# Author: .zanefrs#7619
# 15 September 2021 - Zane's Starter Bot

# THESE ARE RANDOM IMPORTS I USE. YOU DO NOT NEED TO INSTALL ALL BELOW BUT INSTALL THE ONES YOUR CONSOLE TELLS YOU. You can install all of these so you wont need to in the future if you want.

import discord
import asyncio
import requests
import ctypes
import threading
import datetime
import json
import re
import socket
import time
import os
import os.path
import io
import sys
import platform
import subprocess
import psutil
import ast
import logging
import timedelta
import traceback
import clock
from discord.utils import get
from os import system, path
from datetime import datetime, timedelta
from discord import Member
from discord.ext import commands

bot=commands.Bot(command_prefix="!") # Sets prefix to what you desire

bot.uptime = datetime.utcnow() # This will Define the bots uptime/time/date

bot.remove_command('help') # This removes the default help command.

#on start activities for the bot
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Games with friends!")) # Changes the presence of the bot.
    print(f'Bot Is Online') # Tells that bot is online in the console.


# This is the INFO command. This is an example for a simple command.
@bot.command(name='info', aliases=['about'])
async def info(ctx):
	await ctx.message.delete() # This deletes your message when you do the command.
	embed = discord.Embed(title='**Simple Starter Bot by zanefrs#7619**', description='You can do `!help` for a list of commands!', color=0x89cff0) # Author: .zanefrs.
	embed.add_field(name='Made by', value='[zanefrs#7619](https://discordapp.com/users/302607309019021322)')
	await ctx.send(embed=embed) # Sends the Embed in your channel.


#This is the Ping Command. This will show the bots Ping.
@bot.command(name='ping') # name will = what you want to type in your channel. (ex. !ping)
async def ping(ctx):
	await ctx.message.delete() # This deletes your message when you do the command.
	await ctx.send("**Checking Ping...**")
	await ctx.send("🏓") 
	await asyncio.sleep(.5) # Makes the bot wait a certain amount of time before posting.
	await ctx.send(f"**Result:** `{round(bot.latency * 1000)}`") # This will grab the ping of the bot.

#Help Command
@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='**Starter Bot Commands**', description='*You can test these commands in your discord channels and edit them how you want!*', color=0x36393F)
    embed.add_field(name='!ping', value="Shows the bots ping!")
    embed.add_field(name='!info', value="Gives a simple information embed!")
    embed.add_field(name='!count', value="Shows how many members you have in your server!")
    embed.add_field(name="!whois", value="Gives a members information!")
    embed.add_field(name="!say (message)", value="Will send whatever you want to say but will make the bot say it!")
    embed.set_footer(text="Discord Starter Bot by zanefrs")
    await ctx.send(embed=embed)

#Get Member Count
@bot.command()
@commands.has_permissions(kick_members=True) # If you have Kick Members permission in the discord you are in you can use this command. You can change this to whatever.
async def count(ctx):
    await ctx.message.delete()
    print(ctx.guild.member_count) # This is here to test to see if your console is working.
    embed = discord.Embed(description=f"➤ Discord member count: **{ctx.guild.member_count}**", color=0x36393F, delete_after=5.0) # This will show the member count.
    embed.set_footer(text="Discord Starter Bot by zanefrs")
    await ctx.send(embed=embed) # Sends the embed in the channel

#Get User info
@bot.command()
@commands.has_permissions(kick_members=True)
async def whois(ctx, member: discord.Member = None):
    await ctx.message.delete()
    member = ctx.author if not member else member
    roles = [role for role in member.roles]
    current_utc = datetime.utcnow() # Grabs the current time.

    embed = discord.Embed(color=0x36393F, timestamp=ctx.message.created_at)
    embed.set_author(name=f"{member}", url="https://discordapp.com") # Their name
    embed.add_field(name=f"**➤** User ID", value=member.id) # Grabs the members user ID.
    embed.add_field(name=f"**➤** Created at", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p")) # Shows when the members account was made. (read docs if you dont understand %a, etc)
    embed.add_field(name=f"**➤** Joined At", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p")) # When the member joined your server.
    embed.add_field(name="➤ Top Role:", value=member.top_role.mention) # The Highest role in your guild.
    embed.add_field(name=f"➤ Bot?", value=member.bot) # Identifies if the member is a bot or not.
    embed.set_footer(text="Discord Starter Bot by zanefrs") # Bottom text
    await ctx.send(embed=embed)

#Say Command
@bot.command()
async def say(ctx, *, message=None):
    await ctx.message.delete()
    await ctx.send(message) # This will make the bot delete your message and post what you said but by itself.

bot.run("ODM1NjI1NDE2MDA5NDQ5NDcy.YISK0A.qzsQVaJ8N3MX7rh6mvoCVw5CZjA") # Put your bot token here. Make sure to read Readme.md if you have not already!


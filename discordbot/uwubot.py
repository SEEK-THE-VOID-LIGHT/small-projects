# uwubot.py

import discord
import io
from discord.ext import commands
import youtube_dl
from discord.utils import get
from discord import FFmpegPCMAudio
import os
from os import system
import random as r
from random import randint
import asyncio
import sys
import pyfiglet
from varia import *

bot = commands.Bot(command_prefix="pls ")

bilder = ["bild1.jpg", "bild2.jpg", "bild3.jpg", "bild4.jpg", "bild5.jpg", "bild6.jpg", "bild7.jpg", "bild8.jpg", "bild9.jpg", "bild10.jpg", "bild11.jpg", "bild12.jpg", "bild13.jpg"]
anime = ["ani1.jpg", "ani2.jpg", "ani3.jpg", "ani4.jpg", "ani5.jpg", "ani6.jpg"]
image_count = 13
ani_count = 6
passwort=0

confirm1 = False
confirm2 = False



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "Hallo":  #Hallo
        print("motion-trigger: friendly approach")
        await message.channel.send(f"Hallo {message.author.mention}")

    if message.content.lower().find(" raumschiff") != -1:   #raumschiff find
        print("motion-trigger: raumschiff")
        await message.channel.send("Ist es ne S-Klasse?\nOder was anderes?")

    if message.content.lower().find("rechte") != -1:   #sucht nach dem wort rechte
        print("motion-trigger: rechte")
        await message.channel.send("Es geht nicht immer nur um Rechte. Mein, dein. Das sind nur bürgerliche Kategorien.")

    if message.content.lower() == "wer bist du?":   #identität
        identität = "Hallo. ich bin ein Bot, der aber nicht alles kann. Ich bin " + str(os.path.getsize('uwubot.py')) + "Byte groß und bin nicht böse. Ich bin noch nicht fertig programmiert.\nIch bin nicht immer online. Ich bin dann online, wenn das Script, was mich ausmacht, läuft."
        print("identität angeordnet")
        await message.channel.send(identität)

    if message.content.lower() == "gib mir ein bild": #bilder
        print("Bilderreihe")
        bilderreihe = r.choice(bilder)
        await message.channel.send("Hier hast du ein aus " + str(image_count) + " Bildern zufällig ausgewähltes Bild :wink:" , file=discord.File(bilderreihe))

    if message.content.lower().find("mädchen") != -1 or message.content.lower().find("girl") != -1:     #maedchen
        print("motion-trigger: girl or mädchen")
        await message.channel.send("Hello girl :smirk:! Let me sing my ABC to you :smirk:\n\nI'll give you an 'A' because you're AWESOME.\nI'll give you a 'B' because you're BEAUTIFUL.\nI'll give you a 'C' because you're confident.\nAnd I'll give you this D because you deserve it.\n\n\nDO YOU WANT THE D??? :smiley:")

    if message.content.lower().find("anime") != -1: #motion-trigger:anime
        print("motion-trigger: anime")
        animebild = r.choice(anime)
        await message.channel.send("Apropros anime: Hier hast du ein Bild von einem Animecharakter, der aus " + str(ani_count) + " Bilder zufällig ausgewählt wurde :wink:", file=discord.File(animebild))

    if message.content.lower().find("terror") != -1:
        print("motion-trigger: terror")
        await message.channel.send("Epic saleel al sawarim for you :gun:")    #motion-trigger:terror

    await bot.process_commands(message)

#This shutdown method is not used
"""@bot.command(description='close the bot instance')
async def bot_shutdown(ctx):
    print("logout attempted with code")
    if ctx.author.id == 336808735391612938:
        print("<1>")
        await ctx.send("logout-process initiated")
        await bot.logout()
    else:
        print("<0>")
        await ctx.send(f"Du hast keine Rechte dazu {message.author.mention}")"""


#begin shutdown with password lock
@bot.command(description="shut down the bot. USE WITH CAUTION!")
async def bot_shutdown(ctx):
    """shut the bot down"""
    global confirm1
    global confirm2
    confirm1 = True
    confirm2 = False
    global passwort
    passwort=r.randint(100000, 999999)
    print("the current password is " + str(passwort))
    await ctx.send("Code erfolgreich generiert!\nNutze '?confirm <Passwort>', um den Bot herunterzufahren...")
#end shutdown with password
    
@bot.command(description="display current password of the logout state")
async def display_passwd(ctx):
    """display generated password"""
    print("password display exited with code")
    if confirm1 == True:
        if ctx.author.id == 336808735391612938:
            print("<1>")
            await ctx.send("Das Passwort ist: " + str(passwort))
        else:
            print("<0>")
            await ctx.send("Du musst nich nicht herunterfahren!")
    else:
            print("<1>")
            await ctx.send("Das Passwort ist: " + str(passwort))
        
def revertzero():
    global passwort
    global confirm1
    global confirm2
    confirm1 == False
    confirm2 == False
    passwort == 0
    
@bot.command(pass_context=True)
async def confirm(ctx, password):
    """confirm action with password"""
    global passwort
    if confirm1 == True:
        if int(password) == passwort:
            passwort=0
            await ctx.send("logout initiated with exit code 0")
            print("logout started")
            await bot.logout()
        else:
            await ctx.send("logout aborted with exit code 0")
            print("logout canceled")
            await ctx.send("that was the wrong password!")
    elif confirm2 == True:
        if int(password) == passwort:
            passwort == 0
            print("sourcode is starting")
            sourcecode = open("uwubot.py","r")
            await ctx.send("Der Quellcode von mir:\n")
            for line in sourcecode:
                if not line.isspace():
                    await ctx.send(line)
            #works, but file is too big
            """sourcecode = open("uwubot.py","r")
            sourcecodestring = sourcecode.read()
            await ctx.send("Der Code...")
            embed=discord.Embed(title="uwubot.py", description="Mein Code", color=0x00ff00)
            embed.add_field(name="code", value=f'``` {sourcecodestring} ```', inline=False)
            await ctx.send(embed=embed)"""
            
            revertzero()
        else:
            await ctx.send("wrong password")
            revertzero()
    else:
        await ctx.send("Hmm, aber alles Gut :wink: Es wurde noch kein Passwort generiert.\nSieht so aus, als würde keins gebraucht werden.")

        
        
@bot.command()
async def mehr(ctx):
    print("more displayed")
    await ctx.send("Ich reagiere manchmal auf ein paar Sachen, die du sagst.\nwenn du wissen willst, wer ich bin und was ich mache, gib 'Wer bist du?' ein.")
    
@bot.command(description='more commands')
async def command_list(ctx):
    """additional commands"""
    print("help+ listet")
    await ctx.send("Hier sind noch ein paar kleine Befehle, die aber eher unwichtig sind:\n'Wer bist du?'\n'Gib mir ein Bild'\n'Wer bin ich?'\nich reagiere zum Beispiel darauf, wenn du Wörter wie Raumschiff oder Anime sagst... Aber auch andere Wörter :wink:\nIch werde weiterentwickelt, also keine Sorge :)")

@bot.command()
async def userinfo(ctx, member: discord.Member):
    """zeig info über einen mentioned user"""
    print(f"information redeemed of member {member.name}")
    rolesstringwtf = ' , '.join(str(x) for x in member.roles)
    await ctx.send(f'User name: {member.name}, id: {member.id}, roles: {rolesstringwtf.replace("@everyone","everyone")}')
    
    
@bot.command()
async def gruesse(ctx, member: discord.Member):
    """gruesst einen mentioned user"""
    print(f"{member.name} wurde gegruesst")
    await ctx.send(f"Ich gruesse {member.mention} :smiley:")


@bot.command()
async def servers(ctx):
    """servers the bot is in"""
    if ctx.author.id == 336808735391612938:
        await ctx.send(bot.guilds)
        print("Bot guild request positive")
    else:
        print("Bot guild request negative")
        await ctx.send("Du musst nicht umbedingt wissem, wo ich überall bin...")
        
@bot.command()
async def ascii(ctx, text):
    """convert text to ascii"""
    banner = pyfiglet.figlet_format(text)
    print(f"ascii request with '{text}'")
    await ctx.send(f"```{banner}```")


@bot.command()
async def sourcecode(ctx, description="displays the sourcecode. USE WITH CAUTION"):#BETA
    """offline"""
    await ctx.send("Feature currently unavailable")
    """print("sourcecode sequence initiated. Waiting to confirm...")
    global confirm2
    global confirm1
    confirm1 = False
    confirm2 = True
    global passwort
    passwort = r.randint(100000, 999999)
    await ctx.send("Are you sure you want to see the source code? These are many lines and you may have the bot stuck.\nIf you are sure, look up you password with ?display_passwd and confirm it with ?confirm")"""
    
    
    
    
@bot.command(pass_context=True)
async def play(ctx, url: str, description="be connected before the bot does"):
    """play music from youtube url"""
    channel = ctx.author.voice.channel
    await channel.connect()
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        print("PermissionError: Da ist was schiefgeleaufen")
        return
    await ctx.send("Ich mache es fertig, gib mir ne Sekunde")
    print(f"music sequence started successful by {ctx.author.name}")
    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()
    
@bot.command(description='leave current voice channel')
async def stop(ctx):
    """stop the music"""
    if ctx.author.id == 390594608922624000:
        await ctx.send("Tja ich bin jetzt sauer auf dich :(")
    else:
        await ctx.voice_client.disconnect()
    
#here comes the new feature if added


@bot.command()
async def changelog(ctx, description="Displays the changelog and current version"):
    await ctx.send("""
```Changelog: Flixiplay's interessanter Bot
Version: 0.2.11

--> fixed bug in ?userinfo: displaying @ everyone ==> replayced all @ everyone with everyone
--> fixed bug in ?userinfo: displaying role IDs
--> added ?sourcecode
--> added ?ascii command: Convert Text to ascii
--> added ?play and ?stop command: Play sound on voice channel
--> deleted ?join and ?leave command```
""")

  
@bot.event
async def on_ready():
    print('Login initiation done as')
    print(bot.user.name)
    print(bot.user.id)
    activity = discord.Game(name="pls help", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)


bot.run(LOGIN_TOKEN1)

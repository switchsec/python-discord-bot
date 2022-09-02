import discord
from discord.ext import commands
import time#Developer SwitchSec

from os import system

intents = discord.Intents(messages = True, guilds= True, reactions = True, members = True, presences = True)
Bot = commands.Bot(command_prefix = "ocx!", intents = intents)
Bot.remove_command('help')
#Developer SwitchSec

@Bot.event
#Burayı ellemeyin yoksa bot bozulur
async def on_ready():
    print("Ben Hazırım!")
    activity = discord.Activity(type=discord.ActivityType.watching, name="TabPlusDev & Ocx Security Systems")
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='TabPlusDev & Ocx Security Systems'))
    print("---------------")
    print("Ocx Security")
    print("Switch Space")
    print("Ashwai")#Emeğe saygı için lütfen değiştirmeyiniz
    print("---------------")
    print("Bot Aktif !")
    user = Bot.get_user(539696174190559232)
    await user.send('Artık aktifim haberin olsun :)')#Developer SwitchSec

#--------------------------------------------------------------

@Bot.event
async def on_command_error(ctx ,eror):
    await ctx.send(f'Command is not found')
  
@Bot.event
async def on_member_join(member): #Sunucuya üye katıldıysa
    channel = discord.utils.get(member.guild.text_channels, name="kanal_adi")#Developer SwitchSec

    await channel.send(f"{member} aramıza katıldı :)")
    await member.send(f'```  {member} aramıza hoşgeldin kanka .\n\t Web Page : https://www.tabplusdev.tk \n\n\t TabPlusDev Adlı Sunucu Ocx Security Bot Tarafından Korunmaktadır . \n\t Senden sunucunu Korumak  istiyorsan adminlerime ulaşabilirsin ``` ')

@Bot.event
async def on_member_remove(member): #Sunucudan üye ayrıldıysa
    channel = discord.utils.get(member.guild.text_channels, name="kanal_adi")#Developer SwitchSec

    await channel.send(f"{member} aramızdan ayrıldı :(")#Developer SwitchSec


#Küfürler 
badwords = ['yarrak', 'amk','amina','amınakoyum','amına','amık','yarak','göt','napim','awk','piç','urxbu','çocu','çocuğu','ananı sikerim','sik','sikerim']
@Bot.event
async def on_message(message):
   for i in badwords: # Go through the list of bad words;
       
        if i in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention} Don't use that word!")
            Bot.dispatch('profanity', message, i)
            return # So that it doesn't try to delete the message again, which will cause an error.
   await Bot.process_commands(message)#Developer SwitchSec

@Bot.event
async def on_profanity(message, word):
   channel = Bot.get_channel(839869309480337518) # for me it's bot.get_channel(817421787289485322)
   embed = discord.Embed(title="Profanity Alert!",description=f"{message.author.name} just said ||{word}||", color=discord.Color.blurple()) # Let's make an embed!
   await channel.send(embed=embed)
#Developer SwitchSec




#User Commands 
@Bot.command()#Developer SwitchSec

async def tabplusdev(ctx):
    await ctx.send("En İyisi!")#Eğer tabplusdev yazıldıysa
@Bot.command()
async def kurucu(ctx):
    await ctx.send("Switch Sec \n Github : switchsec \n İnstagram : _ahmetonlinee")#Emeğe saygı için lütfen ellemeyiniz
    #Emeğe saygı#Developer SwitchSec

@Bot.command(name = 'prefix')
async def on_message(ctx):
    prefix = "ocx!"#Prefix ayarlama
    await ctx.send(f'İşte prefixim || {prefix} ||')
    
@Bot.command(name = 'chat-bot')#Napim ve sanane engel
async def on_message(ctx):
    napimEngel = ["Napim","NAPİM","napim","napım","nApİm","n4p1m","npm","napiimm","napm"]
    sananeEngel = ["Sanane","sanane","snne","snane","s4n4n3","san4ne","s4nan3","sanan3","sAnAnE","SaNaNe"]
    for commandsnapim in napimEngel :#Developer SwitchSec

        if commandsnapim in message.content:
            await ctx.send("Kardeş burdan bir vurarsam ölersin ")
    for commandsanane in sananeEngel : 
        if commandsanane in message.content:#Developer SwitchSec

            await ctx.send("Hıııı saman ye saman ye")
    

    



#Help Commands Category#Developer SwitchSec

@Bot.command(name='help-commands')
async def on_message(ctx):
    await ctx.send("``` Help Commands \n\t ocx!help-commands = Show the help commands \n\t ocx!help-user = Show user commands \n\t ocx!help-admin = Show the admin commands \n\n\t Prefix = ocx! \n\n Developer : TabPlusDev & Ashware // Asheap ```")
@Bot.command(name='help-user')
async def on_message(ctx):
    await ctx.send("```User Commands \n\t ocx!help-commands = Show the help commands \n\t ocx!tabplusdev = Show best  \n\t ocx!prefix = Show the prefix \n\n\t Prefix = ocx! \n\n Developer : TabPlusDev & Ashware // Asheap``` ")
@Bot.command(name='help-admin')
async def on_message(ctx):
    await ctx.send("``` Admin Commands \n\t ocx!help-commands = Show the help commands \n\t ocx!server = Show the server info \n\t ocx!clear value = Cleans up to the value you give \n\t ocx!ban @member = Ban command \n\t ocx!kick @member = Kick command \n\t ocx!say = Counts server members  \n\n\t Prefix = ocx! \n\n Developer : TabPlusDev & Ashware // Asheap```")

#Developer SwitchSec




#Admin Commands
@Bot.command(name='say')#Server Üye Sayısını verir
@commands.has_role("Admin")
async def fetchServerInfo(context):
	guild = context.guild#Developer SwitchSec

	await context.send(f'Server Size: {len(guild.members)}')


@Bot.command()
@commands.has_role("Admin")#Eğer kullanıcıda Admin rolü varsa 
async def clear(ctx, amount=5):#Kanal siler
    await ctx.channel.purge(limit=amount)
    await ctx.send("Refreshing channel .")#Developer SwitchSec


@Bot.command()
@commands.has_role("Admin")#Eğer kullanıcıda Admin rolü varsa 
async def kick(ctx, member: discord.Member ,*args, reason="Yok" ):
    if commands.has_role:#Üye kickleme
        await member.kick(reason=reason)#Developer SwitchSec
    else:#Developer SwitchSec

        await ctx.send("You don't have a role to do that")

@Bot.command()
@commands.has_role("Admin")#Eğer kullanıcıda Admin rolü varsa 
async def ban(ctx, member: discord.Member ,*args, reason="Yok" ):
    await member.ban(reason=reason)#Üye banlama
#Developer SwitchSec

@Bot.command(name='server')#Server bilgi
@commands.has_role("Admin")#Eğer kullanıcıda Admin rolü varsa 
async def fetchServerInfo(context):
	guild = context.guild#Developer SwitchSec
	await context.send(f'Server Name: {guild.name}')
	await context.send(f'Server Size: {len(guild.members)}')#Developer SwitchSec

	await context.send(f'Server Owner: {guild.owner.display_name}')

@Bot.command(name='activity')#Botun aktivitesini gösterir
@commands.has_role("Admin") #Eğer kullanıcıda Admin rolü varsa 
async def on_message(ctx):#Developer SwitchSec
#Developer SwitchSec

    aktivite = activity=discord.Activity(type=discord.ActivityType.watching, name='Switch Space & Ocx Security Systems')
    await ctx.send(f'{aktivite}')#Developer SwitchSec



Bot.run('BURAYA_TOKEN_GİR') 
    #Developer SwitchSec


#Developer SwitchSec



import discord
from discord.ext import commands
import logging

#logging.basicConfig(level=logging.DEBUG)
bot = commands.Bot(command_prefix='!', description='Labelis Personal Bot')

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name + ' - (' + bot.user.id + ')')
    print()
    
# Iam Commands and Info
iamhelp = '''```COMMAND: !iam
DESCRIPTION: Assign yourself one of the optional roles
USAGE:
    !iam list     - List your optional roles
    !iam GDS      - Become a Game Design Student```'''

iamListNames = ['Game Design Student']
iamListAlias = ['GDS']

@bot.command(pass_context=True)
async def iam(ctx):
    command = ctx.message.content
    argument = ''
    try:
        argument = command.split(' ', 1)[1]
    except:
        await bot.send_message(ctx.message.channel, iamhelp)
        
    if(argument == 'list'):
        roleList = '```List of your optional roles:\n'
        found = False
        for i in ctx.message.author.roles:
            if(i.name in iamListNames):
                found = True
                roleList = roleList + '- ' + i.name + '\n'
        if(not found):
            roleList += '- none'
        await bot.send_message(ctx.message.channel, roleList + '```')
    
    if(argument == iamListAlias[0]):
        roleName = iamListNames[0]
        role = discord.utils.get(ctx.message.server.roles, name=roleName)
        
        found = False
        for i in ctx.message.author.roles:
            if(i.name == roleName):
                found = True
        if(not found):
            await bot.add_roles(ctx.message.author, role)
            await bot.send_message(ctx.message.channel, 'You are now a ' + iamListNames[0])
        else:
            await bot.send_message(ctx.message.channel, 'You already are a ' + iamListNames[0])

bot.run(os.environ.get('BOT_TOKEN', True))
import os
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
iamListNames = ['Game Design Student']
iamListAlias = ['GDS']

# Iam Help menu
def setup_ihelp():
    h = '''```COMMAND: !i
DESCRIPTION: Assign yourself one of the optional roles
USAGE:
    !i list
        List your optional roles
    !i roles
        List possible roles
    !iam <role>
        Add yourself to <role>
    !iamnot <role>
        Remove yourself from <role>```'''
    return h

ihelp = setup_ihelp()



@bot.command(pass_context=True)
async def i(ctx):
    command = ctx.message.content
    argument = ''
    try:
        argument = command.split(' ', 1)[1]
    except:
        await bot.send_message(ctx.message.channel, ihelp)
        return
    
    #!i list
    if(argument == 'list'):
        mes = await bot.send_message(ctx.message.channel, 'Showing list...')
        ilist = 'List of your optional roles:\n'
        found = False
        for i in ctx.message.author.roles:
            for j in range (len(iamListNames)):
                if(i.name == iamListNames[j]):
                    found = True
                    ilist = ilist + '`' + iamListAlias[j] + '` - ' + iamListNames[j] + '\n'
        if(not found):
            ilist += '- none'
        await bot.edit_message(mes, new_content=ilist)
        return
    
    #!i roles
    if(argument == 'roles'):
        mes = await bot.send_message(ctx.message.channel, 'Showing roles...')
        iroles = 'List of roles you can assign yourself:'
        for i in range(len(iamListNames)):
            iroles = iroles + '\n`' + iamListAlias[i] + '` - ' + iamListNames[i]
        await bot.edit_message(mes, new_content=iroles)
        return

@bot.command(pass_context=True)
async def iam(ctx):
    command = ctx.message.content
    argument = ''
    try:
        argument = command.split(' ', 1)[1]
    except:
        await bot.send_message(ctx.message.channel, ihelp)
        return
    
    #!iam <role>
    mes = await bot.send_message(ctx.message.channel, 'Adding role...')
    for i in range(len(iamListAlias)):
        if(argument == iamListAlias[i]):
            roleName = iamListNames[i]
            role = discord.utils.get(ctx.message.server.roles, name=roleName)
            
            found = False
            for r in ctx.message.author.roles:
                if(r.name == roleName):
                    found = True
            if(not found):
                await bot.add_roles(ctx.message.author, role)
                await bot.edit_message(mes, new_content='You are now a ' + iamListNames[i])
                return
            else:
                await bot.edit_message(mes, new_content='You already are a ' + iamListNames[i])
                return
    await bot.edit_message(mes, new_content='Role not found, `!i roles` for list of possible roles')
    
@bot.command(pass_context=True)
async def iamnot(ctx):
    command = ctx.message.content
    argument = ''
    try:
        argument = command.split(' ', 1)[1]
    except:
        await bot.send_message(ctx.message.channel, ihelp)
        return
    
    #!iamnot <role>
    mes = await bot.send_message(ctx.message.channel, 'Removing role...')
    for i in range(len(iamListAlias)):
        if(argument == iamListAlias[i]):
            roleName = iamListNames[i]
            role = discord.utils.get(ctx.message.server.roles, name=roleName)
            
            found = False
            for r in ctx.message.author.roles:
                if(r.name == roleName):
                    found = True
            if(found):
                await bot.remove_roles(ctx.message.author, role)
                await bot.edit_message(mes, new_content='You are no more a ' + iamListNames[i])
                return
            else:
                await bot.edit_message(mes, new_content='You are not a ' + iamListNames[i])
                return
    await bot.edit_message(mes, new_content='Role not found, `!i list` to list your roles that you can remove')

# Run the bot
bot.run(bot.run(os.environ.get('BOT_TOKEN', True)))
### ИМПОРТИРОВАНИЕ ОСНОВНЫХ МОДУЛЕЙ ###

from logging import exception
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

### ИМПОРТИРОВАНИЕ API ###

from api.check import block 
from api.server import base, main

### ИМПОРТИРОВАНИЕ ДОПОЛНИТЕЛЬНЫХ МОДУЛЕЙ ###

import datetime
import os
from discord.utils import get

client = commands.Bot(command_prefix='.')

### ПОДГРУЗКА ПАПКИ events ###

for filename in os.listdir('./events/'):
    if filename.endswith('.py'):
        client.load_extension(f'events.{filename[:-3]}')  

### ИВЕНТСКАЯ ЧАСТЬ ###

@client.group(invoke_without_command=True)
@commands.has_permissions(administrator = True)
async def event(ctx):
    await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "EVENT_NEED")))

@event.command()
@commands.has_permissions(administrator = True)
async def options(ctx):
    if base.eventopt(ctx.guild) is None:
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "EVENT_EMPTY_NEED")))
    else:
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "EVENT_CHECK").format(base.eventopt(ctx.guild)[1], base.eventopt(ctx.guild)[2], base.eventopt(ctx.guild)[3])))

@event.command()
@commands.has_permissions(administrator = True)
async def name(ctx, *, name):
    if base.eventopt(ctx.guild) is None:
        base.send(f"INSERT INTO eventopt VALUES ('{ctx.guild.id}', '{name}', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL)")
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "EVENT_EMPTY")))
        role = discord.utils.get(ctx.guild.roles, name="Event")
        if role is None:
            await ctx.guild.create_role(name="Event")
    else:
        base.send(f"UPDATE eventopt SET name = '{name}' WHERE id = {ctx.guild.id}")
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "EVENT_NAME").format(name)))

@event.command()
@commands.has_permissions(administrator = True)
async def desc(ctx, *, desc):
    if base.eventopt(ctx.guild) is None:
        base.send(f"INSERT INTO eventopt VALUES ('{ctx.guild.id}', NULL, '{desc}', NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL)")
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "EVENT_EMPTY")))
        role = discord.utils.get(ctx.guild.roles, name="Event")
        if role is None:
            await ctx.guild.create_role(name="Event")
    else:
        base.send(f"UPDATE eventopt SET desc = '{desc}' WHERE id = {ctx.guild.id}")
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "EVENT_DESC").format(desc)))

@event.command()
@commands.has_permissions(administrator = True)
async def rules(ctx, *, rules):
    if base.eventopt(ctx.guild) is None:
        base.send(f"INSERT INTO eventopt VALUES ('{ctx.guild.id}', NULL, NULL, '{rules}', 0, 0, NULL, NULL, NULL, NULL, NULL, NULL)")
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "EVENT_EMPTY")))
        role = discord.utils.get(ctx.guild.roles, name="Event")
        if role is None:
            await ctx.guild.create_role(name="Event")        
    else:
        base.send(f"UPDATE eventopt SET rules = '{rules}' WHERE id = {ctx.guild.id}")
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "EVENT_RULES").format(rules)))

@event.command(aliases=['вопрос1', '1', 'первый', 'первое'])
@commands.has_permissions(administrator = True)
async def question(ctx, *, q):
    if base.eventopt(ctx.guild) is None:
        base.send(f"INSERT INTO eventopt VALUES ('{ctx.guild.id}', NULL, NULL, NULL, 0, 0, '{q}', NULL, NULL, NULL, NULL, NULL)")
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "EVENT_EMPTY")))
        role = discord.utils.get(ctx.guild.roles, name="Event")
        if role is None:
            await ctx.guild.create_role(name="Event")        
    else:
        base.send(f"UPDATE eventopt SET q = '{q}' WHERE id = {ctx.guild.id}")
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "EVENT_Q1").format(q)))

@event.command(aliases=['вопрос2', '2', 'второй', 'второе'])
@commands.has_permissions(administrator = True)
async def questiontwo(ctx, *, q2):
    if base.eventopt(ctx.guild) is None:
        base.send(f"INSERT INTO eventopt VALUES ('{ctx.guild.id}', NULL, NULL, NULL, 0, 0, NULL, '{q2}', NULL, NULL, NULL, NULL)")
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "EVENT_EMPTY")))
        role = discord.utils.get(ctx.guild.roles, name="Event")
        if role is None:
            await ctx.guild.create_role(name="Event")        
    else:
        base.send(f"UPDATE eventopt SET q2 = '{q2}' WHERE id = {ctx.guild.id}")
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "EVENT_Q2").format(q2)))

@event.command(aliases=['вопрос3', '3', 'третий', 'третье'])
@commands.has_permissions(administrator = True)
async def questionthree(ctx, *, q3):
    if base.eventopt(ctx.guild) is None:
        base.send(f"INSERT INTO eventopt VALUES ('{ctx.guild.id}', NULL, NULL, NULL, 0, 0, NULL, NULL, '{q3}', NULL, NULL, NULL)")
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "EVENT_EMPTY")))
        role = discord.utils.get(ctx.guild.roles, name="Event")
        if role is None:
            await ctx.guild.create_role(name="Event")        
    else:
        base.send(f"UPDATE eventopt SET q3 = '{q3}' WHERE id = {ctx.guild.id}")
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "EVENT_Q3").format(q3)))        

@event.command(aliases=['вопрос4', '4', 'четвертый', 'четвертое'])
@commands.has_permissions(administrator = True)
async def questionfour(ctx, *, q4):
    if base.eventopt(ctx.guild) is None:
        base.send(f"INSERT INTO eventopt VALUES ('{ctx.guild.id}', NULL, NULL, NULL, 0, 0, NULL, NULL, NULL, '{q4}', NULL, NULL)")
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "EVENT_EMPTY")))
        role = discord.utils.get(ctx.guild.roles, name="Event")
        if role is None:
            await ctx.guild.create_role(name="Event")        
    else:
        base.send(f"UPDATE eventopt SET q4 = '{q4}' WHERE id = {ctx.guild.id}")
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "EVENT_Q4").format(q4)))

@event.command(aliases=['вопрос5', '5', 'пятый', 'пятое'])
@commands.has_permissions(administrator = True)
async def five(ctx, *, q5):
    if base.eventopt(ctx.guild) is None:
        base.send(f"INSERT INTO eventopt VALUES ('{ctx.guild.id}', NULL, NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, '{q5}', NULL)")
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "EVENT_EMPTY")))
        role = discord.utils.get(ctx.guild.roles, name="Event")
        if role is None:
            await ctx.guild.create_role(name="Event")        
    else:
        base.send(f"UPDATE eventopt SET q5 = '{q5}' WHERE id = {ctx.guild.id}")
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "EVENT_Q5").format(q5)))

@event.command(aliases=['вопрос6', '6', 'шестой', 'шестое'])
@commands.has_permissions(administrator = True)
async def six(ctx, *, q6):
    if base.eventopt(ctx.guild) is None:
        base.send(f"INSERT INTO eventopt VALUES ('{ctx.guild.id}', NULL, NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, '{q6}')")
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "EVENT_EMPTY")))
        role = discord.utils.get(ctx.guild.roles, name="Event")
        if role is None:
            await ctx.guild.create_role(name="Event")        
    else:
        base.send(f"UPDATE eventopt SET msg = '{q6}' WHERE id = {ctx.guild.id}")
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "EVENT_Q6").format(q6)))        

@event.command(name='post')
@commands.cooldown(1, 22221600, commands.BucketType.user)
async def posthelp(ctx):
    message = await ctx.send(embed=main.rule(ctx.guild, main.get_lang(ctx.guild, "HELP_BASE").format(base.eventopt(ctx.guild)[10])))
    #message = await ctx.send(f'{main.get_lang(ctx.guild, "HELP_BASE").format(base.eventopt(ctx.guild)[10])}')

    emoji = '<:bitty_rules:935193629792804935>'

    await message.add_reaction(emoji)

    def check(reaction, user):
        return not user == user.bot and user == user and str(reaction) == emoji

    while True:
            reaction, user = await client.wait_for("reaction_add", check=check)
            try:
                if str(reaction.emoji) == emoji:
                    await user.send(embed=main.rule(ctx.guild, main.get_lang(ctx.guild, "HELP_BASE").format(base.eventopt(ctx.guild)[11])))
            except:
                ch = client.get_channel(934866808547184680)
                await ch.send(embed=main.warn(ctx.guild, main.get_lang(ctx.guild, "HELP_DM").format(user.mention)))    
@posthelp.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(embed = main.deny(ctx.guild, f"У вас задежка на данную команду. Попробуйте через `{error.retry_after:.0f}` секунд"))                
               
@event.command()
@commands.has_permissions(administrator = True)
async def reset(ctx):
    base.send(f"DELETE FROM eventopt WHERE id = {ctx.guild.id}")
    base.send(f"DELETE FROM event WHERE guild = {ctx.guild.id}")
    role = discord.utils.get(ctx.message.guild.roles, name="Event")
    await role.delete()
    await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "EVENT_RESET")))

### КЛИЕНТСКАЯ ЧАСТЬ ###

@client.command(aliases=['отказаться', 'refus'])
@commands.has_role("Event")
async def refuse(ctx):
    if base.event(ctx.author) is not None:
        base.send(f"UPDATE users SET uncount = uncount + 1 WHERE id = {ctx.author.id}")
        base.send(f"UPDATE eventopt SET active = active - 1 WHERE id = {ctx.guild.id}")
        base.send(f"UPDATE eventopt SET unactive = unactive + 1 WHERE id = {ctx.guild.id}")
        base.send(f"DELETE FROM event WHERE id = {ctx.author.id}")
        role = discord.utils.get(ctx.guild.roles, name="Event")
        await ctx.author.remove_roles(role)
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "REFUSE_DONE")))

@client.group(invoke_without_command=True)
async def apl(ctx):
    await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "APL_NEED").format(ctx.prefix, base.eventopt(ctx.guild)[6], base.eventopt(ctx.guild)[7], base.eventopt(ctx.guild)[8], base.eventopt(ctx.guild)[9]))) 

@apl.command(aliases=['1', 'один', 'адин', '11', 'onee', 'solo', 'soloo', 'соло', 'солоо', 'question-one', 'вопрос-один'])
async def one(ctx, *, one): 
    if base.apl(ctx.author) is None or base.user(ctx.author) is None:
        base.send(f"INSERT INTO apl VALUES ('{ctx.author.name}', '{ctx.author.id}', '{one}', NULL, NULL, NULL)")
        base.send(f"INSERT INTO users VALUES ('{ctx.author.id}', '{ctx.author.name}', 0, 0, 0)")
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "APL_EMPTY")))
    else:
        base.send(f"UPDATE apl SET question = '{one}' WHERE id = {ctx.author.id}")
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "APL_ONE").format(one)))

@apl.command(aliases=['2', 'два', 'двое', '22', 'twoo', 'question-two', 'duo', 'duoo', 'дуо', 'дуоо', 'вопрос-два'])
async def two(ctx, *, two):    
    if base.apl(ctx.author) is None or base.user(ctx.author) is None:
        base.send(f"INSERT INTO apl VALUES ('{ctx.author.name}', '{ctx.author.id}', NULL, '{two}', NULL, NULL)")
        base.send(f"INSERT INTO users VALUES ('{ctx.author.id}', '{ctx.author.name}', 0, 0, 0)")
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "APL_EMPTY")))
    else:
        base.send(f"UPDATE apl SET question2 = '{two}' WHERE id = {ctx.author.id}")
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "APL_TWO").format(two)))

@apl.command(aliases=['3', 'три', 'трое', '33', 'threee', 'thre', 'trio', 'трио', 'question-three', 'вопрос-три'])
async def three(ctx, *, three):     
    if base.apl(ctx.author) is None or base.user(ctx.author) is None:
        base.send(f"INSERT INTO apl VALUES ('{ctx.author.name}', '{ctx.author.id}', NULL, NULL, '{three}', NULL)")
        base.send(f"INSERT INTO users VALUES ('{ctx.author.id}', '{ctx.author.name}', 0, 0, 0)")
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "APL_EMPTY")))
    else:
        base.send(f"UPDATE apl SET question3 = '{three}' WHERE id = {ctx.author.id}")
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "APL_THREE").format(three)))

@apl.command(aliases=['4', 'четыре', 'четверо', '44', 'fourr', 'fou', 'squad', 'сквад', 'скуад', 'question-four', 'вопрос-четыре', 'четыри', 'вопрос-четыри'])
async def four(ctx, *, four):   
    if base.apl(ctx.author) is None or base.user(ctx.author) is None:
        base.send(f"INSERT INTO apl VALUES ('{ctx.author.name}', '{ctx.author.id}', NULL, NULL, NULL, '{four}')")
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "APL_EMPTY")))
    else:
        base.send(f"UPDATE apl SET question4 = '{four}' WHERE id = {ctx.author.id}")
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "APL_FOUR").format(four)))

@apl.command(aliases=['настройки', 'opt', 'настройка', 'профиль', 'profile', 'prof', 'проф', 'user', 'юзер', 'пользователь'])
async def options(ctx):     
    if base.apl(ctx.author) is None:
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "APL_EMPTY_NEED")))
    else:
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "APL_CHECK").format(base.apl(ctx.author)[2], base.apl(ctx.author)[3], base.apl(ctx.author)[4], base.apl(ctx.author)[5])))

@apl.command(aliases=['отправить', 'submit', 'заявка', 'отправить-заявку', 'отправить-профиль'])
@commands.cooldown(1, 21600, commands.BucketType.user)
async def zayavka(ctx):      
    if base.apl(ctx.author) is None:
        await ctx.reply(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "APL_EMPTY_NEED")))
    else:
        channel = client.get_channel(934866808547184680) 
        embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "APL_MEMBER").format(ctx.author.mention, base.apl(ctx.author)[2], base.apl(ctx.author)[3], base.apl(ctx.author)[4], base.apl(ctx.author)[5], base.user(ctx.author)[2], base.user(ctx.author)[3], base.user(ctx.author)[4]))
        embed.set_footer(text=f'{main.get_lang(ctx.guild, "APL_MEMBER_FOOTER").format(ctx.prefix)}')
        await channel.send(embed=embed)
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "APL_SUBMIT")))      

@zayavka.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(embed = main.deny(ctx.guild, f"У вас задежка на данную команду. Попробуйте через `{error.retry_after:.0f}` секунд"))

### ЗАЯВКОВАЯ ЧАСТЬ ###

@client.command(aliases=['accept', 'acc', 'ac', 'принять', 'прин', 'принят'])
@commands.has_permissions(administrator = True)
async def a(ctx, member: discord.Member):
    if base.eventopt(ctx.guild) is not None and base.event(member) is None:
        base.send(f"UPDATE users SET count = count + 1 WHERE id = {member.id}")
        base.send(f"INSERT INTO event VALUES ('{member.name}', '{member.id}', '{ctx.guild.id}')")
        base.send(f"UPDATE eventopt SET active = active + 1 WHERE id = {ctx.guild.id}")
        role = discord.utils.get(ctx.guild.roles, name="Event")
        await member.add_roles(role)
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "ACCEPT_DONE").format(member.mention)))
        await member.send(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "ACCEPT_MEMBER").format(ctx.author.mention, base.eventopt(ctx.guild)[1], base.eventopt(ctx.guild)[2], base.eventopt(ctx.guild)[3])))
    else:
        await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "ACCEPT_ERROR")))

@client.command(aliases=['deny', 'отказать', 'отклонить', 'denyy', 'отклон', 'отклонять'])
@commands.has_permissions(administrator = True)
async def d(ctx, member: discord.Member):
    if base.eventopt(ctx.guild) is not None and base.event(member) is None:
        base.send(f"UPDATE users SET deny = deny + 1 WHERE id = {member.id}")
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "DENY_DONE").format(member.mention)))
    else:
        await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "ACCEPT_ERROR")))

### У МАЛЬЧИКА СТРЕСС У МАЛЬЧИКА СТРЕСС С О С О СО СО У МАЛЬЧИКА СТРЕСС ###

@client.command(aliases = ['бот-бан', 'бот-блок', 'бот-забанить', 'ббан', 'block', 'блок'])
@commands.has_permissions(administrator = True)
async def bban(ctx, member: discord.Member, *, reason = None):
    if base.blacklist(member) is not None: 
        await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "BBAN_ERROR").format(member.mention)))                
    else: 
        myopt = datetime.datetime.now()
        myoption = myopt.strftime(r"%x")
        base.send(f"INSERT INTO blacklist VALUES ('{member.name}', '{member.id}', '{reason}', '{ctx.author.name}', '{ctx.author.id}', '{myoption}')")  
        await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "BBAN_SUCESS").format(member.mention)))

client.run("OTM3MzIzMjI3MzI2MzI0ODA2.YfaESA.GHQvIA5pNPjCCaNqWcmrc3aVA74")
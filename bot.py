import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

# the ID of the role that can make channels
approved_role_id = '436979620882153472'

bot.remove_command("help")

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print("Good day sir, thank you for starting me.")


@bot.command(pass_context=True)
async def make(ctx):
    author = ctx.message.author
    server = ctx.message.server
    approved_role = discord.utils.get(server.roles, id=approved_role_id)
    if approved_role is None:
        return
    if approved_role not in author.roles:
        return
    else:
        chtype = None
        chname = None
        await bot.send_message(author, 'Are you making a text or voice channel?')
        while chtype is None:
            response = await bot.wait_for_message(author=author, timeout=10)
            if response is None:
                await bot.send_message(author, 'Channel making session has timed out.')
                return
            if response.content.lower() == 'text':
                chtype = discord.ChannelType.text
            if response.content.lower() == 'voice':
                chtype = discord.ChannelType.voice
            elif chtype is None:
                await bot.send_message(author, 'Invalid choice, please choose **text** or **voice**')
        await bot.send_message(author, 'What is the name of the channel?')
        chname = await bot.wait_for_message(author=author, timeout=10)
        if chname is None:
            await bot.send_message(author, 'Channel making session has timed out.')
            return
        await bot.create_channel(server, chname.content, type=chtype)
        await bot.send_message(author, '**{}** channel **{}** has been created'.format(chtype, chname.content))


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print("user has pinged")


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined the community at: {}".format(user.joined_at))


@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(
        ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="UnmetPlayer")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(
        ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)



bot.run('NDM3MzM1NjUzOTkxMTg2NDMy.DcEY_g.Vo6A5lpd79K148ubGqV9LZrKPAw')

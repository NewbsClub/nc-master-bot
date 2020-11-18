import discord
import asyncio as pytime
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from itertools import cycle

client = commands.Bot(command_prefix='>')

statuses = cycle([
    'Vaelya! 💕',
    'My Prefix: > 😊',
    'Have a goood day! 💖',
    "My Author is DylanDeNewb#0731! 😂"])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(next(statuses)))

@client.event
async def on_ready():
    print("NewbsBot starting up...")
    change_status.start()

@client.event
async def on_command_error(ctx, error):
    return;

# @client.command()
# async def help(ctx):
#     embed = discord.Embed(
#         title = "**Help**",
#         description = "*Available commands!",
#         colour = discord.Colour.from_rgb
#     )

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permssions: MANAGE_MESSAGES")

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):

    embed = discord.Embed(
        title = "**Kick**",
        description = "*Member kick report*",
        colour = discord.Colour.from_rgb(247, 201, 255)
    )

    embed.set_footer(text="Powered by NewbsDev")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/761285015928963132/767213242464337930/newbs.png")
    embed.set_author(name="NewbsBot")

    embed.add_field(name="Member", value=f'{member}', inline=True)
    embed.add_field(name="Reason", value=f'{reason}', inline=False)

    await ctx.send(embed=embed)
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):

    embed = discord.Embed(
        title = "**Ban**",
        description = "*Member ban report*",
        colour = discord.Colour.from_rgb(247, 201, 255)
    )

    embed.set_footer(text="Powered by NewbsDev")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/761285015928963132/767213242464337930/newbs.png")
    embed.set_author(name="NewbsBot")

    embed.add_field(name="Member", value=f'{member}', inline=True)
    embed.add_field(name="Reason", value=f'{reason}', inline=False)

    await ctx.send(embed=embed)
    await member.ban(reason=reason)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permssions: BAN_MEMBERS")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please include all required arguments! >ban <member> <reason>")

@client.command()
async def remind(ctx, role : discord.Role, channel : discord.TextChannel, time : int, *, reminder : str):
    await pytime.sleep(time)

    embed = discord.Embed(
        title = "**Reminder**",
        description = "*New reminder!*",
        colour = discord.Colour.from_rgb(247, 201, 255)
    )

    embed.set_footer(text="Powered by NewbsDev")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/761285015928963132/767213242464337930/newbs.png")
    embed.set_author(name="NewbsBot")

    embed.add_field(name="Role", value=f'{role.mention}')
    embed.add_field(name="Reminder", value=f'{reminder}')

    await ctx.message.delete()
    await channel.send(embed=embed)

@remind.error
async def remind_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please include all required arguments! >remind <role> <channel> <time> <reminder>")

@client.command()
async def accept(ctx, member : discord.Member):

    embed = discord.Embed(
        title="**Accepted!**",
        description="*You've been accepted to FantasyRP*",
        colour= discord.Colour.from_rgb(247,201,255)
    )

    embed.set_footer(text="Nation Documentation - https://bit.ly/31Iemvy\nPowered by NewbsDev 💕")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/761285015928963132/767213242464337930/newbs.png")
    embed.set_author(name="NewbsBot")

    embed.add_field(name="Kingdom of Rheynland", value="(Khan#1650) https://discord.gg/ZDceK2a\n*The Kingdom of Rheynland lies, appropriately, in the prosperous and hilly west of Enarion. Resting against the ocean shores and commanding entrance to the Bay of Syra, the human settlement dominates its surroundings; squat stone walls and burnished brick roofs reflect the orange of the setting sun behind its walls.*", inline=False)
    embed.add_field(name="Kingdom of Aellen", value="(🎃 Calloween 🎃#9575) https://discord.gg/QgQRqtT\n*The Elven Kingdom of Aellen (formally called Tor Ascara) hails in the East of Enarion— filled with Elves originating from various backgrounds & cultures. The culture-based entity is headed by a King advised by multiple sect-leaders.*", inline=False)
    embed.add_field(name="Kingdom of Nordavik", value="(TuskenArcher#3697) https://discord.gg/dvuryRa\n*After the fall of Ordheim, the Dwarves were left with no place to go. Many fled and immigrated to different lands, but some had different plans.*", inline=False)
    embed.add_field(name="Kingdom of Brenna", value="(Angiru#6950) https://discord.gg/EG7UBP5\n*A nation of hardy, stalwart stout northmen based in Enarion's farthest highlands. Comprised of both Dwarves and Men living side by side as equals, the Brennish highlands are inhabited only by the most adventurous and hardy of souls, given that it's not an easy place to live.*", inline=False)
    embed.add_field(name="Republic of Valora", value="(Cele-Scream 🎃👻#2436) https://discord.gg/qhvjEYw\n*This land is rife with conflict. The powerful abuse their position to wage selfish wars that fuel coffer and ego at the expense of the common man.*", inline=False)
    embed.add_field(name="Order of Saint Alba", value="(BunnyHop#2243) https://discord.gg/nS2edC\n*Saint Alba is the saint of the sun and slayer of evil, long ago she helped slay the evil Marukh who is a demonic spirit who raised the undead. Alba chased Marukh out of the continent and he was slain by our Saint and sealed.*", inline=False)

    await member.send(embed=embed)


@client.listen('on_message')
async def poll(message):

    emojis=['👍', '👎', '🤷‍♂️']

    if message.content.startswith('Poll:'):
        for emoji in emojis:
            await message.add_reaction(emoji)


client.run("NzE2MzY0NTQzNzE0MDAwOTI2.XtKseA.mAD3GPD9yZWicyHQqXjCEcuV-7I")

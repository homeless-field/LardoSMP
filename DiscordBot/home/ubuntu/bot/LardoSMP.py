import boto3
import discord
from discord.ext import commands
 
ec2 = boto3.client('ec2',
                   'us-west-2',
                   aws_access_key_id='AWS KEY',
                   aws_secret_access_key='AWS TOKEN')

ssm_client = boto3.client('ssm',
			  region_name='us-west-2',
			  aws_access_key_id='AWS KEY',
                   	  aws_secret_access_key='AWS TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents)

@bot.command()
async def roles(ctx):
	await ctx.send("""Hark, stranger! Claim yon clan[s] (colloquially known as a "role") in this message!\n\n<:lardo:707341985186316298> ``@Regulars``: This group of yung maidens LOVES being pinged in the rear guard. Choose this role if you wish'ith to frequent these parts\n<:sand_tsunami:779440160232308737> ``@LardoSMP``: Listen here lad, that business with Dream is IN THE PAST\n<:dung_eater:962574208989265991> ``@Leagulars``: All worthy kingdoms have a latrine pit. This is ours. Prithee be careful\n<:triple_chocolate_crepe:877749423566897193> ``@DnD``: Nerrrd\n<:adodo:973061689102721104> ``@Warframe``: Feeling laborious? Why not take a stroll by our Orokin-inspired "open" "pasture" farms?\n<:tim_reaction:973064203571171378> ``@Fighting Games``: Yo yo yo, let's jus _**FUCKIN**_ kill each other""")

@bot.command()
async def startserver(ctx):
	ec2Response = ec2.start_instances(InstanceIds=['INSTANCE ID',],)
	await ctx.send("Host's a-kickin'! If that Minecraft server don't mosey on up in 5 minutes, you better wrangle up ``@ADMIN USERNAME``. \n\nWe're ridin' on the IP ``SERVER IP``! Yeehaw! 🤠🌵🔫")

bot.run('BOT TOKEN')

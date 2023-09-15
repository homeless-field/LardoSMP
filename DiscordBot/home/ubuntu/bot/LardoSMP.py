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
async def startserver(ctx):
	ec2Response = ec2.start_instances(InstanceIds=['INSTANCE ID',],)
	await ctx.send("Host's a-kickin'! If that Minecraft server don't mosey on up in 5 minutes, you better wrangle up ``@ADMIN USERNAME``. \n\nWe're ridin' on the IP ``SERVER IP``! Yeehaw! 🤠🌵🔫")

bot.run('BOT TOKEN')

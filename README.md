# LardoSMP
A collection of helper scripts and other files for running our Minecraft server. This was created with the assistance of [this tutorial](https://farnsworth.engineering/index.php/2020/01/19/amazon-aws-minecraft-server-with-remote-start-of-course/)

Each folder in the repo represents a separate AWS EC2 server. The Discord bot is running on an x86 t2.micro free tier instance, and the host server is an Arm t4g.medium instance. The host server contains an additional user, called "minecraft", for added security. Both run Ubuntu 22.04 and DuckDNS is used for the server IP

In short, users can send -startserver to a Discord bot, and the bot will send a call to EC2 and start an instance which will run Minecraft on startup. That server also shuts down with 30 minutes of inactivity

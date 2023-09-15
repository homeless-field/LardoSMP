```
# This file contains the added cronjobs, accessible by using:
# $crontab -e

# Starts discord bot on each startup
# This ensures that the instance just needs to be started for the bot to be active
@reboot python3 /home/ubuntu/bot/LardoSMP.py
```
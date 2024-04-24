```
# This file contains the added cronjobs ran by root, accessible as the root user by using:
# $crontab -u root -e
# To view output, use:
# $grep 'check4users' /var/log/syslog

# Shuts down server every 30 minutes if no one's connected
# This cuts down AWS costs by limiting usage hours
*/30 * * * * sudo sh /home/minecraft/Minecraft/scripts/check4users.sh 2>&1 | logger -t check4users
```

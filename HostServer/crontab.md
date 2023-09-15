```
# This file contains the added cronjobs, accessible by using:
# $crontab -e

# Updates DuckDNS reference IP on each startup
# This ensures the same IP can be used each time, regardless of whether the server's changes
@reboot ~/duckdns/duck.sh >/dev/null 2>&1
```
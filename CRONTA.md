Schedule the script on a linux server with

crontab -e /usr/bin/python3 /opt/splunk/splunk-pull-only/dev/mpspl-git-pull/mpspl-git-pull.py -e gen-shcluster

List the current cron

crontab -l

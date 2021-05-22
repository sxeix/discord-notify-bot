# discord-notify-bot
This bot enables you to store short keywords/phrases you wish to be notified about. The bot will tag you in any messages on a server that contain a stored word of yours. 

This requires discord.py so run the command to install it + if you don't already have it, mysql.connector will also be needed
```
py -3 -m pip install -U discord.py
py -3 -m pip install -U  mysql-connector
```

Run using 
```
py NotifyBot.py
```

Note: this requires a mysql database to communicate with. This involves creating a csv type file with the name `dbCreds` and using the schema. Additionally in the resources directory you will need a `token` file with the discord api token.

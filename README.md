## nba-start-active-players-bot

**What**

Python Selenium script that logs into your Yahoo fantasy basketball account and starts active players for today and upcoming days. Accepts arguments username, password and the number of days you would like the bot to process into the future.

For example to start active players for the next week including today you would use run the following from the command line.

`python start-active-players.py 7 username password`


**Why**

1. Never leave a player on the bench because you forgot to set your lineup
2. Why not

**Dependencies**

* Python 2.7
* Selenium WebDriver
* ChromeDriver

**How**

1. Download the script locally
2. Run the script and pass the number of days you want to automate, your Yahoo usename, and account password as command line arguments.

**To-Do**

1. Try / Except for missing command line argv.
2. Change sleeps to implicit waits
3. Try / Excepts for key UI elements to ensure Selenium can find them before we click them.

**Contribute**

If you think this is a cool idea, but kind of inefficient, please submit a PR and let's make this better.

© 2015, Devin Mancuso · MIT License you know the deal

## nba-start-active-players-bot

**What**

Python Selenium script that logs into your Yahoo fantasy basketball account and starts active players for today and upcoming days. Accepts arguments username, password and the number of days you would like the bot to process into the future.

**Why**

1. Never leave a player on the bench because you forgot to set your lineup
2. Why not

**Dependencies**

* Python 2.7
* [Click](http://click.pocoo.org/)
* Selenium WebDriver
* ChromeDriver

**How**

1. Download script
2. Install dependencies
3. Run

To run the program

`python start-active-players.py`

You will be prompted to enter the number of days you want the script to process and your Yahoo credentials. 

You can include these details as options to avoid having to fill them in each time. For example to start active players for the next week including today.

`python start-active-players.py --days=7 --username=YahooUsername@yahoo.com.au --password=Y0urYah00Passw0rd`

use `--help` for help documentation.

**To-Do**

- [x] Try / Except for missing command line argv.
- [ ] Change sleeps to implicit waits
- [ ] Try / Excepts for key UI elements to ensure Selenium can find them before we click them.
- [x] Include confirmations for each date as they are processed

**Contribute**

If you think this is a cool idea, but kind of inefficient, please submit a PR and let's make this better.

© 2015, Devin Mancuso · MIT License you know the deal

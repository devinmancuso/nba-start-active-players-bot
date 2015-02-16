## nba-start-active-players-bot

**What**

Python Selenium script that logs into your Yahoo fantasy basketball account and starts active players for today and upcoming days. Accepts arguments username, password, the number of days you would like the bot to process into the future and whether you want to see what the browser is running (useful for debugging) or run in headless mode.

**Why**

1. Never leave a player on the bench because you forgot to set your lineup
2. Why not

**Dependencies**

* Python 2.7
* [Click](http://click.pocoo.org/)
* Selenium WebDriver
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* PhantomJS

**How**

1. Download script
2. Install dependencies

```bash
pip install selenium click 
brew install node
curl https://www.npmjs.org/install.sh | sh
npm install phantomjs
```

You'll have to grab ChromeDriver manually.

3. Run the program

To run the program

`python start-active-players.py`

You will be prompted to enter the number of days you want the script to process, your Yahoo credentials and whether you want the script to run in headless mode (you can't watch what it's doing in the browser). 

You can include these details as options to avoid having to fill them in each time. For example to start active players for the next week including today.

`python start-active-players.py --days=7 --username=YahooUsername@yahoo.com.au --password=Y0urYah00Passw0rd --headless=False`

use `--help` for help documentation.

**To-Do**

- [x] Try / Except for missing command line argv.
- [x] Add headless support for PhantomJS
- [ ] Try / Excepts for key UI elements to ensure Selenium can find them before we click them.
- [ ] Put more asserts in places to tighten it all up
- [x] Include confirmations for each date as they are processed

**Contribute**

If you think this is a cool idea, but kind of inefficient, please submit a PR and let's make this better.

© 2015, Devin Mancuso · MIT License you know the deal

# py_api_link_observer

## About <a name = "about"></a>

Python FastAPI app that stores links-xpath-stringValue entry in the SQLAlchemy database and checks periodically using Selenium if this value changes. Useful if you need to snipe something from online-shops or in case you dont trust auto-emailing systems.

This project is not very scalable (for now), so it's for personal use only.

Python version used - 3.11.

## Installing <a name = "getting_started"></a>

### Before everything else

Install Firefox.
If you don't have telegram-bot account: https://t.me/botfather
Install selenium. Guide to How-To: https://www.geeksforgeeks.org/how-to-install-selenium-in-python/

### Setting up environment

```
git clone https://github.com/MsUn-123/py_api_link_observer
cd py_api_link_observer
python -m venv venv
source venv/bin/activate #on lunix
pip install requirements.txt
```

### Setting up Telegram bot

Create settings.py file with these variables:

```
key = "<Your bots API token>"
owner = <Your own Telegram ID>
apiport = <Port you started API on. Default: 8000>
period = <Time in minutes after which the bot will start checking links from database. Default: 5>
```

### Booting everything up

1 - FastAPI

```
uvicorn app.api:app --reload
# Database entries.db will be created on the first startup.
```

2 - Telegram bot

```
python3 telegram/bot.py
```

## Usage <a name = "usage"></a>

You can use api (and should) with Telegram bot.
List of available commands:

```
/add - Add entry to the database. Input: /add <link> <xpath>
/check - Get value from webpage using xpath. Input: /check <link> <xpath>
/list - List all entries from database.
/remove - Removes entry from database. Input: /remove <id>
```

Every set period of time (you chose) bot will notify you about changes on following websites (if any).

## TO-DO

###

- [ ] - Add command to edit check period in the telegram bot.
- [x] - Make scraper headless.
- [x] - Add aliases for links.
- [x] - Use markdown to shorten URLs in /list command.
- [ ] - Add entry datetime created field.
- [ ] - Replace time.sleep in scraper.
- [x] - Change variables in settings.py to upper-case. Because they are CONSTANTS.
- [x] - Rename period CONSTANT in settings.py.
- [ ] - Rework input validation.
- [ ] - Add more ways to find data on webpage besides xpath.
- [ ] - Add support for other browsers (Chrome, Opera, etc.)
- [ ] - Add support for requests-lib scraper to reduce scrape time.
    - [ ] - Add parser type to entity in DB.
    - [ ] - Add headers column for requests parser.
- [ ] - Make scraper+telegram-bot async.

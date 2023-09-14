# py_api_link_observer

## About <a name = "about"></a>

Python FastAPI app that stores links-xpath-stringValue entry in the SQLAlchemy database and checks periodically using Selenium if this value changes. Useful if you need to snipe something from online-shops or in case you dont trust auto-emailing systems.

This project is not very scalable (for now), so it's for personal use only.

Python version used - 3.11.

## Installing <a name = "getting_started"></a>

### Before everything else

Install selenium. Guide to How-To: https://www.geeksforgeeks.org/how-to-install-selenium-in-python/

### Setting up environment

```
git clone https://github.com/MsUn-123/py_api_link_observer
cd py_api_link_observer
python -m venv <env_name>
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

## TO-DO <a name = "todo"></a>

- [ ] - Add command to edit check period in the telegram bot.
- [ ] - Make scraper headless.
- [ ] - Short url in /list if url length > 40. Make it optional (/listfull?)
- [ ] - Replace time.sleep in scraper to smthn else.
- [ ] - Rework input validation.
- [ ] - Add support for requests-lib scraper to reduce scrape time.
    - [ ] - Add parser type to entity in DB.
    - [ ] - Add headers column for requests parser.
- [ ] - Make scraper async.

- [ ] - Change variables in settings.py to upper-case. Because they are CONSTANTS.
- [ ] - Rename period CONSTANT in settings.py.

- [ ] - Learn git workflow.

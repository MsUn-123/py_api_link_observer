# py_api_link_observer

## Table of Contents

- [About](#about)
- [Installing](#installing)
- [Usage](#usage)

## About <a name = "about"></a>

Python FastAPI app that stores links-xpath-stringValue entry in the SQLAlchemy database and checks periodically using Selenium if this value changes.

This project is not very scalable (for now), so it's for personal use only.

Python version used - 3.11.

## Installing <a name = "getting_started"></a>

### Before everything else

Install selenium. Guide to How-To: https://www.geeksforgeeks.org/how-to-install-selenium-in-python/

### Setting up environment

```
git clone https://github.com/MsUn-123/py_api_link_observer > py_api_link_observer
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
```

2 - Telegram bot

```
python3 telegram/bot.py
```

## Usage <a name = "usage"></a>

You can use api (and should) with Telegram bot.
List of available commands:

```
/add - Add link to the database. Input: <link> <xpath> "<value>"
/check - Get value from webpage using xpath. Input: <link> <xpath>
/list - List all links from database.
/remove - Removes link from database. Input: <id>
```

Every set period of time (you chose) bot will notify you about changes on following websites (if any).

## TO-DO

Empty. For now!

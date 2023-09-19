import telebot
import settings, utils
from scraper import Scraper
import requests, threading, schedule
import time


bot = telebot.TeleBot(settings.KEY)
scraper = Scraper()
task_worker = Scraper()


@bot.message_handler(commands=['start'])
def send_welcome(message):
	if message.from_user.id == settings.OWNER:
		bot.send_chat_action(message.chat.id, 'typing')
		bot.reply_to(message, 'Welcome!\n' +
							'List of available commands:\n' +
							'/add - Add link to the database. Input: <link> <xpath> "<alias>"\n'+
							'/check - Get value from webpage using xpath. Input: <link> <xpath>\n'+
							'/list - List all links from database.\n'+
							'/remove - Removes link from database. Input: <id>\n')
	
@bot.message_handler(commands=['add'])
def add_entry(message):
	if message.from_user.id == settings.OWNER:
		bot.send_chat_action(message.chat.id, 'typing')
		input = utils.extract_arg(message.text)
		if utils.validate_input_add(input):
			scraper.start()
			value = scraper.get_by_xpath(input[0], input[1])
			scraper.quit()
			headers = {
				'accept': 'application/json',
				'Content-Type': 'application/json',
				}
			json_data = {
				'link': f'{input[0]}',
				'xpath': f'{input[1]}',
				'value': f'{value}',
				'alias': f'{input[2]}'
				}
			response = requests.post(f'http://localhost:{settings.APIPORT}/entries/add', headers=headers, json=json_data)
			bot.reply_to(message, response.json()['msg'])
		else: bot.reply_to(message, 'Incorrect input. Usage: /add <link> <xpath>') #

@bot.message_handler(commands=['check'])
def check_value(message):
	if message.from_user.id == settings.OWNER:
		bot.send_chat_action(message.chat.id, 'typing')
		input = utils.extract_arg(message.text)
		if utils.validate_input_test(input):
			scraper.start()
			value = scraper.get_by_xpath(input[0], input[1])
			scraper.quit()
			bot.reply_to(message, value)
		else: bot.reply_to(message, 'Incorrect input. Usage: /check <link> <xpath>')

@bot.message_handler(commands=['list'])
def list_entries(message):
	if message.from_user.id == settings.OWNER:
		bot.send_chat_action(message.chat.id, 'typing')
		response = requests.get(f'http://localhost:{settings.APIPORT}/entries/all').json()
		if len(response) > 0:
			msg = ''
			for link in response:
				msg += str(link['id']) + ' - ' + telebot.formatting.hlink(link['alias'], link['link']) + ': ' + utils.clear_escapes(link['value']) + '\n'
			bot.reply_to(message, msg, parse_mode='HTML')
		else:
			bot.reply_to(message, 'List is empty! Add links with /add command')

@bot.message_handler(commands=['remove'])
def remove_entry(message):
	if message.from_user.id == settings.OWNER:
		input = utils.extract_arg(message.text)
		if utils.validate_input_remove(input[0]):
			headers = { 'accept': 'application/json' }
			response = requests.delete(f'http://localhost:{settings.APIPORT}/entries/delete/{input[0]}', headers=headers)
			bot.reply_to(message, response.json()['msg'])
		else: bot.reply_to(message, 'Incorrect input. Usage: /remove <id>')  

@bot.message_handler(commands=['process']) #for debug purposes
def process_list(message):
	if message.from_user.id == settings.OWNER:
		bot.send_chat_action(message.chat.id, 'typing')
		response = requests.get(f'http://localhost:{settings.APIPORT}/entries/all').json()
		task_worker.start()
		if len(response) > 0:
			msg = ''
			for entry in response:
				value = task_worker.get_by_xpath(entry['link'], entry['xpath'])
				if str(value) != str(entry['value']): 
					msg += f"{entry['id']} - Old value: {entry['value']}, New value: {value}\n"
			if len(msg) > 0:
				bot.send_message(chat_id=settings.OWNER, text='Got changes on these pages:\n' + str(msg))
		task_worker.quit()

def scheduled_task():
	#bot.send_message(chat_id=settings.owner, text='Checking website changes...')
	bot.send_chat_action(settings.OWNER, 'typing')
	response = requests.get(f'http://localhost:{settings.APIPORT}/entries/all').json()
	task_worker.start()
	if len(response) > 0:
		msg = ''
		for entry in response:
			value = task_worker.get_by_xpath(entry['link'], entry['xpath'])
			if str(value) != str(entry['value']): 
				msg += f"{entry['id']} - Old value: {entry['value']}, New value: {value}\n"
		if len(msg) > 0:
			bot.send_message(chat_id=settings.OWNER, text='Got changes on these pages:\n' + str(msg))
	task_worker.quit()
	#bot.send_message(chat_id=settings.owner, text='Task done.')


if __name__ == '__main__':
    print('Bot started!')
    schedule.every(settings.TIMER).minutes.do(scheduled_task)
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        schedule.run_pending()
        time.sleep(1)
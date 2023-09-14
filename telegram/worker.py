from selenium import webdriver
from selenium.webdriver.remote.command import Command
from bs4 import BeautifulSoup as bs
from lxml import etree
import time


class Scraper():
    def __init__(self):
        # self.headers = {
        #     "User-Agent": "Your user agent",
        #     "Cookie": "Your cookies",
        # }
        self.driver = None

    def start(self):
        self.driver = webdriver.Firefox()

    def get_by_xpath(self, url, xpath, filter=False):
        try:
            self.driver.get(url)
            time.sleep(5)
            html = self.driver.page_source
            soup = bs(html, "lxml")
            dom = etree.HTML(str(soup))
            result = dom.xpath(f'{xpath}')[0].text
            if filter: result = self.format_result(result)
            return result
        except Exception as e:
            return f'Error: {e}'
    
    def format_result(self, input):
        output = input.replace(' ','').replace('\n', '')
        return output

    def quit(self):
        self.driver.close()
        self.driver.quit()

    def close(self):
        self.driver.close()

if __name__ == "__main__":
    pass
    # worker = Scraper()
    # worker.start()
    # value = worker.get_by_xpath('https://en.wikipedia.org/wiki/Nike,_Inc.', '//*[@id="History"]')
    # worker.quit()
    # print(value)
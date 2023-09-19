from selenium import webdriver
from selenium.webdriver.remote.command import Command
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as bs
from lxml import etree
import time


class Scraper():
    def __init__(self):
        # self.headers = None
        self.options = Options()
        self.options.add_argument("-headless")
        self.driver = None

    def start(self):
        self.driver = webdriver.Firefox(options=self.options)

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

    def quit(self):
        self.driver.close()
        self.driver.quit()

    def close(self):
        self.driver.close()

if __name__ == "__main__":
    ...
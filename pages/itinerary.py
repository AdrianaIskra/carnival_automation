import re

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains


class Itinerary:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.days = self.driver.find_elements_by_xpath("//p[@class='day']/span")
        self.book_now = self.driver.find_elements_by_xpath("//div[@class='ready']//a")

    def each_day_detail(self, total_days):
        for i in range(total_days + 1):
            assert int(self.days[i].text) == i+1, "the day are not complete"

    def book_now_button(self):
        self.book_now[0].click()


import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchCruise:

    def __init__(self, driver):
        self.driver = driver
        self.sail_to_xpath = self.driver.find_element_by_xpath("//*[contains(text(), 'Sail To')]")
        self.duration_xpath = self.driver.find_element_by_xpath("//*[contains(text(), 'Duration')]")

    def select_destination(self, destination):
        text = "//*[contains(text(), '%s')]" % destination
        self.sail_to_xpath.click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, text))).click()


    def select_duration(self):
        self.duration_xpath.click()
        self.driver.implicitly_wait(5)
        self.days_text = self.driver.find_element_by_xpath("//*[contains(text(), '6 - 9 Days')]")
        self.days_text.click()

    def result_in_grid(self):
        assert self.driver.find_elements_by_class_name("ccs-search-results"), "Results are not present"
        return self.driver.find_element_by_xpath("//*[contains(text(),'Grid view active')]")

    def filter_by_price(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Pricing')]"))).click()
        self.slider_min = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='rz-pointer rz-pointer-min rz-active']")))
        move = ActionChains(self.driver)
        move.click_and_hold(self.slider_min).move_by_offset(500, 0).release().perform()
        self.slider_max = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='rz-pointer rz-pointer-max']")))
        move = ActionChains(self.driver)
        move.click_and_hold(self.slider_max).move_by_offset(-50, 0).release().perform()


    def price_range(self):
        price_ini = self.slider_min.get_attribute("aria-valuenow")
        price_fin = self.slider_max.get_attribute("aria-valuenow")
        grid_prices = self.driver.find_elements_by_xpath("//*[@class='vrgf-price-box__price']")
        for i in range(len(grid_prices) - 1):
            price = int(re.findall('\d+', grid_prices[i].text)[0])
            assert price > int(price_ini), "the results is cheaper than the range"
            assert price < int(price_fin), "the results is more expensive than the range"


    def order_by_price(self):
        grid_prices = self.driver.find_elements_by_xpath("//*[@class='vrgf-price-box__price']")
        for i in range(len(grid_prices) - 2):
            price = int(re.findall('\d+', grid_prices[i].text)[0])
            price_next = int(re.findall('\d+', grid_prices[i + 1].text)[0])
            assert price < price_next, "the results are not sorted by cheaper"

    def learn_more(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Pricing')]"))).click()
        self.days = self.driver.find_elements_by_xpath("//*[@class ='cgc-cruise-glance__days']")[0].text
        more = self.driver.find_elements_by_xpath("//*[@class='vrgf-learn-more']//a[1]")[0]
        more.click()
        return self.days


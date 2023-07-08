
class AvitoParser(object):
    def __init__(self, url: str, items: list, pages_count: int = 100, browser_version=None):
        """init method"""
        self.url = url
        self.items = items
        self.pages_count = pages_count
        self.browser_version = browser_version
        self.data = []

    def __set_config(self):
        """ private method
        run browser"""
        options = Options()
        options.add_argument('--headless')
        self.driver = uc.Chrome(browser_version=self.browser_version, options=options)

   
    def __get_url(self):
        """get page"""
        self.driver.get(self.url)

    def __paginator(self):
        """ private method
        click next page"""
        while self.driver.find_elements(By.CSS_SELECTOR,
                                        "[data-marker='pagination-button/next']") and self.pages_count > 0:
            self.__parse_page()
            self.driver.find_element("[data-marker='pagination-button/next']").click()
            self.pages_count -= 1

    def __parse_page(self):
        """ private method
         parse one page"""
        titles = self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for title in titles:
            name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
            description = title.find_element(By.CSS_SELECTOR, "[class*='item-description']")
            url = title.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
            price = title.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute('content')
            data = {'name': name, 'description': description, 'url': url, 'price': price}
            if any([item.lower() in description for item in self.items]) and int(price) == 0:
                self.data.append(data)
        self.save_data()

    def save_data(self):
        """ save data """
        pass 
    def parse(self):
        """ main method"""

if __name__ == '__main__':
    AvitoParser()

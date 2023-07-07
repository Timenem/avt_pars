
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
        """ get page"""

    def __paginator(self):
        """ private method
        click next page"""

    def __parse_page(self):
        """ private method
         parse one page"""

    def save_data(self):
        """ save data """
    def parse(self):
        """ main method"""



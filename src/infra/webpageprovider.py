import requests

class WebPageProvider(object):
    def __init__(self, url):
        self.url = url

    def get_page(self):
        page = requests.get(self.url)
        if page.status_code == 200:
            return page.content
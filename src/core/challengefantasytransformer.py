import re

from bs4 import BeautifulSoup

class ChallengeFantasyTransformer(object):
    def __init__(self, content):
        self.soup = BeautifulSoup(content, "html.parser")

    def parse(self):
        for entry in self.soup.find_all("div", class_="panel-default"):
            heading = entry.find("div", class_="panel-heading")
            if heading:
                name = heading.find("span").get_text() #this is the name of the contestant

                body = entry.find("div", class_="panel-body").find_all("li")
                for score in body:
                    name = name
                    text = score.get_text()
                    identifier = text.split("(")[0].strip().replace(",", "")
                    occurences = int(re.search("\((\d*)\)", text).group(1).strip())
                    total = int(text.split(":")[1].strip())

                    yield f"{name},{identifier},{occurences},{total}"

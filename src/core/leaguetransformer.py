from bs4 import BeautifulSoup

class LeagueTransformer(object):
    def __init__(self, content):
        self.soup = BeautifulSoup(content, "html.parser")

    def parse(self, start, end):
        parent_table = self.soup.select(".table-responsive")[0]
        headers = parent_table.select("h4")
        week_tables = parent_table.select("table")

        for i in range(0, len(headers)):
            week = int(headers[i].get_text().split(" ")[1])
            if week >= start and week <= end:
                player_rows = week_tables[i].find_all("td", class_="player")
                for player_row in player_rows:
                    player = player_row.get_text().split("(Eliminated)")[0].strip()
                    yield f"{week},{player}"


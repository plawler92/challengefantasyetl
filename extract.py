from src.infra.webpageprovider import WebPageProvider
from src.infra.localfilewriter import LocalFileWriter
from src.core.challengefantasytransformer import ChallengeFantasyTransformer
from src.core.leaguetransformer import LeagueTransformer
import config as cfg

def extract_show_scores(start_week, end_week):
    l = LocalFileWriter("scores.csv")
    l.open()
    l.write("week,name,identifier,occurrences,total_points\n")

    for week in range(start_week, end_week + 1):
        w = WebPageProvider(cfg.base_url + str(week))
        content = w.get_page()
        
        if content:
            t = ChallengeFantasyTransformer(content)

            for score in t.parse():
                l.write(f"{week},{score}\n")

    l.close()

def extract_league_scores(start_week, end_week):
    #11459 my team
    l = LocalFileWriter("league_scores.csv")
    l.open()
    l.write("team,week,player\n")

    for team in cfg.team_ids:
        w = WebPageProvider(cfg.team_url + str(team))
        content = w.get_page()
        if content:
            t = LeagueTransformer(content)

        for score in t.parse(start_week, end_week):
            l.write(f"{team},{score}\n")

    l.close()

if __name__ == "__main__":
    extract_show_scores(1, 6)
    #extract_league_scores(1, 6)

    


import bs4
import requests


premier_league = requests.get('https://www.soccer.ru/tournament/england/results')
parce = bs4.BeautifulSoup(premier_league.text, "html.parser")
home_team = parce.select('.home .sc .score')
count_of_goals_by_home_team = home_team[0].getText()
visit_team = parce.select('.visit .sc .score')
count_of_goals_by_visit_team = visit_team[0].getText()

home = parce.select('.home .team-name')
textfield_home_team = home[0].getText()

visit = parce.select('.visit .team-name')
textfield_visit_team = visit[0].getText()

print(textfield_home_team, count_of_goals_by_home_team + " : " + count_of_goals_by_visit_team, textfield_visit_team)


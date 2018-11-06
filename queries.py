from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sports.db')

Session = sessionmaker(bind=engine)
session = Session()

def return_teams_for_new_york():
    # here we want to return all teams that are associated with New York City
    ny = session.query(City).filter(City.name == "New York").first()
    return ny.teams

def return_players_for_la_dodgers():
    dodgers = session.query(Team).filter(Team.name == "Dodgers").first()
    return dodgers.roster

def return_sorted_new_york_knicks():
    knicks = session.query(Team).filter(Team.name == "Knicks").first()
    team = knicks.roster
    return sorted(team, key = lambda item: item.number)
    # sorted in ascending (small -> big) order by their number

def return_youngest_basket_ball_player_in_new_york():
    # here we want to sort all the players on New York Knicks by age
    # and return the youngest player
    pass

def return_all_players_in_los_angeles():
    lateams = session.query(City).filter(City.name == "Los Angeles").first().teams
    players = [item.roster for item in lateams]
    return players

def return_tallest_player_in_los_angeles():
    lateams = session.query(City).filter(City.name == "Los Angeles").first().teams
    players = [item.roster for item in lateams]
    empty = []
    for item in players:
        for player in item:
            empty.append(player)
    return max(empty, key = lambda item: item.height)
    # return max(players, key = lambda item: item.height)

def return_team_with_heaviest_players():

    pass

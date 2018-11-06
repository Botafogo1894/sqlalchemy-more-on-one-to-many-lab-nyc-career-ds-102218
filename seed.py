from models import *
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///sports.db')

Session = sessionmaker(bind=engine)
session = Session()

# below we are reading the csv files to create the data we will need to create the players
# pandas returns a DataFrame object from reading the CSV
# we then tell the DataFrame object to turn each row into dictionaries
# by giving to_dict the argument "orient='records'"
# we are telling our DataFrame to make each row a dictionary using the column headers
# as the keys for the key value pairs in each new dictionary
# feel free to uncomment lines 18-21 to see each step of the process in your terminal
# ____ example ______
# la_dodgers0 = pd.read_csv('la_dodgers_baseball.csv')
# la_dodgers1 = pd.read_csv('la_dodgers_baseball.csv').to_dict()
# la_dodgers2 = pd.read_csv('la_dodgers_baseball.csv').to_dict(orient='records')
# import pdb; pdb.set_trace()
# __________________
la_dodgers = pd.read_csv('la_dodgers_baseball.csv').to_dict(orient='records')
la_lakers = pd.read_csv('la_lakers_basketball.csv').to_dict(orient='records')
ny_yankees = pd.read_csv('ny_yankees_baseball.csv').to_dict(orient='records')
ny_knicks = pd.read_csv('ny_knicks_basketball.csv').to_dict(orient='records')

#cities
nyc = City(name = "New York", state = "NY")
la =  City(name = "Los Angeles", state = "CA")
cities = [nyc, la]
#sports
basketball = Sport(name = "basketball")
baseball = Sport(name = "baseball")
sports = [basketball, baseball]
#teams
dodgers = Team(name = "Dodgers", city = la, sport = baseball)
lakers = Team(name = "Lakers", city = la, sport = basketball)
yankees = Team(name = "Yankees", city = nyc, sport = baseball)
knicks = Team(name = "Knicks", city = nyc, sport = basketball)
teams = [dodgers, lakers, yankees, knicks]
#players
def create_player(data, team):
    empty = []
    for player in data:
        try:
            players = Player(name = player['name'], number = player['number'], height = player['height'], weight = player['weight'], team = team)
            empty.append(players)
        except KeyError:
            players = Player(name = player['name'], height = player['height'], weight = player['weight'], team = team)
            empty.append(players)
    return empty

dodgers_players = create_player(la_dodgers, dodgers)
lakers_players = create_player(la_lakers, lakers)
yankees_players = create_player(ny_yankees, yankees)
knicks_players = create_player(ny_knicks, knicks)

session.add_all(teams)
session.add_all(cities)
session.add_all(sports)
session.add_all(dodgers_players)
session.add_all(lakers_players)
session.add_all(yankees_players )
session.add_all(knicks_players)

session.commit()



# now that we have the data for each player

# add and commit the players, teams, sports and cities below
# we will need to probably write at least one function to iterate over our data and create the players
# hint: it may be a good idea to creat the Teams, Cities, and Sports first

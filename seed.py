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

#teams
dodgers = Team(name = "Dodgers")
lakers = Team(name = "Lakers")
yankees = Team(name = "Yankees")
knicks = Team(name = "Knicks")
teams = [dodgers, lakers, yankees, knicks]
#cities
nyc = City(name = "New York", state = "NY")
la =  City(name = "Los Angeles", state = "CA")
cities = [nyc, la]
#sports
basketball = Sport(name = "basketball")
baseball = Sport(name = "baseball")
sports = [basketball, baseball]
#players

team_list = [la_dodgers, la_lakers, ny_yankees, ny_knicks]

def create_player(data):
    empty = []
    for team in data:
        for player in team:
            try:
                players = Player(name = player['name'], number = player['number'], height = player['height'], weight = player['weight'])
                empty.append(players)
            except KeyError:
                player = Player(name = player['name'], height = player['height'], weight = player['weight'])
                empty.append(players)
    return empty

final_players = create_player(team_list)

session.add_all(teams)
session.add_all(cities)
session.add_all(sports)
session.add_all(final_players)

session.commit()



# now that we have the data for each player

# add and commit the players, teams, sports and cities below
# we will need to probably write at least one function to iterate over our data and create the players
# hint: it may be a good idea to creat the Teams, Cities, and Sports first

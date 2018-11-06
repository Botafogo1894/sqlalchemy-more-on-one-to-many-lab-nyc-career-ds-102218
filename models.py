from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()


# write the Player, City, Sport and Team tables below

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    number = Column(Integer)
    height = Column(String)
    weight = Column(Integer)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship('Team', back_populates = 'roster')

class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship('City', back_populates = 'teams')
    sport_id = Column(Integer, ForeignKey('sports.id'))
    sport = relationship('Sport', back_populates = 'teams')
    # player_id = Column(Integer, ForeignKey('players.id'))
    roster = relationship('Player', order_by = Player.id, back_populates = 'team')

class Sport(Base):
    __tablename__ = 'sports'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    # team_id = Column(Integer, ForeignKey('teams.id'))
    teams = relationship('Team', order_by = Team.id, back_populates = 'sport')

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    state = Column(String)
    # team_id = Column(Integer, ForeignKey('teams.id'))
    teams = relationship('Team', order_by = Team.id, back_populates = 'city')


engine = create_engine('sqlite:///sports.db')
Base.metadata.create_all(engine)

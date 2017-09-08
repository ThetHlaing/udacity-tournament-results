#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2, bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    db = psycopg2.connect("dbname=tournament")
    cursor = db.cursor()
    """Better to return cursor"""
    return db,cursor

def execute(query,para=None):
    """Executing the query without returning the result"""
    db,db_cursor = connect()
    if para == None:
        db_cursor.execute(query);
    else:
        db_cursor.execute(query,para);
    db.commit()
    db.close()


def fetch_data(query, para=None):
    """Executing the query and return the result values"""
    db,db_cursor = connect()
    if para == None:
        db_cursor.execute(query)
    else:
        db_cursor.execute(query, para)
    result = db_cursor.fetchall()
    db.close()
    return result


def deleteMatches():
    """Remove all the match records from the database."""
    execute('delete from matches')



def deletePlayers():
    """Remove all the player records from the database."""
    execute('delete from players');


def countPlayers():
    """Returns the number of players currently registered."""
    return_data = fetch_data('select count(*) from players')
    return int(return_data[0][0])


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    execute('insert into players (full_name) values (%s)',(bleach.clean(name),))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    return fetch_data('select * from player_standing')



def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    execute('insert into matches (winner, loser) values (%s, %s)',(winner,loser,))


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    players = playerStandings()
    pairings = []

    """assuming there will be always even number of players"""
    for index in range(0, len(players) -1, 2):
        first_player = players[index]
        second_player = players[index+1]
        """0 is id, 1 is name """
        paired_list = (first_player[0], first_player[1], second_player[0], second_player[1])
        pairings.append(paired_list)

    return pairings


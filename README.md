# udacity-tournament-results

Detail of the functions inside tournament.py
--------------------------------------------

registerPlayer(name)
Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.


countPlayers()
Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

deletePlayers()
Clear out all the player records from the database.

reportMatch(winner, loser)
Stores the outcome of a single match between two players in the database.

deleteMatches()
Clear out all the match records from the database.

playerStandings()
Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

swissPairings()
Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function should return four pairings. This function should use playerStandings to find the ranking of players.

Creating Database
-----------------

Before you can run your code or create your tables, you'll need to use the create database command in psql to create the database. 
Use the name tournament for your database.

Then you can connect psql to your new database and create your tables from the statements you've written in tournament.sql. 
You can do this in either of two ways:

Paste each statement in to psql.
Use the command \i tournament.sql to import the whole file into psql at once.

Running project!
----------------

To run the series of tests defined in this test suite, run the program from the command line $ python tournament_test.py 

Result should be "Success! All tests pass!" if there is no error. 

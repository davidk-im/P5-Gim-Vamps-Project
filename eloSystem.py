userDatabase = open("accounts.txt").read()

# A lot of this will be to get a working model in python, but with the actual database when that's complete, the code would be much simpler

# Note: sample database in accounts.txt is in the format:
# -UsernameTacticsEloMultiplayerEloStreakScore

"""
Goal:
Create an ELO system to rate chess players on our website -

Tactics: Gain/Lose elo based on completion of the puzzle, with bonuses for solving multiple in a row, and penalties for ansewring multiple in a row incorrectly.
Create a formula to create a bell curve distribution of scores, mainly between 500 and 2500, with 1500 as the mode of the users, assuming that players correctly solve puzzles 50% of the time.

Multiplayer games: Gain/Lose elo based on win or draw, based on the elos of the players.  For example, if a higher rated player won against a lower rated player, they would earn less compared to if a lower rated player won against a higher rated player.  In a draw, the lower rated player would gain elo while the higher rated player would lose elo.
Create a formula with the same goal for distribution as with tactics, though as it's based on the ratings of the individual players, would require more variables.
"""

"""
Tactics
StreakScore = amount of puzzles a user has gotten correct in a row
Equation if player wins:
if PlayerElo > 1000
PlayerElo = PlayerElo + 15(2290000/(PlayerElo)** + (200)**) + 3(StreakScore)(3610000/PlayerElo + 400)**
if PlayerElo > 500 and < 1000
PlayerElo = PlayerElo + 37000000/(PlayerElo** + 170000) + 10(StreakScore)(500/PlayerElo + 1000)
PlayerElo cannot go under 500

Equation if player loses:
Same as if player wins, but if the elo gain is x, then
PlayerElo = (1400000/(x+15)**3)

Multiplayer
Equation if player wins:
PlayerDiff = PlayerElo - OpponentElo
PlayerElo = PlayerElo + 5(PlayerElo - x)
x = 1 / 10**-(PlayerDiff + 600)/1000 + 1
If player loses, equation is the same, but with player diff reversed and subtracting 5(PlayerElo - x)
"""

def Tactic(userDatabase):
  indexing = -1
  userfound = False
  user = input("Which user is solving this puzzle?\n")
  result = input("Did they solve the puzzle correctly? (y/n)\n")
  if result.lower() != "y" and result.lower() != "n":
    print("Invalid result!")
    Tactic(userDatabase)
  userdata = []
  usernameLength = len(user)
  for letter in userDatabase:
    indexing += 1
    if letter == "-":
      userCheck = userDatabase[indexing+1:indexing+usernameLength+1]
      if user == userCheck:
        userdata = [user,userDatabase[indexing+usernameLength+1:indexing+usernameLength+5],userDatabase[indexing+usernameLength+5:indexing+usernameLength+9],userDatabase[indexing+usernameLength+9]]
        userfound = True
        break
  if userfound == True:
    if userdata[1][0] == 0:
      playerElo = int(userdata[1][1:4])
    elif userdata[1][0] != 0:
      playerElo = int(userdata[1])
    streakScore = int(userdata[3])

    if result.lower() == "y" and playerElo >= 1000:
      divisor1  = playerElo**2 + 200**2
      divisor2 = playerElo + 400
      playerElo = playerElo + (34350000/divisor1) + 3*streakScore*3610000/divisor2**2
      playerElo = int(round(playerElo))
      print("User " + user + " now has a tactics rating of " + str(playerElo) + " points!")
      playerElo = str(playerElo)
      streakScore += 1
      return [playerElo, streakScore, userdata[2]]
    elif result.lower() == "y" and playerElo < 1000:
      divisor1 = playerElo**2 + 170000
      divisor2 = playerElo + 1000
      playerElo = playerElo + (37000000/divisor1) + (streakScore*5000/divisor2)
      playerElo = int(round(playerElo))
      print("User " + user + " now has a tactics rating of " + str(playerElo) + " points!")
      if playerElo < 1000:
        playerElo = str("0" + str(playerElo))
      streakScore += 1
      return [playerElo, streakScore, userdata[2]]

    if result.lower() == "n" and playerElo >= 1000:
      divisor1  = playerElo**2 + 200**2
      divisor2 = playerElo + 400
      variable1 = (34350000/divisor1) + 3*streakScore*3610000/divisor2**2
      divisor3 = (variable1 + 15)**3
      subtract1 = 1400000 / divisor3
      playerElo = playerElo - subtract1
      playerElo = int(round(playerElo))
      print("User " + user + " now has a tactics rating of " + str(playerElo) + " points!")
      if playerElo < 1000:
        playerElo = str("0" + str(playerElo))
      streakScore = 0
      return [playerElo, streakScore, userdata[2]]
    elif result.lower() == "n" and playerElo < 1000:
      divisor1 = playerElo**2 + 170000
      divisor2 = playerElo + 1000
      variable1 = (37000000/divisor1) + (streakScore*5000/divisor2)
      divisor3 = (variable1 + 15)**3
      subtract1 = 1400000 / divisor3
      playerElo = playerElo - subtract1
      playerElo = int(round(playerElo))
      print("User " + user + " now has a tactics rating of " + str(playerElo) + " points!")
      playerElo = str("0" + str(playerElo))
      streakScore = 0
      return [playerElo, streakScore, userdata[2]]

  else:
    print("Invalid User!")
    Tactic(userDatabase)


def Multi(userDatabase):
  indexing = -1
  userfound = False
  user2found = False
  user = input("Who is the first user?\n")
  user2 = input("Who is the second user?\n")
  result = input("Which user won? (1/2)\n")
  if result != "1" and result != "2":
    print("Invalid result!")
    Multi(userDatabase)
  userdata = []
  user2data = []
  usernameLength = len(user)
  username2Length = len(user2)
  for letter in userDatabase:
    indexing += 1
    if letter == "-":
      userCheck = userDatabase[indexing+1:indexing+usernameLength+1]
      if user == userCheck:
        userdata = [user,userDatabase[indexing+usernameLength+1:indexing+usernameLength+5],userDatabase[indexing+usernameLength+5:indexing+usernameLength+9],userDatabase[indexing+usernameLength+9]]
        userfound = True
        break
  indexing = -1
  for letter in userDatabase:
    indexing += 1
    if letter == "-":
      userCheck = userDatabase[indexing+1:indexing+username2Length+1]
      if user2 == userCheck:
        user2data = [user,userDatabase[indexing+username2Length+1:indexing+username2Length+5],userDatabase[indexing+username2Length+5:indexing+username2Length+9],userDatabase[indexing+username2Length+9]]
        user2found = True
        break
#  if userfound == True and user2found == True:
  if userdata[2][0] == 0:
    playerElo = int(userdata[2][1:4])
  elif userdata[2][0] != 0:
    playerElo = int(userdata[2])
  if user2data[2][0] == 0:
    player2Elo = int(user2data[2][1:4])
  elif user2data[2][0] != 0:
    player2Elo = int(user2data[2])

  if result == "1":
    playerDiff = player2Elo - playerElo + 600
    divisor1 = 1 + 10**(playerDiff/1000)
    var1 = 1 / divisor1
    var2 = 1 - var1
    playerElo = playerElo + 50 * var2
    playerElo = int(round(playerElo))
    print(user + " now has an ELO rating of " + str(playerElo))
    if playerElo < 1000:
      playerElo = str("0" + str(playerElo))
    return [userdata[1], userdata[3], playerElo]

  elif result == "2":
    playerDiff = playerElo - player2Elo + 600
    divisor1 = 1 + 10**(playerDiff/1000)
    var1 = 1 / divisor1
    var2 = 1 - var1
    playerElo = playerElo - 50 * var2
    playerElo = int(round(playerElo))
    print(user + " now has an ELO rating of " + str(playerElo))
    if playerElo < 1000:
      playerElo = str("0" + str(playerElo))
    return [userdata[1], userdata[3], playerElo]


mode = input("Which mode would you like to test?\n1. Tactics\n2. Multiplayer\n")

runMode = {"1":Tactic, "2":Multi}

funcCall = runMode[mode]
funcCall(userDatabase)

#user_update_stats([])

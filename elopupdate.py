def Multi(user1, elo1, user2, elo2, winner):

    userdata = [user1, elo1]
    user2data = [user2, elo2]
    playerElo = userdata[1]
    player2Elo = user2data[1]
    final = []

    if winner == "1":
        playerDiff = player2Elo - playerElo + 600
        divisor1 = 1 + 10**(playerDiff/1000)
        var1 = 1 / divisor1
        var2 = 1 - var1
        playerElo = playerElo + 50 * var2
        playerElo = int(round(playerElo))
        if playerElo < 1000:
            playerElo = str("0" + str(playerElo))
        final.append[userdata[0], playerElo]

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
        final.append[userdata[0], playerElo]

    tempvar = playerElo
    playerElo = player2Elo
    player2Elo = tempvar

    if winner == "2":
        playerDiff = player2Elo - playerElo + 600
    divisor1 = 1 + 10**(playerDiff/1000)
    var1 = 1 / divisor1
    var2 = 1 - var1
    playerElo = playerElo + 50 * var2
    playerElo = int(round(playerElo))
    if playerElo < 1000:
        playerElo = str("0" + str(playerElo))
    final.append[user2data[0], playerElo]

    elif result == "1":
    playerDiff = playerElo - player2Elo + 600
    divisor1 = 1 + 10**(playerDiff/1000)
    var1 = 1 / divisor1
    var2 = 1 - var1
    playerElo = playerElo - 50 * var2
    playerElo = int(round(playerElo))
    print(user + " now has an ELO rating of " + str(playerElo))
    if playerElo < 1000:
        playerElo = str("0" + str(playerElo))
    final.append[user2data[0], playerElo]

    return final

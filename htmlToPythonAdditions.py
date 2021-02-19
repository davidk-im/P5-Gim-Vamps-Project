from movepiece import *

def HTPlen5(usermove, board, storeboard, whitemove, whitecolor, blackcolor):
    if usermove == "0-0-0":
        if str(whitemove + "R1n") in storeboard["d1"] and board["e1"] == "WK1n":
            try:
                for i in storeboard["d1"]:
                    if i[0].lower() == "b":
                        raise Exception("no")
                for i in storeboard["c1"]:
                    if i[0].lower() == "b":
                        raise Exception("no")
                for i in storeboard["b1"]:
                    if i[0].lower() == "b":
                        raise Exception("no")
                board["e1"] = "  "
                board["d1"] = "WR1"
                board["c1"] = "WK1"
                board["a1"] = "  "
                whitemove = "B"
                storeboard = storeboardset(board, storeboard, whitemove, 1)
                game_create(gameID, movenumber, whitemove, usermove)
            except:
                print("Please enter a valid move.")
        elif str(whitemove + "R1n") in storeboard["d8"] and board["e8"] == "BK1n":
            try:
                for i in storeboard["d8"]:
                    if i[0].lower() == "w":
                        raise Exception("no")
                for i in storeboard["c8"]:
                    if i[0].lower() == "w":
                        raise Exception("no")
                for i in storeboard["b8"]:
                    if i[0].lower() == "w":
                        raise Exception("no")
                board["e8"] = "  "
                board["d8"] = "BR1"
                board["c8"] = "BK1"
                board["a8"] = "  "
                whitemove = "W"
                storeboard = storeboardset(board, storeboard, whitemove, 1)
                game_create(gameID, movenumber, whitemove, usermove)
            except:
                return "invalid"
        else:
            return "invalid"
    try:
        if usermove[2] == ' ':
            piece = board[usermove[0:2]]
            startpos = usermove[0:2]
            if piece in storeboard[usermove[3:5]]:
                board[startpos] = '  '
                board[usermove[3:5]] = piece
                game_create(gameID, movenumber, whitemove, usermove)
                if whitemove == "W":
                    blackpersp(whitecolor, blackcolor, board)
                    whitemove = "B"
                else:
                    whitemove = "W"
                    whitepersp(whitecolor, blackcolor, board)
                storeboard = storeboardset(board, storeboard, whitemove, 1)
            else:
                return "invalid"
    except Exception as e:
        return "invalid"

    return board, whitemove
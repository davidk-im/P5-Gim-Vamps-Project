from movepiece import *

def HTPlen5(usermove, board, storeboard, whitemove, whitecolor, blackcolor):
    if str(whitemove + "R1n") in storeboard["d1"] and board["e1"] == "WK1n" and usermove == "e1 c1":
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
            blackpersp(whitecolor, blackcolor, board)
            whitemove = "B"
            storeboard, checkmate = storeboardset(board, whitemove, 1)
            aiturn = True
        except:
            print("Please enter a valid move.")
    elif str(whitemove + "R1n") in storeboard["d8"] and board["e8"] == "BK1n" and usermove == "e8 c8":
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
            whitepersp(whitecolor, blackcolor, board)
            whitemove = "W"
            storeboard, checkmate = storeboardset(board, whitemove, 1)
            aiturn = True
        except:
            print("Please enter a valid move.")
    elif str(whitemove + "R2n") in storeboard["f1"] and board["e1"] == "WK1n" and usermove == "e1 g1":
        try:
            for i in storeboard["f1"]:
                if i[0].lower() == "b":
                    raise Exception("no")
            for i in storeboard["g1"]:
                if i[0].lower() == "b":
                    raise Exception("no")
            board["e1"] = "  "
            board["f1"] = "WR2"
            board["g1"] = "WK1"
            board["h1"] = "  "
            blackpersp(whitecolor, blackcolor, board)
            whitemove = "B"
            storeboard, checkmate = storeboardset(board, whitemove, 1)
            aiturn = True
        except:
            print("Please enter a valid move.")
    elif str(whitemove + "R2n") in storeboard["f8"] and board["e8"] == "BK1n" and usermove == "e8 g8":
        try:
            for i in storeboard["f8"]:
                if i[0].lower() == "w":
                    raise Exception("no")
            for i in storeboard["g8"]:
                if i[0].lower() == "w":
                    raise Exception("no")
            board["e8"] = "  "
            board["f8"] = "BR2"
            board["g8"] = "BK1"
            board["ah8"] = "  "
            whitepersp(whitecolor, blackcolor, board)
            whitemove = "W"
            storeboard, checkmate = storeboardset(board, whitemove, 1)
            aiturn = True
        except:
            print("Please enter a valid move.")
    else:
        try:
            if usermove[2] == ' ':
                piece = board[usermove[0:2]]
                startpos = usermove[0:2]
                if piece in storeboard[usermove[3:5]]:
                    board[startpos] = '  '
                    board[usermove[3:5]] = piece
                    if whitemove == "W":
                        blackpersp(whitecolor, blackcolor, board)
                        whitemove = "B"
                    else:
                        whitemove = "W"
                        whitepersp(whitecolor, blackcolor, board)
                    storeboard, checkmate = storeboardset(board, whitemove, 1)
                else:
                    return "invalid"
        except Exception as e:
            return "invalid"
    return checkmate, board, whitemove, usermove
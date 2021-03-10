from movepieceai import *
from replaygamehtml import *
from replaygame import *
from piecedefinitions import *
from zwhitepersp import *
from zblackpersp import *
from checkfunctions import *
from static.protectionfunctions import *

def HTPailen5(usermove, board, storeboard, whitemove, whitecolor, blackcolor, turnnum, aicolor):
    piece = board[usermove[0:2]]
    startpos = usermove[0:2]
    board[startpos] = '  '
    board[usermove[3:5]] = piece
    if whitemove == "W":
            whitemove = "B"
    else:
        whitemove = "W"
    storeboard = storeboardset(board, storeboard, whitemove, 1)
    return [storeboard, whitemove, board]

def HTPaimovepiece(board, storeboard, whitemove, whitecolor, blackcolor, turnnum, aiturn, aicolor):
    usermove = primaryai(board, storeboard, whitemove, whitecolor, blackcolor, turnnum)
    returnedlist = HTPailen5(usermove, board, storeboard, whitemove, whitecolor, blackcolor, turnnum, aicolor)
    return returnedlist[3], returnedlist[2]

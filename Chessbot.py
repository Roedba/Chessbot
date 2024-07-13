import pygame
import sys

pygame.init()
before_piece_pos = []
last_last_move = ""
last_move = ""
move_count = 1
move = ""
move_right = "w"
king_move_count = 0
rook_move_count = 0
pygame.display.set_caption("Schachengine")
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
font = pygame.font.Font(None,36)
input_rect = pygame.Rect(150, 550, 40, 600)
user_text = ""
text_surface = font.render(user_text, True, (255,255,255))

brett = pygame.image.load("Chessbot/schachbrett.jpg")
imagesW = [pygame.image.load("Chessbot/images/wR1.png"),pygame.image.load("Chessbot/images/wN1.png"),
           pygame.image.load("Chessbot/images/wB1.png"),pygame.image.load("Chessbot/images/wQ1.png"),
           pygame.image.load("Chessbot/images/wK1.png"),pygame.image.load("Chessbot/images/wB2.png"),
           pygame.image.load("Chessbot/images/wN2.png"),pygame.image.load("Chessbot/images/wR2.png")]

imagesB = [pygame.image.load("Chessbot/images/bR1.png"),pygame.image.load("Chessbot/images/bN1.png"),
           pygame.image.load("Chessbot/images/bB1.png"),pygame.image.load("Chessbot/images/bQ1.png"),
           pygame.image.load("Chessbot/images/bK1.png"),pygame.image.load("Chessbot/images/bB2.png"),
           pygame.image.load("Chessbot/images/bN2.png"),pygame.image.load("Chessbot/images/bR2.png")]
pawnB = pygame.image.load("Chessbot/images/bP1.png")
pawnW = pygame.image.load("Chessbot/images/wP1.png")
piece_pos = {
    "wR1": "a1", "wN1": "b1", "wB1": "c1", "wQ1": "d1", "wK1": "e1", "wB2": "f1", "wN2": "g1", "wR2": "h1",
    "bR1": "a8", "bN1": "b8", "bB1": "c8", "bQ1": "d8", "bK1": "e8", "bB2": "f8", "bN2": "g8", "bR2": "h8",
    "wP1": "a2", "wP2": "b2", "wP3": "c2", "wP4": "d2", "wP5": "e2", "wP6": "f2", "wP7": "g2", "wP8": "h2",
    "bP1": "a7", "bP2": "b7", "bP3": "c7", "bP4": "d7", "bP5": "e7", "bP6": "f7", "bP7": "g7", "bP8": "h7"
}
possible_piece_pos=piece_pos

piece_posW = {
    "wR1": "a1", "wN1": "b1", "wB1": "c1", "wQ1": "d1", "wK1": "e1", "wB2": "f1", "wN2": "g1", "wR2": "h1",
    "wP1": "a2", "wP2": "b2", "wP3": "c2", "wP4": "d2", "wP5": "e2", "wP6": "f2", "wP7": "g2", "wP8": "h2"
}
piece_posB = {
    "bR1": "a8", "bN1": "b8", "bB1": "c8", "bQ1": "d8", "bK1": "e8", "bB2": "f8", "bN2": "g8", "bR2": "h8",
    "bP1": "a7", "bP2": "b7", "bP3": "c7", "bP4": "d7", "bP5": "e7", "bP6": "f7", "bP7": "g7", "bP8": "h7"
}

sq = {'a8': '42|25', 'b8': '101|25', 'c8': '160|25', 'd8': '219|25', 'e8': '278|25', 'f8': '337|25', 'g8': '396|25', 'h8': '455|25',
       'a7': '42|84', 'b7': '101|84', 'c7': '160|84', 'd7': '219|84', 'e7': '278|84', 'f7': '337|84', 'g7': '396|84', 'h7': '455|84',
         'a6': '42|143', 'b6': '101|143', 'c6': '160|143', 'd6': '219|143', 'e6': '278|143', 'f6': '337|143', 'g6': '396|143',
           'h6': '455|143', 'a5': '42|202', 'b5': '101|202', 'c5': '160|202', 'd5': '219|202', 'e5': '278|202', 'f5': '337|202',
             'g5': '396|202', 'h5': '455|202', 'a4': '42|261', 'b4': '101|261', 'c4': '160|261', 'd4': '219|261', 'e4': '278|261',
               'f4': '337|261', 'g4': '396|261', 'h4': '455|261', 'a3': '42|320', 'b3': '101|320', 'c3': '160|320', 'd3': '219|320',
                 'e3': '278|320', 'f3': '337|320', 'g3': '396|320', 'h3': '455|320', 'a2': '42|379', 'b2': '101|379', 'c2': '160|379',
                   'd2': '219|379', 'e2': '278|379', 'f2': '337|379', 'g2': '396|379', 'h2': '455|379', 'a1': '42|438', 'b1': '101|438',
                     'c1': '160|438', 'd1': '219|438', 'e1': '278|438', 'f1': '337|438', 'g1': '396|438', 'h1': '455|438'}

#def is_check():
    #king_pos = possible_piece_pos[move_right+"K1"]
    #for move in get_reverse_legal_moves():
    #    if move[2]+move[3]==king_pos:
    #        return True
    #return False

legal_moves = []
reverse_legal_moves=[]
next_legal_moves=[]
def get_legal_moves():
    global move_right,move_count
    possible_piece_pos = piece_pos
    legal_moves.clear()
    reiheW = "abcdefgh"
    zeileW = "12345678"
    zeileB = "87654321"
    reiheB = "hgfedcba"
    if move_count % 2 == 0:
        move_right = "b"
    else:
        move_right = "w"

    if move_right == "w":
        for i,square in piece_pos.items():
            king_pos = piece_pos[move_right+"K1"]
            if i[0]=="w":
                if i[1]== "B":
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_move = "B"+i[2]+now_square[0]+now_square[1]
                                legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                for _ in get_next_legal_moves(legal_move):
                                    if legal_move[2]+legal_move[3] == king_pos:
                                        del legal_moves[legal_move]
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_move = "B"+i[2]+now_square[0]+now_square[1]
                                    legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    for _ in get_next_legal_moves(legal_move):
                                        if legal_move[2]+legal_move[3] == king_pos:
                                            del legal_moves[legal_move]
                                    break

                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_move = "B"+i[2]+now_square[0]+now_square[1]
                                legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                for _ in get_next_legal_moves(legal_move):
                                        if legal_move[2]+legal_move[3] == king_pos:
                                            del legal_moves[legal_move]
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_move = "B"+i[2]+now_square[0]+now_square[1]
                                    legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    for _ in get_next_legal_moves(legal_move):
                                        if legal_move[2]+legal_move[3] == king_pos:
                                            del legal_moves[legal_move]
                                    break

                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_move = "B"+i[2]+now_square[0]+now_square[1]
                                legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                for _ in get_next_legal_moves(legal_move):
                                        if legal_move[2]+legal_move[3] == king_pos:
                                            del legal_moves[legal_move]
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_move = "B"+i[2]+now_square[0]+now_square[1]
                                    legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    for _ in get_next_legal_moves(legal_move):
                                        if legal_move[2]+legal_move[3] == king_pos:
                                            del legal_moves[legal_move]
                                    break

                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_move = "B"+i[2]+now_square[0]+now_square[1]
                                legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                for _ in get_next_legal_moves(legal_move):
                                        if legal_move[2]+legal_move[3] == king_pos:
                                            del legal_moves[legal_move]
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_move = "B"+i[2]+now_square[0]+now_square[1]
                                    legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    for _ in get_next_legal_moves(legal_move):
                                        if legal_move[2]+legal_move[3] == king_pos:
                                            del legal_moves[legal_move]
                                    break

                if i[1]== "Q":
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) +z < len(reiheW) and 0 <= zeileW.find(square[1])  < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) -z < len(reiheW) and 0 <= zeileW.find(square[1]) < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) +z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) -z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                if i[1] == "R":
                    for z in range(1,9):
                        # Rechts
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1]) < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0]) + z], zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Links
                        if 0 <= reiheW.find(square[0]) - z >= 0 and 0 <= zeileW.find(square[1]) < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0]) - z], zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Oben
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) + z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])], zeileW[zeileW.find(square[1]) + z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Unten
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) - z >= 0:
                            now_square = [reiheW[reiheW.find(square[0])], zeileW[zeileW.find(square[1]) - z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break   
                if i[1]=="K":
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])+1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])+1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])-1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])-1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +1 < len(reiheW) and 0 <= zeileW.find(square[1])  < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -1 < len(reiheW) and 0 <= zeileW.find(square[1]) < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) -1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                if i[1]=="N":
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])+2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])+2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])-2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])-2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +2 < len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+2],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -2 < len(reiheW) and 0 <= zeileW.find(square[1]) +1< len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-2],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +2< len(reiheW) and 0 <= zeileW.find(square[1]) -1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+2],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -2 < len(reiheW) and 0 <= zeileW.find(square[1]) -1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-2],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                if i[1]=="P":
                    if 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                        if square[1] == "2":
                                now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+2]]
                                if now_square[0]+now_square[1] not in piece_pos.values():
                                    legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +1< len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] in piece_pos.values():
                            legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -1< len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] in piece_pos.values():
                            legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    
            if (king_move_count and rook_move_count)==0 and "R2f1" in legal_moves:
                if "0-0" not in legal_moves:
                    key = [k for k, v in piece_pos.items() if v == "f1"[1]]
                    if not key:
                        legal_moves.append("0-0")
            if (king_move_count and rook_move_count)==0 and "R1d1" in legal_moves:
                if "0-0-0" not in legal_moves:
                    key = [k for k, v in piece_pos.items() if v == "d1"[1]]
                    if not key:
                        legal_moves.append("0-0-0")
        #fake_legal_moves = legal_moves
        #for move2 in fake_legal_moves:
            #king_pos = piece_pos[move_right+"K1"]
            #possible_piece_pos[move_right+ move2[0]+move2[1]]=move2[2]+move2[3]
            #for idk in get_reverse_legal_moves():
                #if idk[2]+idk[3]==king_pos:
                    
                    #possible_piece_pos = piece_pos
    if move_right == "b":
        for i,square in piece_pos.items():
            if i[0] == "b":
                if i[1]== "B":
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                if i[1]== "Q":
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) +z < len(reiheB) and 0 <= zeileB.find(square[1])  < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) -z < len(reiheB) and 0 <= zeileB.find(square[1]) < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) +z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) -z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                if i[1] == "R":
                    for z in range(1,9):
                        # Rechts
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1]) < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0]) + z], zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Links
                        if 0 <= reiheB.find(square[0]) - z >= 0 and 0 <= zeileB.find(square[1]) < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0]) - z], zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Oben
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) + z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])], zeileB[zeileB.find(square[1]) + z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Unten
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) - z >= 0:
                            now_square = [reiheB[reiheB.find(square[0])], zeileB[zeileB.find(square[1]) - z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break   
                if i[1]=="K":
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])+1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])+1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])-1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])-1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +1 < len(reiheB) and 0 <= zeileB.find(square[1])  < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -1 < len(reiheB) and 0 <= zeileB.find(square[1]) < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) -1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                if i[1]=="N":
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])+2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])+2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])-2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])-2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +2 < len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+2],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -2 < len(reiheB) and 0 <= zeileB.find(square[1]) +1< len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-2],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +2< len(reiheB) and 0 <= zeileB.find(square[1]) -1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+2],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -2 < len(reiheB) and 0 <= zeileB.find(square[1]) -1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-2],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                if i[1]=="P":
                    if 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                        if square[1] == "7":
                                now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+2]]
                                if now_square[0]+now_square[1] not in piece_pos.values():
                                    legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +1< len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] in piece_pos.values():
                            legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -1< len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] in piece_pos.values():
                            legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    
            if (king_move_count and rook_move_count)==0 and "R2f8" in legal_moves:
                if "0-0" not in legal_moves:
                    key = [k for k, v in piece_pos.items() if v == "f8"[1]]
                    if not key:
                        legal_moves.append("0-0")
            if (king_move_count and rook_move_count)==0 and "R1d8" in legal_moves:
                if "0-0-0" not in legal_moves:
                    key = [k for k, v in piece_pos.items() if v == "d8"[1]]
                    if not key:
                        legal_moves.append("0-0-0") 
    return legal_moves





def get_next_legal_moves(the_legal_move):
    global move_right,move_count
    next_legal_moves.clear()
    reiheW = "abcdefgh"
    zeileW = "12345678"
    zeileB = "87654321"
    reiheB = "hgfedcba"
    if move_count % 2 == 0:
        move_right = "w"
        rev_move_right = "b"
    else:
        move_right = "b"
        rev_move_right = "w"

    next_piece_pos = piece_pos
    next_piece_pos[rev_move_right+the_legal_move[0]+the_legal_move[1]]=the_legal_move[2]+the_legal_move[3]
    
    if move_right == "w":
        for i,square in next_piece_pos.items():
            if i[0]=="w":
                if i[1]== "B":
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                if i[1]== "Q":
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) +z < len(reiheW) and 0 <= zeileW.find(square[1])  < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) -z < len(reiheW) and 0 <= zeileW.find(square[1]) < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) +z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) -z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                if i[1] == "R":
                    for z in range(1,9):
                        # Rechts
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1]) < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0]) + z], zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Links
                        if 0 <= reiheW.find(square[0]) - z >= 0 and 0 <= zeileW.find(square[1]) < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0]) - z], zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Oben
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) + z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])], zeileW[zeileW.find(square[1]) + z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Unten
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) - z >= 0:
                            now_square = [reiheW[reiheW.find(square[0])], zeileW[zeileW.find(square[1]) - z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break   
                if i[1]=="K":
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])+1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])+1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])-1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])-1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +1 < len(reiheW) and 0 <= zeileW.find(square[1])  < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -1 < len(reiheW) and 0 <= zeileW.find(square[1]) < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) -1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                if i[1]=="N":
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])+2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])+2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])-2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])-2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +2 < len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+2],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -2 < len(reiheW) and 0 <= zeileW.find(square[1]) +1< len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-2],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +2< len(reiheW) and 0 <= zeileW.find(square[1]) -1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+2],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -2 < len(reiheW) and 0 <= zeileW.find(square[1]) -1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-2],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                if i[1]=="P":
                    if 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                        if square[1] == "2":
                                now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+2]]
                                if now_square[0]+now_square[1] not in next_piece_pos.values():
                                    next_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +1< len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            next_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -1< len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            next_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    
            if (king_move_count and rook_move_count)==0 and "R2f1" in next_legal_moves:
                if "0-0" not in next_legal_moves:
                    key = [k for k, v in next_piece_pos.items() if v == "f1"[1]]
                    if not key:
                        next_legal_moves.append("0-0")
            if (king_move_count and rook_move_count)==0 and "R1d1" in next_legal_moves:
                if "0-0-0" not in next_legal_moves:
                    key = [k for k, v in next_piece_pos.items() if v == "d1"[1]]
                    if not key:
                        next_legal_moves.append("0-0-0")
        #fake_next_legal_moves = next_legal_moves
        #for move2 in fake_next_legal_moves:
            #king_pos = next_piece_pos[move_right+"K1"]
            #possible_next_piece_pos[move_right+ move2[0]+move2[1]]=move2[2]+move2[3]
            #for idk in get_reverse_next_legal_moves():
                #if idk[2]+idk[3]==king_pos:
                    
                    #possible_next_piece_pos = next_piece_pos
    if move_right == "b":
        for i,square in next_piece_pos.items():
            if i[0] == "b":
                if i[1]== "B":
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                if i[1]== "Q":
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) +z < len(reiheB) and 0 <= zeileB.find(square[1])  < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) -z < len(reiheB) and 0 <= zeileB.find(square[1]) < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) +z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) -z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                if i[1] == "R":
                    for z in range(1,9):
                        # Rechts
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1]) < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0]) + z], zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Links
                        if 0 <= reiheB.find(square[0]) - z >= 0 and 0 <= zeileB.find(square[1]) < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0]) - z], zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Oben
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) + z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])], zeileB[zeileB.find(square[1]) + z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Unten
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) - z >= 0:
                            now_square = [reiheB[reiheB.find(square[0])], zeileB[zeileB.find(square[1]) - z]]
                            if now_square[0]+now_square[1] not in next_piece_pos.values():
                                next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in next_piece_pos.values():
                                key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right:
                                    break
                                if key[0]!=move_right:
                                    next_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break   
                if i[1]=="K":
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])+1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])+1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])-1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])-1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +1 < len(reiheB) and 0 <= zeileB.find(square[1])  < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -1 < len(reiheB) and 0 <= zeileB.find(square[1]) < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) -1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                if i[1]=="N":
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])+2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])+2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])-2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])-2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +2 < len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+2],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -2 < len(reiheB) and 0 <= zeileB.find(square[1]) +1< len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-2],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +2< len(reiheB) and 0 <= zeileB.find(square[1]) -1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+2],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -2 < len(reiheB) and 0 <= zeileB.find(square[1]) -1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-2],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            key = [k for k, v in next_piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right:
                                next_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                if i[1]=="P":
                    if 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in next_piece_pos.values():
                            next_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                        if square[1] == "7":
                                now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+2]]
                                if now_square[0]+now_square[1] not in next_piece_pos.values():
                                    next_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +1< len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            next_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -1< len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] in next_piece_pos.values():
                            next_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    
            if (king_move_count and rook_move_count)==0 and "R2f8" in next_legal_moves:
                if "0-0" not in next_legal_moves:
                    key = [k for k, v in next_piece_pos.items() if v == "f8"[1]]
                    if not key:
                        next_legal_moves.append("0-0")
            if (king_move_count and rook_move_count)==0 and "R1d8" in next_legal_moves:
                if "0-0-0" not in next_legal_moves:
                    key = [k for k, v in next_piece_pos.items() if v == "d8"[1]]
                    if not key:
                        next_legal_moves.append("0-0-0") 
    return next_legal_moves
        






def get_reverse_legal_moves():
    global move_right2,move_count
    reverse_legal_moves.clear()
    reiheW = "abcdefgh"
    zeileW = "12345678"
    zeileB = "87654321"
    reiheB = "hgfedcba"
    if move_count % 2 == 0:
        move_right2 = "w"
    else:
        move_right2 = "b"

    if move_right2 == "w":
        for i,square in piece_pos.items():
            if i[0]=="w":
                if i[1]== "B":
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                if i[1]== "Q":
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) +z < len(reiheW) and 0 <= zeileW.find(square[1])  < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) -z < len(reiheW) and 0 <= zeileW.find(square[1]) < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) +z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) -z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                if i[1] == "R":
                    for z in range(1,9):
                        # Rechts
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1]) < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0]) + z], zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Links
                        if 0 <= reiheW.find(square[0]) - z >= 0 and 0 <= zeileW.find(square[1]) < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0]) - z], zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Oben
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) + z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])], zeileW[zeileW.find(square[1]) + z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Unten
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) - z >= 0:
                            now_square = [reiheW[reiheW.find(square[0])], zeileW[zeileW.find(square[1]) - z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break   
                if i[1]=="K":
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])+1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])+1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])-1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])-1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +1 < len(reiheW) and 0 <= zeileW.find(square[1])  < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -1 < len(reiheW) and 0 <= zeileW.find(square[1]) < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) -1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                if i[1]=="N":
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])+2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])+2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])-2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])-2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +2 < len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+2],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -2 < len(reiheW) and 0 <= zeileW.find(square[1]) +1< len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-2],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +2< len(reiheW) and 0 <= zeileW.find(square[1]) -1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+2],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -2 < len(reiheW) and 0 <= zeileW.find(square[1]) -1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-2],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                if i[1]=="P":
                    if 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                        if square[1] == "2":
                                now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+2]]
                                if now_square[0]+now_square[1] not in piece_pos.values():
                                    reverse_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +1< len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] in piece_pos.values():
                            reverse_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -1< len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] in piece_pos.values():
                            reverse_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    
            if (king_move_count and rook_move_count)==0 and "R2f1" in reverse_legal_moves:
                if "0-0" not in reverse_legal_moves:
                    key = [k for k, v in piece_pos.items() if v == "f1"[1]]
                    if not key:
                        reverse_legal_moves.append("0-0")
            if (king_move_count and rook_move_count)==0 and "R1d1" in reverse_legal_moves:
                if "0-0-0" not in reverse_legal_moves:
                    key = [k for k, v in piece_pos.items() if v == "d1"[1]]
                    if not key:
                        reverse_legal_moves.append("0-0-0")
    if move_right2 == "b":
        for i,square in piece_pos.items():
            if i[0] == "b":
                if i[1]== "B":
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                if i[1]== "Q":
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) +z < len(reiheB) and 0 <= zeileB.find(square[1])  < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) -z < len(reiheB) and 0 <= zeileB.find(square[1]) < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) +z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) -z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                if i[1] == "R":
                    for z in range(1,9):
                        # Rechts
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1]) < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0]) + z], zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Links
                        if 0 <= reiheB.find(square[0]) - z >= 0 and 0 <= zeileB.find(square[1]) < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0]) - z], zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Oben
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) + z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])], zeileB[zeileB.find(square[1]) + z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Unten
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) - z >= 0:
                            now_square = [reiheB[reiheB.find(square[0])], zeileB[zeileB.find(square[1]) - z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==move_right2:
                                    break
                                if key[0]!=move_right2:
                                    reverse_legal_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break   
                if i[1]=="K":
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])+1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])+1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])-1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])-1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +1 < len(reiheB) and 0 <= zeileB.find(square[1])  < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -1 < len(reiheB) and 0 <= zeileB.find(square[1]) < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) -1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("K"+i[2]+now_square[0]+now_square[1])
                if i[1]=="N":
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])+2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])+2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])-2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])-2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +2 < len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+2],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -2 < len(reiheB) and 0 <= zeileB.find(square[1]) +1< len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-2],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +2< len(reiheB) and 0 <= zeileB.find(square[1]) -1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+2],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -2 < len(reiheB) and 0 <= zeileB.find(square[1]) -1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-2],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=move_right2:
                                reverse_legal_moves.append("N"+i[2]+now_square[0]+now_square[1])
                if i[1]=="P":
                    if 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            reverse_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                        if square[1] == "7":
                                now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+2]]
                                if now_square[0]+now_square[1] not in piece_pos.values():
                                    reverse_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +1< len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] in piece_pos.values():
                            reverse_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -1< len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] in piece_pos.values():
                            reverse_legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    
            if (king_move_count and rook_move_count)==0 and "R2f8" in reverse_legal_moves:
                if "0-0" not in reverse_legal_moves:
                    key = [k for k, v in piece_pos.items() if v == "f8"[1]]
                    if not key:
                        reverse_legal_moves.append("0-0")
            if (king_move_count and rook_move_count)==0 and "R1d8" in reverse_legal_moves:
                if "0-0-0" not in reverse_legal_moves:
                    key = [k for k, v in piece_pos.items() if v == "d8"[1]]
                    if not key:
                        reverse_legal_moves.append("0-0-0") 
    return reverse_legal_moves
print(get_legal_moves())


def draw_pieces():
    for i,char in piece_pos.items():
        image_draw_piece = pygame.image.load("Chessbot/images/"+i+".png")
        list_sqq = sq[char].split("|")
        screen.blit(image_draw_piece,(int(list_sqq[0]),int(list_sqq[1])))


def is_legal():
    global move_count,king_move_count,rook_move_count,move_right
    if move == "":
        return False
    if move == "0-0-0" or move == "0-0":
        if move in get_legal_moves():
            move_count+=1
            return True
    if move != "":
        if move[0] == "R" or move[0] == "N" or move[0] == "B" or move[0] == "Q" or move[0] == "K" or move[0] == "P":
            if move[1]== "1" or move[1] == "2" or move[1] == "3" or move[1] == "4" or move[1] == "5" or move[1] == "6" or move[1] == "7" or move[1] == "8":
                if move in get_legal_moves():
                    key = [k for k, v in piece_pos.items() if v == move[2]+move[3]]
                    if key:
                        if key[0] in piece_pos:
                            del piece_pos[key[0]]
                            print("Movecount:",move_count)
                            print("Das sind alle möglichen Züge1:\n",get_legal_moves())
                            print(move_right)
                            move_count+=1
                            return True
                    else:
                        if move[0]== "K":
                            king_move_count +=1
                        if move[0]== "R":
                            rook_move_count +=1
                        print("Move Count:",move_count)
                        print("Das sind alle möglichen Züge2:\n",get_legal_moves())
                        print(move_right)
                        move_count+=1
                        return True

def move_piece():
    global move_right,move,last_last_move,before_piece_pos,last_move
    if is_legal():
        if len(move) == 4 and move != "0-0-0" and move!="0-0": 
            before_piece_pos = piece_pos
            piece_pos[move_right+move[0]+move[1]] = move[2]+move[3]
            last_last_move = last_move
            last_move = move
            move = ""
        if move == "0-0-0":
            if move_right == "w":
                piece_pos[move_right+"K1"] = "c1"
                piece_pos[move_right+"R1"]= "d1"
                move=""
            if move_right == "b":
                piece_pos[move_right+"K1"] = "g8"
                piece_pos[move_right+"R2"]= "f8"
                move=""
        if move == "0-0":
            if move_right == "w":
                piece_pos[move_right+"K1"] = "g1"
                piece_pos[move_right+"R2"]= "f1"
                move=""
            if move_right == "b":
                piece_pos[move_right+"K1"] = "g8"
                piece_pos[move_right+"R2"]= "f8"
                move=""
        if len(move)==7:
            if move [4]+move[5]+move[6]=="e.p":
                if move_right == "w":
                    piece_pos[move_right+move[0]+move[1]] = move[2]+move[3]
                    key = [k for k, v in piece_pos.items() if v == move[2]+"5"]
                    if key:
                        print(key[0])
                        if key[0] in piece_pos:
                            del piece_pos[key[0]]
                if move_right == "b":
                    piece_pos[move_right+move[0]+move[1]] = move[2:3]
                    key = [k for k, v in piece_pos.items() if v == move[2]+"4"]
                    if key:
                        print(key[0])
                        if key[0] in piece_pos:
                            del piece_pos[key[0]]



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                move = user_text
                user_text = ""
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (0,0,0), input_rect)
    pygame.draw.rect(screen, (0,0,0), input_rect, 2)
    text_surface = font.render(user_text, True, (255,255,255))
    width = max(200, text_surface.get_width()+10)
    input_rect.w = width
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

    screen.blit(brett, (0, 0))
    move_piece()
    draw_pieces()
    clock.tick(10)
    pygame.display.flip()
pygame.quit()
sys.exit()

import pygame
import sys
from functions import *
from definitions import *

pygame.init()

pygame.display.set_caption("Schachengine")
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
font = pygame.font.Font(None,36)
input_rect = pygame.Rect(150, 550, 40, 600)
text_surface = font.render(user_text, True, (255,255,255))

brett = pygame.image.load("schachbrett.jpg")
imagesW = [pygame.image.load("images/wR1.png"),pygame.image.load("images/wN1.png"),
           pygame.image.load("images/wB1.png"),pygame.image.load("images/wQ1.png"),
           pygame.image.load("images/wK1.png"),pygame.image.load("images/wB2.png"),
           pygame.image.load("images/wN2.png"),pygame.image.load("images/wR2.png")]

imagesB = [pygame.image.load("images/bR1.png"),pygame.image.load("images/bN1.png"),
           pygame.image.load("images/bB1.png"),pygame.image.load("images/bQ1.png"),
           pygame.image.load("images/bK1.png"),pygame.image.load("images/bB2.png"),
           pygame.image.load("images/bN2.png"),pygame.image.load("images/bR2.png")]
pawnB = pygame.image.load("images/bP1.png")
pawnW = pygame.image.load("images/wP1.png")


#def is_check():
    #king_pos = possible_piece_pos[move_right+"K1"]
    #for move in get_reverse_legal_moves():
    #    if move[2]+move[3]==king_pos:
    #        return True
    #return False


"""
def get_next_legal_moves(the_legal_move):
    global move_right,move_count
    next_legal_moves.clear()
    reiheW = "abcdefgh"
    zeileW = "12345678"
    zeileB = "87654321"
    reiheB = "hgfedcba"
    if move_count % 2 == 0:
        move_right = "w"
    else:
        move_right = "b"

    next_piece_pos = piece_pos
    next_piece_pos[move_right+the_legal_move[0]+the_legal_move[1]]=the_legal_move[2]+the_legal_move[3]
    
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
"""     

"""
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
"""
print(get_legal_moves())

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                move = user_text
                user_text = ""
                move_piece(move)
                print(legal_moves)
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
    draw_pieces(screen)
    clock.tick(10)
    pygame.display.flip()
pygame.quit()
sys.exit()

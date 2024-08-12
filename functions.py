from definitions import *
import pygame
import random
def get_legal_moves():
    global move_right,move_count, move, last_move
    legal_moves.clear()
    enpassant_moves.clear()
    reiheW = "abcdefgh"
    zeileW = "12345678"
    zeileB = "87654321"
    reiheB = "hgfedcba"
    if move_count % 2 == 0:
        move_right = "b"
        opposite_move_right = "w"
    else:
        move_right = "w"
        opposite_move_right = "b"
    if move_right == "w":
        for i,square in piece_pos.items():
            king_pos = piece_pos[move_right+"K1"]
            if i[0]=="w":
                if i[1]== "B":
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])+z]]
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
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])+z]]
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
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])-z]]
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
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])-z]]
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
                                p_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+1]]
                                now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+2]]
                                if now_square[0]+now_square[1] not in piece_pos.values() and p_square[0]+p_square[1] not in piece_pos.values():
                                    legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +1< len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])+1]]
                        key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]]
                        if key:
                            if now_square[0]+now_square[1] in piece_pos.values() and key[0][0] == "b":
                                legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -1< len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])+1]]
                        key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]]
                        if key:
                            if now_square[0]+now_square[1] in piece_pos.values() and key[0][0] == "b":
                                legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if square[1] == "5" and last_move[0] == "P" and reiheW.find(last_move[2])+1 == reiheW.find(square[0]):
                        if int(i[2])-1 > 0 and opposite_move_right+"P"+str(int(i[2])-1) in last_piece_pos:
                            if int(last_piece_pos[opposite_move_right+"P"+str(int(i[2])-1)][1]) == 7 and opposite_move_right+"P"+str(int(i[2])-1) in piece_pos:
                                if int(piece_pos[opposite_move_right+"P"+str(int(i[2])-1)][1]) == 5:
                                    now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])+1]]
                                    legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                                    print(legal_moves)
                                    enpassant_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if square[1] == "5" and last_move[0] == "P" and reiheW.find(last_move[2])-1 == reiheW.find(square[0]):
                        if int(i[2])+1 < 9 and opposite_move_right+"P"+str(int(i[2])+1) in last_piece_pos:
                            if int(last_piece_pos[opposite_move_right+"P"+str(int(i[2])+1)][1]) == 7 and opposite_move_right+"P"+str(int(i[2])+1) in piece_pos:
                                if int(piece_pos[opposite_move_right+"P"+str(int(i[2])+1)][1]) == 5:
                                    now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])+1]]
                                    legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                                    enpassant_moves.append("P"+i[2]+now_square[0]+now_square[1])

            if (king_move_count and rook_move_count)==0 and "R2f1" in legal_moves and "K1f1" in legal_moves:
                if "0-0" not in legal_moves:
                    key = [k for k, v in piece_pos.items() if v == "f1"[1]]
                    if not key:
                        legal_moves.append("0-0")
            if (king_move_count and rook_move_count)==0 and "R1d1" in legal_moves and "K1d1" in legal_moves:
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
                                pb_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+1]]
                                now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+2]]
                                if now_square[0]+now_square[1] not in piece_pos.values() and pb_square[0]+pb_square[1] not in piece_pos.values():
                                    legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +1< len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+1]]
                        key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]]
                        if now_square[0]+now_square[1] in piece_pos.values() and key[0][0] == "w":
                            legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -1< len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+1]]
                        key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]]
                        if now_square[0]+now_square[1] in piece_pos.values() and key[0][0] == "w":
                            legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    
                    if square[1] == "4" and last_move[0] == "P" and reiheB.find(last_move[2])+1 == reiheB.find(square[0]):
                        if int(i[2])-1 > 0 and opposite_move_right+"P"+str(int(i[2])-1) in last_piece_pos:
                            if int(last_piece_pos[opposite_move_right+"P"+str(int(i[2])-1)][1]) == 2 and opposite_move_right+"P"+str(int(i[2])+1) in piece_pos:
                                if int(piece_pos[opposite_move_right+"P"+str(int(i[2])+1)][1]) == 4:
                                    now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+1]]
                                    legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                                    enpassant_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if square[1] == "4" and last_move[0] == "P" and reiheB.find(last_move[2])-1 == reiheB.find(square[0]):
                        if int(i[2])+1 < 9 and opposite_move_right+"P"+str(int(i[2])+1) in last_piece_pos:
                            if int(last_piece_pos[opposite_move_right+"P"+str(int(i[2])+1)][1]) == 2 and opposite_move_right+"P"+str(int(i[2])-1) in piece_pos:
                                if int(piece_pos[opposite_move_right+"P"+str(int(i[2])-1)][1]) == 4:
                                    now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+1]]
                                    legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
                                    enpassant_moves.append("P"+i[2]+now_square[0]+now_square[1])

            if (king_move_count and rook_move_count)==0 and "R2f8" in legal_moves and "K1f8" in legal_moves:
                if "0-0" not in legal_moves:
                    key = [k for k, v in piece_pos.items() if v == "f8"[1]]
                    if not key:
                        legal_moves.append("0-0")
            if (king_move_count and rook_move_count)==0 and "R1d8" in legal_moves and "K1d8" in legal_moves:
                if "0-0-0" not in legal_moves:
                    key = [k for k, v in piece_pos.items() if v == "d8"[1]]
                    if not key:
                        legal_moves.append("0-0-0") 
    """
    true_legal_moves = []
    if not is_check(get_enemy_moves()):
        for current_move in legal_moves:
            piece_pos_change = piece_pos[move_right+current_move[0]+current_move[1]]
            piece_pos[move_right+current_move[0]+current_move[1]]=current_move[2]+current_move[3]
            if not is_check(get_enemy_moves()):
                #print(current_move)
                true_legal_moves.append(current_move)
            piece_pos[move_right+current_move[0]+current_move[1]]= piece_pos_change
    
    return true_legal_moves
    """


    filter_legal_moves()

    return legal_moves

def filter_legal_moves():
    global legal_moves
    new_legal_moves = []
    if "0-0" in legal_moves:
        legal_moves.remove("0-0")
        if move_right == "w":
            legal_moves.append("K1g1")
        if move_right == "b":
            legal_moves.append("K1g8")
    if "0-0-0" in legal_moves:
        legal_moves.remove("0-0-0")
        if move_right == "w":
            legal_moves.append("K1c1")
        if move_right == "b":
            legal_moves.append("K1c8")
    for current_move in legal_moves:
        # Speichern der aktuellen Position des bewegten Stücks
        piece_pos_change = piece_pos[move_right + current_move[0] + current_move[1]]


        #aus piece_pos die geschlagene figur entfernen und dann gucken ob ohne die figur man immernoch im schach steht
        piece_to_delete = [key for key, value in piece_pos.items() if value == current_move[2]+current_move[3]]
        if piece_to_delete:
            for key in piece_to_delete:
                del piece_pos[key]


        # Den Zug ausführen
        piece_pos[move_right + current_move[0] + current_move[1]] = current_move[2] + current_move[3]
        # Überprüfen, ob der Zug den König in Schach lässt
        if not is_check(get_enemy_moves()):
            new_legal_moves.append(current_move)
        
        # Den Zug rückgängig machen
        piece_pos[move_right + current_move[0] + current_move[1]] = piece_pos_change
        for key in piece_to_delete:
            piece_pos[key] = current_move[2]+current_move[3]
        if move_right == "w" and current_move[0] == "P" and current_move in new_legal_moves:
            if current_move[3] == "8":
                new_legal_moves.append(current_move+"Q")
                new_legal_moves.append(current_move+"B")
                new_legal_moves.append(current_move+"N")
                new_legal_moves.remove(current_move)

        if move_right == "b" and current_move[0] == "P" and current_move in new_legal_moves:
            if current_move[3] == "1":
                new_legal_moves.append(current_move+"Q")
                new_legal_moves.append(current_move+"B")
                new_legal_moves.append(current_move+"N")
                new_legal_moves.remove(current_move)
    if move_right == "w":
        if "K1f1" in new_legal_moves and "K1g1" in new_legal_moves:
            new_legal_moves.remove("K1g1")
            new_legal_moves.append("0-0")
        if "K1d1" in new_legal_moves and "K1c1" in new_legal_moves:
            new_legal_moves.remove("K1c1")
            new_legal_moves.append("0-0-0")
    if move_right == "b":
        if "K1f8" in new_legal_moves and "K1g8" in new_legal_moves:
            new_legal_moves.remove("K1g8")
            new_legal_moves.append("0-0")
        if "K1d8" in new_legal_moves and "K1c8" in new_legal_moves:
            new_legal_moves.remove("K1c8")
            new_legal_moves.append("0-0-0")
    legal_moves = new_legal_moves
    return legal_moves

def is_check(enemy_moves):
    global legal_moves
    for current_move in enemy_moves:
        if current_move != "0-0" and current_move != "0-0-0" and current_move[2]+current_move[3] == piece_pos[move_right +"K1"]:
            
            return True

def is_checkmate():
    if not get_legal_moves():
        if is_check(get_enemy_moves()):
            return "CHECKMATE"
        else:
            return "STALEMATE"

def get_enemy_moves():
    global opposite_move_rightove_right,move_count, move
    enemy_moves.clear()
    reiheW = "abcdefgh"
    zeileW = "12345678"
    zeileB = "87654321"
    reiheB = "hgfedcba"
    if move_count % 2 == 0:
        opposite_move_rightove_right = "w"
    else:
        opposite_move_rightove_right = "b"

    if opposite_move_rightove_right == "w":
        for i,square in piece_pos.items():
            king_pos = piece_pos[opposite_move_rightove_right+"K1"]
            if i[0]=="w":
                if i[1]== "B":
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    
                                    break

                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                if i[1]== "Q":
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])+z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) - z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1])-z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) +z < len(reiheW) and 0 <= zeileW.find(square[1])  < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])+z],zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) -z < len(reiheW) and 0 <= zeileW.find(square[1]) < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])-z],zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) +z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) -z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                if i[1] == "R":
                    for z in range(1,9):
                        # Rechts
                        if 0 <= reiheW.find(square[0]) + z < len(reiheW) and 0 <= zeileW.find(square[1]) < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0]) + z], zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Links
                        if 0 <= reiheW.find(square[0]) - z >= 0 and 0 <= zeileW.find(square[1]) < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0]) - z], zeileW[zeileW.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Oben
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) + z < len(zeileW):
                            now_square = [reiheW[reiheW.find(square[0])], zeileW[zeileW.find(square[1]) + z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Unten
                        if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) - z >= 0:
                            now_square = [reiheW[reiheW.find(square[0])], zeileW[zeileW.find(square[1]) - z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break   
                if i[1]=="K":
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])+1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])+1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])-1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])-1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +1 < len(reiheW) and 0 <= zeileW.find(square[1])  < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -1 < len(reiheW) and 0 <= zeileW.find(square[1]) < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) < len(reiheW) and 0 <= zeileW.find(square[1]) -1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                if i[1]=="N":
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])+2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])+2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) - 1 < len(reiheW) and 0 <= zeileW.find(square[1])-2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) + 1 < len(reiheW) and 0 <= zeileW.find(square[1])-2 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +2 < len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+2],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -2 < len(reiheW) and 0 <= zeileW.find(square[1]) +1< len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-2],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +2< len(reiheW) and 0 <= zeileW.find(square[1]) -1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+2],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -2 < len(reiheW) and 0 <= zeileW.find(square[1]) -1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-2],zeileW[zeileW.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                if i[1]=="P":
                    if 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("P"+i[2]+now_square[0]+now_square[1])
                        if square[1] == "2":
                                now_square = [reiheW[reiheW.find(square[0])],zeileW[zeileW.find(square[1])+2]]
                                if now_square[0]+now_square[1] not in piece_pos.values():
                                    enemy_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) +1< len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])+1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] in piece_pos.values():
                            enemy_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheW.find(square[0]) -1< len(reiheW) and 0 <= zeileW.find(square[1]) +1 < len(zeileW):
                        now_square = [reiheW[reiheW.find(square[0])-1],zeileW[zeileW.find(square[1])+1]]
                        if now_square[0]+now_square[1] in piece_pos.values():
                            enemy_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    
            if (king_move_count and rook_move_count)==0 and "R2f1" in enemy_moves:
                if "0-0" not in enemy_moves:
                    key = [k for k, v in piece_pos.items() if v == "f1"[1]]
                    if not key:
                        enemy_moves.append("0-0")
            if (king_move_count and rook_move_count)==0 and "R1d1" in enemy_moves:
                if "0-0-0" not in enemy_moves:
                    key = [k for k, v in piece_pos.items() if v == "d1"[1]]
                    if not key:
                        enemy_moves.append("0-0-0")
        #fake_enemy_moves = enemy_moves
        #for move2 in fake_enemy_moves:
            #king_pos = piece_pos[opposite_move_rightove_right+"K1"]
            #possible_piece_pos[opposite_move_rightove_right+ move2[0]+move2[1]]=move2[2]+move2[3]
            #for idk in get_reverse_enemy_moves():
                #if idk[2]+idk[3]==king_pos:
                    
                    #possible_piece_pos = piece_pos
    if opposite_move_rightove_right == "b":
        for i,square in piece_pos.items():
            if i[0] == "b":
                if i[1]== "B":
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("B"+i[2]+now_square[0]+now_square[1])
                                    break

                if i[1]== "Q":
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])+z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) - z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1])-z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) +z < len(reiheB) and 0 <= zeileB.find(square[1])  < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])+z],zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) -z < len(reiheB) and 0 <= zeileB.find(square[1]) < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])-z],zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) +z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) -z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])-z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("Q"+i[2]+now_square[0]+now_square[1])
                                    break
                if i[1] == "R":
                    for z in range(1,9):
                        # Rechts
                        if 0 <= reiheB.find(square[0]) + z < len(reiheB) and 0 <= zeileB.find(square[1]) < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0]) + z], zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Links
                        if 0 <= reiheB.find(square[0]) - z >= 0 and 0 <= zeileB.find(square[1]) < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0]) - z], zeileB[zeileB.find(square[1])]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Oben
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) + z < len(zeileB):
                            now_square = [reiheB[reiheB.find(square[0])], zeileB[zeileB.find(square[1]) + z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break
                    for z in range(1,9):
                        # Unten
                        if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) - z >= 0:
                            now_square = [reiheB[reiheB.find(square[0])], zeileB[zeileB.find(square[1]) - z]]
                            if now_square[0]+now_square[1] not in piece_pos.values():
                                enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                            if now_square[0]+now_square[1] in piece_pos.values():
                                key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                                if key[0]==opposite_move_rightove_right:
                                    break
                                if key[0]!=opposite_move_rightove_right:
                                    enemy_moves.append("R"+i[2]+now_square[0]+now_square[1])
                                    break   
                if i[1]=="K":
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])+1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])+1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])-1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])-1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +1 < len(reiheB) and 0 <= zeileB.find(square[1])  < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -1 < len(reiheB) and 0 <= zeileB.find(square[1]) < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) < len(reiheB) and 0 <= zeileB.find(square[1]) -1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("K"+i[2]+now_square[0]+now_square[1])
                if i[1]=="N":
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])+2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])+2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) - 1 < len(reiheB) and 0 <= zeileB.find(square[1])-2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) + 1 < len(reiheB) and 0 <= zeileB.find(square[1])-2 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])-2]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +2 < len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+2],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -2 < len(reiheB) and 0 <= zeileB.find(square[1]) +1< len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-2],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +2< len(reiheB) and 0 <= zeileB.find(square[1]) -1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+2],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -2 < len(reiheB) and 0 <= zeileB.find(square[1]) -1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-2],zeileB[zeileB.find(square[1])-1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                        if now_square[0]+now_square[1] in piece_pos.values():
                            key = [k for k, v in piece_pos.items() if v == now_square[0]+now_square[1]][0]
                            if key[0]!=opposite_move_rightove_right:
                                enemy_moves.append("N"+i[2]+now_square[0]+now_square[1])
                if i[1]=="P":
                    if 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] not in piece_pos.values():
                            enemy_moves.append("P"+i[2]+now_square[0]+now_square[1])
                        if square[1] == "7":
                                now_square = [reiheB[reiheB.find(square[0])],zeileB[zeileB.find(square[1])+2]]
                                if now_square[0]+now_square[1] not in piece_pos.values():
                                    enemy_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) +1< len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] in piece_pos.values():
                            enemy_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    if 0 <= reiheB.find(square[0]) -1< len(reiheB) and 0 <= zeileB.find(square[1]) +1 < len(zeileB):
                        now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+1]]
                        if now_square[0]+now_square[1] in piece_pos.values():
                            enemy_moves.append("P"+i[2]+now_square[0]+now_square[1])
                    
            if (king_move_count and rook_move_count)==0 and "R2f8" in enemy_moves:
                if "0-0" not in enemy_moves:
                    key = [k for k, v in piece_pos.items() if v == "f8"[1]]
                    if not key:
                        enemy_moves.append("0-0")
            if (king_move_count and rook_move_count)==0 and "R1d8" in enemy_moves:
                if "0-0-0" not in enemy_moves:
                    key = [k for k, v in piece_pos.items() if v == "d8"[1]]
                    if not key:
                        enemy_moves.append("0-0-0") 
    return enemy_moves

def draw_pieces(screen):
    global move
    for i,char in piece_pos.items():
        image_draw_piece = pygame.image.load("images/"+i+".png")
        list_sqq = sq[char].split("|")
        screen.blit(image_draw_piece,(int(list_sqq[0]),int(list_sqq[1])))

def is_legal(move):
    global move_count,king_move_count,rook_move_count
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
                            move_count+=1
                            return True
                    if move in enpassant_moves and move_right == "w":
                        asdfgj = int(move[3])-1
                        key = [k for k, v in piece_pos.items() if v == move[2]+str(asdfgj)]
                        if key:
                            del piece_pos[key[0]]
                            move_count+=1
                            return True
                    if move in enpassant_moves and move_right == "b":
                        asdfgj = int(move[3])+1
                        key = [k for k, v in piece_pos.items() if v == move[2]+str(asdfgj)]
                        if key:
                            del piece_pos[key[0]]
                            move_count+=1
                            return True
                    
                    else:
                        if move[0]== "K":
                            king_move_count +=1
                        if move[0]== "R":
                            rook_move_count +=1
                        move_count+=1

                        return True

def move_piece(move):
    global move_right,last_last_move,last_move, last_piece_pos, w_queen_count, w_bishop_count, w_knight_count, b_bishop_count, b_knight_count, b_queen_count, b_rook_count, w_rook_count

    if is_legal(move):
        if len(move) == 4 and move != "0-0-0" and move!="0-0": 
            last_piece_pos = piece_pos.copy()
            piece_pos[move_right+move[0]+move[1]] = move[2]+move[3]
            last_last_move = last_move
            last_move = move
            move = ""
        if len(move) == 5 and move != "0-0-0" and move!="0-0": 
            if move_right == "w":
                if move[4] == "Q":
                    del piece_pos[move_right+move[0]+move[1]]
                    w_queen_count += 1
                    piece_pos[move_right+"Q"+str(w_queen_count)] = move[2]+move[3]

                if move[4] == "R":
                    del piece_pos[move_right+move[0]+move[1]]
                    w_rook_count += 1
                    piece_pos[move_right+"r"+str(w_rook_count)] = move[2]+move[3]

                if move[4] == "N":
                    del piece_pos[move_right+move[0]+move[1]]
                    w_knight_count += 1
                    piece_pos[move_right+"N"+str(w_knight_count)] = move[2]+move[3]

                if move[4] == "B":
                    del piece_pos[move_right+move[0]+move[1]]
                    w_bishop_count += 1
                    piece_pos[move_right+"B"+str(w_bishop_count)] = move[2]+move[3]

            if move_right == "b":
                if move[4] == "Q":
                    del piece_pos[move_right+move[0]+move[1]]
                    b_queen_count += 1
                    piece_pos[move_right+"Q"+str(b_queen_count)] = move[2]+move[3]

                if move[4] == "R":
                    del piece_pos[move_right+move[0]+move[1]]
                    b_rook_count += 1
                    piece_pos[move_right+"R"+str(b_rook_count)] = move[2]+move[3]

                if move[4] == "N":
                    del piece_pos[move_right+move[0]+move[1]]
                    b_knight_count += 1
                    piece_pos[move_right+"N"+str(b_knight_count)] = move[2]+move[3]

                if move[4] == "B":
                    del piece_pos[move_right+move[0]+move[1]]
                    b_bishop_count += 1
                    piece_pos[move_right+"B"+str(b_bishop_count)] = move[2]+move[3]

        if move == "0-0-0":
            last_piece_pos = piece_pos
            last_last_move = last_move
            if move_right == "w":
                piece_pos[move_right+"K1"] = "c1"
                piece_pos[move_right+"R1"]= "d1"
                move=""
            if move_right == "b":
                piece_pos[move_right+"K1"] = "g8"
                piece_pos[move_right+"R2"]= "f8"
                move=""
        if move == "0-0":
            last_piece_pos = piece_pos
            last_last_move = last_move
            if move_right == "w":
                piece_pos[move_right+"K1"] = "g1"
                piece_pos[move_right+"R2"]= "f1"
                move=""
            if move_right == "b":
                piece_pos[move_right+"K1"] = "g8"
                piece_pos[move_right+"R2"]= "f8"
                move=""
        """
        if len(move)==7:
            if move [4]+move[5]+move[6]=="e.p":
                if move_right == "w":
                    piece_pos[move_right+move[0]+move[1]] = move[2]+move[3]
                    key = [k for k, v in piece_pos.items() if v == move[2]+"5"]
                    if key:
                        if key[0] in piece_pos:
                            del piece_pos[key[0]]
                if move_right == "b":
                    piece_pos[move_right+move[0]+move[1]] = move[2:3]
                    key = [k for k, v in piece_pos.items() if v == move[2]+"4"]
                    if key:
                        if key[0] in piece_pos:
                            del piece_pos[key[0]]
        """

def eval():
    if len(get_legal_moves()) > 0:
        return random.choice(get_legal_moves())
    else:
        piece_pos.update(starting_pos)
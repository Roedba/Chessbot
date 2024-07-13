from definitions import *
import pygame

def get_legal_moves():
    global move_right,move_count, move
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
    print(move)
    print("TEST")
    if move != "":
        print("step0 islegal")
        if move[0] == "R" or move[0] == "N" or move[0] == "B" or move[0] == "Q" or move[0] == "K" or move[0] == "P":
            print("step1 islegal")
            if move[1]== "1" or move[1] == "2" or move[1] == "3" or move[1] == "4" or move[1] == "5" or move[1] == "6" or move[1] == "7" or move[1] == "8":
                print("step2 islegal")
                if move in get_legal_moves():
                    print("step3 islegal")
                    key = [k for k, v in piece_pos.items() if v == move[2]+move[3]]
                    print("step4 islegal")
                    if key:
                        print("step5 islegal")
                        if key[0] in piece_pos:
                            print("step6 islegal")
                            del piece_pos[key[0]]
                            print("step7 islegal")
                            print("Movecount:",move_count)
                            print("Das sind alle möglichen Züge1:\n",get_legal_moves())
                            print(move_right)
                            move_count+=1
                            print("IS LEGAL WORKS")
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
                        print("IS LEGAL WORKS")

                        return True

def move_piece(move):
    global move_right,last_last_move,before_piece_pos,last_move
    if move != "":
        print("ACDC")
    if is_legal(move):
        print("move piece kind of WORKS")
        if len(move) == 4 and move != "0-0-0" and move!="0-0": 
            before_piece_pos = piece_pos
            piece_pos[move_right+move[0]+move[1]] = move[2]+move[3]
            last_last_move = last_move
            last_move = move
            print("move piece WORKS")
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
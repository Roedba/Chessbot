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
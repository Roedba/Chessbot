if square[1] == "5" and last_move[0] == "P" and reiheB.find(last_move[2])+1 == reiheB.find(square[0]):
    if int(last_piece_pos[opposite_move_right+"P"+str(int(i[2])-1)][1]) == 7:
        if int(piece_pos[opposite_move_right+"P"+str(int(i[2])-1)][1]) == 5:
            now_square = [reiheB[reiheB.find(square[0])-1],zeileB[zeileB.find(square[1])+1]]
            legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
            print(legal_moves)
            enpassant_moves.append("P"+i[2]+now_square[0]+now_square[1])
if square[1] == "5" and last_move[0] == "P" and reiheB.find(last_move[2])-1 == reiheB.find(square[0]):
    if int(last_piece_pos[opposite_move_right+"P"+str(int(i[2])+1)][1]) == 7:
        if int(piece_pos[opposite_move_right+"P"+str(int(i[2])+1)][1]) == 5:
            now_square = [reiheB[reiheB.find(square[0])+1],zeileB[zeileB.find(square[1])+1]]
            legal_moves.append("P"+i[2]+now_square[0]+now_square[1])
            enpassant_moves.append("P"+i[2]+now_square[0]+now_square[1])
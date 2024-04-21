def win(playerMovesDict, coordinates): 
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)] 
    for dx, dy in directions: 
        count = 1 
    for i in range(1, 5): 
        if (coordinates[0] + dx*i, coordinates[1] + dy*i) in playerMovesDict: 
            count += 1 
        else: 
            break 
    for i in range(1, 5): 
        if (coordinates[0] - dx*i, coordinates[1] - dy*i) in playerMovesDict: 
            count += 1 
        else: 
            break 
    if count >= 5: 
        return True 
    
    return False 


def writeMovesTable(movesList): 
    winner = None
    movesDict = [{}, {}] 

    i = 0
    
    for (r, c) in movesList: 
        player = i % 2 
        movesDict[player][(r, c)] = True  # Записываем ход 
        
        if win(movesDict[player], (r, c)): 
            if player == 0:
                winner = "First"
            else: 
                winner = "Second" 
            break 
        
        i += 1

    if winner: 
        if i + 1 < len(movesList):  # Проверяем, были ли лишние ходы после победы 
            return "Inattention" 
        else: 
            return winner 
    else: 
        return "Draw" 



n = int(input)
moves = []
for i in range(n):
    moves.append(list((map(int, input().split()))))

result = writeMovesTable(moves)

print(writeMovesTable(moves)) 
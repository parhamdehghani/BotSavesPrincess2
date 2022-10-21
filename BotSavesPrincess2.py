def nextMove(n,r,c,grid):
    moves = []
    diff = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'p':
                p_index = i,j

    bot_index = r,c
    diff.append(p_index[0] - bot_index[0])
    diff.append(p_index[1] - bot_index[1])
    if diff[0] < 0:
        moves.append(int(abs(diff[0]))*'UP ')
    elif diff[0] > 0:
        moves.append(int(diff[0])*'DOWN ')


    if diff[1] < 0:
        moves.append(int(abs(diff[1]))*'LEFT ')
    elif diff[1] > 0:
        moves.append(int(diff[1])*'RIGHT ')

    score = (n**2 - len(moves)) / 10.0

    return moves[0].split()[0]

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))

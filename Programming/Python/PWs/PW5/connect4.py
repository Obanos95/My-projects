import random

def clear_grid():
    '''
    Returns the starting grid for visualizing
    
    return: starting grid
    '''
    grid = [[[' '],[1],[2],[3],[4],[5],[6],[7],[' ']],
            [[6],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[6]],
            [[5],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[5]],
            [[4],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[4]],
            [[3],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[3]],
            [[2],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[2]],
            [[1],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[1]],
            [[' '],[1],[2],[3],[4],[5],[6],[7],[' ']]]
    return grid

def grid_visualiser(grid):
    '''
    Visualizes current grid

    : param grid: current grid
    : type grid: list
    '''
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(((grid[i])[j])[0],end=' ')
        print('')


def playable(grid,column):
    '''
    Checks and returns if the requested move(column) is playable or not (has at least one empty space)

    : param grid: current grid
    : type grid: list
    : param column: requested column
    : type column: int

    : return: True if the move is playable, othervise False
    '''
    play = False
    for i in grid[-1::-1]:
        if i[column] == [' ']:
            play = True
    return play

def game(grid,column,figure):
    '''
    Game itself

    : param grid: current grid
    : type grid: list
    : param column: requested column
    : type column: int
    : param figure: current figure that "plays"
    : type figure: str

    : return: the modified grid and if the player actually played or not  
    '''
    played = False
    if playable(grid,column) == False:
        print('Not playable')
    else:
        for i in range(2,8):
            if (grid[-i])[column] == [' ']:
                (grid[-i])[column] = [figure]
                break
        played = True
    return grid,played

def wincheck(grid,figure):
    '''
    Checks the winning

    : param grid: current grid
    : type grid: list
    : param figure: current figure that "plays"
    : type figure: str

    : return: True if the player won, othervise False
    '''
    #horizontal check
    win = False
    count = 0
    for row in grid:
        for column in row:
            if column == [figure]:
                count += 1
                if count >= 4:
                    win = True
                    break
            else:
                count = 0
    
    #vertical check
    for column in range(9):
        for row in grid[-1:-8:-1]:
            if (row[column][0]) == figure:
                count += 1
                if count >= 4:
                    win = True
                    break
            else:
                count = 0

    #diagonal-to-right check
    for rowplus in range(3):
        for columnplus in range(4):
            for i in range(1,5):
                if (grid[i+rowplus])[i+columnplus] == [figure]:
                    count += 1
                    if count >= 4:
                        win = True
                        break
                else:
                    count = 0

    #diagonal-to-left check
    for rowplus in range(3):
        for columnplus in range(4):
            for i in range(1,5):
                if (grid[i+rowplus])[-i-columnplus] == [figure]:
                    count += 1
                    if count >= 4:
                        win = True
                        break
                else:
                    count = 0

    return win

def recommend(grid,figure):
    '''
    Checks for a recommended move

    : param grid: current grid
    : type grid: list
    : param figure: current figure that "plays"
    : type figure: str

    : return: if there is a recommended move, True and number of column
    '''
    #horizontal check
    recom_move = False
    recom_column = None
    count = 0
    for row in grid:
        for column in row:
            if column == [figure]:
                count += 1
            else:
                if count >= 2:
                    recom_move = True
                    recom_column = row.index(column)
                count = 0
    
    #vertical check
    for column in range(9):
        for row in grid[-1:-8:-1]:
            if (row[column][0]) == figure:
                count += 1
            else:
                if count >= 2:
                    recom_move = True
                    recom_column = column
                count = 0

    #diagonal-to-right check
    for rowplus in range(3):
        for columnplus in range(4):
            for i in range(1,5):
                if (grid[i+rowplus])[i+columnplus] == [figure]:
                    count += 1
                    if count >= 2:
                        recom_move = True
                        break
                else:
                    count = 0

    #diagonal-to-left check
    for rowplus in range(3):
        for columnplus in range(4):
            for i in range(1,5):
                if (grid[i+rowplus])[-i-columnplus] == [figure]:
                    count += 1
                    if count >= 2:
                        recom_move = True
                        break
                else:
                    count = 0

    return recom_move, recom_column

grid = clear_grid()
grid_visualiser(grid)
turn = 'y'
win = False
figures = {'r':'*','y':'o'}
while win != True:
    if turn == 'y':
        recom_move,recom_column = recommend(grid,figures[turn])
        if recom_move == True:
            print(f'Recommended column: {recom_column}')
        column = int(input('Which column do you want to play? '))
    else:
        column = random.randint(1,7)
    played = False
    grid, played = game(grid,column,figures[turn])
    grid_visualiser(grid)
    win = wincheck(grid,figures[turn])
    if played == True:
        if turn == 'y':
            turn = 'r'
        elif turn == 'r':
            turn = 'y'
else:
    if turn == 'y':
        print('Red win!')
    else:
        print('Yellow win!')
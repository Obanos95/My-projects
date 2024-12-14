def move(map):
    pos = [1,0]
    direction = 'down'
    while pos != [5,8]:
        if direction == 'down':
            if (map[(pos[1])])[pos[0]+1] == 0:
                pos[1] = pos[1] + 1
            else:
                (map[(pos[1])])[pos[0]+1] = 1
                direction = 'right'
        elif direction == 'right':
            if map[(pos[1]+1)(pos[0])] == 0:
                pos[0] = pos[0] + 1
            else:
                map[(pos[1]+1)(pos[0])] = 1
                direction = 'up'
        elif direction == 'up':
            if map[(pos[1])(pos[0]-1)] == 0:
                pos[1] = pos[1] - 1
            else:
                map[(pos[1])(pos[0]+1)] = 1
                direction = 'left'
        else:
            if map[(pos[1]-1)(pos[0])] == 0:
                pos[0] = pos[0] + 1
            else:
                map[(pos[1]-1)(pos[0])] = 1
                direction = 'down'
        print(direction)

map = [[1,0,1,1,1,1,1,1,1,1],
       [1,0,0,0,1,0,0,0,0,1],
       [1,1,1,0,1,1,1,0,1,1],
       [1,0,0,0,1,0,0,0,0,1],
       [1,0,1,1,1,0,1,0,1,1],
       [1,0,0,0,0,0,1,0,0,1],
       [1,0,1,1,1,1,1,1,0,1],
       [1,0,1,0,1,0,0,0,0,1],
       [1,1,1,1,1,0,1,1,1,1]]

move(map)
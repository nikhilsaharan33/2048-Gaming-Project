import random
import pandas


def start_game():
    mat = [[0 for i in range(4)] for j in range(4)]
    return mat


def add_new_2(mat):
    filled = True
    for row in range(4):
        for col in range(4):
            if (mat[row][col] == 0):
                filled = False
    if (filled):
        return
    col = random.randint(0, 3)
    row = random.randint(0, 3)

    while (mat[row][col] != 0):
        col = random.randint(0, 3)
        row = random.randint(0, 3)

    mat[row][col] = 2


def initialise_game():
    game = start_game()

    add_new_2(game)

    add_new_2(game)

    return game


def move_up(game):
    changed = False
    for col in range(4):

        for row in range(4):

            # if current element is 0 we move the nearest neighbor of it to its position and then merge same numbered-
            # -blocks if possible or else just move the next neighbor up

            if (game[row][col] == 0):

                # move nearest neighbor to its position:

                for i in range(row + 1, 4):
                    if (game[i][col] != 0):
                        game[row][col] = game[i][col]
                        game[i][col] = 0
                        break

                # do merging if possible or else move the next neighbor up

                for i in range(row + 1, 4):

                    if (game[i][col] != 0):  # if we encounter the next neighbor

                        if (game[i][col] == game[row][col]):  # if the next neighbor == nearest neighbor then we merge
                            game[row][col] *= 2
                            game[i][col] = 0

                        else:  # if the next neighbor != nearest neighbor then we just move the next neighbor up

                            # if game[row+1][col] != 0 this means the next neighbor is already at its topmost position
                            # so we just check for i > row+1: (actually the code in if condition below will
                            # cause trouble if we encounter i = row+1

                            if (i != row + 1):
                                game[row + 1][col] = game[i][col]
                                game[i][col] = 0
                        break
                changed = True

            # if current element is not 0 we just do merging or else just move the next neighbor up if possible
            else:

                for i in range(row + 1, 4):

                    if (game[i][col] != 0):  # if we encounter the next neighbor

                        if (game[i][col] == game[row][col]):  # if the next neighbor == nearest neighbor then we merge
                            game[row][col] *= 2
                            game[i][col] = 0
                            changed = True

                        else:  # if the next neighbor != nearest neighbor then we just move the next neighbor up

                            # if game[row+1][col] != 0 this means the next neighbor is already at its topmost position-
                            # -so we just check for i > row+1: (actually the code in if condition below will
                            # cause trouble if we encounter i = row+1

                            if (i != row + 1):
                                game[row + 1][col] = game[i][col]
                                game[i][col] = 0
                                changed = True
                        break
    return game, changed


def move_down(game):
    changed = False
    for col in range(4):

        for row in range(3, -1, -1):

            # if current element is 0 we move the nearest neighbor of it to its position and then merge same numbered-
            # -blocks if possible or else just move the next neighbor down

            if (game[row][col] == 0):

                # move nearest neighbor to its position:

                for i in range(row - 1, -1, -1):
                    if (game[i][col] != 0):
                        game[row][col] = game[i][col]
                        game[i][col] = 0
                        break

                # do merging if possible or else move the next neighbor down

                for i in range(row - 1, -1, -1):

                    if (game[i][col] != 0):  # if we encounter the next neighbor

                        if (game[i][col] == game[row][col]):  # if the next neighbor == nearest neighbor then we merge
                            game[row][col] *= 2
                            game[i][col] = 0

                        else:  # if the next neighbor != nearest neighbor then we just move the next neighbor down

                            # if game[row+1][col] != 0 this means the next neighbor is already at its bottommost -
                            # -position so we just check for i < row-1: (actually the code in if condition below will
                            # cause trouble if we encounter i = row-1

                            if (i != row - 1):
                                game[row - 1][col] = game[i][col]
                                game[i][col] = 0
                        break
                changed = True
            # if current element is not 0 we just do merging if possible or else just move the next neighbor down
            else:

                for i in range(row - 1, -1, -1):

                    if (game[i][col] != 0):  # if we encounter the next neighbor

                        if (game[i][col] == game[row][col]):  # if the next neighbor == nearest neighbor then we merge
                            game[row][col] *= 2
                            game[i][col] = 0
                            changed = True
                        else:  # if the next neighbor != nearest neighbor then we just move the next neighbor down

                            # if game[row+1][col] != 0 this means the next neighbor is already at its bottommost -
                            # -position so we just check for i < row-1: (actually the code in if condition below will
                            # cause trouble if we encounter i = row-1

                            if (i != row - 1):
                                game[row - 1][col] = game[i][col]
                                game[i][col] = 0
                                changed = True
                        break
    return game, changed


def move_left(game):
    changed = False
    for row in range(4):

        for col in range(4):

            # if current element is 0 we move the nearest neighbor of it to its position and then merge same numbered-
            # -blocks if possible or else just move the next neighbor left

            if (game[row][col] == 0):

                # move nearest neighbor to its position:

                for i in range(col + 1, 4):
                    if (game[row][i] != 0):
                        game[row][col] = game[row][i]
                        game[row][i] = 0
                        break

                # do merging if possible or else move the next neighbor left

                for i in range(col + 1, 4):

                    if (game[row][i] != 0):  # if we encounter the next neighbor

                        if (game[row][i] == game[row][col]):  # if the next neighbor == nearest neighbor then we merge
                            game[row][col] *= 2
                            game[row][i] = 0

                        else:  # if the next neighbor != nearest neighbor then we just move the next neighbor up

                            # if game[row][col+1] != 0 this means the next neighbor is already at its leftmost position
                            # so we just check for i > col+1: (actually the code in if condition below will
                            # cause trouble if we encounter i = col+1

                            if (i != col + 1):
                                game[row][col + 1] = game[row][i]
                                game[row][i] = 0

                        break
                changed = True
            # if current element is not 0 we just do merging if possible or else just move the next neighbor left
            else:

                for i in range(col + 1, 4):

                    if (game[row][i] != 0):  # if we encounter the next neighbor

                        if (game[row][i] == game[row][col]):  # if the next neighbor == nearest neighbor then we merge
                            game[row][col] *= 2
                            game[row][i] = 0
                            changed = True
                        else:  # if the next neighbor != nearest neighbor then we just move the next neighbor up

                            # if game[row][col+1] != 0 this means the next neighbor is already at its leftmost position
                            # so we just check for i > col+1: (actually the code in if condition below will
                            # cause trouble if we encounter i = col+1

                            if (i != col + 1):
                                game[row][col + 1] = game[row][i]
                                game[row][i] = 0
                                changed = True
                        break
    return game, changed


def move_right(game):
    changed = False
    for row in range(4):

        for col in range(3, -1, -1):

            # if current element is 0 we move the nearest neighbor of it to its position and then merge same numbered-
            # -blocks if possible or else just move the next neighbor right

            if (game[row][col] == 0):

                # move nearest neighbor to its position:

                for i in range(col - 1, -1, -1):
                    if (game[row][i] != 0):
                        game[row][col] = game[row][i]
                        game[row][i] = 0
                        break

                # do merging if possible or else move the next neighbor right

                for i in range(col - 1, -1, -1):

                    if (game[row][i] != 0):  # if we encounter the next neighbor

                        if (game[row][i] == game[row][col]):  # if the next neighbor == nearest neighbor then we merge
                            game[row][col] *= 2
                            game[row][i] = 0

                        else:  # if the next neighbor != nearest neighbor then we just move the next neighbor right

                            # if game[row][col-1] != 0 this means the next neighbor is already at its rightmost
                            # position so we just check for i < col-1: (actually the code in if condition below will
                            # cause trouble if we encounter i = col-1

                            if (i != col - 1):
                                game[row][col - 1] = game[row][i]
                                game[row][i] = 0

                        break
                changed = True
            # if current element is not 0 we just do merging if possible or else just move the next neighbor right
            else:

                for i in range(col - 1, -1, -1):

                    if (game[row][i] != 0):  # if we encounter the next neighbor

                        if (game[row][i] == game[row][col]):  # if the next neighbor == nearest neighbor then we merge
                            game[row][col] *= 2
                            game[row][i] = 0
                            changed = True
                        else:  # if the next neighbor != nearest neighbor then we just move the next neighbor right

                            # if game[row][col-1] != 0 this means the next neighbor is already at its rightmost
                            # position so we just check for i < col-1: (actually the code in if condition below will
                            # cause trouble if we encounter i = col-1

                            if (i != col - 1):
                                game[row][col - 1] = game[row][i]
                                game[row][i] = 0
                                changed = True
                        break
    return game, changed


def check_2048(game):
    win = False
    for row in range(4):
        for col in range(4):
            if (game[row][col] == 2048):
                win = True
                break

    return win


def check_over(game):
    # if there is a 0
    for row in range(4):
        for col in range(4):
            if (game[row][col] == 0):
                return False

    # if merging is possible:

    # for 0<=row<=2 ; 0<=col<=2

    for row in range(3):
        for col in range(3):
            if (game[row][col] == game[row + 1][col] or game[row][col] == game[row][col + 1]):
                return False

    # for last row

    for col in range(3):
        if (game[3][col] == game[3][col + 1]):
            return False

    # for last column

    for row in range(3):
        if (game[row][3] == game[row + 1][3]):
            return False

    return True

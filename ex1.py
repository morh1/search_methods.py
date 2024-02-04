import search
import math
import utils

id = "315112870"

""" Rules """
RED = 20
BLUE = 30
YELLOW = 40
GREEN = 50
PACMAN = 77

"""gets 2 points and calc manhattan distance"""

def manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


"""convert list to tuple"""

def list_to_tuple(s):
    return tuple(tuple(inner_list) for inner_list in s)


class PacmanProblem(search.Problem):
    """This class implements a pacman problem"""

    def __init__(self, initial):
        """ Magic numbers for ghosts and Packman: 
        2 - red, 3 - blue, 4 - yellow, 5 - green and 7 - Packman."""

        self.locations = dict.fromkeys((7, 2, 3, 4, 5))
        self.dead_end = False

        """ Constructor only needs the initial state.
        Don't forget to set the goal or implement the goal test"""
        search.Problem.__init__(self, initial)

    """ return the pacman index location in the board """
    def pacman_location(self, state):
        for i, row in enumerate(state):
            for j, number in enumerate(row):
                if number == 77:
                    return i, j
        # Pacman not found, return a default value
        return -1, -1

    """ return bool according to the value in the index. 
    wall or out of board ->False, else->True"""

    def valid_pacman_move(self, i, j, state):
        # the pacman can only move inside the game board not on walls and ghosts.
        if 0 <= i < len(state) and 0 <= j < len(state[0]) and (state[i][j] == 11 or state[i][j] == 10):
            return True
        else:
            return False

    """ return all the steps that the pacman can choose according to its position """

    def allowed_actions(self, state):
        actions = []
        i, j = self.pacman_location(state)
        # pacman wasn't found
        if i == -1:
            return ()
        if self.valid_pacman_move(i, j + 1, state):
            actions.append('R')
        if self.valid_pacman_move(i, j - 1, state):
            actions.append('L')
        if self.valid_pacman_move(i + 1, j, state):
            actions.append('D')
        if self.valid_pacman_move(i - 1, j, state):
            actions.append('U')
        return tuple(actions)

    """return a new list of lists according to the pacman movement """

    def mov_pacman(self, action, state):
        s = [list(row) for row in state]
        i, j = self.pacman_location(s)
        # empty
        s[i][j] = 10
        if action == 'R':
            s[i][j + 1] = 77
        if action == 'L':
            s[i][j - 1] = 77
        if action == 'U':
            s[i - 1][j] = 77
        if action == 'D':
            s[i + 1][j] = 77
        return s

    """ return the ghost index location in the board """

    def ghost_location(self, ghost_number, state):
        for i, row in enumerate(state):
            for j, number in enumerate(row):
                if number == ghost_number or number == ghost_number + 1:
                    return i, j, number
        # Ghost not found, return a default value
        return -1, -1, -1

    """ return bool according to the value in the index. 
         wall, out of board or step into anther ghost square ->False, else->True"""

    def valid_ghost_move(self, i, j, s):
        if (0 <= i < len(s) and 0 <= j < len(s[0])) and (s[i][j] == 11 or s[i][j] == 10 or s[i][j] == 77):
            return True
        else:
            return False

    """return a new updated list of lists according to the red ghost movement """

    def mov_ghost(self, step, ghost, s):
        i, j, x = self.ghost_location(ghost, s)
        # ghost cant move
        if step == 0:
            return s

        if i == -1:
            return s
        if x % 10 == 1:
            s[i][j] = 11
        else:
            s[i][j] = 10

        if step == 'R':
            if s[i][j + 1] == 77:
                s[i][j + 1] = 88
            elif s[i][j + 1] % 10 == 1:
                s[i][j + 1] = ghost + 1
            else:
                s[i][j + 1] = ghost
            return s

        if step == 'L':
            if s[i][j - 1] == 77:
                s[i][j - 1] = 88
            elif s[i][j - 1] % 10 == 1:
                s[i][j - 1] = ghost + 1
            else:
                s[i][j - 1] = ghost
            return s

        if step == 'U':
            if s[i - 1][j] == 77:
                s[i - 1][j] = 88
            elif s[i - 1][j] % 10 == 1:
                s[i - 1][j] = ghost + 1
            else:
                s[i - 1][j] = ghost
            return s

        if step == 'D':
            if s[i + 1][j] == 77:
                s[i + 1][j] = 88
            elif s[i + 1][j] % 10 == 1:
                s[i + 1][j] = ghost + 1
            else:
                s[i + 1][j] = ghost
            return s
        return s

    """returns the action that the ghost should make to get closer to the pacman according to manhattan distance with 
    the gama limitation on the ghost move"""

    def min_dis(self, row, col, s):
        valid_mov = ()
        p_row, p_col = self.pacman_location(s)
        if self.valid_ghost_move(row, col + 1, s):
            right_dis = manhattan_distance(col + 1, row, p_col, p_row)
            valid_mov += (('R', right_dis),)
        if self.valid_ghost_move(row + 1, col, s):
            down_dis = manhattan_distance(col, row + 1, p_col, p_row)
            valid_mov += (('D', down_dis),)
        if self.valid_ghost_move(row, col - 1, s):
            left_dis = manhattan_distance(col - 1, row, p_col, p_row)
            valid_mov += (('L', left_dis),)
        if self.valid_ghost_move(row - 1, col, s):
            up_dis = manhattan_distance(col, row - 1, p_col, p_row)
            valid_mov += (('U', up_dis),)
        if len(valid_mov) == 0:
            return 0
        min_tuple = min(valid_mov, key=lambda x: x[1])
        return min_tuple[0]

    """The successor function get a state and return tuple of tuples with all the allowed steps and their equivalent 
    new state"""

    def successor(self, state):
        successors = ()
        actions = self.allowed_actions(state)
        # pacman wasn't found no need to develop this state or can't move
        if len(actions) == 0:
            return successors
        for action in actions:
            successors += ((action, self.result(state, action)),)
        return successors

    def result(self, state, move):
        new_state = self.mov_pacman(move, state)
        x1, y1, w1 = self.ghost_location(20, new_state)
        new_state = self.mov_ghost(self.min_dis(x1, y1, new_state), 20, new_state)

        x2, y2, w2 = self.ghost_location(30, new_state)
        new_state = self.mov_ghost(self.min_dis(x2, y2, new_state), 30, new_state)

        x3, y3, w3 = self.ghost_location(40, new_state)
        new_state = self.mov_ghost(self.min_dis(x3, y3, new_state), 40, new_state)

        x4, y4, w4 = self.ghost_location(50, new_state)
        new_state = self.mov_ghost(self.min_dis(x4, y4, new_state), 50, new_state)

        return list_to_tuple(new_state)

    def goal_test(self, state):
        """ given a state, checks if this is the goal state, compares to the created goal state"""
        for i, row in enumerate(state):
            for j, number in enumerate(row):
                # the board still contain food or pacman was eaten
                if number % 10 == 1 or number == 88:
                    return False
        # food not found
        return True

    def h(self, node):
        """ This is the heuristic. It get a node (not a state)
        and returns a goal distance estimate"""
        counter = 0
        for inner_list in node.state:
            for val in inner_list:
                if (val % 10 == 1) and (val != 99 and val != 77):
                    counter = counter + 1
        return counter


def create_pacman_problem(game):
    print("<<create_pacman_problem")
    """ Create a pacman problem, based on the description.
    game - matrix as it was described in the pdf file"""
    return PacmanProblem(game)

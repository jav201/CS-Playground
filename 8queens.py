import timeit

class board(object):

    def __init__(self):
        self.board = [['-' for x in range(8)] for y in range(8)]
        self.queens_positions = []
        self.unattacked_positions = self.get_unattacked_positions()

    def reset_board(self):
        self.board = [['-' for x in range(8)] for y in range(8)]

    def print_board(self):
        # Pretty print a rudimentary chess board
        for line in self.board:
            for space in line:
                print('[{0}] '.format(space),end='')
            print('\n')

    def set_piece(self,x,y):
        # Set the queen in a valid place or return 'INVALID' warning
        space = self.board[x][y]
        if space == '-':
            self.board[x][y] = 'Q'
            self.queens_positions.append([x,y])
        else:
            print('INVALID')
        self.cancel_out()

    def detect_diagonal(self,x,y):
        # Return a diagonal set of coordinates negative rate
        x_listf = [x for x in range(x,8)]
        y_listf = [y for y in range(y,8)]
        x_listb = [x for x in range(x-1,-1, -1)]
        y_listb = [y for y in range(y-1,-1, -1)]
        f_list = [[x,y] for x,y in zip(x_listf, y_listf)]
        b_list = [[x,y] for x,y in zip(x_listb, y_listb)]
        return (f_list + b_list)

    def detect_diagonal2(self,x,y):
        # Return a diagonal set of coordinates positive rate
        x_listf = [x for x in range(x,-1,-1)]
        y_listf = [y for y in range(y,8)]
        x_listb = [x for x in range(x+1,8)]
        y_listb = [y for y in range(y-1,-1, -1)]
        f_list = [[x,y] for x,y in zip(x_listf, y_listf)]
        b_list = [[x,y] for x,y in zip(x_listb, y_listb)]
        return(f_list + b_list)
    
    def cancel_out(self):
        # Cancel spaces of the chess board
        for x,y in self.queens_positions:
            for x_, y_ in self.detect_diagonal(x,y) + self.detect_diagonal2(x,y):
                self.board[x_][y_] = 'x'
            self.board[x][:] = ['x']*8
            for i in range(8):
                self.board[i][y] = 'x'
            self.board[x][y] = 'Q'

    def get_unattacked_positions(self):
        out_list = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == '-':
                    out_list.append([i,j])
        return out_list

def queens(obj_board):
    # If all quens placed, print and return the board
    if len(obj_board.queens_positions) == 8:
        obj_board.print_board()
        return obj_board
    # if not... check available pos and set a queen...
    for x,y in obj_board.get_unattacked_positions():
        print(obj_board.get_unattacked_positions())
        print(obj_board.queens_positions)
        obj_board.set_piece(x,y)
        # Save the board with a placed queen
        # THIS DECLARATION ENTERS TO A RECURSIVE SUBLEVEL
        # THAT WILL CREATE BOARDS UNTIL THERE ARE NO MORE UNATTACKED SPACES
        # AND WILL RETURN FALSE IF THERE ARE NOT 8 QUEENS IN PLACE
        # THEN A QUEEN WILL BE REMOVED FROM THE QUEENS PLACED POSITIONS
        # AND THE PREVIOUS BOARD WILL BE BROUGHT FORWARD AND CONTINUE
        # SETTING QUEENS ON ITS UNATTACKED SPACES...
        solution = queens(obj_board)
        # Return the board IF there is a solution...
        if solution:
            return solution
    # When there are no more available spaces and no solution
    # the last placed queen gets removed from the position list
    # and the previous saved boeard gets used!!!!
    print(obj_board.queens_positions)
    obj_board.queens_positions.pop()
    print(obj_board.queens_positions)
    obj_board.reset_board()
    obj_board.cancel_out()
    return False

obj_board = board()
queens(obj_board)
import random

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #Create the board
        self.board = self.make_new_board()
        self.assign_values_to_board()




        self.dug = set()


    def make_new_board(self):
        # Construct a new board based on the dim size and num bombs

        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # Generate a new board


        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row] [col] == '*':
                # This means we've actually planted a bomb there already so keep going
                continue

            board[row] [col] = '*' 
            # plant the bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this is already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col+1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right:(row+1, col+1)

        # make sure to not go out of bounds

        num_neighboring_bombs = 0
        for r in range(max(row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size - 1, col+1)+1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs


    def dig(self, row, col):
        # dig at that location!
        # return True if succesful dig, False if bomb dug

        # a few scenarios:
        # hit a bomb (game over)
        # dig at location with neighboring bombs (finish dig)
        # dig at location with no neighboring bombs (dig neighbors)

        self.dug.add((row, col))    # keep track that we dug here
        
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        




#play the game
def play(dim_size = 10, num_bombs = 10):
    


    # Step 1: Create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: Show the user the board and ask for where they want to dig
    # Step 3: If location is a bomb, show game over message
    # Step 4: If location is not a bomb, dig recursively until each square is at
    #   next to a bomb 
    # Step 5: Repeat step 2, 3 and 4 until there are no more places to dig(You win)
    pass
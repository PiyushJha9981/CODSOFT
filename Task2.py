import math

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # 3x3 board
        self.current_winner = None  # Track the winner!

    def print_board(self):
        # Print the board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        # Return list of available spots on the board
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        # Assign square to letter on the board, then return if win
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Winner if 3 in a row anywhere, check row/col/diags
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in col]):
            return True
        if square % 2 == 0:
            # Check diagonals
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X"  # Starting letter
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("")

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter  # Ends the loop and exits the game

            letter = "O" if letter == "X" else "X"  # Switch player

    if print_game:
        print("It's a tie!")

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val

class GeniusComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = 0  # Choose a random corner
        else:
            # Use minimax to find the best move
            _, square = self.minimax(game, self.letter)
        return square

    def minimax(self, state, player, alpha=-math.inf, beta=math.inf):
        max_player = self.letter  # AI is max player
        other_player = "O" if player == "X" else "X"

        # Base case: previous move is a winner
        if state.current_winner == other_player:
            return (
                1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1),
                None
            )
        elif not state.empty_squares():
            return (0, None)

        if player == max_player:
            best = (-math.inf, None)
        else:
            best = (math.inf, None)

        for possible_move in state.available_moves():
            # Try move
            state.make_move(possible_move, player)
            sim_score, _ = self.minimax(state, other_player, alpha, beta)
            # Undo move
            state.board[possible_move] = " "
            state.current_winner = None

            if player == max_player:
                if sim_score > best[0]:
                    best = (sim_score, possible_move)
                alpha = max(alpha, sim_score)
                if beta <= alpha:
                    break  # Alpha-beta pruning
            else:
                if sim_score < best[0]:
                    best = (sim_score, possible_move)
                beta = min(beta, sim_score)
                if beta <= alpha:
                    break  # Alpha-beta pruning

        return best

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    t = TicTacToe()
    x_player = HumanPlayer("X")
    o_player = GeniusComputerPlayer("O")
    play(t, x_player, o_player, print_game=True)
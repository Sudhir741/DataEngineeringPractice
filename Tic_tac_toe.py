import numpy as np

# Initialize the board
board = np.full((3, 3), ' ')

# Print the board
for row in board:
    print('|'.join(row))
    print('-' * 5)

# Main game loop
current_player = 'X'
game_over = False

while not game_over:
    for row in board:
        print('|'.join(row))
        print('-' * 5)
    
    row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
    col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
    
    if board[row, col] == ' ':
        board[row, col] = current_player
        
        # Check for a win
        win = False
        for i in range(3):
            if all([cell == current_player for cell in board[i, :]]) or all([cell == current_player for cell in board[:, i]]):
                win = True
        if all([board[i, i] == current_player for i in range(3)]) or all([board[i, 2 - i] == current_player for i in range(3)]):
            win = True
        
        if win:
            for row in board:
                print('|'.join(row))
                print('-' * 5)
            print(f"Player {current_player} wins!")
            game_over = True
        else:
            # Check for a draw
            draw = True
            for row in board:
                for cell in row:
                    if cell == ' ':
                        draw = False
            if draw:
                for row in board:
                    print('|'.join(row))
                    print('-' * 5)
                print("It's a draw!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("Cell already taken, try again.")

print("Game over!")

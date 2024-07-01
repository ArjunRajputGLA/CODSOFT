
#! TIC-TAC-TOE AI

#? Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player. You can use algorithms like Minimax with or without Alpha-Beta Pruning to make the AI player unbeatable. This project will help you understand game theory and basic search algorithms.


import numpy as np

board = np.full((3, 3), ' ')
print() 
def print_board(board):
    for i, row in enumerate(board):
        print(f"{i+1}  " + ' | '.join(row))
        if i < 2:
            print("  ------------")
    print("\n    1   2   3")

def is_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i, :]]) or all([cell == player for cell in board[:, i]]):
            return True
    if all([board[i, i] == player for i in range(3)]) or all([board[i, 2-i] == player for i in range(3)]):
        return True
    return False

def is_draw(board):
    return all([cell != ' ' for row in board for cell in row])

def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, 'X'):
        return -1
    if is_winner(board, 'O'):
        return 1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == ' ':
                    board[i, j] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i, j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = np.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == ' ':
                    board[i, j] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i, j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

def best_move(board):
    best_score = -np.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i, j] == ' ':
                board[i, j] = 'O'
                score = minimax(board, 0, False, -np.inf, np.inf)
                board[i, j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    while True:
        print_board(board)
        
        # Human move
        user_input = input("Enter your move (row <space> column, 1-3) or 'q' to quit: ")
        if user_input.lower() == 'q':
            print("Thanks for playing! Goodbye.")
            break
        
        try:
            row, col = map(int, user_input.split())
            row -= 1
            col -= 1
            if not (0 <= row < 3 and 0 <= col < 3):
                print("Invalid move! Row and column must be between 1 and 3.")
                continue
            if board[row, col] != ' ':
                print("Invalid move! The cell is already occupied.")
                continue
        except ValueError:
            print("Invalid input! Please enter row and column as two integers separated by space.")
            continue
        
        board[row, col] = 'X'
        
        if is_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # AI move
        move = best_move(board)
        if move:
            board[move[0], move[1]] = 'O'
        
        if is_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

play_game() 
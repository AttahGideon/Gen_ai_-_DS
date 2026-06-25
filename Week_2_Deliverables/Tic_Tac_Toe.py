# Create board
def create_board(board):
    print(f'\n{board[0]} | {board[1]} | {board[2]}\n---+---+---\n{board[3]} | {board[4]} | {board[5]}\n---+---+---\n{board[6]} | {board[7]} | {board[8]} ')

# win combinations
def check_win(board, player):
    win_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a,b,c in win_combinations:
        if board[a] == board[b] == board[c] ==player: return True
    return False

#for a tie
def is_tie(board):
    return ' ' not in board

#Minimax algorithm for AI decision making
def minimax(board, is_ai_turn, ai_player, user):
    if check_win(board, ai_player):
        return 1   #Ai wins
    if check_win(board, user):
        return -1  #user wins
    if is_tie(board):
        return 0   #tie
    
    scores = []
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai_player if is_ai_turn else user 

            score = minimax(board, not is_ai_turn, ai_player, user)
            scores.append(score)

            board[i]= ' '
    return max(scores) if is_ai_turn else min(scores)


 #user choice nd execution
def play_game():
    board = [' '] * 9
    print('Welcome to Tic-Tac-Toe!')
    create_board([str(i) for i in range(9)])

    # User picks character
    user = ' '
    while user not in ['X', 'O']:
        user = input('What Character do you pick ? X or O (X goes first):').upper()

    #assigning the AI the leftover charcter 
    ai_player = 'O' if user == 'X' else 'X'
    print(f'You are {user}. THe AI is {ai_player}')


    #Turn Logic
    #X should go on even turns, O on odd
    for turn in range(9):
        turn_marker = 'X' if turn % 2 == 0 else 'O'

        #user turn
        if turn_marker == user:
            valid_move = False
            while not valid_move:
                try:
                    move = int(input(f'Your turn {user}. Enter move (0-8)'))
                    if move < 0 or move > 8 or board[move] != ' ':
                        print('invalid move, try again')
                    else:
                        board[move] = user
                        valid_move = True
                except ValueError:
                    print('please type a valid number')

            create_board(board)
            if check_win(board, user):
                return print('you win! (wait, how ??)')
            

             #ai turn
        else:
            print(f"AI ({ai_player}) is calculating...")
            best_score = -float('inf')
            best_move = 0
            
            for i in range(9):
                if board[i] == ' ':
                    board[i] = ai_player
                    score = minimax(board, False, ai_player, user)
                    board[i] = ' '
                    
                    if score > best_score:
                        best_score = score
                        best_move = i
            
            board[best_move] = ai_player
            create_board(board)
            if check_win(board, ai_player): return print("AI wins! Better luck next time.")

    print("It's a tie!")

play_game()

   
    
    


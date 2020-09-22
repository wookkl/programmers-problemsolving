def solution(board):
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i-1][j-1] and board[i-1][j] and board[i][j-1] and board[i][j]:
                if board[i-1][j-1] == board[i-1][j] == board[i][j-1]:
                    board[i][j]=board[i-1][j]+1
                else:
                    board[i][j] = min(board[i-1][j-1],board[i-1][j],board[i][j-1])+1
    return max(map(max, board))**2
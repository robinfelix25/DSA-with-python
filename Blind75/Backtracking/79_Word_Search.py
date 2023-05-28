
'''
need to look for the word variable i, bcz it valuates when the exiting
'''
def exist_sol1(board, word):
    ROWS, COLS = len(board), len(board[0])
    visited  =set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        
        if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS or
            word[i] != board[r][c] or
            (r,c) in visited):
            return False
        
        visited.add((r,c))
        res = (dfs(r+1, c, i +1) or
               dfs(r-1, c, i +1) or
               dfs(r, c+1, i +1) or
               dfs(r, c-1, i +1))
        visited.remove((r,c))
        return res
    
    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0): return True
        
    return False

#reference solution
def backtracking(i, j,word,board):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return False
        if board[i][j] == word[0]:
            board[i][j] = "~"
            if (backtracking(i+1, j, word[1:],board) or 
                backtracking(i-1, j, word[1:],board) or 
                backtracking(i, j+1, word[1:],board) or 
                backtracking( i, j-1, word[1:],board)):
                return True
            board[i][j] = word[0]
        return False

def exist_sol2(board, word):
    for i in range(len(board)):
            for j in range(len(board[i])):
                if backtracking(i, j,word,board):
                    return True
    return False
#reference solution
'''
https://leetcode.com/problems/word-search/solutions/2439953/python-faster-than-98-w-proof-easy-to-understand/
'''

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = 'ABCCED'

board = [["A","C"],["B","D"]]
word = "AB"
print(exist_sol1(board, word))
print(exist_sol2(board, word))
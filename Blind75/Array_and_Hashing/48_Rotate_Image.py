
'''
Interesting question, need to get back here
'''

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def rotatematrix(matrix):
    """
    challenge is we need to do it in-place
    """
    l, r = 0, len(matrix) - 1
    
    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            topLeft = matrix[l][l + i]
            matrix[l][l + i] = matrix[r - i][l]
            matrix[r - i][l] = matrix[r][r - i]
            matrix[r ][r - i] = matrix[l +i][r]
            matrix[l+i][r] = topLeft
        l += 1
        r -= 1
    
    print(matrix)

rotatematrix(matrix)
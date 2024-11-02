def NQueens(n):
    column = set()
    positive_diagonal = set() # r+c
    negative_diagonal = set() # r-c
    
    res = []
    board = [["."]*n for i in range(n)]
    
    def backTrack(r):
        if r==n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in column or r-c in negative_diagonal or r+c in positive_diagonal:
                continue
            column.add(c)
            negative_diagonal.add(r-c)
            positive_diagonal.add(r+c)
            board[r][c] = "Q"
            
            backTrack(r+1)
            
            column.remove(c)
            positive_diagonal.remove(r+c)
            negative_diagonal.remove(r-c)
            board[r][c] = "."
    backTrack(0)
    print(res)
NQueens(8)

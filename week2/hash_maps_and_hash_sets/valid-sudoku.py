class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        index = (0,3,6)
        for x in board:
            r = set()
            for i in x:
                if i in r:
                    # print(1)
                    return False
                elif i !='.':
                    r.add(i)
        
        for i in range(0,9):
            r = set()
            for x in board:
                if x[i] in r:
                    # print(2)
                    return False
                elif x[i] !='.':
                    r.add(x[i])
                    
        for x in index:
            for y in index:
                r = set()
                for i in range(x,x+3):
                    for j in range(y,y+3):
                        a = board[i][j]               
                        if a in r:
                            # print(3)
                            return False
                        elif a !='.':
                            r.add(a)
                            
        return True
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #valid row :

        for i in range(9):
            seen = set()
            for j in range(9):
                c = board[i][j]
                if c in seen :
                    return False 
                elif c != '.' :
                    seen.add(c)

        #valid column 

        for i in range(9):
            seen = set()
            for j in range(9):
                c = board[j][i]
                if c in seen:
                    return False 
                elif c != '.':
                    seen.add(c)
        
        #valid box 

        starts = [(0,0) , (0,3) , (0,6) ,
                  (3,0) , (3,3) , (3,6) ,
                  (6,0) , (6,3) , (6,6)]
        
        for i , j in starts:
            seen = set()
            for row in range(i , i + 3):
                for col in range(j , j + 3):
                    c = board[row][col]
                    if c in seen:
                        return False 
                    elif c != '.':
                        seen.add(c)
        
        return True 
        
s = Solution()
board = [] 
for i in range(9):
    row = [] 
    for j in range(9):
        row.append(input())
    board.append(row)

print(s.isValidSudoku(board))


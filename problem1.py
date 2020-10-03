#Problem Statement:
#Given a 2D board and a word, find if the word exists within the grid. The word can be constructed
#from letters of sequentially adjacent cells, where "adjacent" cells are those horizontally or vertically
#neighbouring. The same letter cell may not be used more than once.

class Problem1:
    def word_search(board, word):
        W = len(board[0]) #width of the board
        H = len(board) #height of the board
        P = len(word) #length of the word

        def check(i,j,pos):
            if pos >= P:
                return True
            elif 0 <= i<H and 0 <=j<W and board[i][j] == word[pos]:
                temp = board[i][j]
                board[i][j] = None
                #check - up, down, left, right
                if check(i-1,j,pos+1) or check(i+1,j,pos+1) or check(i,j-1,pos+1) or check(i,j+1,pos+1):
                    return True
                board[i][j] = temp
            return False

        for i in range(H):
            for j in range(W):
                if check(i,j,0):
                    return True
        return  False

if __name__=="__main__":
    #Test Case
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    testcase = Problem1.word_search(board,'SEE')
    print(testcase)

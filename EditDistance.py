'''
In this lab we had to solve the problem of Edit Distance by using dynamic programming. I added comments to the implementation
in order for better understanding.
'''




def EditDistance(word1, word2):
    w1 = len(word1) + 1 #you have to increase by one since we havce to include the empty space ""
    w2 = len(word2) + 1 #you have to increase by one since we havce to include the empty space ""
    matrix = [[0 for _ in range(w2)] for _ in range(w1)]

    #fill up the first column and first row
    for i in range(w1):
        matrix[i][0] = i
    for j in range(w2):
        matrix[0][j] = j

    #checking the matrix
    for i in range(1, w1):
        for j in range(1, w2):

            #if the subword is not the same from the subword from word2
            if word1[i - 1] != word2[j - 1]:
                matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + 1) #grabs the minimunm of the adjacent 3 numbers
            else:
                matrix[i][j] = matrix[i - 1][j - 1] #else it grabs the number that is diagonal from it.

    #returns the last index of the matrix
    return matrix[-1][-1]
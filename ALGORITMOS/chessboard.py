mat = []

for _ in range(8):
    mat.append(list(input()))

diagonal_left = [False for _ in range(15)]
diagonal_right = [False for _ in range(15)]
rows = [False for _ in range(8)]
cont = 0

def placeQueens(currCol):
    global cont
    if (currCol == 8):
        cont += 1
        return
    for irow in range(8):
        if (mat[irow][currCol] == ".") and (not diagonal_left[irow - currCol + 7]) and (not diagonal_right[irow + currCol]) and (not rows[irow]):
            diagonal_left[irow - currCol + 7] = True
            diagonal_right[irow + currCol] = True
            rows[irow] = True
            placeQueens(currCol + 1)
            diagonal_left[irow - currCol + 7] = False
            diagonal_right[irow + currCol] = False
            rows[irow] = False

placeQueens(0)

print(cont)
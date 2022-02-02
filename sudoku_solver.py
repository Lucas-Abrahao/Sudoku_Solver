def movimento_valido(grid, linha, coluna, num):
    
    for x in range(9):                          #Verifica se o número pode ser inserido na coluna
        if grid[linha][x] == num:
            return False

    for x in range(9):                          #Verifica se o número pode ser inserido na linha
        if grid[x][coluna] == num:
            return False 

    canto_linha = linha - linha % 3             #Definindo os Quadrados do Sudoku
    canto_coluna = coluna - coluna % 3

    for x in range(3):                          #Verifica se o Número pode ser inserido no Quadrado
        for y in range(3):
            if grid[canto_linha + x][canto_coluna + y] == num:
                return False

    return True

def solucao(grid, linha, coluna):

    if coluna == 9:                             #Verificando se chegou ao final 
        if linha == 8:
            return True 

        linha += 1 
        coluna = 0

    if grid[linha][coluna] > 0:                 #Corrigindo Sobreposição de valores
        return solucao(grid, linha, coluna +1)

    for num in range(1, 10):                    #Tentando todos os números possíveis, forçando o Sudoku

        if movimento_valido(grid, linha, coluna, num):
            
            grid[linha][coluna] = num

            if solucao(grid, linha, coluna + 1): #Verifica se está solucionado
                return True

        grid[linha][coluna] = 0                  #Caso não ache um número válido

    return False

grid = [[2, 6, 0, 0, 0, 3, 0, 1, 5],
        [4, 7, 0, 0, 0, 0, 0, 0, 8],
        [5, 8, 1, 0, 0, 4, 7, 6, 3],
        [0, 3, 0, 4, 8, 9, 0, 7, 0],
        [0, 0, 6, 0, 0, 2, 8, 3, 0],
        [0, 0, 8, 3, 1, 0, 0, 0, 0],
        [6, 9, 0, 0, 0, 8, 0, 0, 7],
        [3, 0, 0, 0, 9, 0, 2, 0, 0],
        [0, 1, 0, 5, 0, 0, 0, 9, 6]]

if solucao(grid, 0, 0):                         #Imprime o Sudoku Completo 
    for i in range(9):
        for j in range(9):

            print(grid[i][j], end = ' ')

        print()

else:

    print('Sem Solução para este Sudoku')
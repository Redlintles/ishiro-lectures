import numpy as np

def ex1():
    '''
        Crie um array NumPy com os números de 1 a 10.
    '''
    arr = np.array([x for x in range(1,11)])
    for i in arr:
        print(i)
def ex2():
    '''
        Crie um array NumPy 2D com 5 linhas e 3 colunas preenchido com zeros.
    '''
    arr = np.zeros((5,3))

    for row in arr:
        for col in row:
            print(col)

def ex3():
    '''
        Crie um array NumPy com os números pares de 0 a 10.
    '''
    arr = np.arange(0,10,2)
    for i in arr:
        print(i)

def ex4():
    '''
        Calcule a média dos valores em um array NumPy.
    '''
    arr = np.random.randint(0,100,size = 100)
    avg = np.mean(arr)
    print("Média é ",avg)

def ex5():
    '''
        Crie um array NumPy com 20 números aleatórios entre 0 e 100.
    '''
    arr = np.random.randint(0,100,size = 20)
    for i in arr:
        print(i)
    pass
def ex6(arr):
    '''
        Dado um array NumPy, inverta a ordem dos elementos.
    '''
    rev = arr[::-1]
    for i in rev:
        print(i)
def ex7():
    '''
        Dado um array NumPy, substitua todos os números ímpares por -1.
    '''
    def replaceOdd(x):
        if x % 2 != 0:
            return -1
        else:
            return x
    arr = np.random.randint(0,100,size=20)
    vectorized = np.vectorize(replaceOdd)
    result = vectorized(arr)
    for i in result:
        print(i)

def ex8():
    '''
        Crie uma matriz de identidade 3x3 usando NumPy.
    '''
    arr = np.array([np.random.randint(0,10,size=3) for x in range(3)])

    for row in arr:
        for col in row:
            print(col)
        print("\n")
def ex9():
    '''
        Dado um array NumPy, normalize os valores para o intervalo [0, 1].
    '''
    arr = np.array([x for x in range(0,11)])
    normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
    for x in normalized:
        print(x)
def ex10():
    '''
        Dado um array NumPy 2D, calcule a soma das linhas e das colunas separadamente.
    '''
    arr= np.array(
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
    )

    rowSum = []
    colSum = []
    for row in arr:
        rowSum.append(sum(row))
    for col in range(arr.shape[1]):
        act_col = arr[:, col]
        colSum.append(sum(act_col))
    
    for i in range(3):
        print(f"Soma da linha {i+1}: {rowSum[i]}")
        print(f"Soma da coluna {i+1}: {colSum[i]}")

def ex11(arr1,arr2):
    '''
        Implemente a multiplicação de duas matrizes usando NumPy.
    '''
    result = np.dot(arr1,arr2)
    for row in result:
        print(row)
def ex12(arr1):
    '''
        Dado um array NumPy, encontre os índices dos valores máximos e mínimos.
    '''
    maxVal = np.where(arr1 == np.max(arr1))
    minVal = np.where(arr1 == np.min(arr1))
    print(maxVal[0][0],maxVal[1][0])
    print(minVal[0][0],minVal[1][0])
def ex13(arr1):
    '''
        Dado um array NumPy, remova todos os valores duplicados.
    '''
    uniques = np.unique(arr1).tolist()    
    for i in uniques:
        print(i)
        
    pass
def ex14(arr1,arr2):
    '''
        Crie uma função que receba como entrada dois arrays NumPy e calcule a distância Euclidiana entre eles.
    '''
    de = np.linalg.norm(arr1-arr2)
    print(de)
def ex15(arr1):
    '''
        Dado um array NumPy 2D, encontre os valores únicos em cada linha e troque as repetições por zero
    '''
    def unique(row):
        r = np.unique(row).tolist()
        while len(r) < arr1.shape[0]:
            r.append(0)
        return r
            
    result = np.apply_along_axis(unique,axis=1,arr=arr1)
    print(result)

# ex1()
# ex2()
# ex3()
# ex4()
# ex5()
# ex6(np.array([1,2,3,4,5]))
# ex7()
# ex8()
# ex10()
# ex11(np.array([[1,2],[3,4]]),np.array([[5,6],[7,8]]))
# ex12(np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]))
# ex13(np.array([
#     [1,1,1],
#     [1,1,1],
#     [1,1,1]
# ]))
# ex14(np.array([[1,2,3],[4,5,6],[7,8,9]]),np.array([[1,1,3],[4,5,6],[7,8,9]]))
# ex15(np.array([[2,2,2],[5,5,6],[7,8,9]]))
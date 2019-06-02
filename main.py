import numpy as np

f = open('A.txt', 'r')
mat = f.read()
print(mat)

mat = mat.split('\n')

for i in range(len(mat)):
  if(mat[i] != ''):
    mat[i] = mat[i].split(" ")
  else:
    del mat[i]

tamMat = len(mat)
matriz = []

for k in range (tamMat):
  matriz.append([0]*tamMat)
  for i in range(tamMat):
    matriz[k][i] = 0

for i in range (tamMat):
  for j in range (tamMat):
    matriz[i][j] = int(mat[i][j])

print("\n-*MATRIZ DO GRAFO*-")
print(matriz)

print("\n-*DESCOBRINDO CAMINHOS ENTRE VÉRTICES*-")
matrPow = np.linalg.matrix_power(matriz, tamMat)
print(matrPow)

conexo = 0;
for i in range (tamMat):
  for j in range (tamMat):
    if(matrPow[i][j] == 0):
      conexo +=1

grauImpar =0
for i in range (tamMat):
  for j in range(tamMat):
    if (matriz[i][j] % 2 != 0):
      grauImpar+=1

if (conexo == 0 and grauImpar == 0):
  print("\nO grafo É euleriano")
  print("\n\t pois é conexo e é composto somente de graus pares")
else:
  print("\nO grafo NÃO É euleriano")

if (conexo == 0 and grauImpar == 2):
  print("\nO grafo é semi-euleriano")
  print("\n\t pois é conexo e tem exatamente dois graus ímpares")


if conexo > 0:
  print("\n\tO grafo NÃO É conexo")
else:
  print("\n\tO grafo É conexo")

if grauImpar>0:
  print("\n\tO grafo possui graus ÍMPARES")
else:
  print("\n\tO grafo possui somente graus PARES")
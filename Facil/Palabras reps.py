
#LINK https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter

n = int(input())
tamano_zapato = list(map(int, input().split()))
inventario = Counter(tamano_zapato)
m = int(input())
ganancias = 0

for _ in range(m):
    size, price = map(int, input().split())
    if inventario[size] > 0:
        inventario[size] -= 1
        ganancias += price

print(ganancias)
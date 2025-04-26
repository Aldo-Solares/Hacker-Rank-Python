
#LINK Dada una lista de números, determinar en qué lugar de cada número, manteniendo el orden original de entrada.

lista = [8, 4, 3, 22, 9, 88, 19, 2, 1, 222]

ordenados = sorted((valor, posición) for posición, valor in enumerate(lista))

lista_posiciones = [0] * len(lista)

for lugar, (valor, posición) in enumerate(ordenados, start=1):
    lista_posiciones[posición] = lugar

print(lista_posiciones)

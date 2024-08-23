#função 
calcular_pg = lambda x: x*2

# lista de numeros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# usando a função map para gerar uma lista de progressão
pg = list(map(calcular_pg, numeros))

# exibe a lista
for i in pg:
    print(i)
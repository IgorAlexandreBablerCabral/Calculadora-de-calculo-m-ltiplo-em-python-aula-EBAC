print("Nessa experiencia matematica você irá realizar os calculos de:\n - adição\n - subtração\n - multiplicação\n - divisão com a exibição do resto e quociente.\n Essa calculadora, além de exibir quais dos dois números calculados é o maior,\n também exibe um aviso caso seu resultado for maior que 999")
num_1 = float(input("Insira o primeiro número a ser calculado"))
num_2 = float(input("Agora insira o segundo número a ser calculado"))

#Execução de Cálculos em Lista
resultados = [
    num_1 + num_2,  # [0] Soma
    num_1 - num_2,  # [1] Subtração
    num_1 * num_2,  # [2] Multiplicação
    num_1 / num_2,  # [3] Divisão
    num_1 % num_2,  # [4] Resto
    num_1 // num_2, # [5] Quociente
]

# Exibição para usúario

print("Soma: ", resultados[0])
print("Subtração: ", resultados[1])
print("Multiplicação: ", resultados[2])
print("Divisão: ", resultados[3])
print("Resto da divisão: ", resultados [4])
print("Quociente: ", resultados [5])

# Comparação entre os valores digitados

if num_1 > num_2:
    print("O maior número informado foi" , num_1)
elif num_2 > num_1:
    print("O maior número informado foi: ", num_2)
else:
    print("Os números informados são iguais.")

#Verificação se algum resultado é maior que 999 usando Lista
if max(resultados) >999:
    print("Um ou mais valores utrapassam 999")
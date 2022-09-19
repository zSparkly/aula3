"""
lista1 = [1,2,3,4,5,6]
print(lista1)
novaLista = lista1 * 2
print(novaLista)

soma = 0
for elemento in novaLista:
    print(elemento)
    soma = soma + elemento
print(soma)
"""

carrinho = []
produto = 's'

while produto!= "sair":
    print("Adicione o produto ou sair para encerrar: ")
    produto = input()
    if produto!="sair":
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
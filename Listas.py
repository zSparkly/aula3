"""
Listas => vetores, arrays, matrizes
São dinâmicas -

"""

"""
lista1 = [1,2,3,4,5,6,7,8,9,10]
 print(lista1)
 lista1.sort()
 lista1.extend([40, 50, 60])

 lista1.extend(['Senac'])

lista2 = ['S','e','n','a','c',' ','A','A','R','J']
lista3 = []
lista4 = list(range(11))
 lista4.reverse()
 lista4.insert(1,27)

print(lista4)

print(lista4[::-1])

print(lista2)

print(len(lista2))

print(lista2)




lista5 = list("Senac - Programção em Python")
 lista5.reverse()

 print(lista1)

 print(lista5)

 Podemos achar um valor na lista
letra = input("Digite a letra desejado: ")

if letra in lista5:
    print(f"Achei a letra: {letra}")
else:
    print(f"Não achei a letra: {letra}")
"""


"""
mensagem = "Curso de programção em algoritmo em Python"
print(mensagem)
mensagem = ' '.join(mensagem)
print(mensagem)
resultado = mensagem.split("  ")
print(resultado)
"""

texto = "Estava em viagem quando me senti assediada após 10 minutos"
texto = texto.split()


if 'assediada' in texto:
    print("Aviso sobre assédio - suspensão de viagens")


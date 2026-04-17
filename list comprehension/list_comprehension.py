"""
🔹 Fase 1 — Aquecimento (Iniciante)
1.

Crie uma lista com os números de 1 a 10 usando list comprehension.
"""
# lista_numeros = [numero for numero in range(1,11)]
# print(lista_numeros)

"""
2.

Crie uma lista com os números de 1 a 10 ao quadrado.
"""
# lista_numeros_quadrados = [numero ** 2 for numero in range(1,11)]
# print(lista_numeros_quadrados)


"""
3.

Dada a lista:

numeros = [1, 2, 3, 4, 5]

Crie uma nova lista com todos os números dobrados.
"""
# numeros = [1, 2, 3, 4, 5]
# lista_dobrada = [numero * 2 for numero in numeros]
# print(lista_dobrada)

"""
4.

Dada a lista:

numeros = [1, 2, 3, 4, 5, 6]

Crie uma lista apenas com os números pares.

"""
# numeros = [1, 2, 3, 4, 5, 6]
# numeros_pares = [numero for numero in numeros if numero % 2 == 0]
# print(numeros_pares)

"""
5.

Dada a lista:

nomes = ["ana", "carlos", "joao"]

Crie uma nova lista com os nomes em letras maiúsculas.

"""
# nomes = ["ana", "carlos", "joao"]
# nomes_upper = [nome.upper() for nome in nomes]
# print(nomes_upper)

"""
6.

Dada a lista:

palavras = ["python", "java", "c"]

Crie uma lista com o tamanho de cada palavra.
"""
# palavras = ["python", "java", "c"]
# qtd_caracteres = [len(string) for string in palavras]
# print(qtd_caracteres)

"""
7.

Dada a lista:

numeros = [10, 20, 30, 40]

Crie uma lista dividindo cada número por 2.
"""
# numeros = [10, 20, 30, 40]
# numeros_divididos = [numero / 2 for numero in numeros]
# print(numeros_divididos)

"""
8.

Dada a lista:

nomes = ["Ana", "Carlos", "João", "Be"]

Crie uma lista apenas com os nomes que têm mais de 3 letras.
"""
# nomes = ["Ana", "Carlos", "João", "Be"]
# nomes_com_mais_de_3_caracteres = [nome for nome in nomes if len(nome) > 3]
# print(nomes_com_mais_de_3_caracteres)

"""
9.
Dada a lista:

numeros = [1, 2, 3, 4, 5]

Crie uma lista onde:

números pares → "par"
números ímpares → "impar"
"""
# numeros = [1, 2, 3, 4, 5]
# numeros_par_impar = ["par" if numero % 2 == 0 else "impar" for numero in numeros]
# print(numeros_par_impar)

"""
10.

Dada a lista:

frase = ["olá", "mundo"]

Crie uma lista com cada palavra seguida de "!"
"""
frase = ["olá", "mundo"]
frases = [f"{palavra}!" for palavra in frase]
print(frases)


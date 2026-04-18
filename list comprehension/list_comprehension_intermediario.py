"""
🔹 Fase 2 — Intermediário (onde começa a ficar interessante)

Agora eu quero ver se você realmente domina.
"""

"""
1.

Dada a lista:

numeros = [1, 2, 3, 4, 5, 6]

Crie uma lista com:

número par → número * 2
número ímpar → número * 3
"""
# numeros = [1, 2, 3, 4, 5, 6]

# numeros_par_impar = [numero * 2 if numero % 2 == 0 else numero * 3 for numero in numeros]
# print(numeros_par_impar)

"""
2.

Dada a lista:

palavras = ["python", "java", "javascript", "c"]

Crie uma lista apenas com palavras que têm mais de 4 letras, em maiúsculo.
"""
# palavras = ["python", "java", "javascript", "c"]
# filtro_maiusculo = [palavra.upper() for palavra in palavras if len(palavra) > 4]
# print(filtro_maiusculo)

"""
3.

Dada a lista:

numeros = [10, 15, 20, 25, 30]

Crie uma lista apenas com números que são divisíveis por 5 e por 2 ao mesmo tempo.

"""
# case 1
# numeros = [10, 15, 20, 25, 30]
# divisores_2_5 = [numero for numero in numeros if numero % 2 == 0 and numero % 5 == 0]
# print(divisores_2_5)

"""
4.

Dada a lista:

nomes = ["Ana", "Carlos", "João", "Amanda"]

Crie uma lista com:

nomes que começam com "A" → "Aprovado"
resto → "Reprovado"

"""
# nomes = ["Ana", "Carlos", "João", "Amanda"]
# iniciando_a = ["Aprovado" if nome.lower().startswith("a") else "Reprovado" for nome in nomes]
# print(iniciando_a)

"""
5.

Dada a lista:

frase = ["python", "é", "muito", "bom"]

Crie uma lista onde cada palavra vira:

palavra com mais de 3 letras → maiúscula
caso contrário → minúscula
"""
# frase = ["python", "é", "muito", "bom"]
# maiscula_minuscula = [palavra.upper() if len(palavra) > 3 else palavra.lower() for palavra in frase]
# print(maiscula_minuscula)

"""
6.

Dada a lista:

numeros = [1, 2, 3, 4, 5]

Crie uma lista com o quadrado apenas dos números ímpares.

"""
# numeros = [1, 2, 3, 4, 5]
# numeros_impares_quadrado = [numero ** 2 for numero in numeros if not numero % 2 == 0]
# print(numeros_impares_quadrado)

"""
7.

Dada a lista:

nomes = ["ana", "carlos", "bia", "joao"]

Crie uma lista com nomes que têm até 4 letras, em maiúsculo.
"""
# nomes = ["ana", "carlos", "bia", "joao"]
# nomes_maisculo = [nome.upper() for nome in nomes if len(nome) <= 4]
# print(nomes_maisculo)

"""
8.

Dada a lista:

valores = [100, 200, 300, 400]

Crie uma lista com:

valores acima de 200 → aplicar 10% de desconto
valores até 200 → manter igual

"""
# def aplicar_desconto(valor, desconto):
#     return valor - (valor * desconto)

# valores = [100, 200, 300, 400]
# valores_com_desconto = [aplicar_desconto(valor, 0.10) if valor > 200 else valor for valor in valores]
# print(valores_com_desconto)

"""
9.

Dada a lista:

numeros = [1, 2, 3, 4, 5]

Crie uma lista de strings assim:

"1 é ímpar"
"2 é par"
...
"""
# numeros = [1, 2, 3, 4, 5]
# lista_par_impar = [f"{numero} é par" if numero % 2 == 0 else f"{numero} é ímpar" for numero in numeros]
# print("\n".join(lista_par_impar))

"""

10. (⚠️ Esse separa os bons)

Dada a lista:

lista = ["123", "abc", "456", "def"]

Crie uma lista apenas com os elementos que são números, convertidos para int.
"""
# def verificar_numero(numero):
#     return all(caracter.isdigit() for caracter in numero)

# lista = ["123", "abc", "456", "def"]
# lista_numeros_convertidos = [int(numero) for numero in lista if verificar_numero(numero)]
# print(lista_numeros_convertidos)



"""Preparação para POO"""

"""
🧪 Exercício 1

Crie uma função que:

recebe um nome
retorna uma saudação

Exemplo esperado:

"Olá, Felipe"
"""
# def saudacao(nome):
#     return f"Boa tarde, {nome}!"

# print(saudacao("Felipe"))

"""
🧪 Exercício 2

Crie uma função que:

recebe um número
retorna o dobro desse número
"""
# def dobrar_numero(numero):
#     return numero * 2
# print(dobrar_numero(3))

"""
🧪 Exercício 3

Crie uma função que:

recebe uma lista de números
retorna a soma de todos eles

👉 (pode usar sum() ou fazer na mão — você escolhe)
"""

# def somar_lista(lista_numeros):
#     somatorio = 0
#     for numero in lista_numeros:
#         somatorio += numero
#     return somatorio

# print(somar_lista([4,3,5,10,12]))

"""
🔥 Agora sim — NÍVEL 2 (subindo o jogo)

Aqui começa a ficar mais parecido com o que você vai usar em POO.

👉 usa all() + lógica
"""

"""
🧪 Exercício 4

Crie uma função que:

recebe uma lista de números
retorna apenas os números pares

👉 Quero ver list comprehension aqui
"""

# def retornar_pares(lista):
#     return [numero for numero in lista if numero % 2 == 0]
# print(retornar_pares([4,6,8,3,1,13]))

"""
🧪 Exercício 5

Crie uma função que:

recebe uma lista de nomes
retorna uma nova lista com nomes que têm mais de 4 letras
"""

# def verificar_nomes(lista, tamanho):
#     return [nome for nome in lista if len(nome) > tamanho]
# print(verificar_nomes(["carlos", "pedro","dudu"], 4))

"""
🧪 Exercício 6

Crie uma função que:

recebe uma senha
retorna True se:
tiver pelo menos 1 letra
tiver pelo menos 1 número

👉 usa any()
"""
# def verificar_numero(senha):
#     return any(caracter.isdigit() for caracter in senha)
# def verificar_letra(senha):
#     return any(caracter.isalpha() for caracter in senha)
# def verificacao(senha, verificacoes):
#     return None if all(verificacao(senha) for verificacao in verificacoes) else "Senha invalida"
# senha_sendo_verificada = verificacao("teste", [verificar_numero, verificar_letra])
# if senha_sendo_verificada is not None:
#     print(senha_sendo_verificada)
# else:
#     print("Senha valida!")

"""
🧪 Exercício 7 (começando a evoluir lógica)

Crie uma função que:

recebe uma lista de números
retorna True se todos forem positivos

👉 usa all()
"""
# def verificar_se_todos_positivos(lista):
#     return all(numero > 0 for numero in lista)
# print(f"Todos os numeros são positivos" if verificar_se_todos_positivos([4,3,6,8,809]) else "Algum numero é negativo")
# print(f"Todos os numeros são positivos" if verificar_se_todos_positivos([4,3,6,-8,809]) else "Algum numero é negativo")

"""
🧪 Exercício 8 (importante)

Crie uma função que:

recebe uma lista de nomes
retorna:
"Todos válidos" se todos tiverem mais de 3 letras
"Nome inválido encontrado" caso contrário
"""
# def verificar_tamanho_nome(nome, tamanho):
#     return len(nome) > tamanho
# def verificar_lista(lista):
#     return all(verificar_tamanho_nome(nome, 3) for nome in lista)
# lista_nomes1 = ["carlos", "pe", "henrique"]
# lista_nomes2 = ["carlos", "pero", "henrique"]
# print("Todos válidos" if verificar_lista(lista_nomes1) else "Nome ínvalido encontrado")
# print("Todos válidos" if verificar_lista(lista_nomes2) else "Nome ínvalido encontrado")



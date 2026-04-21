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

"""
def teste(parametros):
    return None
teste(argumento)
"""
"""argumentos posicionais x argumentos nomeados

# argumentos posicionais

São argumentos que dependem da ordem em que são passados na função.
Se a ordem for alterada, os valores podem ser atribuídos aos parâmetros errados,
gerando resultados incorretos.

# argumentos nomeados

São argumentos onde passamos o nome do parâmetro antes do valor,
criando uma associação direta. Isso permite que a ordem dos argumentos
não importe.

* importante

Podemos misturar argumentos posicionais e nomeados, mas com uma regra:
os argumentos posicionais devem vir antes dos nomeados."""

# # argumento posicional
# def soma(x,y):
#     return f"{x=} {y=} | x + y = {x+y}"
# print(soma(4,6))
# #argumento nomeado
# def subtrair(x,y):
#     return f"{x=} {y=} | x - y = {x-y}"
# print(subtrair(y=7, x=3))
# #argumento posicional e nomeados
# def multiplicar(x,y):
#     return f"{x=} {y=} | x * y = {x*y}"
# print(multiplicar(5,y=3)) # caso valido, pois devemos lembrar caso tenhamos mitura de tipos de argumentos o nâo nomeado deve vir na frente, depois que eu nomeio um argumento todos que virem depois dele devem ser nomeados
# print(multiplicar(y=3, 4)) # caso invalido, pois não podemos colocar um argumetno nomeado e depois um não nomeado o programa não sabe aonde colocar o argumento não nomeado gerando um erro de syntaxError

"""
🧠 Fase única — Argumentos posicionais x nomeados (10 exercícios)
"""

"""
🔹 Exercício 1 (aquecimento)

Crie uma função multiplicar(a, b) e chame ela usando argumentos posicionais.
"""

# def multiplicar(a, b):
#     return a * b
# print(multiplicar(4,7))

"""
🔹 Exercício 2

Use a mesma função, mas agora chame usando argumentos nomeados.
"""
# def multiplicar(a, b):
#     return a * b
# print(multiplicar(a=4, b=7))

"""
🔹 Exercício 3

Crie uma função:

def apresentar(nome, idade):

Chame a função:

uma vez com posicionais
uma vez com nomeados
"""
# def apresentar(nome, idade):
#     return f"Me chamo {nome} é tenho {idade} anos."
# print(apresentar("Felipe", 29))
# print(apresentar(idade=29, nome="Felipe"))

"""
🔹 Exercício 4

Crie uma função:

def cadastro(nome, idade, cidade):

Chame a função usando:

todos posicionais
todos nomeados
mistura dos dois (corretamente)
"""
# def cadastro(nome, idade, cidade):
#     return f"Me chamo {nome}, tenho {idade} anos é moro no {cidade}"
# print(cadastro("Felipe", 29, "Rio de Janeiro"))
# print(cadastro(nome="felipe", idade=29, cidade="Rio de Janeiro"))
# print(cadastro("Felipe", idade=29, cidade="Rio de Janeiro"))

"""
🔹 Exercício 5 (pegadinha leve)

Tente executar:

def teste(a, b, c):
    return a + b + c

teste(a=1, 2, 3)

👉 Pergunta:

Vai dar erro ou não?
Por quê?
"""

"""
Vai dar erro pois os argumentos posicionais devem ser passados antes dos nomeados, sempre que um argumento e nomeado todos depois dele devem ser nomeados, se não gera um syntaxError
"""

"""
🔹 Exercício 6

Corrija o código do exercício anterior para funcionar corretamente.
"""
# def teste(a, b, c):
#     return a + b + c

# print(teste(1, 2, 3))
# print(teste(a=1, b=2, c=3))
# print(teste(1, b=2, c=3))
# print(teste(1, 2, c=3))

"""
🔹 Exercício 7

Crie uma função com valor padrão:

def criar_usuario(nome, ativo=True):

Faça chamadas:

passando só o nome
passando nome + ativo como nomeado
"""

# def criar_usuario(nome, ativo=True):
#     if ativo:
#         return f"Usuario já cadastrado"
#     return f"Cadastrando {nome}"

# print(criar_usuario("felipe", False))
# print(criar_usuario("felipe", ativo=True))
# print(criar_usuario("felipe"))

"""
🔹 Exercício 8

Crie uma função:

def pedido(produto, quantidade, urgente=False):

Chame de 3 formas diferentes:

só posicionais
mistura
usando nomeados pra deixar mais claro
"""
# def pedido(produto, quantidade, urgente=False):
#     if urgente:
#         return f"{produto} - {quantidade} *URGENTE"
#     return f"{produto} - {quantidade}"

# print(pedido("calça", 15, True))
# print(pedido("calça", quantidade=15, urgente=False))
# print(pedido(produto="calça", quantidade=15, urgente=True))

"""
🔹 Exercício 9 (nível estágio)

Crie uma função:

def relatorio(titulo, autor, paginas, publicado=True):

👉 Regras:

faça uma chamada difícil de entender usando posicionais
depois refatore usando nomeados para ficar claro
"""
def relatorio(titulo,autor,paginas,publicado=True):
    if publicado:
        return f"LIVRO ANTIGO - {titulo}, {autor}, n° de paginas {paginas}"
    return f"LIVRO NOVO- {titulo}, {autor}, n° de paginas {paginas}"

print(relatorio("Pedro", "Carlos", 45))
print(relatorio("Pedro", "Carlos", 45, False))
print(relatorio("Pedro", "Carlos", 45, publicado=False))
print(relatorio(titulo="Pedro", autor="Carlos", paginas=45, publicado=False))



"""


🔹 Exercício 10 (pensamento crítico — MUITO importante)

Olha essa chamada:

criar_usuario("Felipe", False)

👉 Pergunta:

Isso está claro?
Como você melhoraria usando argumento nomeado?
"""




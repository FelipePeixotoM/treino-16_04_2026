"""
Crie uma função que:

recebe um número x
retorna uma função que:
recebe y
retorna x * y
"""

# def multiplicar(base):
#     total = 0
#     def operacao(usuario):
#         resultado = base * usuario
#         return resultado
#     return operacao
 
# operacao_base_10 = multiplicar(10)
# operacao_base_20 = multiplicar(20)
# print(operacao_base_10(10))
# print(operacao_base_20(10))


"""
🔥 Closures — 10 exercícios (nível básico → leve progressão)

Sem pular etapa. Faz na ordem.

"""


"""
🧪 Exercício 1 (ultra básico)

Crie uma função que:

recebe um número x
retorna uma função que:
recebe y
retorna x + y
"""
# def somar(numero1):
#     def operacao(numero2):
#         return numero1 + numero2
#     return operacao

# somar_10 = somar(10)
# print(somar_10(15))

"""
🧪 Exercício 2

Crie uma função que:

recebe um número
retorna uma função que multiplica qualquer número por esse valor
"""
# def multiplicar(multiplicador):
#     def operacao(multiplicado):
#         return multiplicado * multiplicador
#     return operacao

# multiplicar_por_3 = multiplicar(3)
# print(multiplicar_por_3(10))

"""
🧪 Exercício 3

Crie uma função que:

recebe uma mensagem
retorna uma função que:
imprime essa mensagem
"""
# def receber_mensagem(mensagem):
#     def imprimir():
#         print(mensagem)
#     return imprimir
# dizer_ola = receber_mensagem("Ola mundo!")
# dizer_ola()

"""
🧪 Exercício 4

Crie uma função que:

recebe um nome
retorna uma função que:
recebe outro nome
retorna: "Olá {nome1} e {nome2}"
"""

# def capturar_nome_1(nome1):
#     def pegar_nome_2(nome2):
#         return f"Olá {nome1} e {nome2}"
#     return pegar_nome_2
# pegar_felipe = capturar_nome_1("felipe")
# print(pegar_felipe("carlos"))

"""
🧪 Exercício 5 (começando a fixar)

Crie uma função que:

recebe um número inicial
retorna uma função que:
soma um valor a esse número (sem perder o valor anterior)

👉 dica: precisa “lembrar” do valor
"""
# def calculo_com_acumulador():
#     total = 0
#     def somar(numero):
#         nonlocal total
#         total += numero
#         return total
#     return somar

# calculando = calculo_com_acumulador()
# print(calculando(10))
# print(calculando(10))
# print(calculando(10))

"""
🧪 Exercício 6

Crie uma função que:

começa com uma lista vazia
retorna uma função que:
adiciona elementos nessa lista
retorna a lista atualizada
"""

# def iniciar_lista():
#     lista = list()
#     def adicionar(item):
#         lista.append(item)
#         return lista
#     return adicionar
# lista_iniciada = iniciar_lista()
# lista_iniciada("teste1")
# lista_final = lista_iniciada("teste2")
# print(lista_final)

"""
🧪 Exercício 7

Crie uma função que:

recebe um número limite
retorna uma função que:
recebe um número
retorna True se for maior que o limite
"""

# def criar_limite(limite):
#     def verificar_limite(numero):
#         return numero > limite
#     return verificar_limite
# limite_10 = criar_limite(10)
# print(limite_10(15))
# print(limite_10(9))

"""
🧪 Exercício 8

Crie uma função que:

recebe um texto
retorna uma função que:
verifica se outro texto contém esse texto inicial

Exemplo:

verificar = criar_verificador("py")
print(verificar("python"))  # True
"""
# def receber_texto(texto):
#     def verificar_inicio(string):
#         return string in texto
#     return verificar_inicio

# verificar_texto = receber_texto("felipe")
# print(verificar_texto("fel"))

"""
🧪 Exercício 9

Crie uma função que:

recebe um valor
retorna uma função que:
compara com outro valor
retorna "maior", "menor" ou "igual"
"""
# def comparar_valores(valor):
#     def comparar(valor_comparado):
#         if valor_comparado > valor:
#             return "maior"
#         elif valor_comparado < valor:
#             return "menor"
#         else:
#             return "igual"
#     return comparar

# comparar_10 = comparar_valores(10)
# print(comparar_10(15))
# print(comparar_10(9))
# print(comparar_10(10))

"""
🧪 Exercício 10 (fechamento)

Crie uma função que:

recebe uma lista de números
retorna uma função que:
recebe um número
retorna quantos números da lista são maiores que ele
"""
def receber_lista(lista):
    def verificar_maiores(numero_verificador):
        return len([numero for numero in lista if numero > numero_verificador ])
    return verificar_maiores

lista = [2,4,6,7,15]
verificar_maior_que_5 = receber_lista(lista)
print(verificar_maior_que_5(5))






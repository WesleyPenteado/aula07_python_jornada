# Conteúdo aula - criação e entendimento de funções

# valor_1 = 4
# valor_2 = 6
# valor_4 = 50
# valor_5 = 30
# valor_8 = 0

# def soma(valor_1_para_somar : float, valor_2_para_somar : float = 10) -> float:
#     """
#     uma funcao simples de soma de valores do tipo float que retorna float
#     """
#     resultado_da_soma = valor_1_para_somar + valor_2_para_somar
#     return resultado_da_soma


# valor_3 = soma(valor_1_para_somar=valor_1, valor_2_para_somar=valor_2)  
# valor_6 = soma(valor_4, valor_5)
# valor_7 = soma(valor_8) #10
# valor_10 = soma(0,0) #0

# print(valor_3)
# print(valor_6)
# print(valor_7)
# print(valor_10)


# Exercícios de Funções ----------------------------------------------------------------------

# 1) Calular Média de Valores em uma lista


# from typing import List

# lista_teste = [1,2,3]

# def media_da_lista (lista_1 : list[float]) -> float:
#     '''
#     Função para calcular a média dos valores em uma lista
#     '''
#     resultado = sum(lista_1) / len(lista_1)
#     return resultado

# resultado = media_da_lista(lista_teste)
# print(resultado)

# 2) Filtrar dados acima de um limite


## Usando list comprehension
# def filtrar_dados_acima(n_limite : float, lista : list[float]) -> list:
#     '''
#     Lista para filtrar números acima de um limite
#     '''
#     resultado = [x for x in lista if x > n_limite]
#     return resultado


# lista_01 = [1,10,3,20,50,30,0]
# resultado = filtrar_dados_acima(5, lista_01)
# print(resultado)

## Usando loop for

# def filtrar_dados_acima(n_limite : float, lista : list[float]) -> list:
#     '''
#     Lista para filtrar números acima de um limite
#     '''
#     resultado = []
#     for valor in lista:
#         if valor > n_limite:
#             resultado.append(valor)
#     return resultado

# lista_01 = [1,10,3,20,50,30,0]
# resultado = filtrar_dados_acima(1, lista_01)
# print(resultado)

# 3) Contar valores únicos em uma lista

# def valores_unicos_na_lista (lista : list[float]) -> list[float]:
#     '''
#     Função para selecionar valores únicos em uma lista
#     '''
#     return set(lista)

# lista_01 = [1, 2, 2, 3, 4, 4, 5]
# resultado = valores_unicos_na_lista(lista_01)
# print(resultado)


# 4) Converter celsius para farenheit em uma lista

## Usando loop for

# def converter_lista_de_celsius_em_farenheit(lista : list[float]) -> list[float]:
#     '''
#     Função para converter números de uma lista em celsius para farenheit
#     '''
#     lista_farenheit = []
#     for valor in lista:
#         t_farenheit = ((valor * 9/5) + 32)
#         lista_farenheit.append(t_farenheit)
#     return lista_farenheit

# lista_celsius = [32.5,25,15.5,30,20]

# resultado = converter_lista_de_celsius_em_farenheit(lista_celsius)
# print(resultado)


## Usando list comprehension

# def converter_lista_de_celsius_em_farenheit(lista : list[float]) -> list[float]:
#     return [(valor * 9/5) + 32 for valor in lista]

# lista_celsius = [32.5,25,15.5,30,20]
# resultado = converter_lista_de_celsius_em_farenheit(lista_celsius)
# print(resultado)


# 5) Calcular desvio padrão de uma lista

# import math

# def desvio_padrão_de_lista (lista : list[float]) -> list[float]:
#     '''
#     Função para calcular o desvio padrão de uma lista
#     '''
#     media = sum(lista) / len(lista)
#     variancia =  sum((valor - media)**2 for valor in lista) / len(lista)
#     return math.sqrt(variancia) 

# lista_01 = (5,10,15,20,25,30)
# resultado = desvio_padrão_de_lista(lista_01)
# print(resultado)


# 6) Encontrar valores ausentes em uma sequencia

def encontrar_valores_ausentes(sequencia: list[int]) -> list[int]:
    '''
    Função para encontrar valores ausentes em uma lista
    '''
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

lista01 = [1,2,5,8,10]
resultado = encontrar_valores_ausentes(lista01)
print(resultado)






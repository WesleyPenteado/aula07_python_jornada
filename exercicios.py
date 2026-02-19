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
#     return print(resultado)

# media_da_lista(lista_teste)


# 2) Filtrar dados acima de um limite


# Usando list comprehension
# def filtrar_dados_acima(n_limite : float, lista : list[float]) -> list:
#     '''
#     Lista para filtrar números acima de um limite
#     '''
#     resultado = [x for x in lista if x > n_limite]
#     return print(resultado)


# lista_01 = [1,10,3,20,50,30,0]
# filtrar_dados_acima(5, lista_01)

# 2) Usando loop for
# def filtrar_dados_acima(n_limite : float, lista : list[float]) -> list:
#     '''
#     Lista para filtrar números acima de um limite
#     '''
#     resultado = []
#     for valor in lista:
#         if valor > n_limite:
#             resultado.append(valor)
#     return print(resultado)

# lista_01 = [1,10,3,20,50,30,0]
# filtrar_dados_acima(1, lista_01)


# 3) Contar valores únicos em uma lista

def valores_unicos_na_lista (lista : list[float]) -> list[float]:
    '''
    Função para selecionar valores únicos em uma lista
    '''
    return print(set(lista))

lista_01 = [1, 2, 2, 3, 4, 4, 5]
valores_unicos_na_lista(lista_01)


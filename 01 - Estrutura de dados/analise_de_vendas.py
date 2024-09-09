def analise_vendas(vendas):
    # Calcula o total de vendas
    total_vendas = sum(vendas)
    
    # Calcula a média mensal de vendas
    if len(vendas) > 0:
        media_vendas = total_vendas / len(vendas)
    else:
        media_vendas = 0
    
    # Retorna o total de vendas e a média mensal formatados
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input(" ")
    
    # Converte a entrada em uma lista de inteiros
    vendas = list(map(int, entrada.split(',')))
    
    return vendas

# Obter as vendas do usuário
vendas = obter_entrada_vendas()

# Analisar as vendas e imprimir o resultado
print(analise_vendas(vendas))

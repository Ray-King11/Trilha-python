def produto_mais_vendido(produtos):
    # Contar as ocorrências de cada produto
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    # Encontrar o produto com a maior contagem
    max_produto = None
    max_count = 0
    
    for produto, count in contagem.items():
        if count > max_count:
            max_count = count
            max_produto = produto
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input(" ")
    
    # Converte a entrada em uma lista de strings, removendo espaços extras
    produtos = [produto.strip() for produto in entrada.split(',')]
    
    return produtos

# Obter a lista de produtos do usuário
produtos = obter_entrada_produtos()

# Encontrar e imprimir o produto mais vendido
print(produto_mais_vendido(produtos))
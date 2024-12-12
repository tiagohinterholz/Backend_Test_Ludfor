inventario = {}

def adicionar_produto(nome, categoria, preco, quantidade):
    """Adiciona um novo produto / atualiza a quantidade se já existir."""
    if nome in inventario:
        inventario[nome]['quantidade'] = quantidade
        return f'A quantidade do produto {nome} foi atualizada.\n'
    else:
        novo_produto = {
            'categoria': categoria,
            'preco': preco,
            'quantidade': quantidade
        }
        inventario[nome] = novo_produto
        return f'O produto {nome} foi adicionado ao inventário.\n'

def remover_produto(nome):
    if nome in inventario:
        del inventario[nome]
        return f'O produto {nome} foi removido do inventário.'
    return f'O produto {nome} não foi encontrado no inventário.\n'

def produtos_por_categoria(categoria):

    produtos_da_categoria = []
    for produto, infos in inventario.items():
        if infos['categoria'] == categoria:
            produtos_da_categoria.append(produto)
    if len(produtos_da_categoria) > 0:
        return produtos_da_categoria
    return 'Não há produtos nesta categoria.\n'

def produto_mais_caro():
    if not inventario:
        return 'O inventário está vazio.\n'

    mais_caro = 0
    nome = ''
    for produto, infos in inventario.items():
        if infos['preco'] > mais_caro:
            mais_caro = infos['preco']
            nome = produto

    return f'O produto {nome} é o mais caro e custa R${mais_caro}\n'

def produtos_estoque_min(estoque):

    prod_estoque_min = []
    for produto, infos in inventario.items():
        if infos['quantidade'] < estoque:
            prod_estoque_min.append([produto, infos['quantidade']])
    if len(prod_estoque_min) > 0:
        return (f'Os produtos que foram identificados com menos de {estoque} peças foram os seguintes:\n'
                f'{prod_estoque_min}\n')
    return f'Não há produtos com menos de {estoque} peças.\n'

while True:
    try:
        opcao = int(input('Olá, digite apenas o número da opção selecionada abaixo para trabalhar com o inventário desta loja:\n'
                          'OPÇÃO 1 - ADICIONAR NOVO PRODUTO.\n'
                          'OPÇÃO 2 - REMOVER UM PRODUTO.\n'
                          'OPÇÃO 3 - BUSCAR PRODUTOS POR CATEGORIA.\n'
                          'OPÇÃO 4 - CONSULTAR O PRODUTO MAIS CARO.\n'
                          'OPÇÃO 5 - EXIBIR PRODUTOS ABAIXO DE UM ESTOQUE MÍNIMO\n'
                          'OPÇÃO 6 - DESLOGAR DO SISTEMA\n'))

        if opcao == 1:
            nome = input('Digite o nome do produto:\n')
            categoria = input('Digite a categoria do produto.\n')
            try:
                preco = float(input('Digite o preço do produto:\n'))
                quantidade = int(input('Digite a quantidade do produto:\n'))
                print(adicionar_produto(nome, categoria, preco, quantidade))
            except ValueError:
                print('Preço e quantidade devem ser valores numéricos válidos.\n')

        elif opcao == 2:
            nome = input('Digite o nome do produto:\n')
            print(remover_produto(nome))

        elif opcao == 3:
            categoria = input('Digite a categoria do produto.\n')
            print(produtos_por_categoria(categoria))

        elif opcao == 4:
            print(produto_mais_caro())

        elif opcao == 5:
            try:
                quantidade = int(input('Digite a quantidade mínima que deseja ter de estoque:\n'))
                print(produtos_estoque_min(quantidade))
            except ValueError:
                print('A quantidade deve ser um valor numérico válido.\n')

        elif opcao == 6:
            print('Saindo do sistema...')
            break

        else:
            print('Opção inválida. Por favor, escolha uma opção entre 1 e 6.\n')

    except ValueError:
        print('Entrada inválida. Por favor, digite apenas números.\n')

"""
AREA DE TESTES para validação das funções
adicionar_produto('Camiseta', 'Roupas', 29.99, 10)
print(inventario)
adicionar_produto('Calça Jeans', 'Roupas', 59.99, 5)
print(inventario)
adicionar_produto('Camiseta', 'Roupas', 29.99, 5)
print(inventario)

remover_produto('Camiseta')
print(inventario)

adicionar_produto("Camiseta", "Roupas", 29.99, 28)
adicionar_produto("Meias", "Roupas", 9.99, 100)
adicionar_produto("PS4", "Eletronicos", 929.99, 6)
adicionar_produto("Xbox One", "Eletronicos", 1229.99, 10)

print(produtos_por_categoria('Eletronicos'))
print(produtos_por_categoria('Roupas'))
print(produtos_por_categoria('Acessórios'))

print(produto_mais_caro())
print(produtos_estoque_min(90))
"""
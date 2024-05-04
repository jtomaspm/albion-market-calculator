import json

class Recurso:
    def __init__(self, nome, tiers):
        self.nome = nome
        self.tiers = tiers
    def mostrar_info(self):
        print(f"\nRecurso: {self.nome}, Tiers: {self.tiers}")

    def mostrar_precos(self, tier=None, cidade=None):
        if tier and cidade:
            print(f"\nPreço do recurso '{self.nome}', Tier {tier}, Cidade {cidade}: {self.tiers[tier][cidade]}")
        elif tier:
            print(f"\nPreços do recurso '{self.nome}', Tier {tier}: ", end="")
            for cidade, preco in self.tiers[tier].items():
                print(f"{cidade}: {preco}", end=", ")
            print()  # Adiciona uma nova linha ao final
        elif cidade:
            print(f"\nPreços do recurso '{self.nome}', Cidade {cidade}: ", end="")
            for tier, preco in self.tiers.items():
                print(f"Tier {tier}: {preco}", end=", ")
            print()  # Adiciona uma nova linha ao final
        else:
            for tier, precos in self.tiers.items():
                print(f"\nPreços do recurso '{self.nome}', Tier {tier}: ", end="")
                for cidade, preco in precos.items():
                    print(f"{cidade}: {preco}", end=", ")
                print()  # Adiciona uma nova linha ao final


# Função para carregar recursos a partir de um arquivo JSON
def carregar_recursos():
    recursos = []

    with open("recursos.json", "r") as arquivo:
        data = json.load(arquivo)

        for recurso_data in data:
            nome = recurso_data["nome"]
            tiers = recurso_data["tiers"]
            recurso = Recurso(nome, tiers)
            recursos.append(recurso)

    return recursos

def mostrar_recursos(recursos):
    for recurso in recursos:
        recurso.mostrar_info()

class Item:
    def __init__(self, nome, cidade, recursos_necessarios, taxa_usage_fee):
        self.nome = nome
        self.cidade = cidade
        self.recursos_necessarios = recursos_necessarios
        self.taxa_usage_fee = taxa_usage_fee

    def calcular_custo_total(self):
        total_recursos = 0

        # Itera sobre os recursos necessários do item
        for recurso, quantidade in self.recursos_necessarios.items():
            # Encontra o preço do recurso no tier da cidade
            preco = recursos_disponiveis[0].tiers[self.cidade][recurso]

            # Adiciona o custo do recurso ao custo total
            total_recursos += preco * quantidade

        # Soma a taxa de usage fee ao custo total
        total_recursos += total_recursos * self.taxa_usage_fee

        # Multiplica o custo total por 1.105
        custo_total = total_recursos * 1.105

        return custo_total

    def atualizar_recursos(self, novos_recursos):
        self.recursos_necessarios = novos_recursos
        print(f"\nRecursos do item '{self.nome}' atualizados com sucesso.")

    def atualizar_taxa_usage_fee(self, nova_taxa_usage_fee):
        self.taxa_usage_fee = nova_taxa_usage_fee
        print(f"\nTaxa de utilização do item '{self.nome}' atualizada com sucesso.")

    def mostrar_info(self):
        print(f"\nItem: {self.nome}, Cidade: {self.cidade}, Recursos: {self.recursos_necessarios}, Taxa de Usage Fee: {self.taxa_usage_fee}")


# Exemplo de uso
recursos_disponiveis = carregar_recursos()

# Exemplo de criação de um item
cidade_atual = "ExemploCity"
item_exemplo = Item("Espada Poderosa", cidade_atual, {"Ferro": 10, "Madeira": 5}, 0.03)

while True:
    item_exemplo.mostrar_info()

    print("\n1. Pesquisar Item")
    print("2. Adicionar Item")
    print("3. Remover Item")
    print("4. Atualizar Preço dos Recursos")
    print("5. Atualizar Taxa de Usage Fee do Item")
    print("6. Mostrar Recursos Disponíveis")
    print("7. Sair")

    escolha = input("\nEscolha uma opção (1-8): ")

    if escolha == "1":
        nome_item_pesquisar = input("Digite o nome do item a pesquisar: ")
        if item_exemplo.nome == nome_item_pesquisar:
            item_exemplo.mostrar_info()
        else:
            print("Item não encontrado.")

        # Calcular o custo total e mostrar
        custo_total = item_exemplo.calcular_custo_total()
        print(f"Custo Total do Item '{novo_item.nome}': {custo_total}")

    elif escolha == "2":
        nome_novo_item = input("Digite o nome do novo item: ")
        print("Exemplo de formato para novos recursos: {'Steel': 16}{'Planks': 10, 'Cloth': 5}")
        recursos_necessarios_novo_item = eval(input("Digite os novos recursos necessários: "))

        print("Exemplo de formato para a taxa de usage fee: 0.05")
        taxa_usage_fee_novo_item = float(input("Digite a nova taxa de usage fee: "))

        novo_item = Item(nome_novo_item, cidade_atual, recursos_necessarios_novo_item, taxa_usage_fee_novo_item)
        item_exemplo = novo_item
        print(f"\nItem '{novo_item.nome}' adicionado com sucesso.")

        # Calcular o custo total e mostrar
        custo_total = item_exemplo.calcular_custo_total()
        print(f"Custo Total do Item '{novo_item.nome}': {custo_total}")

    elif escolha == "3":
        print(f"\nItem '{item_exemplo.nome}' removido com sucesso.")
        break

    elif escolha == "4":
        mostrar_recursos(recursos_disponiveis)
        nome_recurso = input("Digite o nome do recurso a atualizar: ")
        novo_preco = float(input("Digite o novo preço para o recurso: "))

        for recurso in recursos_disponiveis:
            if recurso.nome == nome_recurso:
                for tier, precos in recurso.tiers.items():
                    for cidade, _ in precos.items():
                        recurso.tiers[tier][cidade] = novo_preco
                print(f"\nPreços do recurso '{recurso.nome}' atualizados com sucesso.")
                break
        else:
            print("Recurso não encontrado.")


    elif escolha == "5":
        nova_taxa = float(input("Digite a nova taxa de usage fee: "))
        item_exemplo.atualizar_taxa_usage_fee(nova_taxa)

    elif escolha == "6":
        mostrar_recursos(recursos_disponiveis)
        filtro_tier = input("Digite o tier para filtrar (ou deixe em branco para ignorar): ")
        filtro_material = input("Digite o material para filtrar (ou deixe em branco para ignorar): ")
        filtro_cidade = input("Digite a cidade para filtrar (ou deixe em branco para ignorar): ")

        for recurso in recursos_disponiveis:
            if (not filtro_tier or filtro_tier in recurso.tiers) and \
                    (not filtro_material or filtro_material == recurso.nome) and \
                    (not filtro_cidade or filtro_cidade in [cidade for tier in recurso.tiers.values() for cidade in
                                                            tier]):
                recurso.mostrar_precos(tier=filtro_tier, cidade=filtro_cidade)


    elif escolha == "7":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1-8).")

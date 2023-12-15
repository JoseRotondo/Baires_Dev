class Pedido:
    def __init__(self, numero, detalhes, status, em_producao):
        self.numero = numero
        self.detalhes = detalhes
        self.status = status
        self.em_producao = em_producao

    def modificar_item(self, item, novo_detalhe):
        if not self.em_producao:
            self.detalhes[item] = novo_detalhe
            print(f"Item {item} modificado com sucesso.")

    def cancelar_pedido(self):
        if not self.em_producao:
            self.status = "Cancelado"
            print("Pedido cancelado com sucesso.")

    def gerar_fatura(self):
        total_itens = sum([detalhe['quantidade'] for detalhe in self.detalhes.values()])
        valor_total = sum([detalhe['valor_unitario'] * detalhe['quantidade'] for detalhe in self.detalhes.values()])

        if total_itens > 1000:
            valor_total *= 1.10
        elif total_itens < 1000:
            valor_total *= 1.05

        print(f"Fatura do Pedido #{self.numero}")
        print("Detalhes do Pedido:")
        for item, detalhe in self.detalhes.items():
            print(f"{item}: {detalhe['quantidade']} unidades - R$ {detalhe['valor_unitario']} cada")

        print(f"\nTotal de Itens: {total_itens}")
        print(f"Valor Total: R$ {valor_total:.2f}")

# Exibe o Meno de Opcoes
def exibir_menu():
    print("\n1. Modificar Itens do Pedido")
    print("2. Cancelar Pedido")
    print("3. Gerar Fatura")
    print("4. Sair\n")

# Itens disponiveis
detalhes_pedido = {
    'item1': {'quantidade': 2, 'valor_unitario': 10.0},
    'item2': {'quantidade': 3, 'valor_unitario': 8.0},
    # Adionar conforme precisar
}

pedido1 = Pedido(numero=1, detalhes=detalhes_pedido, status="Em andamento", em_producao=False)

while True:
    exibir_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        item_modificar = input("Digite o nome do item a ser modificado: ")
        novo_detalhe = {'quantidade': int(input("Nova quantidade: ")), 'valor_unitario': float(input("Novo valor unitário: "))}
        pedido1.modificar_item(item_modificar, novo_detalhe)
    elif escolha == '2':
        pedido1.cancelar_pedido()
    elif escolha == '3':
        pedido1.gerar_fatura()
    elif escolha == '4':
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")

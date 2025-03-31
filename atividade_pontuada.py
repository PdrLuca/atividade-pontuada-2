
import os

os.system("cls || clear")

pratos_escolhidos = []

while True:
    print("""
Código \t Prato \t\t Valor
1 \t Picanha  \t R$ 25,00
2 \t Lasanha \t R$ 20,00
3 \t Strogonoff \t R$ 18,00
4 \t Bife acebolado  R$ 15,00
5 \t Moqueca \t R$ 30,00
6 \t Acarajé \t R$ 10,00
7 \t Sarapatel \t R$ 20,00
Digite o código do prato desejado (ou 0 para finalizar o pedido):
""")

    opcao = input().strip()

    if opcao == "0":
        break

    match opcao:
        case "1" | "2" | "3" | "4" | "5" | "6" | "7":
            nomes = {
                "1": "Picanha",
                "2": "Lasanha",
                "3": "Strogonoff",
                "4": "Bife acebolado",
                "5": "Pão com ovo",
                "6": "Acarajé",
                "7": "Sushi"
            }
            precos = {
                "1": 25.00,
                "2": 20.00,
                "3": 18.00,
                "4": 15.00,
                "5": 5.00,
                "6": 7.00,
                "7": 25.00
            }
            nome_prato = nomes[opcao]
            preco_prato = precos[opcao]
            pratos_escolhidos.append((nome_prato, preco_prato))
            print(f"Você escolheu: {nome_prato} - R$ {preco_prato:.2f}")
        case _:
            print("Código inválido. Por favor, digite um código válido.")
            continue

    continuar = input("Deseja fazer outro pedido? (s/n): ").strip().lower()
    if continuar != "s":
        break

if not pratos_escolhidos:
    print("Nenhum prato foi escolhido. Encerrando o programa.")
else:
    subtotal = sum(preco for _, preco in pratos_escolhidos)
    
    print("Escolha a forma de pagamento:")
    print("1. À vista (10% de desconto)")
    print("2. Cartão de crédito (10% de acréscimo)")
    
    while True:
        forma_pagamento_opcao = input().strip()
        match forma_pagamento_opcao:
            case "1":
                forma_pagamento = "avista"
                break
            case "2":
                forma_pagamento = "cartao"
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")
    
    if forma_pagamento == "avista":
        desconto_ou_acrescimo = -subtotal * 0.10
    elif forma_pagamento == "cartao":
        desconto_ou_acrescimo = subtotal * 0.10
    total = subtotal + desconto_ou_acrescimo

    print("\nResumo do Pedido:")
    for nome_prato, preco_prato in pratos_escolhidos:
        print(f"- {nome_prato}: R$ {preco_prato:.2f}")
    
    print(f"\nSubtotal: R$ {subtotal:.2f}")
    print(f"Forma de pagamento: {'À vista' if forma_pagamento == 'avista' else 'Cartão de crédito'}")
    print(f"{'Desconto' if desconto_ou_acrescimo < 0 else 'Acréscimo'} aplicado: R$ {abs(desconto_ou_acrescimo):.2f}")
    print(f"Total a pagar: R$ {total:.2f}")
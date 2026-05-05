from Roupa import Roupa
from Eletronico import Eletronico
from Carrinho import CarrinhoDeCompras




def exibir_menu():
    print("\n" + "=" * 45)
    print(" 🏪 MENU DA LOJA ONLINE 🏪 ".center(45))
    print("="*45)
    print(" [ 1 ] 👕 Adicionar Roupa")
    print(" [ 2 ] 🔌 Adicionar Eletrônico")
    print(" [ 3 ] 🛒 Ver resumo do Carrinho")
    print(" [ 4 ]  Remover item")
    print(" [ 0 ] 🚪 Sair")
    print("="*45)




def main():
    
    carrinho = CarrinhoDeCompras()
    
    
    print("\n Bem-vindo ao Sistema de gestão da loja!")
    while True:
        exibir_menu()
        opcao = input(" Escolha uma opção: ")
        
        
        if opcao == "1":
            print("\n ----- Cadastranndo Roupa -----")
            nome = input("Nome da roupa: ")
            
            try:
                preco = float(input("Preço: R$ "))
                tamanho = input("Tamanho (P/M/G): ")
                nova_roupa = Roupa(nome, preco, tamanho)
                carrinho.adicionar_produto(nova_roupa)

            except ValueError:
                print("Erro: por favor, digite um valor numerico válido para o preço")
                
        elif opcao == "2":
            print("\n ---- Cadastrado Eletrônico -----")
            nome = input(" nome do eletrônico: ")
        
            try:
                preco = float(input("Preco: R$ "))
                voltagem = input("Voltagem (120V/220V) ")
                novo_eletronico = Eletronico(nome, preco, voltagem)
                carrinho.adicionar_produto(novo_eletronico)
                
            except ValueError:
                print("Erro: por favor, digite um valor numerico válido para o preço")
            
        elif opcao == "3":
            carrinho.exibir_resumo()
            
        elif opcao == "4":
            nome = input("qual produto quer remover ")
            carrinho.remover_produto(nome)

        elif opcao == "0":
            print("\n Encerramento o sistema.")
            break
        
        else:
            print("\n opcao invalida escolha um número de 0 a 4.")
            
            

if __name__ == "__main__":
    main()
mensagem = "Conta a realizar"
opcao = 4
while (mensagem != opcao):
  print("Digite abaixo a operação desejada")
  print("1: Soma 2: Subtração 3: Multiplicação 4: Divisão 0: Sair")
  operacao = int(input())
if opcao == 4:
   for i in range(1, 2):
    print(i, "Escolha a opção")
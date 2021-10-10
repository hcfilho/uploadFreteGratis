confirmacao = 's'

soma = 0
while confirmacao == 's':
    if confirmacao == 's':
        produto = float(input("Insira o valor do produto(apenas números)R$: "))
        confirmacao = input("Deseja adicionar mais valores de produtos?(s/n) ")
        while confirmacao != 's' and confirmacao != 'n':
            print("Opção inválida!Digite novamente")
            confirmacao = input("Deseja adicionar mais valores de produtos?(s/n) ")
        soma = produto + soma
        produto = produto + 1
    else:
        pass
        break
print("Compra finalizada, seu total é:", soma)

if soma > 200:
    print("Parabéns! Você ganhou frete grátis!")
else:
    print("Obrigado pela preferência, volte sempre!")

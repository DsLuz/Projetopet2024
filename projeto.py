import random

times = ['Flamengo', 'Vasco', 'Fluminense', 'Botafogo', 'Atlético-mg', 'Bahia']
saldo = 0
cupom = ('pet2024')

cupom_inserido = str(input('Digite o cupom:'))
if cupom_inserido == cupom:
    saldo += 100
    print('Parabéns R$ 100,00 foi depositado em sua conta')
else:
    print("Cupom inválido/n Digite novamente:")
     
while True:
    print('Bem-vindo ao Petano \n insira um comando numérico de 1 a 4')
    comando = int(input('Comando: '))
    
    if comando not in range (1,5): # validar o comando
        print('Comando inválido \n Digite outro comando.')

    else:
        if comando == 1:                  #comando
            valor = float(input('Valor a ser depositado:'))
            saldo += valor 
            print(f'Novo saldo:R${saldo}')

        elif comando == 2:
            valor = float(input('Valor a ser sacado:'))  
            while valor >= saldo:
                print('Saldo insuficiente./n Digite outro valor')
                valor = float(input('valor a ser sacado'))
        
            saldo -= valor
            print (f"O valor foi sacado /n o seu saldo atual é de : {saldo}")
        
        elif comando == 3:
            print (f'Saldo atual:R${saldo}')



        
        
       



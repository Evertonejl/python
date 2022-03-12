# Elabore um algoritimo que peça  para o usuario informar dois valores inteiros.
# calculadora devera imprimir a SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, E DIVISÃO dos valores.



# Agora o sistema deve perguntar qual operação aritmética o cliente deseja executar


# print(n1-n2)

# print(n1*n2)

# print(n1/n2)

# print('Este valor com ' + str('deste valor'))
# print('Soma: ' + str((n1+n2)))
# print('Subtração: ' + str((n1-n2)))
# print('Multiplicação: ' + str((n1*n2)))
# print('Divisão: ' + str((n1/n2)))

# op = input('Qual operação deseja executar? [1 - soma | 2 - subtração | 3-multiplicação | 4- divisão')
# if op == 1:
#   print('soma ' + int(n1+n2))
# elif op == 2:
#   print('Subtração ' + int(n1+n2))
# elif op == 3:    

#   print('Divisão ' + int(n1+n2))
# elif op == 4:    

from re import S


n1 = int(input('Informe um valor inteiro: '))
n2 = int(input('Informe outro valor inteiro: '))

op = int(input('Qual operação deseja executar? [1- soma | 2- subtracao | 3- multiplicacao | 4- divisao ]  '))
if op == 1:
    print('soma: ' + str(n1+n2))
elif op == 2:
    print('Subtração: ' + str((n1-n2)) + ' qualquer coisa')  
elif op == 3:
    print('Multiplicação: ' + str((n1*n2)))
elif op == 4:
    print('Divisão: ' + str((n1/n2)))
else:
    print('Operação Inválida')              

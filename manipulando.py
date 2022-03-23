# from genericpath import exists


# if exists('arquivo.txt'):
#   arq = open('arquivo.txt', 'r')
#   arq.close()
# else:
#     arq = open('arquivo.txt', 'w')
#     arq.close()

try:
    arq = open('arquivo.txt','r')
    arq.close()
    print('Arquivo foi aberto para leitura e está fechado')
except FileExistsError :
    print('O arquivo não exite e será criado')
    arq = open('arquivo.txt','w')
    arq.close()
    print('')
except:
    print('Ocorreu algum erro ao tentar abrir o arquivo')
try:
    arq = open('arquivo.txt','w')
    arq.write('ola mundo')
    arq.close()
except:
    print('ocorreu um erro ao tentar escrever o arquivo ')
try:
    arq = open('arquivo.txt','w')
    arq.write('seja bem vindo á manipulação de textos')
    arq.close()
except:
    print('ocorreu um erro ao tentar escrever o arquivo')
try:
    arq = open('arquivo.txt','r')
    conteudo = arq.read()
    print(conteudo)
    arq.close()
except:
    print('erro ao abrir arquivo para leitura')    

                    


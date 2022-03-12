
# o codigo de transito brasileiro oreve que, para conduzir veiculos automotores apessoa precisa 
# ter idade minima de 18 anos
# elabore um algoritimo que peça o nome e em que ano a pessoa nasceu, e retorne se esta pode ou não dirigir
# não totalmente satisfeito com o sistema e precisando de mais informaçoes
#o cliente precisa saber agora, quando não puder dirigir, quantos anos ele precisa esperar para poder dirigir




nome = input('Informe o nome da pessoa: ')
nasc = int(input('em que ano '+ nome + ' nasceu? '))
idade = 2022 - nasc
if ((2022 - nasc) < 18):
    print(nome + ' não pode dirigir. Faltam ' + (str(18- idade)) + ' ano para dirigir')
else:
    print(nome + ' PODE DIRIGIR')    
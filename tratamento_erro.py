try:
    try:
        try:
            vl1 = int(input('informe um valor inteiro: '))
            vl2 = int(input('informe outro valor inteiro: '))
            print('o resultado da divisão dos valores é ' + str(vl1 / vl2))
            print('obrigado por usar nsso sistema')
        except NameError:
            print('alguma variavel não existe')
        except ZeroDivisionError:
            print("impossivel dividir por zero")
        except ValueError:
            print('algum valor inválido foi passado')
        except TypeError:
            print('tipo de dado invalido')
        except:
            print('Algo deu erro')
    except:
        print('Erro ao informar o primeiro valor.')
except:
    print('Erro ao efetuar a divisão')                                    
 
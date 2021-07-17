def principal():
    num = int(input('Forneça um número entre 0 e 999: '))
    calDezena = (num // 10) % 10
    calCentena = (num // 100) % 10
    calUnidade = num % 10
    if num < 0 or num > 999 :
        print('Não sei o valor por extenso')
    else :
        #professor coloquei em uma função a parte pois tem muitos "if" e fica melhor de organizar
        texto(calDezena, calCentena, calUnidade, num)
def unidade(unidade):
    listaUnidade = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    return listaUnidade[unidade - 1]
def dezena(numero, dezena, unidade):
    if dezena == 1:
        listaDezena1 = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
        unidade = numero % 10
        return listaDezena1[unidade]
    else:
        listaDezena2 = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
        return listaDezena2[dezena - 2]
def centena(centena):
    listaCentena = ['cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos',
                    'oitocentos', 'novecentos']
    return listaCentena[centena - 1]
def texto(d, c, u, num):
    if c==0 and d==0 and u==0:
        print('Número por extenso é zero')
    elif c == 0:
        if d == 1: #se não tiver centena e dezena for 1 ex(013)
            print('Número por extenso é {}'.format(dezena(num, d, u)))
        elif d == 0 and u != 0: #se não tiver nem centena nem dezena ex(003)
            print('Número por extenso é {}'.format(unidade(u)))
        elif d != 0 and u == 0: #não tem centena e unidade é zero ex(90)
            print('Número por extenso é {}'.format(dezena(num, d, u)))
        else: #somente a centena é zero ex(97)
            print('Número por extenso é {} e {}'.format(dezena(num, d, u), unidade(u)))
    elif d == 0:
        if u == 0 and c== 1: #tem só a centena que é um (100)
            print('Número por extenso é cem')
        elif u== 0 and c !=0: #só tem a centena diferente de zero ex(300)
            print('Número por extenso é {}'.format(centena(c)))
    elif d == 1 and c!= 0: #dezena é 1 e centena diferente de zero ex(217)
        print('Número por extenso é {} e {}'.format(centena(c), dezena(num, d, u)))
    elif c!= 0 and d!= 0 and d!= 1 and u != 0: #nenhum nulo e dezena diferente de 1 ex(278)
        print('Número por extenso é {} e {} e {}'.format(centena(c), dezena(num, d, u), unidade(u)))
principal()

unidades = ['','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
especiais = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
dezenas = ['', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
centenas = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']



def leitura_numero(numero, qtn_characters):
    digito_1 = int(numero[0])

    if qtn_characters == 1:
        print(unidades[digito_1])

    elif qtn_characters ==2:
        digito_2 = int(numero[1])

        if digito_1 == 1:
            print(f"{especiais[int(numero[-1])]}")

        else:
            if digito_2 != 0:
                print(f"{dezenas[digito_1]} e {unidades[digito_2]}")
            else:
                print(f"{dezenas[digito_1]}")

    elif qtn_characters == 3:
        digito_2 = int(numero[1])
        digito_3 = int(numero[2])
        if digito_2 != 0 and digito_3 != 0:
            print(f"{centenas[digito_1]} e {dezenas[digito_2]} e {unidades[digito_3]}")
        elif digito_2 == 0:
            print(f"{centenas[digito_1]} e {unidades[digito_3]}")
        elif digito_3 == 0:
            print(f"{centenas[digito_1]} e {dezenas[digito_2]}")



while True:
    numero = input("Digite um numero entre 0 a 999 ....\n")
    qtn_characters = len(numero)
    if qtn_characters > 3:
        print("digite um numero valido....")
    else:
        leitura_numero(numero, qtn_characters)

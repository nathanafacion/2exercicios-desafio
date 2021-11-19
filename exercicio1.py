import re

conversor = {
    '00':'zero',
    '0': 'zero',
    '1': 'um',
    '2': 'dois',
    '3': 'três',
    '4': 'quatro',
    '5': 'cinco',
    '6': 'seis',
    '7': 'sete',
    '8': 'oito',
    '9': 'nove',
    '10': 'dez',
    '11': 'onze',
    '12': 'doze',
    '13': 'treze',
    '14': 'quatorze',
    '15': 'quinze',
    '16': 'dezesseis',
    '17': 'dezesete',
    '18': 'dezoito',
    '19': 'dezenove',
    '20': 'vinte',
    '30': 'trinta',
    '40': 'quareta',
    '50': 'cinquenta',
    '60': 'sessenta',
    '70': 'setenta',
    '80': 'oitenta',
    '90': 'noventa',
    '100': 'cem',
    '200': 'duzentos',
    '300': 'trezentos',
    '400': 'quatrocentos',
    '500': 'quinhentos',
    '600': 'seissentos',
    '700': 'setecentos',
    '800': 'oitocentos',
    '900': 'novecentos',
    '1000': 'mil',
    '1000000':'milhão'    
}


def core_do_conversor(valor):
    # vai ser usado para fazer diferenca entre valores
    diferenca_valores = int(valor)
    numero_escrito = None
    while diferenca_valores != 0:
        # vai achar o maior valor que corresponde ao dicionario
        maior_valor = valor[0] + (len(valor)-1) * '0'
        diferenca_valores = int(valor) - int(maior_valor)
        if numero_escrito == None:
            numero_escrito = conversor[maior_valor]
        else:
            numero_escrito = numero_escrito +' e '+ conversor[maior_valor]
        valor = str(diferenca_valores)
    return numero_escrito


def converte_numero_para_escrito(valor):
    # divide em antes da vírgula e depois da vírgula
    separar_valor = valor.split(",")
    reais = separar_valor[0]
    centavos = separar_valor[1]

    # verifica se esta no dicionario
    if reais in conversor:
        print(conversor[reais] + ' reais e '+ conversor[centavos] + ' centavos.')
    else:
        print(core_do_conversor(reais) + ' reais e '+ core_do_conversor(centavos) + ' centavos.')


# expressao regular
def valida_valor(valor):
    if(re.match("^\d*,\d{2}$", valor)):
        return True
    return False


if __name__ == "__main__":
    valor = str(input('Entre com o numero: '))
    # fazer regex
    
    if valida_valor(valor):
        converte_numero_para_escrito(valor)
    else:
        print('esse valor não é valido, digite um numero de até nove número antes da vírgula e dois números após a vírgula.')    


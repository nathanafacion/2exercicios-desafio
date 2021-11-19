import re
from dicionario import conversor
from collections import Counter

def core_do_conversor(valor):
    # vai ser usado para fazer diferenca entre valores
    diferenca_valores = int(valor)
    numero_escrito = None
    while diferenca_valores != 0:
        # vai achar o maior valor que corresponde ao dicionario
        maior_valor = valor[0] + (len(valor)-1) * '0'
        diferenca_valores = int(valor) - int(maior_valor)
        if numero_escrito == None:
            numero_escrito = conversor[str(maior_valor)]
        else:
            numero_escrito = numero_escrito +' e '+ conversor[maior_valor]
        valor = str(diferenca_valores)
    return numero_escrito

def remove_palavra_mil(valor_escrito):
    conta_mil = Counter(valor_escrito.split())
    return valor_escrito.replace("mil ","",conta_mil['mil']-1)
    
def converte_numero_para_escrito(valor):
    # divide em antes da vírgula e depois da vírgula
    separar_valor = valor.split(",")
    reais = separar_valor[0]
    centavos = separar_valor[1]

    # string final para impressao
    valor_escrito = ''    
    # verifica se esta no dicionario
    if reais in conversor:
        valor_escrito = conversor[str(int(reais))] + ' reais '
    else:
        valor_escrito = core_do_conversor(reais) + ' reais '
    
      
    if centavos in conversor:
        valor_escrito = valor_escrito + conversor[str(int(centavos))] + ' centavos '
    else:
        valor_escrito = valor_escrito + core_do_conversor(centavos) + ' centavos '
    
    print(remove_palavra_mil(valor_escrito))



# expressao regular
def valida_valor(valor):
    if(re.match("^\d{1,9},\d{2}$", valor)):
        return True
    return False


if __name__ == "__main__":
    valor = str(input('Entre com o numero: '))
    
    if valida_valor(valor):
        converte_numero_para_escrito(valor)
    else:
        print('esse valor não é valido, digite um numero de até nove número antes da vírgula e dois números após a vírgula.')    


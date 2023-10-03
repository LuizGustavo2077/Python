# função que não tem retorno
def funcaoSemRetorno(a, b):
    resultado = a + b
    print('exibindo resultado da função: {}'.format(resultado))

funcaoSemRetorno(1, 5)

# função que retorna um valor
def funcaoComRetorno(a, b):
    resultado = a + b
    print('com retorno DENTRO da função: {}'.format(resultado))
    return resultado

resultado = funcaoComRetorno(3, 5)
print('com retorno FORA da função: {}'.format(resultado))

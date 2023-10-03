def soma(a, b):
    return a + b

# subtrai dois números
def subtracao(a, b):
    return a - b

# multiplicação
def multiplicacao(a, b):
    return a * b
    
# divisão
def divisao(a, b):
    return a / b

# potência nutela
def potenciaNutela(base, expoente):
    return base ** expoente

# potência raiz
def potenciaCaseira(base, expoente):
    r = 1
    for x in range(0, expoente):
        r = r * base
    return r

# área do círculo
def areaCirculo(r):
    # return 3.141592654 * r**2
    return 3.141592654 * potenciaNutela(r, 2)

# hipotenusa
def hipotenusa(co, ca):
    # co: cateto oposto ao ângulo
    # ca: cateto adjacente ao ângulo
    return ((co ** 2) + (ca ** 2)) ** (1/2)

## tente sozinho fazer:
# 1. fazer cálculo do fatorial
# 2. fazer cálculo da fórmula de bhaskhara
# 3. ... algum outro cálculo (use a imaginação)

# executando as funções
print('soma: {}'.format(soma(33, 67)))
print('subtracao: {}'.format(subtracao(100.53, 33.48)))
print('multiplicacao: {}'.format(multiplicacao(23, 8.5)))
print('divisao: {}'.format(divisao(9, 41)))
print('potência nutela: {}'.format(potenciaNutela(7, 3)))
print('potência raiz: {}'.format(potenciaCaseira(2.5, 4)))
print('área do círculo: {}'.format(areaCirculo(4)))
print('hipotenusa: {}'.format(hipotenusa(3, 4)))

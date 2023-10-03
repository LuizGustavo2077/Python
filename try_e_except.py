def dividi_cinco_by(numero):
    try:
        value = 5/numero
    except ZeroDivisionError:
        print("Dividiu por zero error")
        value = 1
    return value
print(dividi_cinco_by(5))
print(dividi_cinco_by(0))
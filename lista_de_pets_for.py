pets={
    "carol":1,
    "luiz":1,
    "aurora":2,
    "bianca":2,
    "kaique":3,
    "Lump":3,
}
for pessoa in pets:
    qnt= pets[pessoa]
    if qnt == 2:
       print("{} tem {} pets".format(pessoa,qnt))
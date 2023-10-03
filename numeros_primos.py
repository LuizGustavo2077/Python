for n in range(1,251):
    primo=True
    for b in range(2,n):
        if n%b==0:
            primo=False
    if primo==True:
        print(n)
    

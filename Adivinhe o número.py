lista = []
print("Pense em um número no intervalo entre i e f.")
i=int(input("Digite o início: "))
f=int(input("Digite o fim: "))
for n in range(i, f+1):
    lista.append(n)
f=i-1+ len(lista)//2
while len(lista)>1:
    if len(lista)>4:
        r = input("O número está entre {} e {}? [S/N] ".format(i, f))
        if r in "Ss":
            p=lista.index(f)+1
            del lista[p:len(lista)]
            if f-i==2 and len(lista)>3:
                for n in lista:
                    if n!=i and n!=f and n!=i+1:
                        lista.remove(n)
                del lista[3]
            f = len(lista) // 2
            if f<i:
            	f=f+i
        elif r in "Nn":
            l=lista.index(f)
            del lista[0:l]
            i=f+1
            f=f+len(lista)//2
            del lista[0]
    elif 5>len(lista)>2:
        r = input("O número é {} ou {}? [S/N] ".format(lista[0], lista[1]))
        if r in "Ss":
            for n in lista:
                if n!=lista[0] and n!=lista[1]:
                    lista.remove(n)
            if len(lista)==3:
            	del lista[2]
        elif r in "Nn":
            for k in lista:
                if k==lista[0] or k==lista[1]:
                    lista.remove(k)
            lista[0]=lista[0] + 1
    elif len(lista)==2:
        r = input("O número é {}? [S/N] ".format(lista[0]))
        if r in "Ss":
            del lista[1]
            break
        elif r in "Nn":
            del lista[0]
            break
print("O número é {}.".format(lista[0]))
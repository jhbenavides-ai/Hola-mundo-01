#tema nuevo de python
meses=["enero","febrero","marzo"]
print(meses)


print("ingrese  los mese que faltan ; 'fin  para terminar")
m='xxx'
while m != 'fin':
    m=input("ingrese  el siguiente mes: \n")
    meses.append(m)


for name in meses :
    print( ">" ,name)


print("chao")
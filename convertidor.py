res=0 #resultado
exp=0 # exponente de cada digito
numero= int(input("Digite numero que desea convertir "))# el número que se va a convertir
base=int(input("Digite en qué base está el número a convertir ")) # la base en que está el número que se desea convertir
baseDestino=int(input("Digite la base a la que desea convertir ")) #la base a la quiere convertir el numero
conversion = []

while numero>0:
    residuo=numero%10
    res=residuo*base**exp+res
    exp+=1
    numero=numero//10
if baseDestino != 10:
    while res != 0:
        conversion.append(res%baseDestino)
        res = res // baseDestino
    for i in reversed(conversion):
        print(i, end="")
else:
    print("Su resultado es:",res)
   


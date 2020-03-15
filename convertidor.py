res=0 #resultado
exp=0 # esponente de cada digito
base=int(input("digite en qué base está el número a convertir")) # la base en que está el número que se desea convertir
numero= int(input("digite numero que desea convertir"))# el número que se va a convetir
while numero>0:
    residuo=numero%10
    res=residuo*base**exp+res
    exp+=1
    numero=numero//10
print("su resultado es",res)    


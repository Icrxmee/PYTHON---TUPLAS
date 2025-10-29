t = ()
t1 = ()

for i in range (4):

    v = int ( input(f"Digite o {i+1}° número: "))
    t += (v,)

    if v % 2 == 0:

        t1 += (v,)
         

print (f"Você digitou os números: {t}")
print (f"O número 9 apareceu {t.count(9)} vezes")
print (f"O número 3 aparece na posição {t.index(3)}")
print (f"Os números {t1} são pares")

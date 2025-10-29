t = ("Lápis",1.75,"Borracha",2.00,"Cderno",15.90,"Estojo",25.00,"Transferidor",4.20,
     "Compasso",9.99,"Mochila",120.32,"Canetas",22.30,"Livro",34.00)

print("--"*25)
print("Listagem de Preços".center(50))
print("--"*25)

for i in range (0, len(t)):
    
    if i % 2 == 0:
        print(f"{t[i]:.<30}", end="")
    else:
        print(f"R$`{t[i]:>7.2f}")
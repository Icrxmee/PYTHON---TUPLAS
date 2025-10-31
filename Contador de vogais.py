t = ("Jose","Pedro","Icaro","Mouta","Macedo")
v = 'aeiou'


for i in t:

    print (f"\nA palavra {i} tem as vogais: ", end="")

    for n in i:

        if n.lower() in 'aeiou':

            print (n, end="")

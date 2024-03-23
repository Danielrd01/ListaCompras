lista_compras= []

producto = input("Ingrese productos para comprar o ingrese terminar para finalizar la compra: ")

while producto != "terminar":

        lista_compras.append(producto)
        producto = input("Ingrese otro producto para comprar o terminar para finalizar: ")


print("la lista de compras: ") 

for producto in lista_compras:
    print(producto)
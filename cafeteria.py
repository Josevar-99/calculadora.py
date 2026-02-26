


menu_de_cafeteria

saldo_total = 0

 print("menu de cafeteria")

 menu = {
    1: ("cafe", 3000)
    2: ("chocolate",2000)
    3: ("croasant", 5000)
    4: ("cafe expresso", 4000)
    5: ("dona",2500)
 }

 # Mostrar menu
 print("\n---menu---")
for clave, valor in menu.intems():
    print(clave,"_",valor[0], "$", valor[1])

 #cuantos productos va a pedir
 cantidad =int(input("\n¿cuantos productos va a pedir? "))

 contador = 0

 while  contador < cantidad:
    opcion  = int(input("\nElige el numero del producto: "))

    if opcion in menu:
        producto, precio =menu[opcion]
        saldo_total += precio
        print("agregaste.", producto)
        contador += 1
    else:
        print("opcion invalida")

print("\ntotal precio a pagar: $", saldo_total)
print("gracias por tu compra")

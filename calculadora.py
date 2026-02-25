

while True:
    print("---calculadora ---")
    print("1.sumar")            
    print("2.restar")
    print("3.multiplicar")
    print("4.dividir")
    print("5.potencia")
    print("6.raiz")
    print("7.porcentaje")
    print("8.modulo")
    print("9.promedio")
    print("10.salir")
    try:
        opcion  = input("Elige una opcion (1-10):" )

    if opcion == "10":  
        print("hasta luego")
    else:
        print("elija una opcion valida")
        break
     

    num1 = float(input("ingresa el primer numero: "))
    num2 = float(input("ingresa el segundo numero: "))

    if opcion == "1":
        print("resultado:",num1+num2)

    elif opcion == "2":
        print("resultado:",num1-num2)

    elif opcion == "3":
        print("resultado:",num1*num2) 

    elif opcion == "4":
        if num2 != 0:   
            print("resultado:",num1/num2)
        else:
            print("no se puede dividir entre 0")



    if opcion == "5":
        Base = float(input("ingresa la base: "))
        exponente = float(input("ingresa el exponente: "))    
        print("resultado:", Base ** exponente)

    elif opcion =="6":
        numero = float(input("ingresa el numero: "))
        if numero >= 0:
            print("resultado:", math.sqrt(numero))
        else:
            print("no se puede sacar raiz de numero negativo")

    elif opcion =="7":
        numero = float(input("ingresa el numero: ")) 
        porcentaje = float("ingresa el porcentaje: ")
        print("resultado:", (numero*porcentaje)/100)

    elif opcion =="8":
        num1 = int(input("ingresa el primer numero: "))
        num2 = int(input("ingresa el segundo numero: "))
        print("resultado:", num1 % num2)

    elif opcion =="9":
        cantidad = int(input("¿cuantos numeros vas a promediar? "))
        suma = 0
        Contador = 0

        while Contador < cantidad:
            numero = float(input("ingresa un numero: "))
            suma += numero
            Contador += 1

        print("promedio:", suma/cantidad) 
    
    if opcion == "10":  
        print("hasta luego")
        break





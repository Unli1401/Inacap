#Transformar grados farenheit a celsius = (grado °F − 32) × 5/9 = 0 °C
#transformar grados celsius a fahrenheit = (grado°C × 9/5) + 32 = 32 °F
#transformar grados celsius a kelvin = grados °C + 273.15 = 273.15 K

"""
print ("Opciones:")
print ("Elige el numero de la opción que deseas elegir:")
print ("1. Transformar grados Celsius a Farenheit") #(grado°C × 9/5) + 32 = 32 °F
print ("2. Transformar grados Farenheit a Celsius" ) #(grado °F − 32) × 5/9 = 0 °C
print ("3. Transformar grados Celsius a Kelvin") #grados °C + 273.15 = 273.15 K
opcion = (input("Elige una opción: "))
if opcion == 1 :
    grado = float(input("OK, transformaremos C° a F°, ingresa el valor: "))
calculo = (grado * 9/5) + 32
print (f"Los {grado}°C son {calculo} °F")
#else:
#    print ("fin")
"""
seguir =""
print ("ESTE PEQUEÑO PROGRAMA HACE LA CONVERSION A LOS DISTINTOS TIPOS DE TEMPERATURA: GRADOS CELSIUS, FARENHEIT Y KELVIN")
print ("")
nombre = input("Primero, dame tu nombre: ")
while True: 
    print("")
    print(f"{nombre}, elige el numero de la opción que deseas elegir:")
    print("1. Transformar grados Celsius a Farenheit") #(grado°C * 9/5) + 32 = 32 °F
    print("2. Transformar grados Farenheit a Celsius" ) #(grado °F - 32) * 5/9 = 0 °C
    print("3. Transformar grados Celsius a Kelvin") #grados °C + 273.15 = 273.15 K
    print("4. Transformar grados Kelvin a Celsius ") #°C = gradoK - 273.15
    print("5. Transformar grados Farenheit a Kelvin")#(32 °F − 32) × 5/9 + 273.15 = 273.15 K
    print("6. Transformar grados Kelvin a Farenheit")#(0 K − 273.15) × 9/5 + 32 = -459.7 °F
    print("7. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        grado = float(input(f"OK {nombre} , transformaremos °C a °F, ingresa el valor: "))
        calculo = (grado * 9/5) + 32
        print("\n" + "=" * 50)
        print(f"      Listo {nombre}, los {grado}°C son {calculo:.1f} °F")
        print("=" * 50 + "\n")
    elif opcion == 2:
        grado = float(input(f"OK {nombre} , transformaremos °F a °C, ingresa el valor: "))
        calculo = (grado - 32) * 5/9
        print("\n" + "=" * 50)
        print(f"      Listo {nombre}, los {grado}°F son {calculo:.1f} °C")
        print("=" * 50 + "\n")
    elif opcion == 3:
        grado = float(input("OK, transformaremos °C a K, ingresa el valor: "))
        calculo = grado + 273.15
        print("\n" + "=" * 50)
        print (f"      Listo {nombre}, los {grado} °F son {calculo:.2f}K")
        print("=" * 50 + "\n")
    elif opcion == 4:#Kelvin a Celsius ") #°C = gradoK - 273.15
        grado = float(input("OK, transformaremos K a °C, ingresa el valor: "))
        calculo = grado - 273.15
        print("\n" + "=" * 50)
        print (f"      Listo {nombre}, los {grado} K son {calculo:.1f} °C")
        print("=" * 50 + "\n")
    elif opcion == 5:#Farenheit a Kelvin")#(32 °F - 32) * 5/9 + 273.15 = 273.15 K
        grado = float(input("OK, transformaremos °F a K, ingresa el valor: "))
        calculo = (grado - 32)*(5/9 ) + 273.15
        print("\n" + "=" * 50)
        print (f"      Listo {nombre}, los {grado} °F son {calculo:.2f}K")
        print("=" * 50 + "\n")
    elif opcion == 6:#Kelvin a Farenheit")#(0 K − 273.15) × 9/5 + 32 = -459.7 °F
        grado = float(input("OK, transformaremos K a °F, ingresa el valor: "))
        calculo = (grado - 273.15) * (9/5) + 32 #= -459.7 °F
        print("\n" + "=" * 50)
        print (f"      Listo {nombre}, los {grado} K son {calculo:.2f} °F")
        print("=" * 50 + "\n")
    elif opcion == 7:
        print(f"Adios {nombre}, Saliendo...")
        break
    else:
        print (f"Ingresaste una opción no válida, {nombre}")
        
    seguir = input(f"Deseas hacer otros calculos, {nombre}, Escribe S ó N: ")
    if seguir.lower() == "s":
        continue
    else:
        print(f"Adios {nombre}, Saliendo...")
        break
    
    #de farenheit a kelvin
    #de kelvin a farenheit
    #de kelvin a celsius
    
"""print("\n" + "=" * 50)
print(f"Los {grado}°C son {calculo:.1f} °F")
print("=" * 50 + "\n")"""
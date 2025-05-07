def mostrar_menu():
    print("\nCalculadora en Python")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def calcular():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
            except ValueError:
                print("Por favor, introduce solo números.")
                continue

            if opcion == "1":
                print("Resultado:", num1 + num2)
            elif opcion == "2":
                print("Resultado:", num1 - num2)
            elif opcion == "3":
                print("Resultado:", num1 * num2)
            elif opcion == "4":
                if num2 == 0:
                    print("Error: No se puede dividir entre cero.")
                else:
                    print("Resultado:", num1 / num2)
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar la calculadora
calcular()

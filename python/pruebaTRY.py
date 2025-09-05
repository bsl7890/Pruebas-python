import os


# while True:
#     os.system("cls")
#     try:
#         print('======================================================')
#         print("|                     >>Menu<<                         |")
#         print('|    1. Division                                       |')
#         print('|    2. Archivo                                        |')
#         print('|    3. Operador                                       |')
#         print('|    4. Salir                                          |')
#         print('======================================================')
#         opcion = int(input("Seleccione una opción: "))
#         if opcion == 1:
#             while True:
#                 os.system("cls")  
#                 try:
#                     x = int(input("Ingrese un número: "))
#                     y = int(input("Ingrese otro número: "))
#                     division = x / y
#                 except ZeroDivisionError:
#                     print("❌ Error: No se puede dividir por cero.")
#                     input("Presione Enter para intentar de nuevo...")
#                 except ValueError:
#                     print("❌ Error: Ingrese numeros no letras.")
#                     input("Presione Enter para intentar de nuevo...")
#                 else:
#                     print(f"✅ El resultado de la división es: {division}")
#                     input("Presione Enter para continuar...")
#                     break  
#         elif opcion == 2:
#             while True:
#                 try:
#                     archivo = open('datos.txt')
#                     contenido = archivo.read()
#                 except FileNotFoundError:
#                     print("❌ Error: El archivo 'datos.txt' no se encontró.")
#                     input("Presione Enter para intentar de nuevo...")
#                     break
#                 except Exception as e:
#                     print(f"Ocurrio un error inesperado: {e}.")
#                     input("Presione Enter para intentar de nuevo...")
#                 else:
#                     print(f"✅ El resultado del texto es: {contenido}")
#                     input("Presione cualquier tecla para terminar..")
#                     archivo.close()
#                     break 
#         elif opcion == 3:
#             while True:
#                 try:
#                     x = int(input("Ingrese un número: "))
#                     y = int(input("Ingrese otro número: "))
#                     operador = input("Ingrese la operación (+, -, *, /, ^):")
#                     if operador == "+":
#                         resultado = x + y
#                     elif operador == "-":
#                         resultado = x - y
#                     elif operador == "*":
#                         resultado = x * y
#                     elif operador == "/":
#                         resultado = x / y
#                     elif operador == "^":
#                         resultado = x ** y
#                     else:
#                         print("❌ Error: Ingrese uno de los operadores válidos (+, -, *, /, ^).")
#                         input("Presione Enter para intentar de nuevo...")
#                         continue
#                 except ZeroDivisionError:
#                     print("❌ Error: No se puede dividir por cero.")
#                     input("Presione Enter para intentar de nuevo...")
#                 except ValueError:
#                     print("❌ Error: Ingrese numeros no letras.")
#                     input("Presione Enter para intentar de nuevo...")
#                 else:
#                     print(f"✅ El resultado de la operación {operador} es: {resultado}")
#                     input("Presione Enter para continuar...")
#                     break
#         elif opcion == 4:
#             print("👋 Saliendo del programa...")
#             break
#         else:
#             print("❌ Opción no válida. Intente de nuevo.")
#             input("Presione Enter para continuar...")
#     except ValueError:
#         print("Porfavor ingrese un numero")
#         input("Presione Enter para continuar...")



try:
    with open('datos.txt', 'r') as archivo:
        contenido = archivo.read()
        print (int(contenido))
        input("Presione cualquier tecla para terminar...")
except FileNotFoundError:
    print("❌ Error: El archivo 'datos.txt' no se encontró.")
    input("Presione Enter para intentar de nuevo...")
except Exception as e:
    print(f"❌ el archivo no tiene numeros.")
    input("Presione Enter para intentar de nuevo...")
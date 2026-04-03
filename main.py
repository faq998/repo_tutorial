print("Hola Mundo")
nombre= input("Ingrese su nombre: ").strip().upper()
while not nombre.isalpha():
    nombre=input("Se aceptan unicamente letras, escriba correctamente: ")

print(f"Hola,{nombre}")
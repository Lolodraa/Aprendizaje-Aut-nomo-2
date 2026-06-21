#Trabajo autonomo 2

import random

print("GENERADOR SEGURO DE CONTRASEÑAS")

# Definición de variables
minus = "abcdefghijklmnñopqrstuvwxyz"
capital = minus.upper()
number = "1234567890"
characters = "!°#$%&/()=?¡*¨[]_:;.,}{<>?→↑"

while True:
    entrada = input("Ingrese la longitud de la contraseña: ")

    if not entrada.isdigit():
        print("Error: Debe ingresar solo números.")
        continue

    longitud = int(entrada)

    if longitud < 10:
        print(" Nivel BAJO no permitido. Mínimo 10 caracteres.")

    elif 10 <= longitud < 20:
        print(" Nivel MEDIO seleccionado.")
        opcion = input("¿Desea cambiar a nivel ALTO (20 o más)? (s/n): ").lower()

        if opcion == "s":
            nueva = input("Ingrese nueva longitud (mínimo 20): ")
            
            if nueva.isdigit() and int(nueva) >= 20:
                longitud = int(nueva)
                print(" Cambiado a nivel ALTO.")
                break
            else:
                print("Se mantiene nivel MEDIO.")
                break
        else:
            print("Continuando con nivel MEDIO.")
            break

    else:
        print("Nivel ALTO seleccionado.")
        break

# Generación segura
contraseña = []
contraseña.append(random.choice(capital))
contraseña.append(random.choice(minus))
contraseña.append(random.choice(number))
contraseña.append(random.choice(characters))

todos = capital + minus + number + characters

# Completar con WHILE
i = 4
while i < longitud:
    contraseña.append(random.choice(todos))
    i += 1

# Mezclar
random.shuffle(contraseña)

# Convertir a texto (FOR)
contraseña_final = ""
for c in contraseña:
    contraseña_final += c

print("Contraseña generada:", contraseña_final)

# Evaluación final
tiene_mayus = any(c in capital for c in contraseña_final)
tiene_num = any(c in number for c in contraseña_final)
tiene_sim = any(c in characters for c in contraseña_final)

es_valida = tiene_mayus and tiene_num and tiene_sim

if longitud >= 20 and es_valida:
    print("Nivel de seguridad: ALTO")
elif longitud >= 10 and es_valida:
    print("Nivel de seguridad: MEDIO")

  #Nunca imprimira else  
"""else:
    print("Nivel de seguridad: INSUFICIENTE (Faltan caracteres requeridos)")"""
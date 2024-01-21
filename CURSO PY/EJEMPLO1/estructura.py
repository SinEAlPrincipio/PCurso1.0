'''vamos a realizar una agenda telefonica

nombre=input("Digtar Nombre")
Apellido = input("Digitar Apellidos")
id= int(input("Digita tu Cedula"))
'''
agenda={
    1067879338 : "Jose",
    4523897654 : "Maria",
    1234567890 : "Juan",
    }
consul = True

while consul:
    print()
    print("Mi agenda")
    print("-----------------")
    print("1. Consultar \n2. Añadir \n3. Modificar \n4. Borrar \n5. Salir")
    
    opcion= ""
    
    while opcion not in ("1","2","3","4","5"):
        opcion = input("-> ")

    if opcion == "1":
        id=int(input("Digtar ID: "))
        if id not in agenda:
            print("Este Usuario no exite en la Base de datos")
            
        else:
            nombre = agenda[id]
            print(id, ":", nombre)
            
    elif opcion == "2":
        id=int(input("Digtar ID: "))
        if id in agenda:
            print("Este Usuario ya exite en la Base de datos")
        else:
            nombre= str(input("Digtar Nombre"))
            agenda[id] = nombre
            print("El Usuario se ha añadido correctamente a la base de datos")
    
    elif opcion == "3":
        id=int(input("Digtar ID: "))
        if id not in agenda:
            print("Este Usuario no exite en la Base de datos")
        else:
            nombre= str(input("Digtar Nombre"))
            agenda[id] = nombre
            print("El Usuario se ha modificado correctamente")
    
    elif opcion == "4":
        id=int(input("Digtar ID: "))
        if id not in agenda:
            print("Este Usuario no exite en la Base de datos")
        else:
            del agenda[id]
            print("El usuario se ha borrado correctamente")
    
    elif opcion == "5":
        consultado = False
        print("Gracias por utilizar este servicio")


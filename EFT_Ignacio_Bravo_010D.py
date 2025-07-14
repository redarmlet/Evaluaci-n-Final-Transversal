productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

#######################################

def stock_marca(marca):
    if marca == "lenovo":
        print("Usted selecciono Lenovo")
        stock_total = stock['2175HD'][1]+stock['123FHD'][1]+stock['342FHD'][1]
        print(f"El stock de productos lenovo es de :{stock_total} productos")
    elif marca == "hp":
        print("Usted selecciono HP")
        stock_total = stock['8475HD'][1]+stock['fgdxFHD'][1]
        print(f"El stock de productos HP es de :{stock_total} productos")
    elif marca == "asus":
        print("Usted selecciono Asus")
        stock_total = stock['JjfFHD'][1]+stock['GF75HD'][1]
        print(f"El stock de productos ASUS es de :{stock_total} productos")
    elif marca == "dell":
        print("Usted selecciono DELL")
        stock_total = stock['UWU131HD'][1]
        print(f"El stock de productos Dell es de :{stock_total} productos")
    else:
        print("La marca seleccionada no es válida")

def busqueda_precio(p_min,p_max):
    print("Los productos dentro del presupuesto son: ")
    if p_min<=387990 and 387990<=p_max and stock['8475HD'][1]>0:
        print("HP modelo 8475HD")
    if p_min<=327990 and 327990<=p_max and stock['2175HD'][1]>0:
         print("Lenovo modelo 2175HD")
    if p_min<=424990 and 424990<=p_max and stock['JjfFHD'][1]>0:
        print("Asus modelo JjfFHD")

    if p_min<=664990 and 664990<=p_max and stock['fgdxFHD'][1]>0:
         print("HP modelo fgdxFHD")
    if p_min<=290890 and 290890<=p_max and stock['123FHD'][1]>0:
         print("Lenovo modelo 123FHD")
    if p_min<=444990 and 444990<=p_max and stock['342FHD'][1]>0:
         print("Lenovo modelo 342FHD")

    if p_min<=749990 and 749990<=p_max and stock['GF75HD'][1]>0:
         print("HP modelo GF75HD")
    if p_min<=349990 and 349990<=p_max and stock['UWU131HD'][1]>0:
         print("Dell modelo UWU131HD")
    else:
        print("No se han encontrado resultados para el rango especificado.")

def actualizar_precio(modelo,p):
    if modelo=='8475HD':
        stock['8475HD'][1]=p
        print(f"Se ha cambiado el precio de {modelo} a ${p}.")
    elif modelo=='2175HD' :
            stock['2175HD'][1]=p
            print(f"Se ha cambiado el precio de {modelo} a ${p}.")
    elif modelo== 'JjfFHD':
            stock['JjfFHD'][1]=p
            print(f"Se ha cambiado el precio de {modelo} a ${p}.")
    elif modelo=='fgdxFHD' :
            stock['fgdxFHD'][1]=p
            print(f"Se ha cambiado el precio de {modelo} a ${p}.")
    elif modelo=='123FHD' :
            stock['123FHD'][1]=p
            print(f"Se ha cambiado el precio de {modelo} a ${p}.")
    elif modelo=='342FHD' :
            stock['342FHD'][1]=p
            print(f"Se ha cambiado el precio de {modelo} a ${p}.")
    elif modelo=='GF75HD' :
            stock['GF75HD'][1]=p
            print(f"Se ha cambiado el precio de {modelo} a ${p}.")
    elif modelo=='UWU131HD' :
            stock['UWU131HD'][1]=p
            print(f"Se ha cambiado el precio de {modelo} a ${p}.")
    elif modelo=='FS1230HD' :
        stock['FS1230HD'][1]=p
        print(f"Se ha cambiado el precio de {modelo} a ${p}.")
    else:
         print("El modelo ingresado no es válido.")

#######################################
while True:
    print("Bienvenido a Pybooks")
    print("MENU PRINCIPAL")
    print("1. Stock marca")
    print("2. Busqueda por precio")
    print("3. Actualziar Precio")
    print("4. Salir")
    try:
        opt=int(input("ingrese la opcion deseada: "))

        if opt==1:
            marca=input("Ingrese la marca de la que desee chequear el stock: ")
            stock_marca(marca)
        elif opt==2:
            print("usted seleccionó buscar por precio")
            try:
                p_min=int(input("Ingrese el precio mínimo: "))
            except ValueError:
                 print("Debe ingresar valores enteros")
            try:
                p_max=int(input("Ingrese el precio máximo: "))
            except ValueError:
                 print("Debe ingresar valores enteros")
            busqueda_precio(p_min,p_max)
        elif opt==3:
            modelo=input("ingrese el modelo del que desea actualizar el precio: ")
            p=int(input(f"Ingrese el precio que desee establecer para {modelo}: "))
            actualizar_precio(modelo,p)
            try:
                sn=True
                while sn:
                    loop=input("¿Desea actualizar el precio de otro modelo?(s/n): ")
                    if loop=="s":
                        modelo=input("ingrese el modelo del que desea actualizar el precio: ")
                        p=int(input(f"Ingrese el precio que desee establecer para {modelo}: "))
                        actualizar_precio(modelo,p)
                    elif loop=="n":
                        print("Usted seleccionó salir")
                        sn=False
            except ValueError:
                 print("ingrese una opción válida")
        elif opt==4:
            print("Saliendo del sistema")
            break
        else:
             print("Debe seleccionar una opción válida")
    except ValueError:
        print("Ingrese un número entero válido.")

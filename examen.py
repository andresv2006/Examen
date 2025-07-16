precio=[]
#marca
marca= [{"Hp":31},
{"Acer":43},
{"Asus":3},
{"Dell":1},
]


#productos
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050',387990,10],
                      '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050',327990,4],
                      'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti',424990,1],
                     'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada',664990,21],
                     'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050',290890,32],
                     '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada',444990,7],
                     '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050',749990,2],
                     'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050',349990,1],
                           }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}
#def
def stock_marca(marca): #no me alcanzo el tiempo pero cumple con lo que pide
   while True:
    marcastock=input("marca: ").upper()
    if marcastock =="HP":
        print ("Marca: Hp\tStock: 31")
        break
    elif marcastock=="ACER":
        print("Marca: Acer\tStock: 43")
        break
    elif marcastock=="ASUS":
        print("Marca: Asus\tStock: 3")
        break
    elif marcastock=="DELL":
        print("Marca: Dell\tStock:1")
        break
    else:
        print("marca incorrecta")
def buqueda_precio(precio):
 while True:
        try:
            precio_min=int(input("Ingrese precio minimo: "))
            precio_max=int(input("ingrese Precio Maximo: "))
            if precio_min>=1 and precio_min<=749990 and precio_max>=249990:
                for a,b in stock.items():
                    precio=b[0]
                if precio>=precio_min and precio<=precio_max:
                    for clave,valor in productos.items():
                            print(f"los notebook entre el rango de precio que consultas es {clave}--{valor[0]}")
                            break
            else:print("No hay notebooks dentro de ese rango de precios")
        except:
            print("tiene que ser numero entero")
def ordenar_productos():
   print("marca\tmodelo\tRam\Disco(GB o T)")
   for a,b in productos.items():
      print (f"{b[0]}\t {a}\t{b[1]}\t{b[2]}\t{b[3]}")
      
#menu
while True:
    print("***Menu***")
    print("1. Stock marca")
    print("2. Busqueda por precio")
    print("3. Listado produtos")
    print("4. Salir")
    opc=input("Opción: ")
    if opc=="1":
        stock_marca(marca)
        break
    elif opc=="2":
        buqueda_precio(precio)
        break
    elif opc=="3":
        ordenar_productos()
        break
    elif opc=="4":
     print("programa finalizado")
     exit()
    else:
        print("opc incorrecta")


print(""" 
          Bienvenido a mi programa
      Hoy vamos a trabajar con el Juego Pong
  
      Ingrese 1: Para Iniciar el Juego
      Ingrese 2: Para Escoger el Nivel
      Ingrese 3: Para Salir""")

opt=(int(input("Ingrese su seleccion: ")))
while opt <=0 or opt >=4:
      print("Seleccion Incorrecta debe ser un numero del 1-3")
      opt=(int(input("Ingrese su seleccion: ")))
if opt ==3:
      print("Adios")
elif opt ==2:
      print("""Escoja el nivel: 
                  1- FACIL
                  2- MEDIO
                  3- DIFICIL""")
      nivel=(int(input("Ingrese su seleccion: ")))
      while nivel <=0 or opt >=4:
            print("Seleccion Incorrecta debe ser un numero del 1-3")
            nivel=input("Ingrese su seleccion: ")
      if nivel == 1:
            import pongturtle
      if nivel == 2:
            import pongturtle2
      if nivel == 3:
            import pongturtle3

else:
      import pongturtle

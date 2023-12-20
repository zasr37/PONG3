import turtle
#Creacion ventana tamaño, color 
ventana = turtle.Screen()
ventana.title("Pong by ZAS")
ventana.bgcolor("black")
ventana.setup(width=800,height=600)
ventana.tracer(0)
#Creacion creacion jugador A
JugadorA= turtle.Turtle()
JugadorA.speed(0)
JugadorA.shape("square")
JugadorA.color("blue")
JugadorA.penup()
JugadorA.goto(-350,0)
JugadorA.shapesize(stretch_wid=5,stretch_len=1)
#Creacion jugador B

JugadorB= turtle.Turtle()
JugadorB.speed(0)
JugadorB.shape("square")
JugadorB.color("green")
JugadorB.penup()
JugadorB.goto(350,0)
JugadorB.shapesize(stretch_wid=5,stretch_len=1)

#Creacion balon
Balon= turtle.Turtle()
Balon.speed(0)
Balon.shape("circle")
Balon.color("white")
Balon.penup()
Balon.goto(0,0)
Balon.dx= 0.50
Balon.dy= -0.50
#Creacion linea central
Linea= turtle.Turtle()
Linea.color("white")
Linea.goto(0,400)
Linea.goto(0,-400)
#Marcador
marcador= turtle.Turtle()
marcador.speed(0)
marcador.color("red")
marcador.penup()
marcador.hideturtle()
marcador.goto(0,260)
marcador.write("Jugador A: 0     Jugador B: 0",align= "center", font=("Courier", 24, "normal"))
#Puntaje
PuntajeA=0
PuntajeB=0

#Movimiento Arriba jugador A y limites
def JugadorA_up():
    y = JugadorA.ycor()
    y += 50
    if y > 290:
        y= 240
    JugadorA.sety(y)
#Movimiento Abajo jugador A y limites 
def JugadorA_down():
    y = JugadorA.ycor()
    y -= 50
    if y < -290:
        y=-240
    JugadorA.sety(y)
ventana.listen()
ventana.onkeypress(JugadorA_up,"w")
ventana.onkeypress(JugadorA_down,"s")
#Movimiento Arriba jugador B y limites
def JugadorB_up():
    y = JugadorB.ycor()
    y += 50
    if y >290:
        y = 240
    JugadorB.sety(y)
#Movimiento Abajo jugador B y limites 
def JugadorB_down():
    y = JugadorB.ycor()
    y -= 50
    if y < -290:
        y=-240
    JugadorB.sety(y)
ventana.listen()
ventana.onkeypress(JugadorB_up,"8")
ventana.onkeypress(JugadorB_down,"5")
#Balon movimiento

while True:
    ventana.update()
    Balon.setx(Balon.xcor()+Balon.dx)
    Balon.sety(Balon.ycor()+Balon.dy)
#Balon limites superiores y cambio de sentido
    if Balon.ycor()> 290:
        Balon.dy *=-1
    if Balon.ycor()< -290:
        Balon.dy *=-1
#Balon costados, retorno y cambio de lado
#Actulizacion de marcador
    if Balon.xcor()> 390:
        Balon.goto(0,0)
        Balon.dx= 0.50
        Balon.dy= -0.50
        Balon.dx *= -1
        PuntajeA += 1
        marcador.clear()
        marcador.write("Jugador A: {}     Jugador B: {}".format(PuntajeA,PuntajeB),align= "center", font=("Courier", 24, "normal"))
    if Balon.xcor()< -390:
        Balon.goto(0,0)
        Balon.dx= 0.50
        Balon.dy= -0.50
        Balon.dx *= -1
        PuntajeB += 1
        marcador.clear()
        marcador.write("Jugador A: {}     Jugador B: {}".format(PuntajeA,PuntajeB),align= "center", font=("Courier", 24, "normal"))
#Golpe paleta jugador A y cambio de sentido
    if ((Balon.xcor() >340 and Balon.xcor()<350)
        and (Balon.ycor()< JugadorB.ycor()+50
             and Balon.ycor() >JugadorB.ycor()-50)):
        Balon.dx *=-1
        if(Balon.dy>0 and Balon.dy<1):  
            Balon.dy+=0.05  
        elif(Balon.dy<0 and Balon.dy>-5):
            Balon.dy-=0.05  
        if(Balon.dx>0 and Balon.dx<5):
            Balon.dx+=0.05  
        elif(Balon.dx<0 and Balon.dx>-5): 
            Balon.dx-=0.05  
#Golpe paleta jugador B y cambio de sentido 
    if ((Balon.xcor() < -340 and Balon.xcor()> -350)
        and (Balon.ycor()< JugadorA.ycor()+50
             and Balon.ycor() >JugadorA.ycor()-50)):
        Balon.dx *=-1
        if(Balon.dy>0 and Balon.dy<1):  
            Balon.dy+=0.05  
        elif(Balon.dy<0 and Balon.dy>-5):
            Balon.dy-=0.05  
        if(Balon.dx>0 and Balon.dx<5):
            Balon.dx+=0.05  
        elif(Balon.dx<0 and Balon.dx>-5): 
            Balon.dx-=0.05
       
#Intentos pantalla finalizacion
    if PuntajeA>=3:
        marcadorfinalA= turtle.Turtle()
        marcadorfinalA.speed(0)
        marcadorfinalA.color("green")
        marcadorfinalA.penup()
        marcadorfinalA.hideturtle()
        marcadorfinalA.goto(0,0)
        marcadorfinalA.write("Jugador A GANA FELIDADES",align= "center", font=("Courier", 25, "normal"))
        turtle.done()
    if PuntajeB>=3:
        marcadorfinalB= turtle.Turtle()
        marcadorfinalB.speed(0)
        marcadorfinalB.color("green")
        marcadorfinalB.penup()
        marcadorfinalB.hideturtle()
        marcadorfinalB.goto(0,0)
        marcadorfinalB.write("Jugador B GANA FELIDADES",align= "center", font=("Courier", 35, "normal"))
        turtle.done()

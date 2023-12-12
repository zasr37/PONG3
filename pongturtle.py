import turtle
#Creacion ventana tamaño, color 
ventana = turtle.Screen()
ventana.title("Pong by ZAS")
ventana.bgcolor("black")
ventana.setup(width=800,height=600)
ventana.tracer(0)
#Creacion cracion jugador A
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
Balon.speed(1)
Balon.shape("circle")
Balon.color("white")
Balon.penup()
Balon.goto(0,0)
Balon.dx= 0.20
Balon.dy= 0.20
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

#Movimiento Arriba jugador A
def JugadorA_up():
    y = JugadorA.ycor()
    y += 20
    JugadorA.sety(y)
#Movimiento Abajo jugador A
def JugadorA_down():
    y = JugadorA.ycor()
    y -= 20
    JugadorA.sety(y)
ventana.listen()
ventana.onkeypress(JugadorA_up,"w")
ventana.onkeypress(JugadorA_down,"s")
#Movimiento Arriba jugador B
def JugadorB_up():
    y = JugadorB.ycor()
    y += 20
    JugadorB.sety(y)
#Movimiento Abajo jugador B
def JugadorB_down():
    y = JugadorB.ycor()
    y -= 20
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
        Balon.dx *= -1
        PuntajeA += 1
        marcador.clear()
        marcador.write("Jugador A: {}     Jugador B: {}".format(PuntajeA,PuntajeB),align= "center", font=("Courier", 24, "normal"))
    if Balon.xcor()< -390:
        Balon.goto(0,0)
        Balon.dx *= -1
        PuntajeB += 1
        marcador.clear()
        marcador.write("Jugador A: {}     Jugador B: {}".format(PuntajeA,PuntajeB),align= "center", font=("Courier", 24, "normal"))
#Golpe paleta jugador B y cambio de sentido
    if ((Balon.xcor() >340 and Balon.xcor()<350)
        and (Balon.ycor()< JugadorB.ycor()+50
             and Balon.ycor() >JugadorB.ycor()-50)):
        Balon.dx *=-1
#Golpe paleta jugador B y cambio de sentido 
    if ((Balon.xcor() < -340 and Balon.xcor()> -350)
        and (Balon.ycor()< JugadorA.ycor()+50
             and Balon.ycor() >JugadorA.ycor()-50)):
        Balon.dx *=-1



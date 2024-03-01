import turtle
t = turtle.Turtle()
t.speed(10)
s = turtle.Screen()
s.title('Namas')
####
#### Funkcija, kuri nupiešia vieną langą
def staciakampis():
    t.pensize(2)
    t.fillcolor('white')
    t.begin_fill()
    for i in range(4):
        t.fd(krastineD[i%len(krastineD)])
        t.lt(360/4)
    t.end_fill()
    t.pensize(1)
    for i in range (2):
        for j in range(4):
            t.fd(krastineM[j%len(krastineM)])
            t.lt(360/4)
        t.fd(krastineD[0]/2)
####        
langai = int(s.textinput('Duomenų įvedimas', 'Kiek langų viename aukšte (maks. 7)?'))
aukstai = int(s.textinput('Duomenų įvedimas', 'Kiek aukštų namas? (maks. 6)'))
####
#### Skaičiavimai
krastinesIlgis = 100
# Didelio lango kraštinė
krastineD = [krastinesIlgis/1.5,krastinesIlgis]
# Mažo lango kraštinė
krastineM = [krastineD[0]/2,krastineD[1]/1.5]
namoIlgis = (langai * krastineD[0]) * 2 + krastineD[0]
namoAukstis = (aukstai * krastinesIlgis) + (aukstai * krastineM[0]) + krastineM[0]
namas = [namoIlgis, namoAukstis]
####
t.penup()
pradziaX = -namoIlgis/2
pradziaY = -namoAukstis/2
t.goto(pradziaX,pradziaY)
t.pendown()
#### Namo fasadas
t.pensize(0)
t.pencolor('light blue')
t.fillcolor('light blue')
t.begin_fill()
for i in range(4):
    t.fd(namas[i%len(namas)])
    t.lt(360/4)
t.end_fill()
####
#### Langų piešimas
t.penup()
pradziaPirmoLangoX = pradziaX + krastineD[0]
pradziaPirmoLangoY = pradziaY + krastineM[0]
t.goto(pradziaPirmoLangoX,pradziaPirmoLangoY)
t.pendown()
t.pencolor('black')
####
pradziaLangoY = pradziaPirmoLangoY
for i in range (aukstai):
    for j in range (langai):
        staciakampis()
        t.penup()
        t.fd(krastineM[1])
        t.pendown()
    t.penup()
    pradziaLangoY += krastinesIlgis+krastineM[0]
    t.goto(pradziaPirmoLangoX,pradziaLangoY)
    t.pendown()
####
s.exitonclick()
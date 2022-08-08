import pgzrun, pygame, random, math
import numpy as np

TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708
POPULATION = 20
global tam
global randomnumber
global ftime

class Neuronios():
	
    def Sigmoid(self, neuron):
        self.neuron = z = 1/(1 + np.exp(-neuron))
        return self.neuron
        
    def __init__(self, entrada1, entrada2):

        self.peso1 = random.uniform(-1.0, 1.0)
        self.peso2 = random.uniform(-1.0, 1.0)
        self.peso3 = random.uniform(-1.0, 1.0)
        self.peso4 = random.uniform(-1.0, 1.0)
        self.peso5 = random.uniform(-1.0, 1.0)
        self.peso6 = random.uniform(-1.0, 1.0)
        self.Neuron1 = entrada1
        self.Neuron2 = entrada2
        self.Neuron3 = self.Sigmoid((self.Neuron1*self.peso1) + (self.Neuron2*self.peso3))
        self.Neuron4 = self.Sigmoid((self.Neuron1*self.peso2) + (self.Neuron2*self.peso4))
        self.Neuron5 = self.Sigmoid((self.Neuron4*self.peso5) + (self.Neuron3*self.peso6))

def Sigmoide(num):
    neuron = z = 1/(1 + np.exp(-num))
    return neuron

def Verifica(i, entrada1, entrada2):
    Neuronio1 = Sigmoide((pesoPassaro[i][0]*entrada1) + (pesoPassaro[i][2]*entrada2))
    Neuronio2 = Sigmoide((pesoPassaro[i][1]*entrada1) + (pesoPassaro[i][3]*entrada2))
    Neuronio3 = Sigmoide((pesoPassaro[i][4]*Neuronio2) + (pesoPassaro[i][5]*Neuronio1))
    return Neuronio3

def update():
    global ftime
    global randomnumber
    global tam
    g = 0
    o = 0
    for d in range (1, 10):
     if (barry_the_bird[d].alive):
       barry_the_bird[d].speed += gravity
       barry_the_bird[d].y += barry_the_bird[d].speed
     else:
       barry_the_bird[d].y = -100
    if (barry_the_bird[0].alive):
      barry_the_bird[0].speed += gravity
      barry_the_bird[0].y += barry_the_bird[0].speed
    else:
      barry_the_bird[0].y = -100
    top_pipe.x += scroll_speed
    bottom_pipe.x += scroll_speed
    if top_pipe.right < 0:
       randomnumber = random.randint(300, 600)*-1
       top_pipe.topleft = (WIDTH, randomnumber)
       bottom_pipe.topleft = (WIDTH, top_pipe.height + gap + randomnumber)
       top_pipe.pair_number += 1
       o = top_pipe.height+randomnumber
       print(o)
       ftime = 0
    for d in range (1, 10):
      if ftime == 1:
       param1 = abs((top_pipe.x - barry_the_bird[d].x)/WIDTH)
       param2 = abs(((top_pipe.height - 400) - barry_the_bird[d].y)/HEIGHT)
       IA = Verifica(d-1, param1, param2)
       if IA > 0.5:
        if (barry_the_bird[d].alive):
            barry_the_bird[d].speed = -5.5
      else:
       param1 = abs((top_pipe.x - barry_the_bird[d].x)/WIDTH)
       param2 = abs(((top_pipe.height + randomnumber) - barry_the_bird[d].y)/HEIGHT)
       IA = Verifica(d-1, param1, param2)
       if IA > 0.5:
        if (barry_the_bird[d].alive):
            barry_the_bird[d].speed = -5.5
    for d in range (0, 10):
       if barry_the_bird[d].y > HEIGHT or barry_the_bird[d].y < 0:
         save_score(d)
         barry_the_bird[d].alive = False
       if (barry_the_bird[d].alive == False):
         g += 1
         if g == 10:
           CrossOver()
           reset()
       if (barry_the_bird[d].colliderect(top_pipe) or barry_the_bird[d].colliderect(bottom_pipe) or barry_the_bird[d].colliderect(base)):
         save_score(d)
         hit_pipe(d)
       if barry_the_bird[d].x > top_pipe.x:
         updateScore(d)

def draw():
    screen.blit('background', (0, 0))
    for d in range (0, 10):
      barry_the_bird[d].draw()
    screen.draw.text('Score = '+str(barry_the_bird[0].score), center=(200, 20), color="black")
    top_pipe.draw()
    bottom_pipe.draw()
    base.draw()

def on_mouse_down():
	if(barry_the_bird[0].alive):
	    barry_the_bird[0].speed = -5.5

def reset():
    global ftime
    global tam
    ftime = 1
    print ("Back to the start...")
    top_pipe.pair_number = 1
    for d in range (0, 10):
	    barry_the_bird[d].score = 0
	    barry_the_bird[d].speed = 1
	    barry_the_bird[d].center = (random.randint(75,150), random.randint(100, 600))
	    barry_the_bird[d].image = "bird" + str(d)
	    barry_the_bird[d].alive = True
    tam = -400
    top_pipe.midtop = (300, tam)
    bottom_pipe.midtop = (300, top_pipe.height + gap + tam)
    base.center = (200, 700)

def hit_pipe(d):
    barry_the_bird[d].image = "birddead"
    barry_the_bird[d].alive = False

def save_score(d):
    if (barry_the_bird[d].alive == True):
       a.append(barry_the_bird[d].score)

def CrossOver():
       k = 0
       n = 0
       m = 0
       r = random.randint(0, 100)
       a.sort()
       for d in range(1, 10):
        cont = 0
        if barry_the_bird[d].score == a[9]:
           m = d
        if barry_the_bird[d].score == a[8]:
           k = d
        if barry_the_bird[d].score == a[0]:
           n = d
       AcharMelhorP()
       if a[9] == 0:
        m = random.randint(1, 9)
        n = random.randint(1, 9)
       if m == n:
        m -= 1
       if(r == 1):
        Mutacao()
       j = pesoPassaro[m-1][5]
       c = pesoPassaro[m-1][4]
       pesoPassaro[m-1][5] = pesoPassaro[k-1][5]
       pesoPassaro[m-1][4] = pesoPassaro[k-1][4]
       pesoPassaro[k-1][5] = j
       pesoPassaro[k-1][4] = c

       pesoPassaro[m-1][0] = pesoPassaro[n-1][0]
       pesoPassaro[m-1][1] = pesoPassaro[n-1][1]
       pesoPassaro[m-1][2] = pesoPassaro[n-1][2]
       pesoPassaro[k-1][3] = pesoPassaro[n-1][3]
       pesoPassaro[k-1][4] = pesoPassaro[n-1][4]
       pesoPassaro[k-1][5] = pesoPassaro[n-1][5]
       a.clear()

def Mutacao():
    zapdo = random.randint(1, 9)
    role = random.randint(0, 5)
    print(f'Mutacao no passaro {zapdo}')
    print(zapdo-1)
    print(role)
    pesoPassaro[zapdo-1][role] = random.uniform(-1.0, 1.0)

def updateScore(d):
    if (barry_the_bird[d].alive):
        barry_the_bird[d].score = top_pipe.pair_number

def AcharMelhorP():
    za = 5
    zozo = [99]*10
    for d in range(0, 10):
      cont = 0
      for kk in range(0, 10):
        if barry_the_bird[kk].score == a[d] and cont != 1:
           zozo[d] = kk
           cont = 1
           for n in range(0, d):
             if zozo[d] == zozo[n]:
                cont = 0
    Elitismo(zozo)
    print(zozo)
    print(pesoPassaro[0])
    for i in range(0, za):
     if zozo[i] != 0:
      pesoPassaro[zozo[i]-1][0] = random.uniform(-1.0, 1.0)
      pesoPassaro[zozo[i]-1][1] = random.uniform(-1.0, 1.0)
      pesoPassaro[zozo[i]-1][2] = random.uniform(-1.0, 1.0)
      pesoPassaro[zozo[i]-1][3] = random.uniform(-1.0, 1.0)
      pesoPassaro[zozo[i]-1][4] = random.uniform(-1.0, 1.0)
      pesoPassaro[zozo[i]-1][5] = random.uniform(-1.0, 1.0)
     else:
      za += 1
    print(pesoPassaro[0])

def Elitismo(zozo):
    for i in range(0, 6):
     pesoPassaro[zozo[6]-1][i] = pesoPassaro[zozo[9]-1][i]

global a
a = []
barry_the_bird = []
list = []
pesoPassaro = []
for d in range (0, 10):
    barry_the_bird.append(Actor('bird'+str(d)))
for d in range(0, 9):
    pesoPassaro.append([0] * 6)
for i in range(0, 9):
    list.append(Neuronios(1, 1))
    pesoPassaro[i][0] = list[i].peso1
    pesoPassaro[i][1] = list[i].peso2
    pesoPassaro[i][2] = list[i].peso3
    pesoPassaro[i][3] = list[i].peso4
    pesoPassaro[i][4] = list[i].peso5
    pesoPassaro[i][5] = list[i].peso6
gap = 150
base = Actor('base')
top_pipe = Actor('top')
bottom_pipe = Actor('bottom')
scroll_speed = -1
gravity = 0.3
reset()

pgzrun.go()
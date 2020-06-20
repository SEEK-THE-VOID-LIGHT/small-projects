#!/urs/bin/python

import pygame
import random as r
pygame.init()
win = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
icon = pygame.image.load('turtle3.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("TURTLE RACE")
winner = pygame.image.load('winnercup.png')
turtleimages = [pygame.image.load('turtle1.png'),pygame.image.load('turtle2.png'),pygame.image.load('turtle3.png'),pygame.image.load('turtle4.png'),pygame.image.load('turtle5.png')]
names = ["red", "yellow", "green", "blue", "purple"]


class turtle(object):
    def __init__(self, x, y, image, name):
        self.x = x
        self.y = y
        self.image = image
        self.finished = False
        self.score = 0
        self.name = name

    def draw(self):
        win.blit(turtleimages[self.image], (self.x, self.y))

    def collision(self):
        if self.y <=5:
            return True

def save_scores():
    turtle1_score = 500 - turtles[0].y
    turtle2_score = 500 - turtles[1].y
    turtle3_score = 500 - turtles[2].y
    turtle4_score = 500 - turtles[3].y
    turtle5_score = 500 - turtles[4].y
    with open('turtle0.txt', "a") as file:
        file.write(str(turtle1_score)+"\n")
    with open('turtle1.txt', "a") as file:
        file.write(str(turtle2_score)+"\n")
    with open('turtle2.txt', "a") as file:
        file.write(str(turtle3_score)+"\n")
    with open('turtle3.txt', "a") as file:
        file.write(str(turtle4_score)+"\n")
    with open('turtle4.txt', "a") as file:
        file.write(str(turtle5_score)+"\n")

def clear_files():
    with open('turtle0.txt','w') as file:
        file.write("")
    with open('turtle1.txt','w') as file:
        file.write("")
    with open('turtle2.txt','w') as file:
        file.write("")
    with open('turtle3.txt','w') as file:
        file.write("")
    with open('turtle4.txt','w') as file:
        file.write("")

def evaluate(turtle_number):
    tempscore = 0
    url = f"turtle{turtle_number}.txt"
    with open(url, "r") as file:
        lines = file.readlines()
        for line in lines:
            tempscore += int(line)
    #print(tempscore)
    return tempscore

def calculate():
    temparray = []
    for i in range(5):
        temparray.append(turtles[i].score)
    index = temparray.index(max(temparray))
    return index

def redraw():
    win.fill((255,255,255))
    if visible:
        for i in turtles:
            i.draw()
    if not visible:
        font = pygame.font.SysFont('comicsans', 50)
        text = font.render(f"The {turtles[winnerid].name} turtle has WON", 1, (0,0,0))
        win.blit(text, (15,100))
        win.blit(winner, (120,200))
    pygame.display.update()

if __name__ == "__main__":
    clear_files()
    run = True
    moving = True
    visible = True
    winnerid = 0
    clock.tick(27)
    turtles = []
    for i in range(5):
        turtles.append(turtle(100*i + 30, 450, i, names[i]))
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            moving = False
            visible = False
            for i in range(5):
                turtles[i].score = evaluate(i)
            winnerid = calculate()


        if moving:
            for i in turtles:
                if i.collision():
                    save_scores()
                    for i in turtles:
                        i.y = 450
                    break

        for i in turtles:
            tint = r.randint(30, 100) // 100
            i.y -= tint
        redraw()

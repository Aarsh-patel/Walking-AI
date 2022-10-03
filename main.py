import pygame
import time,sys,math,pymunk

pygame.init()
joints = []
bones = []
muscles = []
n_list = []
def dist(mouse,joints):
    for i in joints:
        if math.sqrt(pow(i[0]-mouse[0],2)+pow(i[1]-mouse[1],2)) < 10:
            return i
def dist_mid(mouse,bones):
    i=0
    while i<len(bones):
        n_list.append(((bones[i][0] + bones[i+1][0])/2, (bones[i][1] + bones[i+1][1])/2))
        i+=2
    for i in n_list:
        if math.sqrt(pow(i[0]-mouse[0],2)+pow(i[1]-mouse[1],2)) < 10:
            return i
is_joint = False
is_bone = False
is_muscle = False
sim = False
def joint(mouse):
    global is_joint
    if(mouse[0]>120):
        if is_joint:    
            joints.append(mouse)
            is_joint = 2
def bone(a):
    global is_bone
    is_bone = 2
res = (1080,780)
bg = pygame.image.load("myCanvas.jpg")
screen = pygame.display.set_mode(res)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Corbel',30)
imp = pygame.font.SysFont('Corbel',25,bold=True)
color = (0,0,0)
text = smallfont.render('Joint' , True , color)
text1 = smallfont.render('Muscle' , True , color)
text2 = smallfont.render('Bone' , True , color)
text3 = imp.render('Simulate' , True , (255,255,255))
while not sim:
    screen.blit(bg, (0, 0))
    for ev in pygame.event.get():  
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 890 <= mouse[0] <= 1100 and height/2+240 <= mouse[1] <= height/2+280:
                is_joint = False
                sim = True
            if is_joint:
                joint(mouse)
            if 0 <= mouse[0] <= 120 and height/2+40 <= mouse[1] <= height/2+80:
                # Joint
                is_joint = True
                is_muscle = False
                is_bone = False
                
            if 0 <= mouse[0] <= 120 and height/2 <= mouse[1] <= height/2+40:
                # muscle
                is_bone = False
                is_joint = False
                is_muscle = True
            if is_muscle == 1:
                c = dist_mid(mouse,bones)
                if c:
                    is_muscle = 2
            if is_muscle == 3:
                d = dist_mid(mouse,bones)
                if d:
                    muscles.append(c)
                    muscles.append(d)
                is_muscle = False
            if 0 <= mouse[0] <= 120 and height/2-40 <= mouse[1] <= height/2:
                is_muscle = False
                is_joint = False
                is_bone = True
                # bone()
            if is_bone==1:
                a=dist(mouse,joints)
                if a:
                    bone(a)
            
            if is_bone == 3:
                b = dist(mouse,joints)
                if b:
                    bones.append(a)
                    bones.append(b)
                is_bone = False
    mouse = pygame.mouse.get_pos()
    if is_bone == 2 or is_bone == 3:
        pygame.draw.line(screen,(255,0,0),a,mouse,10)
        is_bone = 3
    if is_muscle == 2 or is_muscle == 3:
        pygame.draw.line(screen,(125,120,0),c,mouse,10)
        is_muscle = 3
    if is_joint==2 or is_joint:
        pygame.draw.circle(screen,(255,255,0),mouse,10)
    pygame.draw.rect(screen, (255,255,0), pygame.Rect(0, height/2-5, 120, 40))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, height/2-5, 120, 40),1)
    pygame.draw.rect(screen, (255,255,0), pygame.Rect(0, height/2-45, 120, 40))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, height/2-45, 120, 40),1)
    pygame.draw.rect(screen, (255,255,0), pygame.Rect(0, height/2+35, 120, 40))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, height/2+35, 120, 40),1)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(890, height/2+240, 120, 50))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(890, height/2+240, 120, 50),1)

    screen.blit(text , (10,height/2+40))
    screen.blit(text1 , (10,height/2))
    screen.blit(text2 , (10,height/2-40))
    screen.blit(text3 , (900,height/2+250))
    for coord in joints:
        pygame.draw.circle(screen,(255,0,0),coord,10)
    j=0
    while j < len(muscles):
        pygame.draw.line(screen,(255,100,100),muscles[j],muscles[j+1],10)
        j+=2
    if is_muscle:
        for n in n_list:
            pygame.draw.circle(screen,(255,125,0),n,10)
    i=0
    while i < len(bones):
        pygame.draw.line(screen,(255,0,0),bones[i],bones[i+1],10)
        i+=2
    pygame.display.update()
clock = pygame.time.Clock()
class organism:
    def __init__(self):
        self.score = 0
        self.x = 0
        self.y = 0
    def update(self):
        for i in range(len(joints)):
            coord = joints[i]
            if coord[1]<640:
                print("coord")
                coord=(coord[0],coord[1]+10)
                joints[i] = coord
            else:
                coord=(coord[0],640)
                joints[i] = coord
    def draw(self):
        for coord in joints:
            pygame.draw.circle(screen,(255,0,0),coord,10)
        j=0
        while j < len(muscles):
            pygame.draw.line(screen,(255,100,100),muscles[j],muscles[j+1],10)
            j+=2
        i=0
        while i < len(bones):
            pygame.draw.line(screen,(255,0,0),bones[i],bones[i+1],10)
            i+=2
org = organism()
screen.fill((0,120,0))
while sim:
    clock.tick(60)
    screen.blit(bg, (0, 0))
    pygame.draw.line(screen,(255,0,0),(0,649),(1280,649),1)
    for ev in pygame.event.get():  
        if ev.type == pygame.QUIT:
            pygame.quit()
    org.draw()
    org.update()
    pygame.display.update()
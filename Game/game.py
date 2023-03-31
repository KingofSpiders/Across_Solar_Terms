import os
import sys
import pygame

def wj():
    pass

def opengame(numofgame):
    if numofgame>end+1:
        pass
    else:
        wsetting = open(os.getcwd()+"\\Game\\Data\\sap.dat",'w')
        wsetting.write(str(numofgame-1))
        wsetting.close()
        os.system("start "+os.getcwd()+"\\Game\\Data\\main.exe")
        pygame.quit()
        sys.exit()

position=[[[],[],[],[],[],[]],
          [[],[],[],[],[],[]],
          [[],[],[],[],[],[]],
          [[],[],[],[],[],[]]]
pygame.init()

screen = pygame.display.set_mode((1280,760))
pygame.display.set_caption('穿越节气')

screen.fill((80,80,200))

k=1
for i in range(4):
    for j in range(6):
        x=25+(j*30)+(j*180)
        y=8+(i*8)+(i*180)
        screen.blit(pygame.image.load(os.getcwd()+"\\Game\\Data\\Intro\\n"+str(k)+".png"),(x,y))
        position[i][j].append(x)
        position[i][j].append(y)
        position[i][j].append(x+180)
        position[i][j].append(y+180)
        k+=1
screen.blit(pygame.image.load(os.getcwd()+"\\Game\\Data\\Intro\\1.png"),(25,8))
asetting = open(os.getcwd()+"\\Game\\Data\\sap.dat","a");asetting.close();del asetting
rsetting = open(os.getcwd()+"\\Game\\Data\\sap.dat","r")
setting=rsetting.readlines()
rsetting.close()
end=0
if setting != []:
    if setting[0]=="24":
        wj()
    end=int(setting[0].strip())
    k=1
    for i in range(4):
        for j in range(6):
            x=25+(j*30)+(j*180)
            y=8+(i*8)+(i*180)
            if k<=(end+1):
                screen.blit(pygame.image.load(os.getcwd()+"\\Game\\Data\\Intro\\"+str(k)+".png"),(x,y))
            k+=1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os.system("start "+os.getcwd()+"\\launcher.exe")
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex,mousey=event.pos
            if mousex>25 and mousey>8 and mousex<205 and mousey<188:
                opengame(1)
            elif mousex>235 and mousey>8 and mousex<415 and mousey<188:
                opengame(2)
            elif mousex>445 and mousey>8 and mousex<625 and mousey<188:
                opengame(3)
            elif mousex>655 and mousey>8 and mousex<835 and mousey<188:
                opengame(4)
            elif mousex>865 and mousey>8 and mousex<1045 and mousey<188:
                opengame(5)
            elif mousex>1075 and mousey>8 and mousex<1255 and mousey<188:
                opengame(6)
            elif mousex>25 and mousey>196 and mousex<205 and mousey<376:
                opengame(7)
            elif mousex>235 and mousey>196 and mousex<415 and mousey<376:
                opengame(8)
            elif mousex>445 and mousey>196 and mousex<625 and mousey<376:
                opengame(9)
            elif mousex>655 and mousey>196 and mousex<835 and mousey<376:
                opengame(10)
            elif mousex>865 and mousey>196 and mousex<1045 and mousey<376:
                opengame(11)
            elif mousex>1075 and mousey>196 and mousex<1255 and mousey<376:
                opengame(12)
            elif mousex>25 and mousey>384 and mousex<205 and mousey<564:
                opengame(13)
            elif mousex>235 and mousey>384 and mousex<415 and mousey<564:
                opengame(14)
            elif mousex>445 and mousey>384 and mousex<625 and mousey<564:
                opengame(15)
            elif mousex>655 and mousey>384 and mousex<835 and mousey<564:
                opengame(16)
            elif mousex>865 and mousey>384 and mousex<1045 and mousey<564:
                opengame(17)
            elif mousex>1075 and mousey>384 and mousex<1255 and mousey<564:
                opengame(18)
            elif mousex>25 and mousey>572 and mousex<205 and mousey<752:
                opengame(19)
            elif mousex>235 and mousey>572 and mousex<415 and mousey<752:
                opengame(20)
            elif mousex>445 and mousey>572 and mousex<625 and mousey<752:
                opengame(21)
            elif mousex>655 and mousey>572 and mousex<835 and mousey<752:
                opengame(22)
            elif mousex>865 and mousey>572 and mousex<1045 and mousey<752:
                opengame(23)
            elif mousex>1075 and mousey>572 and mousex<1255 and mousey<752:
                opengame(24)
            else:
                pass
    pygame.display.flip()
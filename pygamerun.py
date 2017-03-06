import pygame,sys,glob,time
import serial
from pygame import *
pygame.init()
import time

width=1300
height=700
cyan=(0,255,255)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("First Game On My Own!!!!")
clock=pygame.time.Clock()
currentimage=1
m1=pygame.image.load("run0.png")
m2=pygame.image.load("run4.png")
track=pygame.image.load('Game_play.jpg')
ser = serial.Serial(
    port='COM19',\
    baudrate=38400,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(cyan)
        text_size=pygame.font.Font("freesansbold.ttf",116) ##to display msg we are loading a font and its size
        surf,rect=text_objects("Aimless Run",text_size)
        rect.center=((width/2),(height/2))
        screen.blit(surf,rect)
        #button("Start",200,400,100,50,green)
        #button("Quit",100,100,100,50,green)
        #time.sleep(2)
        
        button("Start",500,400,100,50,green,game_loop)
        #small_text=pygame.font.Font('freesansbold.ttf',30)
        #surface,rectangle=text_objects("Start!",small_text)
        #rectangle.center=((250),(425))
        #screen.blit(surface,rectangle)
        #pygame.display.update()
        #clock.tick(100)
def button(msg,x,y,w,h,ac,action=None):
    pygame.draw.rect(screen,ac,(x,y,w,h))
    click = pygame.mouse.get_pressed()
    if click[0] == 1 and action != None:
            action() 
    #pygame.draw.rect(screen,white,(400,400,100,50))
    #mouse=pygame.mouse.get_pos()
    #print mouse
    
    small_text=pygame.font.Font('freesansbold.ttf',30)
    surface,rectangle=text_objects(msg,small_text)
    rectangle.center=((x+(w/2)),(y+(h/2)))
    screen.blit(surface,rectangle)
    pygame.display.update()
def urscore(count):
    font = pygame.font.SysFont("comicsansms", 25)##to get the system font and its size
    text = font.render("Your Score: "+str(count), True, black) ##.render is used to put some text on the surface using the font 
    screen.blit(text,(0,30))

def text_objects(text, font):
    textSurface = font.render(text, True, blue) ##again getting a font and rendering a text to it
    return textSurface, textSurface.get_rect()  ##need surface to write and shape of the surface here is rectangle
def message_display(text):
    text_size=pygame.font.Font('freesansbold.ttf',30) ##to display msg we are loading a font and its size
    surf,rect=text_objects(text,text_size)    
    screen.blit(surf,rect)
    pygame.display.update()
def crash(timet):
    message_display('Time taken by you:' +str(timet) +' seconds')
    #message_display('\will begin after 30 seconds')
    time.sleep(3)
    game_intro()
    game_loop()
def game_loop():
    #game_intro()
    rflag=0
    lflag=0
    rimage=0
    limage=0
    key_count=0
    score=0
    timeFlag=0
    currentimage=1
    pic_x=230
    pic_y=400
    track_x=0
    track_y=0
    #track_x1=0
    #track_y1=-500
    crashed=False
    key_count=0
    score=0
    #clock.tick(5)
    #time=0
    #crashed=False
    while not crashed:
        #for event in pygame.event.get():
            #if event.type==pygame.QUIT:
                #crashed=True
        x=0
        x=ser.read()
        #print x
        #if x==pygame.KEYDOWN:=0
        if (x is 'L' or x is 'R'):
            print "Milgya"
            
        if x is 'L' and lflag==0:
            ##start a timer here
            #start=time.time()
            #print start
            lflag=1
            rflag=0
            rimage=1
            limage=0
            if timeFlag==0:
                start=time.time()
                timeFlag=1
            pic_x+=25
            track_x-=25
            key_count+=2
            #print key_count
            score+=1
            print start
                    
            ##if score reaches a fixed value then stop the timer and measure time in
            ##between the events()
            if score>120:
                end=time.time()
                crash(end-start)
        if x is 'R' and rflag==0:
            ##start a timer here
            #start=time.time()
            #print start
            rflag=1
            lflag=0
            limage=1
            rimage=0
            if timeFlag==0:
                start=time.time()
                timeFlag=1
            pic_x+=25
            track_x-=25
            key_count+=2
            #print key_count
            score+=1
            print start
                    
            ##if score reaches a fixed value then stop the timer and measure time in
            ##between the events()
            if score>120:
                end=time.time()
                crash(end-start)
            if track_x==-3100:
                track_x=width/2
            if pic_x>width/2:
                pic_x=width/2
                    
                       
        screen.blit(track,(track_x,track_y))
        #screen.blit(m1,(pic_x,pic_y))
        if rimage==1 and limage==0:
            screen.blit(m1,(pic_x,pic_y))
        if limage==1 and rimage==0:
            screen.blit(m2,(pic_x,pic_y))
        #if currentimage==2:
            #currentimage=1
        #else:
            
            #currentimage+=1
        urscore(score)
        pygame.display.update()
        clock.tick(30)


game_intro()
game_loop()

pygame.quit()                
quit()

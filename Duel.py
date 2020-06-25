# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from time import sleep
from threading import Thread
from random import randint
from os import path
    
class BalleGauche(Thread):
    def _init_(self):
        Thread._init_(self)
    def run(self):
        global case_perso_l
        self.ligne = case_perso_l
        self.colonne = 1
        self.case_devant = 0
        self.vitesse = 0.06
        while self.colonne < 14:
            changerCase(self.colonne,self.ligne,0)
            self.case_devant = testCase(self.colonne+1,self.ligne)
            if self.case_devant > 0 and self.case_devant < 4:
                changerCase(self.colonne+1,self.ligne,self.case_devant-1)
                changerCase(self.colonne,self.ligne,0)
                return
            elif self.case_devant == 7:
                global perso_r_vivant
                perso_r_vivant = 0
                changerCase(self.colonne,self.ligne,0)
                return
            elif self.case_devant == 10:
                global score_l
                changerCase(self.colonne,self.ligne,0)
                score_l -= 10
                return
            else:
                self.colonne = self.colonne+1
                changerCase(self.colonne,self.ligne,15)
            sleep(self.vitesse)
        changerCase(self.colonne,self.ligne,0)
            
class BalleDroite(Thread):
    def _init_(self):
        Thread._init_(self)
    def run(self):
        global case_perso_r
        self.ligne = case_perso_r
        self.colonne = 13
        self.case_devant = 0
        self.vitesse = 0.06
        while self.colonne > 0:
            changerCase(self.colonne,self.ligne,0)
            self.case_devant = testCase(self.colonne-1,self.ligne)
            if self.case_devant > 0 and self.case_devant < 4:
                changerCase(self.colonne-1,self.ligne,self.case_devant-1)
                changerCase(self.colonne,self.ligne,0)
                return
            elif self.case_devant == 6:
                global perso_l_vivant
                perso_l_vivant = 0
                changerCase(self.colonne,self.ligne,0)
                return
            elif self.case_devant == 10:
                global score_r
                changerCase(self.colonne,self.ligne,0)
                score_r -= 10
                return
            else:
                self.colonne = self.colonne-1
                changerCase(self.colonne,self.ligne,16)
            sleep(self.vitesse)
        changerCase(self.colonne,self.ligne,0)
            


def afficherCarte():
    case_obstacle_y = -1
    case_obstacle_x = -1
    obstacle_x = 0
    obstacle_y = 0
    for ligne in carte:
            case_obstacle_y = case_obstacle_y+1
            case_obstacle_x = -1
            for case in ligne:
                    case_obstacle_x = case_obstacle_x+1
                    if case > 0 and case < 4:
                        obstacle_x = int(ResoEcran.current_w*case_obstacle_x*64/960)
                        obstacle_y = int(ResoEcran.current_h*case_obstacle_y*64/640)
                        screen.blit(cactus, (obstacle_x, obstacle_y))
                    elif case == 6:
                        obstacle_x = int(ResoEcran.current_w*case_obstacle_x*64/960)
                        obstacle_y = int(ResoEcran.current_h*case_obstacle_y*64/640)
                        screen.blit(perso_l, (obstacle_x, obstacle_y))
                    elif case == 7:
                        obstacle_x = int(ResoEcran.current_w*case_obstacle_x*64/960)
                        obstacle_y = int(ResoEcran.current_h*case_obstacle_y*64/640)
                        screen.blit(perso_r, (obstacle_x, obstacle_y))
                    elif case == 15:
                        obstacle_x = int(ResoEcran.current_w*case_obstacle_x*64/960)
                        obstacle_y = int(ResoEcran.current_h*case_obstacle_y*64/640)
                        screen.blit(tirL, (obstacle_x, obstacle_y))
                    elif case == 16:
                        obstacle_x = int(ResoEcran.current_w*case_obstacle_x*64/960)
                        obstacle_y = int(ResoEcran.current_h*case_obstacle_y*64/640)
                        screen.blit(tirR, (obstacle_x, obstacle_y))
                    elif case == 8:
                        obstacle_x = int(ResoEcran.current_w*case_obstacle_x*64/960)
                        obstacle_y = int(ResoEcran.current_h*case_obstacle_y*64/640)
                        screen.blit(perso_l_dead, (obstacle_x, obstacle_y))
                    elif case == 9:
                        obstacle_x = int(ResoEcran.current_w*case_obstacle_x*64/960)
                        obstacle_y = int(ResoEcran.current_h*case_obstacle_y*64/640)
                        screen.blit(perso_r_dead, (obstacle_x, obstacle_y))
                    elif case == 10:
                        obstacle_x = int(ResoEcran.current_w*case_obstacle_x*64/960)
                        obstacle_y = int(ResoEcran.current_h*case_obstacle_y*64/640)
                        screen.blit(ovni, (obstacle_x, obstacle_y))

def changerCase(x, y, valeur):
    try:
        ligne = carte[y]
        ligne[x] = valeur
        carte[y] = ligne
    except:
        return
                        
def testCase(x, y):
    if y >= len(carte) or y == -1:
    	return 1
    else:
    	ligne = carte[y]
    if x >= len(ligne) or x == -1:
    	return 1
    else:
    	valeur = ligne[x]
    return valeur

pygame.init()
global ResoEcran
ResoEcran = pygame.display.Info()
screen = pygame.display.set_mode((384, 576))
pygame.display.set_caption('FULLSCREEN ?')
fond = pygame.image.load(path.join('data','settingScreen.png')).convert()
choice = None
while choice is None:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            if event.pos[1] < 288:
                choice = True
            else:
                choice = False
    screen.blit(fond, (0,0))
    pygame.display.flip()
pygame.display.set_caption('DUEL !!!')
if choice:
    screen = pygame.display.set_mode((ResoEcran.current_w,ResoEcran.current_h),FULLSCREEN)
else:
    screen = pygame.display.set_mode((ResoEcran.current_w,ResoEcran.current_h))
pygame.mouse.set_visible(0)
global score_l
global score_r
score_l = 0
score_r = 0
boum = pygame.mixer.Sound(path.join("data","son.ogg"))
cache = pygame.Surface((200,54))
cache = cache.convert()
cache.fill((255, 255, 255))
showMes = True
cache = pygame.transform.scale(cache, (int(ResoEcran.current_w*200/960),int(ResoEcran.current_h*50/640)))
font = pygame.font.Font(None, int(ResoEcran.current_w*36/960))
musique = pygame.mixer.music.load(path.join("data","solo.ogg"))
selectorScreen = pygame.image.load(path.join("data","selectorScreen.png")).convert()
listePersoL = ["VampireL","NoneL","GeekL","ClownL","PompomGirlL","LicorneL","CowboyL","MomieL","PirateL","NinjaL","NaziL","ZombieL"]
listePersoR = ["VampireR","NoneR","GeekR","ClownR","PompomGirlR","LicorneR","CowboyR","MomieR","PirateR","NinjaR","NaziR","ZombieR"]
L = -1
R = -1
ChoixPersoL = "InvisibleMan"
ChoixPersoR = "InvisibleMan"
pygame.mixer.music.play(-1)
while True:
    J1PasPret = True
    J2PasPret = True
    perso_l = pygame.image.load(path.join("data",ChoixPersoL,"perso_l64bit.png")).convert_alpha()
    perso_r = pygame.image.load(path.join("data",ChoixPersoR,"perso_r64bit.png")).convert_alpha()
    clock = pygame.time.Clock()
    while J1PasPret or J2PasPret:
        selectorScreenVu = selectorScreen.copy()
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == K_r and J1PasPret:
                    try:
                        L += 1
                        ChoixPersoL = listePersoL[L]
                    except:
                        L=0
                        ChoixPersoL = listePersoL[L]
                    perso_l = pygame.image.load(path.join("data",ChoixPersoL,"perso_l64bit.png")).convert_alpha()
                elif event.key == K_u and J2PasPret:
                    try:
                        R += 1
                        ChoixPersoR = listePersoR[R]
                    except:
                        R=0
                        ChoixPersoR = listePersoR[R]
                    perso_r = pygame.image.load(path.join("data",ChoixPersoR,"perso_r64bit.png")).convert_alpha()
                elif event.key == K_s:
                    J1PasPret = False
                elif event.key == K_o:
                    J2PasPret = False
        selectorScreenVu.blit(perso_l,(139,192))
        selectorScreenVu.blit(perso_r,(277,192))
        screen.blit(pygame.transform.scale(selectorScreenVu, (ResoEcran.current_w,ResoEcran.current_h)),(0,0))
        pygame.display.flip()
    perso_l = pygame.transform.scale(perso_l, (int(ResoEcran.current_w*64/960),int(ResoEcran.current_h*64/640)))       
    perso_r = pygame.transform.scale(perso_r, (int(ResoEcran.current_w*64/960),int(ResoEcran.current_h*64/640)))    
    fond = pygame.image.load(path.join("data","desert64bit.png")).convert()
    fond = pygame.transform.scale(fond, (ResoEcran.current_w,ResoEcran.current_h))
    cactus = pygame.image.load(path.join("data","cactus64bit.png")).convert_alpha()
    cactus = pygame.transform.scale(cactus, (int(ResoEcran.current_w*64/960),int(ResoEcran.current_h*64/640)))
    perso_l_dead = pygame.image.load(path.join("data",ChoixPersoL,"perso_l_dead64bit.png")).convert_alpha()
    perso_l_dead = pygame.transform.scale(perso_l_dead, (int(ResoEcran.current_w*64/960),int(ResoEcran.current_h*64/640)))
    perso_r_dead = pygame.image.load(path.join("data",ChoixPersoR,"perso_r_dead64bit.png")).convert_alpha()
    perso_r_dead = pygame.transform.scale(perso_r_dead, (int(ResoEcran.current_w*64/960),int(ResoEcran.current_h*64/640)))
    ovni = pygame.image.load(path.join("data","ovni64bit.png")).convert_alpha()
    ovni = pygame.transform.scale(ovni, (int(ResoEcran.current_w*64/960),int(ResoEcran.current_h*64/640)))
    tirL = pygame.image.load(path.join("data",ChoixPersoL,"tirL64bit.png")).convert_alpha()
    tirL = pygame.transform.scale(tirL, (int(ResoEcran.current_w*64/960),int(ResoEcran.current_h*64/640)))
    tirR = pygame.image.load(path.join("data",ChoixPersoR,"tirR64bit.png")).convert_alpha()
    tirR = pygame.transform.scale(tirR, (int(ResoEcran.current_w*64/960),int(ResoEcran.current_h*64/640)))
    texte1 = font.render("Score J1 : "+str(score_l), 1, (10, 10, 10))
    texte2 = font.render("Score J2 : "+str(score_r), 1, (10, 10, 10))
    continuer = 1
    while continuer:
        nb_cactus = randint(15,25)
        carte = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        i = 0
        while i != nb_cactus:
            x = randint(2,12)
            y = randint(1,10)
            if testCase(x, y) == 0 and x != 7:
                changerCase(x, y, 3)
                i = i+1
        screen.blit(fond,(0,0))
        afficherCarte()
        add = 100
        nbBalles_l = 0
        nbBalles_r = 0
        global case_perso_l
        global case_perso_r
        case_perso_l = 5
        case_perso_r = 6
        case_ovni = 0
        sens_ovni = -1
        global perso_r_vivant
        perso_r_vivant = 1
        global perso_l_vivant
        perso_l_vivant = 1
        cycleOvni = 0
        while perso_l_vivant and perso_r_vivant and continuer:
            clock.tick(50)
            if cycleOvni == 15:
                if sens_ovni == -1 and case_ovni < 14:
                    changerCase(7, case_ovni, 10)
                    changerCase(7, case_ovni-1,0)
                    case_ovni += 1
                elif sens_ovni == 1 and case_ovni > -1:
                    changerCase(7, case_ovni, 10)
                    changerCase(7, case_ovni+1,0)
                    case_ovni -= 1
                else:
                    sens_ovni *= -1
                cycleOvni = 0
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continuer = 0
                    elif event.key == K_f:
                        if case_perso_l < 9:
                            changerCase(0, case_perso_l, 0)
                            case_perso_l = case_perso_l+1
                            changerCase(0, case_perso_l, 6)
                    elif event.key == K_r:
                        if case_perso_l > 1:
                            changerCase(0, case_perso_l, 0)
                            case_perso_l = case_perso_l-1
                            changerCase(0, case_perso_l, 6)
                    elif event.key == K_s:
                        BalleGauche().start()
                        nbBalles_l += 1
                    elif event.key == K_j:
                        if case_perso_r < 9:
                            changerCase(14, case_perso_r, 0)
                            case_perso_r = case_perso_r+1
                            changerCase(14, case_perso_r, 7)
                    elif event.key == K_u:
                        if case_perso_r > 1:
                            changerCase(14, case_perso_r, 0)
                            case_perso_r = case_perso_r-1
                            changerCase(14, case_perso_r, 7)
                    elif event.key == K_o:
                        BalleDroite().start()
                        nbBalles_r += 1
            cycleOvni += 1
            screen.blit(fond,(0,0))
            texte1 = font.render("Score J1 : "+str(score_l), 1, (10, 10, 10))
            texte2 = font.render("Score J2 : "+str(score_r), 1, (10, 10, 10))
            screen.blit(texte1,(int(ResoEcran.current_w*15/960),15))
            screen.blit(texte2,(int(ResoEcran.current_w*750/960),15))
            afficherCarte()
            screen.blit(cache,(int(ResoEcran.current_w*400/960),0))
            pygame.display.flip()    
        if perso_l_vivant == 0:
            changerCase(0,case_perso_l,8)
            changerCase(1,case_perso_l,0)
            add /= nbBalles_r
            if add == 0:
                add += 1
            score_r += int(add)
            texte1 = font.render("Score J1 : "+str(score_l), 1, (10, 10, 10))
            texte2 = font.render("Score J2 : "+str(score_r), 1, (10, 10, 10))
            screen.blit(fond,(0,0))
            screen.blit(texte1,(int(ResoEcran.current_w*15/960),15))
            screen.blit(texte2,(int(ResoEcran.current_w*750/960),15))
            afficherCarte()
            pygame.display.flip()
            boum.play()
            sleep(4)
        elif perso_r_vivant == 0:
            changerCase(14,case_perso_r,9)
            changerCase(13,case_perso_r,0)
            add /=nbBalles_l
            if add == 0:
                add += 1
            score_l += int(add)
            texte1 = font.render("Score J1 : "+str(score_l), 1, (10, 10, 10))
            texte2 = font.render("Score J2 : "+str(score_r), 1, (10, 10, 10))
            screen.blit(fond,(0,0))
            screen.blit(texte1,(int(ResoEcran.current_w*15/960),15))
            screen.blit(texte2,(int(ResoEcran.current_w*750/960),15))
            afficherCarte()
            pygame.display.flip()
            boum.play()
            sleep(4)
        else:
            continuer = 0
        if score_l == 42 or score_r == 42 and continuer != 0:
            screen.fill((242,193,0))
            screen.blit(font.render("a message from the dev :", 1, (10, 10, 10)), (80, 20))
            screen.blit(font.render("My name is Intronirisme and maybe you're reading this message in", 1, (10, 10, 10)), (15, 80))
            screen.blit(font.render("the source code of my game, or maybe you found it by chance", 1, (10, 10, 10)), (15, 120))#i know you're in the source code
            screen.blit(font.render("in every case it mean that you discoverd a secret (well played).", 1, (10, 10, 10)), (15, 160))
            screen.blit(font.render("I placed it here in order to thank my friends Sloan and Skinny Cunt for", 1, (10, 10, 10)), (15, 200))
            screen.blit(font.render("their help. This is my first video game, I created it when I was 15 but I", 1, (10, 10, 10)), (15, 240))
            screen.blit(font.render("couldn't share it with the world because I hadn't the right for using some", 1, (10, 10, 10)), (15, 280))
            screen.blit(font.render("assets / musics so I keeped this game for my personnal amusement.", 1, (10, 10, 10)), (15, 320))
            screen.blit(font.render("Hopefully I have the best friends of this planet and thank to the ability of", 1, (10, 10, 10)), (15, 380))
            screen.blit(font.render("two of them you can now play to this (awesome) game !", 1, (10, 10, 10)), (15, 420))
            screen.blit(font.render("So thank you Milò (Sloan) for redesign each characters !!!", 1, (10, 10, 10)), (15, 470))
            screen.blit(font.render("Thank you Gaston (Skinny Cunt) for this marvelous music <3", 1, (10, 10, 10)), (15, 510))
            screen.blit(font.render("And thank you to every people who support me in my numerous projects,", 1, (10, 10, 10)), (15, 550))
            screen.blit(font.render("the most fabulous of them is to make art with you", 1, (10, 10, 10)), (15, 590))
            screen.blit(font.render("Long life to Cuivre Game Studio, long life to our friendship !", 1, (10, 10, 200)), (15, 640))
            pygame.display.flip()
            while showMes:
                for event in pygame.event.get():
                    if event.type == KEYDOWN and event.key != K_ESCAPE:
                        showMes = False
    

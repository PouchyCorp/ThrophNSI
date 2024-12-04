from random import *
import pygame
from anim import Animation, Spritesheet
#import sprite

pygame.init()
class Dialogue():
    def __init__(self, fichier):    #nécessite de donner le chemin exacte du fichier
        self.fichier=fichier
        #self.screen=screen    screen
        self.avatar= pygame.image.load('data\Fond.png').convert_alpha()
        self.texte=[]
        self.number=None
        self.format = pygame.font.SysFont("Arial", 20)
        self.bot_surf = None
    

    def load_save(self):
        self.texte=[]  #debogage
        fich_ouvert=open(self.fichier, encoding='utf8') 
        for lines in fich_ouvert:
            mot=''
            intermediate=[]
            for k in range(len(lines)-1):
                mot+=lines[k]
            intermediate.append(mot)
            self.texte.append(intermediate)
        return self.texte
    
    def load_dialogue(self, number):
        talked=""
        for letter in self.texte[number]:
            talked+=letter
        return talked
       
    def show(self, screen):
        txtsurf = self.format.render(self.load_dialogue(self.number), True, (255,255,255))
        screen.blit(pygame.Surface((1000,125)), (200, 750)) #a recadrer
        screen.blit(self.bot_surf, (200, 750)) #a recadrer
        screen.blit(txtsurf,(450, 800)) #a recadrer
        
    def random_dialogue(self):
        self.number=randint(0, (len(self.texte)-1)) 


                        
#SPRITESHEET_BOT = Spritesheet(pygame.image.load('data/test_robot.png'), (48*6, 48*6))
#animated = Animation(sprite.SPRITESHEET_BOT, 0, 7)


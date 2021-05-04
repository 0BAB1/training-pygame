import pygame
import random
from comet import Comet

#creeer une classe qui gère l'event
class CometFallEvent:
    def __init__(self, game):
        self.percent = 0
        #def un roupe de sprites pour stocker les comettes
        self.all_comets = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False

    def add_percent(self):
        self.percent += 0.25
    
    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        #apparaitre des bppules de feu (entre 1 et 10)
        for i in range (random.randint(1,10)):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        #jaue envent totalement chargée
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True #activer l'event
            print("debut event")

    def update_bar(self, surface):
        #add prctage
        self.add_percent()

        #on test si on peu comet fall
        #self.attempt_fall() => on ne test pas a chaque passage de boucle sinon ca surcharge
        #mais on test a chaque mort de monstre quand la barre est full loaded

        #rouge en fg
        pygame.draw.rect(surface, (220,30,10), [
            0, #x
            surface.get_height()-20, #y
            (surface.get_width() / 100)*self.percent, #long
            10 #ep
        ])

        #barre noire en bg
        pygame.draw.rect(surface, (0,0,0), [
            0, #x
            surface.get_height() - 20, #y
            surface.get_width(), #long
            10 #ep
        ])
        #rouge en fg
        pygame.draw.rect(surface, (200,60,10), [
            0, #x
            surface.get_height()-20, #y
            (surface.get_width() / 100)*self.percent, #long
            10 #ep
        ])
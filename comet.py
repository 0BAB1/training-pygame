import pygame
import random

class Comet(pygame.sprite.Sprite):
    def __init__(self, coment_event):
        super().__init__()
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(2,6)
        self.rect.x = random.randint(20,1260)
        self.rect.y = -random.randint(0,800)
        self.comet_event = coment_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        #si ya plus de comette
        if len(self.comet_event.all_comets) == 0:
                print("fin event")
                self.comet_event.reset_percent()
                self.comet_event.game.start_spawn()
                self.comet_event.fall_mode = False
    
    def fall(self):
        self.rect.y += 1
        #si commette contact sol
        if self.rect.y >= 520:
            #retirer commette
            self.remove()
            
        #si comette contact joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            self.remove()
            self.comet_event.game.player.damage(20)

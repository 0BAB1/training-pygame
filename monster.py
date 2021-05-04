import pygame
import random
import animation

class Monster(animation.AnimateSprite):
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.velocity = 4
        self.health = 78
        self.max_health = 100
        self.attack = 0.1
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(10,300)
        self.rect.y = 540 - offset
        self.start_animation()

    def damage(self, amount):
        #infliger les degats
        self.health -= amount
        #verifier si son nouveau nombre de points de vie est inferieru a zero
        if self.health <= 0:
            #reapparaitre comme un nouveau montsre
            self.rect.x = 1000+ random.randint(10,300)
            self.health = self.max_health

            #si la barre d'event est chargée
            if self.game.comet_event.is_full_loaded():
                #retirer du jeu
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):
        #dessinner les barre de vie
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (210, 111, 40), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si en collision avec le oueur , damae
        else:
            self.game.player.damage(self.attack)

#def classe momie
class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))#game required, mummy -> name required, size optionnal

class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 140)#-> offset optionnal
        self.health = 250
        self.max_health = 250
        self.velocity = 2
        self.attack = 0.7
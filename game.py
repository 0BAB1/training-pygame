import pygame
from player import Player
from monster import Mummy, Alien
from comet_event import CometFallEvent

#classe jeu
class Game:
    def __init__(self):
        #definir si notre jeu a commené ou non
        self.is_playing = 0 #0 = menu accueil / 1 = jeu / 2 = ecran game over
        #generer joueur
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        #generer event
        self.comet_event = CometFallEvent(self)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = 1
        self.start_spawn()

    def start_spawn(self):
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def update(self, screen):
        #joueur
        screen.blit(self.player.image, self.player.rect)
        #animation joueur
        self.player.animate()
        #actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)
        #actualiser  barre event
        self.comet_event.update_bar(screen)

        #recuperer projectiles joueur
        for projectile in self.player.all_projectiles:
            projectile.move()
        #recuperer monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            #animation monstre
            monster.animate(loop=True)
        #recuperer comettes
        for comet in self.comet_event.all_comets:
            comet.fall()

        #projectile
        self.player.all_projectiles.draw(screen)
        #monstres
        self.all_monsters.draw(screen)
        #comettes
        self.comet_event.all_comets.draw(screen)

        #verifier si le joueur Gauche ou Droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        #ajouter un monstre
        self.all_monsters.add(monster_class_name.__call__(self))
    
    def game_over(self):
        #remetre le jeu a neuf, monters delete, joueur 100 vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = 2
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
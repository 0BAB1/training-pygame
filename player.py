import pygame
from projectile import Projectile
import animation

#classe joueur
class Player(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 50
        self.velocity = 6
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if (self.health - amount) >= 1:
            self.health -= amount
        else:
            self.game.game_over()

    def launch_projectile(self):
        #creer instance  Projectile
        self.all_projectiles.add(Projectile(self))
        #demarrer animation
        self.start_animation()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 45, self.rect.y +5, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 40), [self.rect.x + 45, self.rect.y +5, self.health, 7])

    def move_right(self):
        #si le joueur n''est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
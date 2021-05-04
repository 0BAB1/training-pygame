import pygame

#classe qui s'occupe des animations
class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.size = size
        self.current_image = 0 #commencer animation a image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #def un merhode pour demarrer l'animation
    def start_animation(self):
        self.animation = True
    
    #def une methode pour animer le sprite
    def animate(self, loop=False):
        #si animation active
        if self.animation:
            #passer imgae suivante
            self.current_image += 1
            #verifier si on a atteint fin de l'animation
            if self.current_image >= len(self.images):
                #remttre animation à 0
                self.current_image = 0
                if loop is False:
                    #desactiver animation
                    self.animation = False
            #modifier image precedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


#fonction pour charger images d'un sprite
def load_animation_images(sprite_name):
    #charger 24 images de ce sprite
    images = []
    path = f"assets/{sprite_name}/{sprite_name}"
    #boucler sur chaque image (24x)
    for num in range(1,24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    return images

#definir un dictionnaore qui va conternir les images hargées de chaque sprites
animations = {
    "mummy" : load_animation_images("mummy"),
    "player" : load_animation_images("player"),
    "alien" : load_animation_images("alien")
}
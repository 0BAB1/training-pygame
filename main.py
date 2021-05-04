import pygame
import math
from game import Game
pygame.init()

#definir une clock
clock = pygame.time.Clock()
FPS = 60

#def resolution
user_x = 640
user_y = 360
ratio = user_x / 1280

#def une font por le txt
font = pygame.font.SysFont(None, 72)
go_txt = font.render("game over, click to continue", True, (255,255,255))

#generer fenetre
pygame.display.set_caption("back on track")
window = pygame.display.set_mode((user_x,user_y))
screen = pygame.Surface((1280, 720))

#importer et charger l'arriere plan
background = pygame.image.load("assets/bg.jpg")

#importer et chargger imae ecran accueil
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() /3.3 )

#importet et charger boutton pour lancer la partie
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.85 )
play_button_rect.y = math.ceil(screen.get_height() / 2)


#charger jeu
game = Game()
running = True

#boucle
while running:

    #arriere plan
    screen.blit(background, (0,-200))

    #virifier si le jeu a commencé ou non
    if game.is_playing == 1:
        #declencer les instructions
        game.update(screen)
    #veifier si on est sur le menu rappel : 0 = menu 1 = playin 2 = gameover screen
    elif game.is_playing == 0:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, (banner_rect.x,0))
    elif game.is_playing == 2:
        screen.blit(go_txt, (20,20))

    #maj ecran
    frame = pygame.transform.scale(screen, (user_x, user_y))
    window.blit(frame, frame.get_rect())
    pygame.display.flip()

    #events
    for event in pygame.event.get():
        #fenetre ferme
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture")
        #clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            #si touche espace, projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #print(event.pos)
            #print(str(play_button_rect.x) + " _____ " + str(play_button_rect.y))
            #verififier si la souroos est en collision avc le boutton
            if game.is_playing == 0:
                if play_button_rect.collidepoint((event.pos[0]/ratio, event.pos[1]/ratio)):
                    game.start()
            elif game.is_playing == 2:
                game.start()
    
    #fixer le nb de fps sur la clock
    clock.tick(FPS)

#Jonomer 

import pygame
import random 

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 900
screen_height = 600

gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Yılan Oyunu")

clock = pygame.time.Clock()
title_font = pygame.font.SysFont(None, 80)  
start_font = pygame.font.SysFont(None, 50)  

small_font = pygame.font.SysFont(None, 30)  

def text_screen(text, color, x, y, font=small_font):  
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

def plot_snake(gamewindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])

def show_start_screen():
    gamewindow.fill(white)

    title_text1 = title_font.render("DÜNYANIN EN ZOR OYUNUNA", True, red)
    title_text2 = title_font.render("HOŞGELDİN", True, red)
    start_text = start_font.render("Başlamak için ENTER'a bas", True, black)

    title_x1 = (screen_width - title_text1.get_width()) // 2
    title_x2 = (screen_width - title_text2.get_width()) // 2
    start_x = (screen_width - start_text.get_width()) // 2

    title_y1 = screen_height // 3
    title_y2 = title_y1 + title_text1.get_height() + 10  
    start_y = title_y2 + title_text2.get_height() + 10  

    gamewindow.blit(title_text1, (title_x1, title_y1))
    gamewindow.blit(title_text2, (title_x2, title_y2))
    gamewindow.blit(start_text, (start_x, start_y))

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    food_x = random.randint(20, screen_width - 30)
    food_y = random.randint(60, screen_height - 30)
    score = 0
    init_velocity = 8 # Yılan Hızını Ayarlamak İsterseniz Azaltabilir - Yükseltebilirsiniz.
    snake_size = 30
    fps = 60

    game_over_font = pygame.font.SysFont(None, 60)

    while not exit_game:
        if game_over:
            gamewindow.fill(white)

            game_over_text1 = game_over_font.render("Oyun Bitti", True, red)
            game_over_text2 = game_over_font.render(" Devam etmek için Enter'a Bas", True, red)

            game_over_x1 = (screen_width - game_over_text1.get_width()) // 2
            game_over_y1 = screen_height // 3 - 45  

            game_over_x2 = (screen_width - game_over_text2.get_width()) // 2
            game_over_y2 = screen_height // 3 + 25 

            gamewindow.blit(game_over_text1, (game_over_x1, game_over_y1))
            gamewindow.blit(game_over_text2, (game_over_x2, game_over_y2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop() 
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity 
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
            
            snake_x += velocity_x
            snake_y += velocity_y
            
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 1
                food_x = random.randint(20, screen_width - 30)
                food_y = random.randint(60, screen_height - 30)
                snk_length += 5
            
            gamewindow.fill(white)

            text_screen("Puan: " + str(score * 10), red, 5, 5)
            text_screen("Not: Küpün Tam Üstünden Saplamalısın", black, 400, 5, font=small_font)

            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])
            pygame.draw.line(gamewindow, red, (0, 40), (900, 40), 5)

            head = [snake_x, snake_y]
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width - 20 or snake_y < 50 or snake_y > screen_height - 20:
                game_over = True

            plot_snake(gamewindow, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)
    
    pygame.quit()

show_start_screen()
gameloop()

# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "For Mother Russia"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GREY = (53, 54, 56)
GRAY = (150, 150, 150)

font = pygame.font.Font(None, 48)

#images
startscreen = pygame.image.load("images/background.png")
endscreen = pygame.image.load("images/endscreen.png")
background = pygame.image.load("images/flag.png")
coin = pygame.image.load("images/coin.png")
vodkapic = pygame.image.load("images/vodka.png")

#sounds
coinsound = pygame.mixer.Sound("sounds/boo.wav")
vodkasound = pygame.mixer.Sound("sounds/grunt.wav")
pygame.mixer.music.load("sounds/anthem.ogg")

# stages
START = 0
PLAYING = 1
END = 2


def setup():
    global player1, player2, player3, vel1, vel2, vel3, player1_speed, player2_speed, player3_speed, score1, score2, score3, stage, time_remaining, ticks, walls, coins, vodka
        # Make a player
    player1 = [750, 0, 25, 25]
    vel1 = [0, 0]
    player1_speed = 5
    score1 = 0

    player2 = [25, 575, 25, 25]
    vel2 = [0, 0]
    player2_speed = 5
    score2 = 0

    player3 = [25, 0, 25, 25]
    vel3 = [0, 0]
    player3_speed = 5
    score3 = 0

    stage = START
    time_remaining = 25
    ticks = 0

    # make walls
    wall1 =  [50, 0, 700, 25]
    wall2 =  [50, 575, 775, 25]
    wall3 =  [0, 0, 25, 600]
    wall4 =  [775, 0, 25, 600]

    wall5 =  [700, 0, 25, 300]
    wall6 =  [625, 300, 100, 25]
    wall7 =  [600, 125, 25, 200]
    wall8 =  [225, 100, 400, 25]
    wall9 =  [425, 100, 25, 100]

    wall10 =  [525, 400, 200, 25]
    wall11 =  [525, 200, 25, 200]
    wall12 =  [325, 300, 200, 25]
    wall13 =  [325, 200, 25, 100]
    wall14 =  [225, 200, 100, 25]
    wall15 =  [225, 200, 25, 100]

    wall16 =  [225, 420, 250, 25]
    wall17 =  [575, 400, 25, 200]

    wall18 =  [25, 200, 100, 25]
    wall19 =  [150, 300, 100, 25]
    wall20 =  [25, 400, 100, 25]
    wall21 =  [165, 450, 25, 150]

    walls = [wall1, wall2, wall3, wall4, wall5,
             wall6, wall7, wall8, wall9, wall10,
             wall11, wall12, wall13, wall14, wall15,
             wall16, wall17, wall18, wall19, wall20,
             wall21]

    # Make coins
    coin1 = [650, 250, 25, 25]
    coin2 = [400, 250, 25, 25]
    coin3 = [75, 500, 25, 25]
    coin4 = [75, 100, 25, 25]
    coin5 = [265, 250, 25, 25]
    coin6 = [650, 500, 25, 25]
    coin7 = [400, 500, 25, 25]
    coin8 = [400, 50, 25, 25]
    coin9 = [450, 350, 25, 25]
    coin10 = [50, 300, 25, 25]
    coin11 = [150, 400, 25, 25]
    coin12 = [650, 50, 25, 25]
    coin13 = [650, 350, 25, 25]

    coins = [coin1, coin2, coin3, coin4, coin5,
             coin6, coin7, coin8, coin9, coin10,
             coin11, coin12, coin13]

    # Make vodka
    vodka1 = [750, 250, 25, 25]
    vodka2 = [400, 200, 25, 25]
    vodka3 = [125, 500, 25, 25]
    vodka4 = [75, 150, 25, 25]
    vodka5 = [200, 250, 25, 25]
    vodka6 = [650, 600, 25, 25]
    vodka7 = [300, 350, 25, 25]
    vodka8 = [400, 550, 25, 25]
    vodka9 = [550, 350, 25, 25]
    vodka10 = [425, 50, 25, 25]
    
    vodka = [vodka1, vodka2, vodka3, vodka4, vodka5,
             vodka6, vodka7, vodka8, vodka9, vodka10]


# Game loop
setup()
pygame.mixer.music.play(-1)
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                pygame.quit()
            
        if stage == START:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                        
        elif stage == PLAYING:
            pressed = pygame.key.get_pressed()

            up = pressed[pygame.K_UP]
            down = pressed[pygame.K_DOWN]
            left = pressed[pygame.K_LEFT]
            right = pressed[pygame.K_RIGHT]

            w = pressed[pygame.K_w]
            s = pressed[pygame.K_s]
            a = pressed[pygame.K_a]
            d = pressed[pygame.K_d]

            key8 = pressed[pygame.K_KP8]
            key2 = pressed[pygame.K_KP2]
            key4 = pressed[pygame.K_KP4]
            key6 = pressed[pygame.K_KP6]

            #player1
            if left:
                vel1[0] = -player1_speed
            elif right:
                vel1[0] = player1_speed
            else:
                vel1[0] = 0

            if up:
                vel1[1] = -player1_speed
            elif down:
                vel1[1] = player1_speed
            else:
                vel1[1] = 0

            #player2
            if a:
                vel2[0] = -player2_speed
            elif d:
                vel2[0] = player2_speed
            else:
                vel2[0] = 0

            if w:
                vel2[1] = -player2_speed
            elif s:
                vel2[1] = player2_speed
            else:
                vel2[1] = 0

            #player 3
            if key4:
                vel3[0] = -player3_speed
            elif key6:
                vel3[0] = player3_speed
            else:
                vel3[0] = 0

            if key8:
                vel3[1] = -player3_speed
            elif key2:
                vel3[1] = player3_speed
            else:
                vel3[1] = 0

        elif stage == END:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    setup()

            
                        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    if stage == PLAYING:
        player1[0] += vel1[0]
        player2[0] += vel2[0]
        player3[0] += vel3[0]

        ''' resolve collisions horizontally '''
        for w in walls:
            #player1 
            if intersects.rect_rect(player1, w):        
                if vel1[0] > 0:
                    player1[0] = w[0] - player1[2]
                elif vel1[0] < 0:
                    player1[0] = w[0] + w[2]
            #player2
            if intersects.rect_rect(player2, w):
                if vel2[0] > 0:
                    player2[0] = w[0] - player2[2]
                elif vel2[0] < 0:
                    player2[0] = w[0] + w[2]
            #player3
            if intersects.rect_rect(player3, w):
                if vel3[0] > 0:
                    player3[0] = w[0] - player3[2]
                elif vel3[0] < 0:
                    player3[0] = w[0] + w[2]

        ''' move the player in vertical direction '''
        player1[1] += vel1[1]
        player2[1] += vel2[1]
        player3[1] += vel3[1]
        
        ''' resolve collisions vertically '''
        for w in walls:
            #player1
            if intersects.rect_rect(player1, w):                    
                if vel1[1] > 0:
                    player1[1] = w[1] - player1[3]
                if vel1[1]< 0:
                    player1[1] = w[1] + w[3]
            #player2        
            if intersects.rect_rect(player2, w):
                if vel2[1] > 0:
                    player2[1] = w[1] - player2[3]
                if vel2[1]< 0:
                    player2[1] = w[1] + w[3]
            #player3
            if intersects.rect_rect(player3, w):
                if vel3[1] > 0:
                    player3[1] = w[1] - player3[3]
                if vel3[1]< 0:
                    player3[1] = w[1] + w[3]


        ''' here is where you should resolve player collisions with screen edges '''
        left1 = player1[0]
        right1 = player1[0] + player1[2]
        top1 = player1[1]
        bottom1 = player1[1] + player1[3]

        left2 = player2[0]
        right2 = player2[0] + player2[2]
        top2 = player2[1]
        bottom2 = player2[1] + player2[3]

        left3 = player3[0]
        right3 = player3[0] + player3[2]
        top3 = player3[1]
        bottom3 = player3[1] + player3[3]
        
        #player1
        if left1 < 0:
            player1[0] = 0
        elif right1 > WIDTH:
            player1[0] = WIDTH - player1[2]

        if top1 < 0:
            player1[1] = 0
        elif bottom1 > HEIGHT:
            player1[1] = HEIGHT - player1[3]
            
        #player2
        if left2 < 0:
            player2[0] = 0
        elif right2 > WIDTH:
            player2[0] = WIDTH - player2[2]

        if top2 < 0:
            player2[1] = 0
        elif bottom2 > HEIGHT:
            player2[1] = HEIGHT - player2[3]
            
        #player3
        if left3 < 0:
            player3[0] = 0
        elif right3 > WIDTH:
            player3[0] = WIDTH - player3[2]

        if top3 < 0:
            player3[1] = 0
        elif bottom3 > HEIGHT:
            player3[1] = HEIGHT - player3[3]

        ''' get the coins '''
        hit_list = []

        for c in coins:
            if intersects.rect_rect(player1, c):
                hit_list.append(c)

            if intersects.rect_rect(player2, c):
                hit_list.append(c)

            if intersects.rect_rect(player3, c):
                hit_list.append(c)
         
        hit_list1 = [c for c in coins if intersects.rect_rect(player1, c)]
        hit_list2 = [c for c in coins if intersects.rect_rect(player2, c)]
        hit_list3 = [c for c in coins if intersects.rect_rect(player3, c)]
        
        for hit in hit_list1:
            coins.remove(hit)
            score1 += 1
            coinsound.play()

        for hit in hit_list2:
            coins.remove(hit)
            score2 += 1
            coinsound.play()

        for hit in hit_list3:
            coins.remove(hit)
            score3 += 1
            coinsound.play()
            
        if len(coins) == 0:
            stage = END


        ''' get the vodka '''
        hit_list = []

        for v in vodka:
            if intersects.rect_rect(player1, v):
                hit_list.append(v)

            if intersects.rect_rect(player2, v):
                hit_list.append(v)

            if intersects.rect_rect(player3, v):
                hit_list.append(v)
         
        hit_list4 = [v for v in vodka if intersects.rect_rect(player1, v)]
        hit_list5 = [v for v in vodka if intersects.rect_rect(player2, v)]
        hit_list6= [v for v in vodka if intersects.rect_rect(player3, v)]
        
        for hit in hit_list4:
            vodka.remove(hit)
            score1 -= 1
            player1_speed -= 1
            vodkasound.play()

        for hit in hit_list5:
            vodka.remove(hit)
            score2 -= 1
            player2_speed -= 1
            vodkasound.play()

        for hit in hit_list6:
            vodka.remove(hit)
            score3 -= 1
            player3_speed -= 1
            vodkasound.play()

        if player1_speed == 0 and player2_speed == 0 and player3_speed == 0:
            stage = END

        ''' timer stuff '''
        if stage == PLAYING:
            ticks += 1

            if ticks % refresh_rate == 0:
                time_remaining -= 1

            if time_remaining == 0:
                stage = END

        
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.blit(background, (0, 0))
    
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, BLACK, player2)
    pygame.draw.rect(screen, GRAY, player3)
    
    ''' walls '''
    for w in walls:
        pygame.draw.rect(screen, GREY, w)

    ''' timer text '''
    timer_text = font.render(str(time_remaining), True, WHITE)
    screen.blit(timer_text, [400, 10])

    '''coins '''
    for c in coins:
        screen.blit(coin, c)

    '''vodka '''
    for v in vodka:
        screen.blit(vodkapic, v)

    '''x to quit'''
    text1 = font.render("(Press X to quit)", True, WHITE)
    screen.blit(text1, [525, 550])
    
    if stage == START:
        screen.blit(startscreen, (0, 0))
        text1 = font.render("(Press SPACE to play)", True, WHITE)
        text2 = font.render("Welcome Comrade, to MOTHER RUSSIA!", True, WHITE)
        text3 = font.render("(Press X to quit)", True, WHITE)
        screen.blit(text1, [250, 150])
        screen.blit(text2, [100, 100])
        screen.blit(text3, [525, 550])
    elif stage == END:
        #screen.blit(endscreen, (0, 0))
        text1 = font.render("Player 1: " + str(score1) , 1, WHITE)
        text2 = font.render("Player 2: " + str(score2) , 1, WHITE)
        text3 = font.render("Player 3: " + str(score3) , 1, WHITE)
        text4 = font.render("(Press R to restart)", True, BLACK)
        text5 = font.render("(Press X to quit)", True, WHITE)
        screen.blit(text1, [0, 0])
        screen.blit(text2, [0, 50])
        screen.blit(text3, [0, 100])
        screen.blit(text4, [250, 200])
        screen.blit(text5, [525, 550])
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()

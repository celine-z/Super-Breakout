'''
Celine Zhang
April 28, 2015
Super Break Game
'''
# I - IMPORT AND INITIALIZE
import pygame, pySprites
pygame.init()
screen = pygame.display.set_mode((640, 480))

def main():
    '''This function is the 'mainline logic' for the Super Break game'''
      
    # DISPLAY
    pygame.display.set_caption("Multiplayer Super Break!")
     
    # ENTITIES
    background = pygame.Surface(screen.get_size())
    screen.blit(background, (0, 0))
    
    # Sprites
    superbreak = pygame.font.Font("Files\\256BYTES.TTF", 50)
    superbreak = superbreak.render("S  U  P  E  R     B  R  E  A  K", 1, \
                                   (255, 0, 0))
    instructions_1 = pygame.font.Font("Files\\256BYTES.TTF", 25)
    instructions_1 = instructions_1.render("This is a multiplayer Super Break game. Use the mouse", 1, \
                                   (255, 102, 0))
    instructions_2 = pygame.font.Font("Files\\256BYTES.TTF", 25)
    instructions_2 = instructions_2.render("to move the top panel & use the arrow keys to move the", 1, \
                                   (255, 255, 0))
    instructions_3 = pygame.font.Font("Files\\256BYTES.TTF", 25)
    instructions_3 = instructions_3.render("bottom panel. The objective of the game is to remove", 1, \
                                   (0, 255, 0))
    instructions_4 = pygame.font.Font("Files\\256BYTES.TTF", 25)
    instructions_4 = instructions_4.render("all the bricks. Do not let the ball touch the ground!", 1, \
                                   (0,0,255))
    instructions_5 = pygame.font.Font("Files\\256BYTES.TTF", 25)
    instructions_5 = instructions_5.render("Press the space bar to begin...", 1, \
                                   (255, 0, 255))

    screen.blit(superbreak, (80, 50))
    screen.blit(instructions_1, (35, 150))
    screen.blit(instructions_2, (35, 190))
    screen.blit(instructions_3, (35, 230))
    screen.blit(instructions_4, (35, 270))
    screen.blit(instructions_5, (145, 310))

    #Background music and sound effects
    pygame.mixer.music.load("Files\\bgmusic.ogg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    # A - Action
    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)    
    
    # L - Loop
    while keepGoing:
    
        # T - Timer to set frame rate
        clock.tick(30)
        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.fadeout(2000)
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
                    pygame.mixer.music.fadeout(2000)
                    keepGoing = False

        # R - Refresh display
        screen.blit(screen, (0, 0))
        pygame.display.flip()
    
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
 
    # Delay game by 3s and the game window
    pygame.time.delay(3000)
    pygame.quit()     
     
def game():
    '''This function is the 'mainline logic' for the Super Break game'''
      
    # DISPLAY
     
    # ENTITIES
    background = pygame.Surface(screen.get_size())
    screen.blit(background, (0, 0))
 
    # Sprites for: Ball, left right boundary, top and bottom endzone, player1, 
    # player2, bricks label, lives label, end game label, win label,
    # end label
    ball = pySprites.Ball(screen)
    boundary_l = pySprites.Boundary(41, 430, 0, 50)
    boundary_r = pySprites.Boundary(41, 430, 599, 50)
    endzone_top = pySprites.Boundary(640, 20, 0, 100)
    endzone_bottom = pySprites.Boundary(640, 1, 0, 479)
    player1 = pySprites.Player(screen, screen.get_height()-75)
    player2 = pySprites.Player(screen, screen.get_height()-30)
    font = pygame.font.Font("Files\\256BYTES.TTF", 40)
    bh_label = pySprites.Message(font, "Bricks Hit: ", 0, (290,20))
    points_label = pySprites.Message(font, "Points: ", 0, (525,20))
    lives = 3
    lives_label = pySprites.Message(font, "Lives: ", lives, (75,20))
    superbreak = pygame.font.Font("Files\\256BYTES.TTF", 50)
    superbreak = superbreak.render("S  U  P  E  R     B  R  E  A  K", 1, \
                                   (255, 255, 0))
    screen.blit(superbreak, (80, 50))
    end_label = pygame.font.Font("Files\\256BYTES.TTF", 92)
    end_label = end_label.render("Game Over!", 1, (225,225,0))
    win_label = pygame.font.Font("Files\\256BYTES.TTF", 92)
    win_label = win_label.render("You Win!", 1, (225,225,0))
    
    colours = [(255, 0, 255), (255, 0, 0), (255, 255, 0), (255, 102, 0), \
               (0, 255, 0), (0,0,255)]
    bricks = []
    y_value = -10
    #controls the rows
    for columns in range(6):
        y_value = y_value + 10
        x_value = -31
        colour = colours[columns]
        #controls the bricks in each row
        for row in range(18):
            x_value = x_value + 31
            brick = pySprites.Brick(screen, x_value, y_value, colour)
            bricks.append(brick)
            
    bricksGroup = pygame.sprite.OrderedUpdates(bricks)    
    allSprites = pygame.sprite.Group(ball, boundary_l, boundary_r, endzone_top, 
                                     endzone_bottom, player1, player2, bh_label, 
                                     lives_label, points_label, bricksGroup)
    
    #Background music and sound effects
    score_point = pygame.mixer.Sound("Files\\ScorePoint.ogg")
    score_point.set_volume(0.2)
    lost_life = pygame.mixer.Sound("Files\\lostlife.ogg")
    lost_life.set_volume(0.9)
    game_over = pygame.mixer.Sound("Files\\GameOver.ogg")
    game_over.set_volume(1)
    win = pygame.mixer.Sound("Files\\YouWin.ogg")
    win.set_volume(1)
    
    # ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
 
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
 
    # LOOP
    while keepGoing:
     
        # TIME
        clock.tick(30)
     
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Right click
                if event.button == 3:
                    player1.change_direction((-1, 0))
                else:
                    player1.change_direction((1, 0))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player2.change_direction((-1, 0))
                elif event.key == pygame.K_LEFT:
                    player2.change_direction((1, 0))
                    
        # Collision detection with players and top endzone with the ball
        if ball.rect.colliderect(player1.rect) or \
           ball.rect.colliderect(player2.rect) or \
           ball.rect.colliderect(endzone_top.rect):
            ball.change_direction()
        
        # Collision detection with the ball and the bottom endzone
        if ball.rect.colliderect(endzone_bottom.rect):
            lives_label.set_num(-1)
            ball.change_direction()
            lost_life.play()
                     
        # Check for collision of bricks and add points according to colour
        for objects in bricksGroup:
            if ball.rect.colliderect(objects.rect):
                bh_label.set_num(1)
                #blue = 1 points
                if objects.get_colour() == (0,0,255):
                    points_label.set_num(1)
                #green = 2 points
                elif objects.get_colour() == (0, 255, 0):
                    points_label.set_num(2)
                #orange = 3 points
                elif objects.get_colour() == (255, 102, 0):
                    points_label.set_num(3)
                #yellow = 4 points
                elif objects.get_colour() == (255, 255, 0):
                    points_label.set_num(4)
                #red = 5 points
                elif objects.get_colour() == (255, 0, 0):
                    points_label.set_num(5)
                #blue = 1 point
                elif objects.get_colour() == (255, 0, 255):
                    points_label.set_num(6)                
        # Collision detection with ball and bricks and removes the bricks
        if pygame.sprite.spritecollide(ball, bricksGroup, True):
            ball.change_direction()
            score_point.play()
            #move all bricks down by 1 pixel
            for objects in bricksGroup:
                objects.y_position()
            
        # Checks if win and displays win label
        if bh_label.get_num() == 108:
            pygame.mixer.music.fadeout(2000)
            win.play()
            screen.blit(win_label, (160, 250))
            pygame.display.flip()
            keepGoing = False    
                
        # Checks if lost and displays game over
        if lives_label.get_num() == 0:
            pygame.mixer.music.fadeout(2000)
            game_over.play()
            screen.blit(end_label, (120, 250))
            pygame.display.flip()
            keepGoing = False
            
        # REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()   

# Call the main function
main()   
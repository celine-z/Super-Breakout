'''
Celine Zhang
April 14, 2015
Super Break Sprites Class
'''
import pygame

class Ball(pygame.sprite.Sprite):
    '''This class defines the sprite for Ball'''
    def __init__(self, screen):
        '''This initializer method takes the screen as parameter and creates the
        ball sprite for this class'''
        # Call the parent of __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
        self.image = pygame.Surface((12, 12))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0,0,0))
        pygame.draw.circle(self.image, (255, 255, 255), (6, 6), 6, 0)
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2,screen.get_height()/2)
 
        # Instance variables to keep track of the screen surface
        # and set the initial x and y direction for the ball
        self.__screen = screen
        self.__dx = 5
        self.__dy = -3
 
    def change_direction(self):
        '''This method reverses the y direction of the Ball'''
        self.__dy = -self.__dy
             
    def update(self):
        '''This method repositions the Ball sprite on the screen'''
        if ((self.rect.left - 42 > 0) and (self.__dx < 0)) or\
           ((self.rect.right + 42 < self.__screen.get_width()) and (self.__dx > 0)):
            self.rect.left += self.__dx
        else:
            self.__dx = -self.__dx

        if ((self.rect.top-71 > 0) and (self.__dy > 0)) or\
           ((self.rect.bottom < self.__screen.get_height()) and (self.__dy < 0)):
            self.rect.top -= self.__dy
        else:
            self.__dy = -self.__dy
            
            
class Boundary(pygame.sprite.Sprite):
    '''This class defines the sprite for the left and right boundary'''
    def __init__(self, width, height, x_position, y_position):
        '''This initializer method takes the width, height, x position, and y
        position as paramaters and make the boundary sprite for the class'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Our endzone sprite will be a 40 pixel wide
        self.image = pygame.Surface((width, height))
        self.image = self.image.convert()
        self.image.fill((225, 0, 0))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left = x_position
        self.rect.top = y_position
        
        
class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for the Player'''
    def __init__(self, screen, x_position):
        '''This initializer takes a screen surface, and player x position as
        parameters and creates the sprite for Player'''
        # Call the parent of __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Define the image attributes
        self.image = pygame.Surface((80,5))
        self.image.fill((255, 255, 0))        
        self.rect = self.image.get_rect()
 
        # Position the player board at approx. middle of the screen
        self.rect.left = (screen.get_width()/2)-25

        # Center the player vertically x_position above the bottom
        self.rect.top = x_position
        self.__screen = screen
        self.__dx = 0
            
    def change_direction(self, x_change):
        '''This method takes a (x,y) tuple as a parameter and takes the x value
        to set the players x direction.'''
        self.__dx = x_change[0]
         
    def update(self):
        '''This method repositions the player sprite on the screen.'''
        if ((self.rect.left - 42 > 0) and (self.__dx > 0)) or\
           ((self.rect.right + 42 < self.__screen.get_width()) and (self.__dx < 0)):
            self.rect.left -= (self.__dx*5)
        
            
class Brick(pygame.sprite.Sprite):
    '''This class defines the brick sprite'''
    def __init__(self, screen, x_value, y_value, colour):
        '''This initializer method takes the screen, x value, y value, and 
        colour as parameters and creates the brick sprite for the class'''
        # Call the parent of __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        self.__colour = colour
        self.image = pygame.Surface((31, 10))
        self.image.fill(self.__colour)        
        self.rect = self.image.get_rect()
        
        # Changes the x value by the width of each brick
        self.__x = 41 + x_value
        # Changes the y value by the height of each brick
        self.__y = 125 + y_value
        
        self.rect.left = self.__x
        self.rect.top = self.__y
    
    def get_colour(self):
        '''This method returns the colour of the brick'''
        return self.__colour
        
    def y_position(self):
        '''This method makes the brick move down by 1 pixel'''
        self.rect.top = self.rect.top +1
        
        
class Message(pygame.sprite.Sprite):
    '''This class defines a label sprite'''
    def __init__(self, font, word, number, position):
        '''This initializer accepts the font, word, number, and position as
        parameters'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the starting score.
        self.__font = font
        self.__num = number
        self.__word = word
        self.__position = position
    
    def set_num(self, num):
        '''This method accepts num as parameter and changes the number value by
        adding the parameter to it'''
        self.__num =  self.__num + num
        
    def get_num(self):
        '''This method returns the number value'''
        return self.__num
        
    def update(self):
        '''This method will be called automatically to display 
        the message desired'''
        self.__message = self.__word+"%d" %self.__num
        self.image = self.__font.render(self.__message, 1, (225, 225, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.__position
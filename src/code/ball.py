import pygame as py
import sound

class Ball:
    def __init__(self, x : int, y : int, radius : float, speed_x : int, speed_y : int):        
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        
        self.radius = radius
        self.gravity = 1.0
        self.elasticity = 0.8
        self.inertia = 0.90

        self.Bonk_Sound = sound.Sound("sound/bonk.mp3", volume=0.2)
        self.PlayedSound = False

        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 960
        
        self.color = (255, 255, 255)

    
    def draw(self, screen : py.display):
        self.screen = screen
        py.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def move(self):
        #Gravity
        self.speed_y += self.gravity
        self.y += self.speed_y
        self.x += self.speed_x

        #The condition is that the circle cannot jump endlessly
        if self.y + self.radius >= self.SCREEN_HEIGHT:
            self.y = self.SCREEN_HEIGHT - self.radius
            self.speed_y = -self.speed_y * self.elasticity
            
            #Sound effects:
            if not self.PlayedSound:
                self.Bonk_Sound.play()
                self.PlayedSound = True
        if self.y + self.radius < self.SCREEN_HEIGHT:
                self.PlayedSound = False
        
                              
        if self.x - self.radius <= 0 or self.x + self.radius >= self.SCREEN_WIDTH:
            self.speed_x = -self.speed_x * self.elasticity
        
        #Сondition for the circle to bounce off the edge of the window
        if self.x - self.radius <= 0:            
            self.speed_x = -self.speed_x * self.elasticity - 15
            self.Bonk_Sound.play()
        if self.x + self.radius >= self.SCREEN_WIDTH - 8:           
            self.speed_x = -self.speed_x * self.elasticity + 15
            self.Bonk_Sound.play()

        #Apply inertia
        self.speed_x *= self.inertia

        #Processing the ball collision with screen edges
        if self.x - self.radius < 0 or self.x + self.radius > self.SCREEN_WIDTH:
            self.speed_x *= -1
        if self.y - self.radius < 0 or self.y + self.radius > self.SCREEN_HEIGHT:
            self.speed_y *= -1
            self.Bonk_Sound.play()
        
        #Teleporting the ball if he out of bounce
        if self.x < -10 or self.x > self.SCREEN_WIDTH + 10 or self.y < -10 or self.y > self.SCREEN_HEIGHT + 10:
            self.x = self.SCREEN_WIDTH / 2
            self.y = self.SCREEN_HEIGHT / 2
import pygame as py
import sys
import ball
import text

class Game:
    def __init__(self, FPS : float):
        py.init()
        self.FPS = FPS
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 960
        
        self.display = py.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))  
        py.display.set_caption("Ball physics simulation")
    
        self.clock = py.time.Clock()
        self.is_running = True
        
        self.Ball_1 = ball.Ball(int(self.SCREEN_WIDTH / 2), int(self.SCREEN_HEIGHT / 2), radius=30, speed_x=5, speed_y=5)

        self.mouse_pressed = False
        self.start_x = 0
        self.start_y = 0

    def run(self):
        while self.is_running:
            self.clock.tick(self.FPS)  
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.is_running = False
                
                #Event thats make to move a circle
                if event.type == py.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        print("Left mouse button pressed")                       
                        mouse_x, mouse_y = py.mouse.get_pos()                       
                        if (mouse_x - self.Ball_1.x) ** 2 + (mouse_y - self.Ball_1.y) ** 2 <= self.Ball_1.radius ** 2:
                            self.mouse_pressed = True   
                            self.start_x, self.start_y = event.pos  # Сохраняем начальные координаты круга
                            self.Ball_1.speed_x, self.Ball_1.speed_y = 0, 0  # Сброс скоростей
                                         
                if event.type == py.MOUSEBUTTONUP:
                    if event.button == 1:  # Left mouse button
                        print("Left mouse button not pressed")
                        self.mouse_pressed = False
                        self.Ball_1.speed_x = (event.pos[0] - self.start_x) / 10  # Горизонтальная скорость зависит от перемещения мыши
                        self.Ball_1.speed_y  = (event.pos[1] - self.start_y) / 10
                
                if event.type == py.K_f:
                    self.Ball_1.x = self.SCREEN_WIDTH / 2
                    self.Ball_1.y = self.SCREEN_HEIGHT / 2
                
            if self.mouse_pressed:
                mouse_x, mouse_y = py.mouse.get_pos()
                        
            #Filling surface: 
            #================================================================================================
            self.display.fill((64, 64, 64))          
            #Drawing a ball: 
            #================================================================================================
            self.Ball_1.draw(self.display)
            self.Ball_1.move()            
            #================================================================================================
            
            #Drawing text to the screen:
            #================================================================================================
            self.FPS_Show = text.FPS(self.clock, self.display, fontsize=24)
            self.FPS_Show.draw()
            #================================================================================================
            self.Position_Show = text.Ball_Position(self.Ball_1.x, self.Ball_1.y, self.display, fontsize=24)
            self.Position_Show.draw()
            #================================================================================================

            #Updating screen:
            #================================================================================================
            py.display.flip()
            py.display.update()  
            #================================================================================================

        py.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game(60)
    game.run()

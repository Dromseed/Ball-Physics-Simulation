import pygame as py

class FPS:
    def __init__(self, clock : py.time.Clock, display : py.display, fontsize : int):
        self.clock = clock
        self.display = display
        self.fontSize = fontsize
        self.font = py.font.SysFont("Arial" , self.fontSize, bold = True)

    def draw(self):
        fps = str(int(self.clock.get_fps()))
        fps_t = self.font.render(f"FPS: {fps}", True, py.Color("GREEN"))
        self.display.blit(fps_t,(0,0))
    
class Ball_Position:
    def __init__(self, BallPos_x : int, BallPos_y: int, display : py.display, fontsize : int):
        self.BallPos_x = BallPos_x
        self.BallPos_y = BallPos_y
        self.fontSize = fontsize
        self.display = display
        self.font = py.font.SysFont("Arial" , self.fontSize, bold = True)
    
    def draw(self):
        posRender_x = self.font.render(f"Ball Position [x]: {int(self.BallPos_x)}", True, py.Color("GREEN"))
        posRender_y = self.font.render(f"Ball Position [y]: {int(self.BallPos_y)}", True, py.Color("GREEN"))
        self.display.blit(posRender_x,(0,50))
        self.display.blit(posRender_y,(0,80))
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, 
                    format='[%(asctime)s] - PID: %(process)d - TID: %(thread)d - %(levelname)s - %(message)s')

import pygame

class Game(object):
    
    def __init__(self, width=640, height=400, fps=30, *args, **kwargs):
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self.fps = fps
    
    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    logging.debug('Exit event: {e}'.format(e=event))
                    self.exit()
            
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(self.fps)
    
    def exit(self):
        pygame.quit()
        sys.exit()
        
if __name__ == '__main__':
    Game().run()
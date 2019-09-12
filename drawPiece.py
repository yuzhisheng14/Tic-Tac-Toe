import pygame
from pygame.sprite import Sprite

class DrawPiece(Sprite):
    def __init__(self, screen, settings, x, y):
        super().__init__()
        self.screen = screen
        self.settings = settings
        if settings.piece_flag:
            self.image = pygame.image.load('images/X.bmp')
        else:
            self.image = pygame.image.load('images/O.bmp')
        self.img_rect = self.image.get_rect()
        column_id = 0
        row_id = 1
        for id in range(9):
            if column_id < 3:
                column_id += 1
            else:
                column_id = 1
                row_id += 1
            if x >= (column_id-1)*self.img_rect.width and x < column_id*self.img_rect.width and \
               y >= (row_id-1)*self.img_rect.height and y < row_id*self.img_rect.height:
                self.img_rect.x = self.img_rect.width * (column_id - 1)
                self.img_rect.y = self.img_rect.height * (row_id - 1)
                self.id = id + 1

    def draw(self):
        self.screen.blit(self.image, self.img_rect)
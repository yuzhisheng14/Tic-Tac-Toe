import pygame.font

class Button():
    def __init__(self, settings, screen, location, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 300, 50
        self.butto_color = (2, 137, 176)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if int(location) == 1:
            loc = -4
            self.width, self.height = 900, 50
            self.butto_color = (230, 230, 230)
            self.text_color = (232, 155, 85)
        elif int(location) == 2:
            loc = -1
        elif int(location) == 3:
            loc = 1
        self.rect.center = self.screen_rect.center
        self.rect.centery = self.rect.centery + loc * self.height

        self.draw_msg(msg)

    def draw_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.butto_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.butto_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

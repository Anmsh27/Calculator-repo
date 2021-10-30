import pygame

class Button:
    def __init__(self, x, y, width, height, color, border_radius, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.border_radius = border_radius
        self.text = text

    def draw_button(self, surface, text_size=None, text_colour=None, text_x=None, text_y=None):
        button_final = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface=surface, color=self.color, rect=button_final, border_radius=self.border_radius)
        font = pygame.font.Font(None, text_size if text_size else 100)
        rendered = font.render(self.text, True, text_colour if text_colour else (0, 0, 0))
        surface.blit(rendered, (text_x if text_x else (self.x + self.width / 2 - 20), text_y if text_y else (self.y + self.height / 2 - 32)))

    def clicked(self, mouse_x, mouse_y):
        return True if (
                mouse_x > self.x and mouse_x < self.x + self.width and mouse_y > self.y and mouse_y < self.y + self.height) else False
import pygame


class FactorialException(Exception):
    pass


def value_error(surface):
    errorfont = pygame.font.Font(None, 100)
    rendered_result = errorfont.render('Error', True, (0, 0, 0))
    surface.blit(rendered_result, (0, 136))


def zero_division_error(surface):
    errorfont1 = pygame.font.Font(None, 48)
    rendered_result1 = errorfont1.render('Error: Dividing by zero', True, (0, 0, 0))
    surface.blit(rendered_result1, (0, 168))


def factorial_error(surface):
    errorfont2 = pygame.font.Font(None, 48)
    rendered_result3 = errorfont2.render('Error:', True, (0, 0, 0))
    rendered_result2 = errorfont2.render('Input a natural number', True, (0, 0, 0))
    surface.blit(rendered_result3, (0, 136))
    surface.blit(rendered_result2, (0, 168))


def overflow_error(surface):
    errorfont = pygame.font.Font(None, 100)
    rendered_result = errorfont.render('Math error', True, (0, 0, 0))
    surface.blit(rendered_result, (0, 136))

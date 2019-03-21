import pygame

background_colour = (0, 120, 255)
(width, height) = (800, 600)


class Particle:
    def __init__(self, position, size):
        self.x, self.y = position
        self.size = size
        self.colour = (0, 0, 0)
        self.thickness = 1

    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Círculo')
screen.fill(background_colour)

my_first_particle = Particle((400, 300), 50)
my_first_particle.display()

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

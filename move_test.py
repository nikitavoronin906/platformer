import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Mario(pygame.sprite.Sprite):
    image = load_image("char_stand.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Mario.image
        self.rect = self.image.get_rect()

    def update(self, args):
        self.rect.x = args[0]
        self.rect.y = args[1]


all_sprites = pygame.sprite.Group()
character_spr = pygame.sprite.Sprite()
character_spr.image = load_image("char_stand.png")
character_spr.rect = character_spr.image.get_rect()


running = True
pygame.init()
pygame.display.set_caption('custom_curs')
size = width, height = 1000, 500
screen = pygame.display.set_mode(size)
arrow = Mario(all_sprites)
screen.fill((255, 255, 255))
character_coords = [0, 0]
clock = pygame.time.Clock()
l_f = False
d_f = False
r_f = False
u_f = False
gravity = 1.035
jump = False
j_count = 10
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    l_f = keys[pygame.K_LEFT] and character_coords[0] > 5
    r_f = keys[pygame.K_RIGHT] and character_coords[0] < 945
    if keys[pygame.K_SPACE]:
        jump = True
    if not jump:
        d_f = keys[pygame.K_DOWN] and character_coords[1] < 945
        u_f = keys[pygame.K_UP] and character_coords[1] > 5
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if j_count >= -10:
            n = 1
            if j_count < 0:
                n = -1
            character_coords[1] -= j_count ** 2 * 0.4 * n
            j_count -= 1
        else:
            j_count = 10
            jump = False

    character_coords[0] += -5 * l_f + 5 * r_f
    character_coords[1] += -5 * u_f + 5 * d_f
    arrow.update((character_coords[0], character_coords[1]))
    print(character_coords)
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    clock.tick(45)
    pygame.display.flip()

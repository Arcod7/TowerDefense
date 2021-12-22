import pygame

pygame.init()

BOX_SIZE = 400
BOX_SURFACE = (3*BOX_SIZE, 3*BOX_SIZE)

pygame.mouse.set_visible(True)
screen = pygame.display.set_mode(BOX_SURFACE)
pygame.display.set_caption("The Best Tower-Defense")


b = ['ld', 'dd', 'dr', 'll', 'square', 'rr', 'ul', 'uu', 'ru']

for path in range(5):
    img = pygame.transform.scale(pygame.image.load(f'all_paths/paths{path}.png').convert_alpha(), BOX_SURFACE)
    screen.blit(img, (0, 0))
    i = 0
    for x in range(3):
        for y in range(3):
            rect = pygame.Rect(x*BOX_SIZE, y*BOX_SIZE, BOX_SIZE, BOX_SIZE)
            sur = screen.subsurface(rect)
            pygame.image.save(sur, f'{path}_{b[i]}.png')
            pygame.display.flip()
            i += 1

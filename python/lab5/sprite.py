import pygame
from animation import Rotation, Linear

class MySprite(pygame.sprite.Sprite):

    def __init__(self, pos):
        super(MySprite, self).__init__()
        self.pos = pos
        self.surf = pygame.Surface((122, 70), pygame.SRCALPHA)
        pygame.draw.polygon(self.surf, pygame.Color('dodgerblue1'),
                        ((1, 0), (120, 35), (1, 70)))
        self.orig_surf = self.surf
        self.rect = self.surf.get_rect(center=self.pos)
        self.rotation = Rotation(0)
        self.linear = None

    def rotate(self, omega, min=None, max=None, on_end=None, back_start=None):
        if on_end is None:
            on_end = lambda s: ()
        if back_start is None:
            back_start = lambda s: ()
        on_end = on_end(self)
        back_start = back_start(self)
        self.rotation = Rotation(omega, min, max)
        self.rotation.on_end(on_end)
        self.rotation.back_on_start(back_start)
        return self

    def linear_move(self, speed, start, end, on_end=None, back_start=None):
        if on_end is None:
            on_end = lambda x: lambda: ()
        if back_start is None:
            back_start = lambda x: lambda: ()
        self.move_to(*start)
        self.linear = Linear(speed, *start, *end)
        self.rotation.on_end(on_end(self))
        self.rotation.back_on_start(back_start(self))
        return self

    def rotate_tick(self):
        self.rotation.update()
        self.surf = pygame.transform.rotozoom(self.orig_surf, self.rotation.rotation, 1)
        self.rect = self.surf.get_rect(center=self.rect.center)
    
    def update(self):
        self.rotate_tick()
        self.linear_tick()
    
    def linear_tick(self):
        if self.linear:
            self.linear.update()
            self.move_to(self.linear.x, self.linear.y)

    def move_to(self, new_x, new_y):
        x = self.rect.x
        y = self.rect.y
        dx = new_x - x - self.rect.width // 2
        dy = new_y - y - self.rect.height // 2
        self.rect.move_ip(dx, dy)

    def add_image(self, path, scale=1):
        self.surf = pygame.image.load(path).convert_alpha()
        if scale != 1:
            height = self.surf.get_width()
            width = self.surf.get_height()
            new_height = int(height * scale)
            new_width = int(width * scale)
            self.surf = pygame.transform.scale(self.surf, (new_width, new_height))
        self.orig_surf = self.surf
        self.rect = self.surf.get_rect(center=self.pos)

    
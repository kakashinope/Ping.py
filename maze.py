from pygame import *

win_width = 700
win_height = 500


window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

class Sprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()

        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 655:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <  500-80:
            self.rect.y += self.speed

class Enemy(Sprite):
    direction = 'left'

    def move(self):
        if self.rect.x < 500:
            self.direction = 'right'
        if self.rect.x > 650:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, rgb, x,y,w,h):
        super().__init__()
        self.rgb = rgb
        self.width = w
        self.height = h
        self.wall = Surface((w,h))
        self.wall.fill(rgb)

        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.wall, (self.rect.x, self.rect.y))


player = Player('hero.png', 5, 80, 4)
monster = Enemy('cyborg.png', 80, 280, 2)
final = Sprite('treasure.png', 570,430, 0)





w1 = Wall((29,65,59), 100,1, 50, 100)
w2 = Wall((29,65,59), 100,200, 50, 320)
w3 = Wall((29,65,59), 300,1, 50, 320)
w4 = Wall((29,65,59), 300,400, 50, 100)
w5 = Wall((29,65,59), 500,1, 50, 100)
w6 = Wall((29,65,59), 500,200, 50, 320)

game = True
clock = time.Clock()
FPS = 60

#музика
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

font.init()
font = font.Font(None,70)
win = font.render('YOU WIN', True,(255,255,255))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0, 0))
    player.reset()
    monster.move()
    player.move()

    if sprite.collide_rect(player, monster) or sprite.collide_rect(player,w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6):
        player.rect.x = 20
        player.rect.y = 20

    if sprite.collide_rect(player, final):
        window.blit(win,(200,200))




    final.reset()
    monster.reset()
    w1.draw()
    w2.draw()
    w3.draw()
    w4.draw()
    w5.draw()
    w6.draw()
    display.update()
    clock.tick(FPS)
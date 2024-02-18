# Importing necessary libraries
from pygame import *

# Setting up window dimensions
win_width = 700
win_height = 500

# Initializing Pygame
init()

# Creating the game window
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")

# Loading background image
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

# Creating a Sprite class for game objects
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

# Creating a Player class, inheriting from Sprite
class Player(Sprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 655:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500-80:
            self.rect.y += self.speed

# Creating an Enemy class, inheriting from Sprite
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

# Creating a Wall class for obstacles
class Wall(sprite.Sprite):
    def __init__(self, rgb, x, y, w, h):
        super().__init__()
        self.rgb = rgb
        self.width = w
        self.height = h
        self.wall = Surface((w, h))
        self.wall.fill(rgb)

        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.wall, (self.rect.x, self.rect.y))

# Creating instances of Player, Enemy, and Walls
player = Player('hero.png', 5, 80, 4)
monster = Enemy('cyborg.png', 80, 280, 2)
final = Sprite('treasure.png', 570, 430, 0)

w1 = Wall((29, 65, 59), 100, 1, 50, 100)
w2 = Wall((29, 65, 59), 100, 200, 50, 320)
w3 = Wall((29, 65, 59), 300, 1, 50, 320)
w4 = Wall((29, 65, 59), 300, 400, 50, 100)
w5 = Wall((29, 65, 59), 500, 1, 50, 100)
w6 = Wall((29, 65, 59), 500, 200, 50, 320)

# Setting up the game loop
game = True
clock = time.Clock()
FPS = 60

# Loading and playing background music
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

# Rendering 'YOU WIN' text
font.init()
text_font = font.Font(None, 70)
win_text = text_font.render('YOU WIN', True, (255, 255, 255))

# Main game loop
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    # Drawing background
    window.blit(background, (0, 0))

    # Moving and drawing player and enemy
    player.reset()
    monster.move()
    player.move()

    # Handling collisions with player and walls
    if sprite.collide_rect(player, monster) or any(sprite.collide_rect(player, wall) for wall in [w1, w2, w3, w4, w5, w6]):
        player.rect.x = 20
        player.rect.y = 20

    # Checking if player reached the treasure
    if sprite.collide_rect(player, final):
        window.blit(win_text, (200, 200))

    final.reset()
    monster.reset()

    # Drawing walls
    w1.draw()
    w2.draw()
    w3.draw()
    w4.draw()
    w5.draw()
    w6.draw()

    # Updating display and controlling FPS
    display.update()
    clock.tick(FPS)

# Quitting Pygame properly
quit()

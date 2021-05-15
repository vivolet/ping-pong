from pygame import *

#mixer.init()
#mixer.music.load('jungles.ogg')
#mixer.music.play()
#money = mixer.Sound('money.ogg')
#kick = mixer.Sound('kick.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

            
back = (255, 255, 255)
win_width = 680
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

display.set_caption('PingPong')
#background = transform.scale(image.load('background.jpg'), (700, 500))
game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tennis_ball.png', 200, 200, 4, 50, 0)
#font.init()
#font = font.Font(None, 70)
#win = font.render('YOU WIN!', True, (255, 215, 0))
#lose = font.render('YOU LOSE!', True, (255, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
                game = False
    if finish != True:
        window.fill(back)
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_l()
        racket2.update_r()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        keys_pressed = key.get_pressed()
        if sprite.collide_rect(hero, treasure):
            window.blit(win, (200, 200))
            finish = True
            money.play()
        if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2) or sprite.collide_rect(hero, wall3) or sprite.collide_rect(hero, wall4) or sprite.collide_rect(hero, wall5):
            window.blit(lose, (200, 200))
            finish = True
            kick.play()
    display.update()
    clock.tick(FPS)
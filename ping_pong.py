from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,Player_speed,width,height):
        super().__init__()
        self.image =  transform.scale(image.load(player_image),(width,height))
        self.speed = Player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys= key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        keys= key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

game = True
finish = False
width = 700
height = 500
window = display.set_mode((width,height))
background = transform.scale(image.load('background.jpg'), (700, 500))

speed_x = 3
speed_y = 3

clock = time.Clock()
FPS = 60

font.init()
font1 = font.SysFont(None, 70)
lose_1 = font1.render("1st player lose",1,(0, 0, 255))
lose_2 = font1.render("2nd player lose",1,(0, 0, 255))

ball = GameSprite("ball.png", 200, 200, 4, 50, 50)
racket_1 = Player("racket.png", 30, 200, 4, 15, 150)
racket_2 = Player("racket.png", 650, 200, 4, 15, 150)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        racket_1.update_l()
        racket_2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        racket_1.reset()
        racket_2.reset()
        if sprite.collide_rect(racket_1, ball) or sprite.collide_rect(racket_2, ball):
            speed_x *= -1
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x > 700:
            window.blit(lose_2,(180, 20))
        if ball.rect.x < 0:
            window.blit(lose_1,(180, 200))
    display.update()
    clock.tick(FPS)
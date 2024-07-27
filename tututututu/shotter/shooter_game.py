#Створи власний Шутер!

from pygame import *
from random import randint

# клас-батько для інших спрайтів
class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    # метод, що малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас головного гравця
class Player(GameSprite):
    def update(self) :
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>4:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x<wind_width-50:
            self.rect.x += self.speed
    
    def shoot(self): 
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.y, 5, 20, 3)
        bullets.add(bullet)
        

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y >480:
            x = randint(5,645)
            speed = randint(1,7)
            self.speed = speed 
            self.rect.x = x
            self.rect.y = 5
            lost = lost + 1 

class Bullet(GameSprite):
    def update(self):
        self.rect.y  -= self.speed
        if self.rect.y == 0:
            self.kill()

wind_height = 500
wind_width = 700

window = display.set_mode((wind_width,wind_height))
display.set_caption("Shooter")
background = transform.scale(image.load("galaxy.jpg"),(wind_width,wind_height))



# mixer.init()
# mixer.music.load("space.ogg")
# mixer.music.play()

lost = 0
score = 0

font.init()
font1 = font.Font(None,36)
font2 = font.Font(None,75)
win_text = font2.render ('YOU WIN', 1, (0,255,0))

lose_text= font2.render ('YOU Lose', 1, (255,0,0))



ship = Player("rocket.png",0,440,50,70,10) 

monters = sprite.Group()
for i in range(5):
    en1 = Enemy("ufo.png", randint(5,645),5, 50,50, randint(1,7))
    monters.add(en1)

bullets = sprite.Group()


#bull1 = Bullet("bullet.png",30,440,10,20,5)


clock = time.Clock()
FPS = 60


game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.shoot()
                #fire_soyr.play()
    #keys = key.get_pressed()
    #if keys[K_SPACE]:
    #    #fire_soyr.play()
    #    ship.shoot()


    if not finish:
        window.blit(background,(0,0))

        score_text =font1.render("Рахунок: " + str(score),1,(255,255,255))
        window.blit(score_text, (10,10))

        lost_text =font1.render("Пропущено: " + str(lost),1,(255,255,255))
        window.blit(lost_text, (10,30))

        
        ship.reset()
        ship.update()

        monters.update()
        monters.draw(window)
       
        bullets.update()
        bullets.draw(window)
        #bull1.reset()
        #bull1.update()

        collides = sprite. groupcollide(monters,bullets,True,True)
        for i in collides:
            score = score +1
            en1 = Enemy("ufo.png", randint(5,645),5, 50,50, randint(1,7))
            monters.add(en1)

        if score> 15:
            finish = True
            window.blit(win_text,(200,200))

        if lost >5 or sprite.spritecollide(ship,monters, False):
            finish = True
            window.blit(lose_text,(200,200))

        display.update()
    
    clock.tick(FPS)

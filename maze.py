#создай игру "Лабиринт"!



from pygame import *
mixer.init()
font.init()

window = display.set_mode((700, 500))

background = transform.scale(image.load("background.jpg"), (700, 500))


player_image = "hero.png"
player_x = 100
player_y = 370

x2 = 400
y2 = 370

clock = time.Clock()
FPS = 60

speed = 5

money = mixer.Sound("money.ogg")
mixer.music.load("jungles.ogg")
mixer.music.play()
k = mixer.Sound("kick.ogg")



game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(60, 50))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    
    def update(self):
        
        keys_pressed = key.get_pressed()

        if keys_pressed [K_w] and self.rect.y > 0:
            self.rect.y -= self.speed


        if keys_pressed [K_s] and self.rect.y < 450:
            self.rect.y += self.speed

        if keys_pressed [K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

        if keys_pressed [K_d] and self.rect.x < 650:
            self.rect.x += self.speed



 

 


class Enemy(GameSprite):
    direction = "left"
    def update(self, x1, x2):
        if self.direction == "right":
            self.rect.x += self.speed

        if self.rect.x > x2:
            self.direction = "left"

        if self.direction =="left":
            self.rect.x -= self.speed

        if self.rect.x < x1:
            self.direction = "right"
 

class Wall(sprite.Sprite):
    def __init__(self, height, width, color1, color2, color3, wall_x, wall_y):
        super().__init__()
        self.height = height
        self.width = width
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color1, self.color2, self.color3)) 
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))    












hero = Player("hero.png", 5, 100, 370)
monster = Enemy("cyborg.png", 4, 500, 370 )
finaly = GameSprite("treasure.png", 0, 600, 450)
wall1 = Wall(300, 30, 124, 145, 140, 100, 20)
wall2 = Wall(30, 300, 124, 145, 140, 100, 20)
wall3 = Wall(500, 30, 124, 145, 140, 200, 150)
wall4 = Wall(500, 120, 124, 145, 140, 200, 150)
wall5 = Wall(300, 30, 124, 145, 140, 100, 20)
wall6 = Wall(300, 30, 124, 145, 140, 400, 20)
wall7 = Wall(100, 30, 124, 145, 140, 400, 400)




font1 = font.SysFont("Arial", 70)
win = font1.render("YOU WIN", True, (212, 206, 0))
font2 = font.SysFont("Arial", 70)
lose = font1.render("YOU LOSE", True, (235, 106, 0))

finish = False

while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))

        monster.update(500, 650)
        monster.reset()
        hero.update()
        hero.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        finaly.update()
        finaly.reset()
        if sprite.collide_rect(hero, finaly):
            window.blit(win,(200, 200))
            finish = True
            money.play()
        if sprite.collide_rect(hero, monster) or sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2) or sprite.collide_rect(hero, wall3) or sprite.collide_rect(hero, wall4) or sprite.collide_rect(hero, wall5) or sprite.collide_rect(hero, wall6) or sprite.collide_rect(hero, wall7):
            window.blit(lose,(200, 200))
            k.play()
            finish = True
    clock.tick(FPS)
    display.update()

    


    






















  #  keys_pressed = key.get_pressed()

   # if keys_pressed [K_w] and player_y > 0:
   #     player_y -= speed


   # if keys_pressed [K_s] and player_y < 400:
   #     player_y += speed

   # if keys_pressed [K_a] and player_x > 0:
   #     player_x -= speed

   # if keys_pressed [K_d] and player_x < 600:
  #      player_x += speed


   # if keys_pressed [K_UP] and y2 > 0:
   #     y2 -= speed


   # if keys_pressed [K_DOWN] and y2 < 400:
   #     y2 += speed

   # if keys_pressed [K_LEFT] and x2 > 0:
   #     x2 -= speed

    #if keys_pressed [K_RIGHT] and x2 < 600:
    #    x2 += speed

    
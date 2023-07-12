# Создай собственный Шутер!
import time
from random import *
from pygame import *
import time as tm

mixer.init()
font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 20)
font3 = font.SysFont('Oxygen', 230)
font4 = font.SysFont('Oxygen', 180)
run = True
say_rules = False
wait_f_t = False
paused = False
monsters = sprite.Group()
asteroids = sprite.Group()
meds = sprite.Group()
num_fire = 0
bullets = sprite.Group()
buttons = sprite.Group()
clock_run = time.Clock()
clock_rules = time.Clock()
FPS = 60
need_to_win = 1
need_to_over = 100
player_speed_m = 10
sec_of_reloading = 3
num_of_bullets = 8
num_of_monsters = 4
num_of_lost = 1
global not_lost
global med
global player_speed
health = 3
num_fire = 0
time_now = False
not_lost = 0
finish = False
uze_pomen = False


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_weight, palyer_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_weight, palyer_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 625:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('pictures/bullet.png', self.rect.centerx, self.rect.top, 15, 10, 20)
        bullets.add(bullet)
        fire_sound.play()

    def pause(self):
        keys = key.get_pressed()
        if keys[K_p] and paused == False:
            print('pause')
            self.speed == 0
            return True
        if keys[K_u] and paused == True:
            print('unpause')
            self.speed == player_speed_m
            return False



lost = 0


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(0, 550)
            lost = lost + 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


class med_kit(GameSprite):
    def update(self, med=None):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(0, 550)
            if med > 0:
                med - 1


class Button(GameSprite):
    def update(self):
        self.rect.y += self.speed

    def press(self):
        keys = key.get_pressed()
        if keys[K_g]:
            return 'easy'
        if keys[K_h]:
            return 'medium'
        if keys[K_j]:
            return 'hard'
    def test(self):
        keys = key.get_pressed()
        if keys[K_e]:
            print(say_rules)


# создание объектов
win_width = 700
win_height = 500
window = display.set_mode(
    (win_width, win_height)
)
display.set_caption('Space shooter')
background = transform.scale(image.load('pictures/galaxy.jpg'), (win_width, win_height))

start_button = Button('pictures/start_button.png', 500, 400, 1, 350, 100)
for i in range(1):
    med_e = Enemy('pictures/first-aid.png', randint(0, 550), 0, 2, 85, 65)
    meds.add(med_e)
for i in range(2):
    asteroid = Enemy('pictures/asteroid.png', randint(0, 600), 0, 1, 85, 65)
    asteroids.add(asteroid)

# создание музыкиa
mixer.music.load('pictures/space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('pictures/fire.ogg')
mixer.music.set_volume(0)
fire_sound.set_volume(0.1)
# вывод правил
while say_rules == False:
    for e in event.get():
        if e.type == QUIT:
            run = False
            exit()
    fon_rules = GameSprite('pictures/galaxy_rules_2.png', 0, 0, 0, 700, 500)
    fon_rules.reset()
    start_button.update()
    if start_button.press() == 'easy':
        health = 5
        need_to_win = 25
        need_to_over = 100
        player_speed_m = 10
        player = Player('pictures/rocket.png', 285, 400, player_speed_m, 60, 65)
        sec_of_reloading = 1
        num_of_bullets = 10
        num_of_monsters = 3
        for i in range(num_of_monsters):
            monster = Enemy('pictures/ufo.png', randint(0, 600), 0, randint(2, 4), 85, 65)
            monsters.add(monster)
        say_rules = True
        print('Game started')
    if start_button.press() == 'medium':
        health = 3
        need_to_win = 25
        need_to_over = 70
        player_speed_m = 7
        player = Player('pictures/rocket.png', 285, 400, player_speed_m, 60, 65)
        sec_of_reloading = 2
        num_of_bullets = 8
        num_of_monsters = 4
        for i in range(num_of_monsters):
            monster = Enemy('pictures/ufo.png', randint(0, 600), 0, randint(2, 4), 85, 65)
            monsters.add(monster)
        say_rules = True
        print('Game started')
    if start_button.press() == 'hard':
        health = 1
        need_to_win = 50
        need_to_over = 70
        player_speed_m = 6
        player = Player('pictures/rocket.png', 285, 400, player_speed_m, 60, 65)
        sec_of_reloading = 3
        num_of_bullets = 7
        num_of_monsters = 4
        for i in range(num_of_monsters):
            monster = Enemy('pictures/ufo.png', randint(0, 600), 0, randint(2, 4), 85, 65)
            monsters.add(monster)
        say_rules = True
        print('Game started')
    start_button.test()
    text_rules = font1.render('Правила', 6, (0, 194, 152))
    text_rules_1 = font2.render('Добро пожаловать в игру Space shooter', 1, (0, 255, 238))
    text_rules_2 = font2.render('твоя цель сбить всех инопланетян и не попастся под астероид.', 1, (0, 255, 238))
    text_rules_3 = font2.render('У тебя есть всего несколько жизни, но ты можешь их увеличить', 1, (0, 255, 238))
    text_rules_4 = font2.render('собирая аптечки разбросанные по космосу', 1, (0, 255, 238))
    text_rules_5 = font2.render('У тебя есть оружие которым ты можешь стрелять по инопланетянам.', 1, (0, 255, 238))
    text_rules_6 = font2.render('К сожелению оно не способно сбить астероид и не может стрелять вечно.', 1,
                                (0, 255, 238))
    text_control_1 = font1.render('Управление:', 1, (0, 194, 152))
    text_control_2 = font2.render('d - Двигатся влево', 1, (0, 255, 238))
    text_control_3 = font2.render('a - Двигатся вправо', 1, (0, 255, 238))
    text_control_4 = font2.render('spase - стрелять', 1, (0, 255, 238))
    text_easy_1 = font2.render('Кнопка: G    режим сложности - EASY', 1, (0, 255, 238))
    text_easy_2 = font2.render('Кнопка: H    режим сложности - MEDIUM', 1, (0, 255, 238))
    text_easy_3 = font2.render('Кнопка: J    режим сложности - HARD', 1, (0, 255, 238))
    window.blit(text_rules, (285, 20))
    window.blit(text_rules_1, (10, 70))
    window.blit(text_rules_2, (10, 100))
    window.blit(text_rules_3, (10, 130))
    window.blit(text_rules_4, (10, 160))
    window.blit(text_rules_5, (10, 190))
    window.blit(text_rules_6, (10, 220))
    window.blit(text_control_1, (275, 270))
    window.blit(text_control_2, (10, 320))
    window.blit(text_control_3, (10, 350))
    window.blit(text_control_4, (10, 380))
    window.blit(text_easy_1, (380, 330))
    window.blit(text_easy_2, (380, 350))
    window.blit(text_easy_3, (380, 370))
    display.update()
    clock_rules.tick(FPS)

# игровой цикл
if say_rules == True:
    mixer.music.set_volume(0.2)
    while run:
        for e in event.get():
            if e.type == QUIT:
                run = False
                exit()
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    if time_now == False:
                        if num_fire <= num_of_bullets:
                            player.fire()
                            num_fire = num_fire + 1
                        else:
                            curn_time = tm.time()
                            time_now = True
                    else:
                        if tm.time() - curn_time >= sec_of_reloading:
                            time_now = False
                            num_fire = 0
                            wait_f_t = False
                        else:
                            wait_f_t = True
        if finish != True:
            window.blit(background, (0, 0))
            if wait_f_t == True:
                text_wait = font1.render('Перезарядка', 1, (255, 0, 0))
                window.blit(text_wait, (275, 250))
            player.update()
            player.reset()
            monsters.draw(window)
            monsters.update()
            meds.draw(window)
            meds.update()
            bullets.draw(window)
            bullets.update()
            asteroids.draw(window)
            asteroids.update()
            if player.pause() == True:
                paused = True
            if player.pause() == False:
                paused = False
            text_lose = font1.render('Пропущено:' + str(lost), 1, (255, 55, 255))
            text_score = font1.render('Счёт:' + str(not_lost), 0, (255, 55, 255))
            text_life = font1.render('Жизни: ' + str(health), 0, (255, 0, 0))
            window.blit(text_lose, (5, 0))
            window.blit(text_score, (5, 50))
            window.blit(text_life, (575, 0))
            sprite_list2 = sprite.groupcollide(meds, bullets, True, True)
            for i in sprite_list2:
                health = health + 1
                med_e = Enemy('pictures/first-aid.png', randint(0, 550), 0, 1, 85, 65)
                meds.add(med_e)
            sprite_list = sprite.groupcollide(monsters, bullets, True, True)
            for i in sprite_list:
                not_lost = not_lost + 1
                monster = Enemy('pictures/ufo.png', randint(0, 600), 0, randint(2, 4), 85, 65)
                monsters.add(monster)
            sprite_list3 = sprite.spritecollide(player, asteroids, True)
            for i in sprite_list3:
                health = health - 1
                asteroid = Enemy('pictures/asteroid.png', randint(0, 600), 0, 1, 85, 65)
                asteroids.add(asteroid)
            if paused == True:
                if uze_pomen == False:
                    num_of_lost = lost
                    uze_pomen = True
                fon_paused = GameSprite('pictures/galaxy_paused.png', 0, 0, 0, 700, 500)
                fon_paused.reset()
                text_need_kill = font2.render(str(need_to_win - not_lost), 1, (0, 255, 238))
                window.blit(text_need_kill, (215, 143))

                text_lifes_left = font2.render(str(health), 1, (255, 0, 0))
                window.blit(text_lifes_left, (232, 243))

                text_fail = font2.render(str(need_to_over - num_of_lost), 1, (0, 255, 238))
                window.blit(text_fail, (310, 343))

                mixer.music.set_volume(0)
                fire_sound.set_volume(0)
            if paused == False:
                if uze_pomen == True:
                    lost = num_of_lost
                    uze_pomen = False
                mixer.music.set_volume(0.1)
                fire_sound.set_volume(0.2)
            if lost >= need_to_over:
                finish = True
                fon_fon = GameSprite('pictures/galaxy.jpg', 0, 0, 0, 700, 500)
                fon_fon.reset()
                text_not_win = font4.render('Game Over', 1, (255, 0, 0))
                window.blit(text_not_win, (11, 200))
                mixer.music.set_volume(0)
                fire_sound.set_volume(0)
            if health <= 0:
                finish = True
                fon_fon = GameSprite('pictures/galaxy.jpg', 0, 0, 0, 700, 500)
                fon_fon.reset()
                text_not_win = font4.render('Game Over', 1, (255, 0, 0))
                window.blit(text_not_win, (11, 200))
                mixer.music.set_volume(0)
                fire_sound.set_volume(0)
            if not_lost >= need_to_win:
                finish = True
                fon_fon = GameSprite('pictures/galaxy.jpg', 0, 0, 0, 700, 500)
                fon_fon.reset()
                text_win = font3.render('You win!', 1, (0, 255, 0))
                window.blit(text_win, (25, 200))
                mixer.music.set_volume(0)
                fire_sound.set_volume(0)
        display.update()
        clock_run.tick(FPS)

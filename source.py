import pygame
import parameter
import random

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('./musics/Denny Roger - All For Love.mp3')
frame=pygame.display.set_mode((800,600))
pygame.display.set_caption("Spark Knight and Tcho-Tcho")
girl = pygame.image.load('./images/keli.png')
backimage = pygame.image.load("./images/background.bmp")
girl_rect = girl.get_rect()
frame_rect = frame.get_rect()
girl_rect.center = frame_rect.center
pygame.mixer.music.play(loops=-1, start=0.0)
monsters=pygame.sprite.Group()
monsters2=pygame.sprite.Group()
bullets=pygame.sprite.Group()
#monsters.add(monster)
# control
level=0
exam=0
score=0
lose=0
totoalmonsters=0
moving_left=False
moving_right=False
moving_up=False
moving_down=False
fire_bullets=False
# plot
clock=pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left=True
            if event.key == pygame.K_RIGHT:
                moving_right=True
            if event.key == pygame.K_UP:
                moving_up=True
            if event.key == pygame.K_DOWN:
                moving_down=True
            if event.key == pygame.K_SPACE:
                fire_bullets=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left=False
            if event.key == pygame.K_RIGHT:
                moving_right=False
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False
            if event.key == pygame.K_SPACE:
                fire_bullets = False
    if fire_bullets:
        new_bullet = pygame.sprite.Sprite()
        new_bullet.image = pygame.image.load('./images/pengpeng.png')
        new_bullet.rect = new_bullet.image.get_rect()
        new_bullet.rect.midtop = girl_rect.midtop
        if len(bullets)< 15:
            bullets.add(new_bullet)
    if moving_up:
        girl_rect.y -= parameter.girl_speed
    elif moving_down:
        girl_rect.y += parameter.girl_speed
    elif moving_left:
        girl_rect.x -= parameter.girl_speed
    elif moving_right:
        girl_rect.x += parameter.girl_speed
    parameter.outrange(girl_rect,800,600)
    frame.blit(backimage,(0,0))
    frame.blit(girl, girl_rect)
    if len(monsters) < 1:
        new_monster = pygame.sprite.Sprite()
        new_monster.image = pygame.image.load('./images/monster.png')
        new_monster.rect = new_monster.image.get_rect()
        new_monster.rect.x = random.randint(0,800)
        new_monster.rect.y = random.randint(0,40)
        monsters.add(new_monster)
    for monster in monsters:
        monsters.draw(frame)
        if random.randint(1,20)==13:
            monster.rect.x+=40
        monster.rect.x += random.randint(-1,10)
        monster.rect.x -= random.randint(0,5)
        monster.rect.y += random.randint(-1,2)
        if monster.rect.x > 800:
            monsters.remove(monster)
            lose += 1
        if monster.rect.x < 0:
            monsters.remove(monster)
            lose += 1

    ###monster 2

    if len(monsters2) < 1:
        new_monster2 = pygame.sprite.Sprite()
        new_monster2.image = pygame.image.load('./images/monster.png')
        new_monster2.rect = new_monster2.image.get_rect()
        new_monster2.rect.x = random.randint(0,800)
        new_monster2.rect.y = random.randint(0, 40)
        monsters2.add(new_monster2)
    for monster2 in monsters2:
        monsters2.draw(frame)
        monster2.rect.x -= random.randint(-1,10)
        monster2.rect.x += random.randint(0,5)
        monster2.rect.y += random.randint(-1,2)
        if monster2.rect.x > 800:
            monsters2.remove(monster2)
            lose += 1
        if monster2.rect.x < 0:
            monsters2.remove(monster2)
            lose += 1


    for bullet in bullets:
        bullets.draw(frame)
        bullet.rect.y -= 10
        if bullet.rect.bottom <0:
            bullets.remove(bullet)
    crack=pygame.sprite.groupcollide(bullets,monsters,True,True)
    if crack:
        for item in crack.values():
            score += len(item)
    crack2 = pygame.sprite.groupcollide(bullets, monsters2, True, True)
    if crack2:
        for item in crack2.values():
            score += len(item)
    prscore = str(score)
    totoalmonsters = score+lose
    prtotoalmonsters = str(totoalmonsters)
    if not totoalmonsters ==0:
        level = score/totoalmonsters
        level=round(level,2)
    if score > 100 and exam==0 and level > 0.5:
        backimage = pygame.image.load("./images/background2.bmp")
        pygame.mixer.music.load('./musics/dj.mp3')
        pygame.mixer.music.play(loops=-1, start=0.0)
        exam += 1
    if score > 300 and exam ==1 and level > 0.6:
        backimage = pygame.image.load("./images/background3.bmp")
        pygame.mixer.music.load('./musics/The Chainsmokers _ Coldplay - Something Just Like This.mp3')
        pygame.mixer.music.play(loops=-1, start=0.0)
        exam +=1
    srlevel=str(level)
    score_font=pygame.font.SysFont(None,48)
    score_image=score_font.render(f'{prscore}:{prtotoalmonsters}',True,(0,0,0),(255,255,255))
    score_rect=score_image.get_rect()
    score_rect.right=frame_rect.right-20
    score_rect.top=20

    level_font=pygame.font.SysFont(None,48)
    level_image=level_font.render(srlevel,True,(0,0,0),(255,255,255))
    level_rect=level_image.get_rect()
    level_rect.right=frame_rect.right-20
    level_rect.top=60
    frame.blit(score_image, score_rect)
    frame.blit(level_image, level_rect)
    pygame.display.flip()


import pygame
import random

# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐, x 좌표는 매번 랜덤
# 3. 캐릭터가 똥을 피하면 다시 똥이 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30으로 고정

# 배경: 480 * 640 - background.png
# 캐릭터: 70 * 70 - character.png
# 똥: 70 * 70 - enemy.png


# ============================================================
# 기본 초기화
# ------------------------------------------------------------
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 타이틀 설정
pygame.display.set_caption("pygame_basic")

# FPS
clock = pygame.time.Clock()
# ============================================================


# ============================================================
# 사용자 게임 초기화 (스프라이트, 좌표, 속도, 폰트 등)
# ------------------------------------------------------------
img_path = "C:\\Users\\gkstm\\Desktop\\Python\\pygame_basic\\images\\basic\\"
background = pygame.image.load(img_path + "background.png")
character = pygame.image.load(img_path + "character.png")
enemy = pygame.image.load(img_path + "enemy.png")

c_width, c_height = character.get_rect().size
c_pos_x = (screen_width - c_width) / 2
c_pos_y = screen_height - c_height
c_trans_x = 0
c_speed = .6

e_width, e_height = enemy.get_rect().size
e_pos_x = 0
e_pos_y = 0 - e_height
e_trans_y = .8
e_is_falling = False
# ============================================================


# 이벤트 루프
running = True
while running: # Unity의 Update()와 같은 역할
    dt = clock.tick(30) # FPS를 설정 (델타타임)

    # ============================================================
    # 이벤트 처리 (키보드, 마우스)
    # ------------------------------------------------------------
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                c_trans_x -= c_speed
            elif event.key == pygame.K_RIGHT:
                c_trans_x += c_speed
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                c_trans_x = 0
    # ============================================================


    # ============================================================
    # 게임 캐릭터 위치 정의
    # ------------------------------------------------------------
    c_pos_x += c_trans_x * dt
    if c_pos_x < 0:
        c_pos_x = 0
    elif c_pos_x > screen_width - c_width:
        c_pos_x = screen_width - c_width
    
    if not e_is_falling:
        e_pos_x = random.randint(0, screen_width - e_width)
        e_pos_y = 0 - e_height
        e_is_falling = True
    e_pos_y += e_trans_y * dt
    if e_pos_y > screen_height:
        e_is_falling = False
    # ============================================================
    

    # ============================================================
    # 충돌 처리
    # ------------------------------------------------------------
    c_rect = character.get_rect()
    c_rect.left = c_pos_x
    c_rect.top = c_pos_y

    e_rect = enemy.get_rect()
    e_rect.left = e_pos_x
    e_rect.top = e_pos_y

    if c_rect.colliderect(e_rect):
        print("충돌!")
        running = False
    # ============================================================


    # ============================================================
    # 화면에 그리기
    # ------------------------------------------------------------
    screen.blit(background, (0,0))
    screen.blit(character, (c_pos_x, c_pos_y))
    screen.blit(enemy, (e_pos_x, e_pos_y))
    # ============================================================

    pygame.display.update() # 화면 그리기
    
pygame.quit()

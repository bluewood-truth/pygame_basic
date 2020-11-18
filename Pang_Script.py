import pygame

# 1. 캐릭터는 화면 아래에 위치, 좌우로 이동 가능
# 2. 스페이스를 누르면 무기를 쏘아 올림
# 3. 큰 공이 1개 나타나서 바운스
# 4. 무기에 닿으면 공은 작은 공 2개로 분할, 가장 작은 크기의 공은 사라짐
# 5. 모든 공을 없애면 게임 종료 (성공)
# 6. 캐릭터는 공에 닿으면 종료 (실패)
# 7. 시간제한 99초 초과 시 종료 (실패)
# 8. FPS는 30으로 고정

# 배경: 640 * 480 - background.png
# 땅: 640 * 50 - land.png
# 캐릭터: 33 * 60 - player.png
# 무기: 20 * 430 - weapon.png
# 공: 160 * 160, 80 * 80, 40 * 40, 20 * 20 - balloon1.png ~ balloon4.png

# ============================================================
# 기본 초기화
# ------------------------------------------------------------
pygame.init()

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 타이틀 설정
pygame.display.set_caption("pygame_pang")

# FPS
clock = pygame.time.Clock()
# ============================================================


# ============================================================
# 사용자 게임 초기화 (스프라이트, 좌표, 속도, 폰트 등)
# ------------------------------------------------------------
img_path = "C:\\Users\\gkstm\\Desktop\\Python\\pygame_basic\\images\\"
player = pygame.image.load(img_path + "player.png")
weapon = pygame.image.load(img_path + "weapon.png")
bg = pygame.image.load(img_path + "background.png")
land = pygame.image.load(img_path + "land.png")
balloon = []
for i in range(1,5):
    balloon.append(pygame.image.load(img_path + f"balloon{i}.png"))

bg_width, bg_height = bg.get_rect().size
bg_pos = (0, 0)
land_width, land_height = land.get_rect().size
land_pos = (0, screen_height - land_height)

p_width, p_height = player.get_rect().size
p_pos_x = (screen_width - p_width) / 2
p_pos_y = screen_height - p_height - land_height
p_trans_x = 0
p_speed = 0.6
p_moving = []

w_width, w_height = weapon.get_rect().size
w_pos_x = w_pos_y = 0
w_speed = 0.5
w_shooting = False
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
                p_moving.append(0)
            if event.key == pygame.K_RIGHT:
                p_moving.append(1)
            if event.key == pygame.K_SPACE and not w_shooting:
                w_pos_x = p_pos_x + (p_width - w_width) / 2
                w_pos_y = screen_height - land_height
                w_shooting = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                p_moving.remove(0)
            if event.key == pygame.K_RIGHT:
                p_moving.remove(1)
    # ============================================================


    # ============================================================
    # 게임 캐릭터 위치 정의
    # ------------------------------------------------------------
    if p_moving:
        p_trans_x = p_speed if p_moving[-1] == 1 else -p_speed
    else:
        p_trans_x = 0
    p_pos_x += p_trans_x * dt
    if p_pos_x < 0:
        p_pos_x = 0
    elif p_pos_x > screen_width - p_width:
        p_pos_x = screen_width - p_width

    if w_shooting:
        w_pos_y -= w_speed * dt
        if w_pos_y < 0:
            w_shooting = 0
    # ============================================================
    

    # ============================================================
    # 충돌 처리
    # ------------------------------------------------------------

    # ============================================================


    # ============================================================
    # 화면에 그리기
    # ------------------------------------------------------------
    screen.blit(bg, bg_pos)
    if w_shooting:
        screen.blit(weapon, (w_pos_x, w_pos_y))
    screen.blit(land, land_pos)
    screen.blit(player, (p_pos_x, p_pos_y))
    # ============================================================

    pygame.display.update() # 화면 그리기
pygame.quit()

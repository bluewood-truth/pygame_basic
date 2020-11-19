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

bg = pygame.image.load(img_path + "background.png")
land = pygame.image.load(img_path + "land.png")
bg_width, bg_height = bg.get_rect().size
bg_pos = (0, 0)
land_width, land_height = land.get_rect().size
land_pos = (0, screen_height - land_height)

player = pygame.image.load(img_path + "player.png")
p_width, p_height = player.get_rect().size
p_pos_x = (screen_width - p_width) / 2
p_pos_y = screen_height - p_height - land_height
p_trans_x = 0
p_speed = 0.4
p_moving = []

weapon = pygame.image.load(img_path + "weapon.png")
w_width, w_height = weapon.get_rect().size
w_pos_x = w_pos_y = 0
w_speed = 0.5
w_shooting = False

ball_imgs = []
for i in range(1,5):
    ball_imgs.append(pygame.image.load(img_path + f"balloon{i}.png"))
ball_speed_y = [ -.36, -.3, -.24, -.18 ] # 공 크기에 따른 최초 스피드
ball_size = [img.get_rect().size for img in ball_imgs]
ball_accel = 0.01 # 공 중력가속도
balls = [{
    "pos_x" : 50, 
    "pos_y" : 50, 
    "img_idx" : 0, 
    "trans_x": .1, # x축 이동방향
    "trans_y": -.1, # y축 이동방향
    "init_spd_y": ball_speed_y[0] # 최초 속도
}]
# ============================================================

# 이벤트 루프
is_is_running = True
is_win = None
while is_running: # Unity의 Update()와 같은 역할
    dt = clock.tick(30) # FPS를 설정 (델타타임)

    # ============================================================
    # 이벤트 처리 (키보드, 마우스)
    # ------------------------------------------------------------
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            is_running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p_moving.append(0)
            if event.key == pygame.K_RIGHT:
                p_moving.append(1)
            if event.key == pygame.K_SPACE and not w_shooting:
                w_pos_x = p_pos_x + (p_width - w_width) / 2
                w_pos_y = p_pos_y
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
        
    for b in balls:
        # x축 이동
        if b["pos_x"] < 0 or b["pos_x"] > screen_width - ball_size[b["img_idx"]][0]:
            b["trans_x"] *= -1
        b["pos_x"] += b["trans_x"] * dt

        # y축 이동
        if b["pos_y"] >= screen_height - land_height - ball_size[b["img_idx"]][1]:
            b["trans_y"] = b["init_spd_y"]
        else:
            b["trans_y"] += ball_accel
        b["pos_y"] += b["trans_y"] * dt
    # ============================================================
    

    # ============================================================
    # 충돌 처리
    # ------------------------------------------------------------
    p_rect = player.get_rect()
    p_rect.left, p_rect.top = p_pos_x, p_pos_y

    w_rect = weapon.get_rect()
    w_rect.left, w_rect.top = w_pos_x, w_pos_y 

    for b in balls:
        b_rect = ball_imgs[b["img_idx"]].get_rect()
        b_rect.left, b_rect.top = b["pos_x"], b["pos_y"]

        if b_rect.colliderect(w_rect) and w_shooting:
            w_shooting = False
            # 가장 작은 공은 소멸
            if b["img_idx"] == len(ball_imgs) - 1:
                balls.remove(b)
            # 그렇지 않을 경우 작은 공으로 분열함
            else:
                b["img_idx"] += 1
                b["trans_y"] = -.1
                balls.append(b.copy())
                b["trans_x"] *= -1

        if b_rect.colliderect(p_rect):
            is_running = False
            is_win = False
    # ============================================================

    if not balls:
        is_running = False
        is_win = True

    # ============================================================
    # 화면에 그리기
    # ------------------------------------------------------------
    screen.blit(bg, bg_pos)
    if w_shooting:
        screen.blit(weapon, (w_pos_x, w_pos_y))
    screen.blit(land, land_pos)
    screen.blit(player, (p_pos_x, p_pos_y))
    for b in balls:
        screen.blit(ball_imgs[b["img_idx"]], (b["pos_x"], b["pos_y"]))
    # ============================================================

    pygame.display.update() # 화면 그리기

pygame.quit()

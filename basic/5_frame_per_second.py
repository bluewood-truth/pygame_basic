import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("pygame_basic")

clock = pygame.time.Clock()


# 이미지 불러오기
img_path = "C:\\Users\\gkstm\\Desktop\\Python\\pygame_basic\\images\\"
background = pygame.image.load(img_path + "background.png")
character = pygame.image.load(img_path + "character.png")

# 캐릭터 스프라이트 설정
character_width, character_height = character.get_rect().size
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = to_y = 0

# 이동 속도
character_speed = .6

# 이벤트 루프
running = True
while running: # Unity의 Update()와 같은 역할
    dt = clock.tick(30) # FPS를 설정 (델타타임)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생시 (x버튼, Ctrl+F4 등)
            running = False # 이벤트 루프를 끝낸다

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                to_x = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                to_y = 0

    # 캐릭터 이동 및 화면 경계 처리
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 화면 그리기 (매 프레임마다 호출해야 됨)

pygame.quit()

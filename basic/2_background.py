import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("pygame_basic")

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\gkstm\\Desktop\\Python\\pygame_basic\\images\\background.png")

# 이벤트 루프
running = True
while running: # Unity의 Update()와 같은 역할
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생시 (x버튼, Ctrl+F4 등)
            running = False # 이벤트 루프를 끝낸다

    # screen.fill((0,0,255)) # 파란색으로 채우기
    screen.blit(background, (0,0)) # 배경 그리기

    pygame.display.update() # 화면 그리기 (매 프레임마다 호출해야 됨)

pygame.quit()

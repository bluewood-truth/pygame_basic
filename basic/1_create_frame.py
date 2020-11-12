import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("pygame_basic")


# 이벤트 루프
running = True
while running: # Unity의 Update()와 같은 역할
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생시 (x버튼, Ctrl+F4 등)
            running = False # 이벤트 루프를 끝낸다

pygame.quit()

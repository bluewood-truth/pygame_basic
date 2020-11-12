import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("pygame_basic")


# 이미지 불러오기
img_path = "C:\\Users\\gkstm\\Desktop\\Python\\pygame_basic\\images\\"
background = pygame.image.load(img_path + "background.png")
character = pygame.image.load(img_path + "character.png")

# 캐릭터 스프라이트 설정
character_width, character_height = character.get_rect().size
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

# 이벤트 루프
running = True
while running: # Unity의 Update()와 같은 역할
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생시 (x버튼, Ctrl+F4 등)
            running = False # 이벤트 루프를 끝낸다

    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 화면 그리기 (매 프레임마다 호출해야 됨)

pygame.quit()

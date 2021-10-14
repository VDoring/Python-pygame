import pygame

pygame.init()  # pygame 사용전 초기화 (필수)

window_size = [1280, 800]  # 1024x768 로 화면 크기 설정
window = pygame.display.set_mode(window_size)  # 화면 크기 적용
pygame.display.set_caption("pygame 화면 사진 출력 코드")  # 창 이름

image_file = pygame.image.load("image/ice.jpg") # 사진 불러오기

is_game_running = True  # 게임 진행 여부 -> True
while is_game_running:
    for event in pygame.event.get():  # 이벤트 발생 여부 확인
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 발생시
            is_game_running = False  # 게임 진행 여부 -> False

    window.blit(image_file, (0, 0)) # 사진 그리기

    pygame.display.update() # 화면 업데이트

pygame.quit()  # pygame 종료
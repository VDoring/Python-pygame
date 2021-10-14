import pygame

pygame.init()  # pygame 사용전 초기화 (필수)

window_size = [480, 480]  # 1024x768 로 화면 크기 설정
window = pygame.display.set_mode(window_size)  # 화면 크기 적용
pygame.display.set_caption("pygame 기본 코드")  # 창 이름

is_game_running = True  # 게임 진행 여부 -> True
while is_game_running:
    for event in pygame.event.get():  # 이벤트 발생 여부 확인
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 발생시
            is_game_running = False  # 게임 진행 여부 -> False

        if event.type == pygame.KEYDOWN: # 키를 눌렀을 경우
            if event.key == pygame.K_UP: # 위쪽 화살표 키를 눌렀을때
                print("UP")
            if event.key == pygame.K_DOWN: # 아래쪽 화살표 키를 눌렀을때
                print("DOWN")
            if event.key == pygame.K_RIGHT: # 오른쪽 화살표 키를 눌렀을때
                print("RIGHT")
            if event.key == pygame.K_LEFT: # 왼쪽 화살표 키를 눌렀을때
                print("LEFT")

pygame.quit()  # pygame 종료
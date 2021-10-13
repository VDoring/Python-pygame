import pygame

pygame.init()  # pygame 사용전 초기화 (필수)

window_size = [1024, 768]  # 1024x768 로 화면 크기 설정
window = pygame.display.set_mode(window_size)  # 화면 크기 적용
pygame.display.set_caption("pygame 음악 재생 코드")  # 창 이름

sound = pygame.mixer.Sound("music/OrangeMusic.mp3") # 음악 경로 설정 및 재생
sound.play(-1) # 음악 무한 재생

is_game_running = True  # 게임 진행 여부 -> True
while is_game_running:
    for event in pygame.event.get():  # 이벤트 발생 여부 확인
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 발생시
            is_game_running = False  # 게임 진행 여부 -> False

pygame.quit()  # pygame 종료
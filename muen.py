import pygame
import sys
import game1
import game2

# 初始化 Pygame
pygame.init()

# 設定視窗大小
WINDOW_SIZE = 400
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Game Selection Menu")

# 定義顏色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def draw_button(text, rect, color):
    pygame.draw.rect(window, color, rect)
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    window.blit(text_surface, text_rect)

def main_menu():
    running = True
    while running:
        window.fill(WHITE)

        # 繪製按鈕
        draw_button("Game 1: Five in a Row", pygame.Rect(50, 150, 300, 50), GREEN)
        draw_button("Game 2: Maze Game", pygame.Rect(50, 250, 300, 50), BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 50 <= x <= 350 and 150 <= y <= 200:  # 按下 Game 1 的按鈕
                    game1_window = pygame.display.set_mode((800, 800))
                    game1.play_game()
                elif 50 <= x <= 350 and 250 <= y <= 300:  # 按下 Game 2 的按鈕
                    game2_window = pygame.display.set_mode((800, 800))
                    game2.play_maze_game()

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()

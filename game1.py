import pygame
import sys

# 初始化 Pygame
pygame.init()

# 設定視窗大小
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2人5子棋遊戲")

# 定義顏色
WHITE = (255, 255, 255)  # 玩家1的顏色
BLACK = (0, 0, 0)        # 玩家2的顏色
LIGHTBLUE = (173, 216, 230)

# 設定棋盤大小
ROWS, COLS = 15, 15
CELL_SIZE = 50

board = [[0 for _ in range(COLS)] for _ in range(ROWS)]

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def draw_piece(row, col, color):
    pygame.draw.circle(screen, color, ((col + 0.5) * CELL_SIZE, (row + 0.5) * CELL_SIZE), CELL_SIZE // 2 - 5)

def check_winner(row, col):
    # 檢查五個連續的相同顏色的棋子以確定勝利
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        count = 1
        for i in range(1, 5):
            r, c = row + dr * i, col + dc * i
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == board[row][col]:
                count += 1
            else:
                break
        for i in range(1, 5):
            r, c = row - dr * i, col - dc * i
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == board[row][col]:
                count += 1
            else:
                break
        if count >= 5:
            return True
    return False

def show_winner_message(winner_color):
    # 彈出新視窗顯示勝利訊息
    pygame.display.set_caption("勝利訊息")
    screen.fill(LIGHTBLUE)
    font = pygame.font.SysFont(None, 50)
    text = font.render(f"{winner_color} Wins!", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

def play_game():
    current_color = BLACK  # 初始為玩家2
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # 返回到主菜單
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col, row = x // CELL_SIZE, y // CELL_SIZE
                if 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == 0:
                    board[row][col] = current_color
                    if check_winner(row, col):
                        winner = "Player 1" if current_color == WHITE else "Player 2"
                        show_winner_message(winner)
                        return  # 返回到主菜單
                    current_color = WHITE if current_color == BLACK else BLACK

        screen.fill(LIGHTBLUE)
        draw_board()
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] != 0:
                    draw_piece(row, col, board[row][col])

        pygame.display.flip()

    return  # 返回到主菜單

if __name__ == "__main__":
    play_game()

import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 設定視窗大小和地圖大小
WINDOW_SIZE = 800
MAP_SIZE = 31
CELL_SIZE = WINDOW_SIZE // MAP_SIZE

# 定義顏色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
COFFEE = (139, 69, 19)  # 咖啡色

# 創建迷宮地圖
def generate_maze():
    maze = [[0] * MAP_SIZE for _ in range(MAP_SIZE)]
    stack = [(1, 1)]
    visited = set()

    while stack:
        x, y = stack[-1]
        maze[x][y] = 1
        visited.add((x, y))

        neighbors = [(x + dx, y + dy) for dx, dy in [(2, 0), (0, 2), (-2, 0), (0, -2)]]
        unvisited_neighbors = [(nx, ny) for nx, ny in neighbors if 0 < nx < MAP_SIZE - 1 and 0 < ny < MAP_SIZE - 1 and (nx, ny) not in visited]

        if unvisited_neighbors:
            nx, ny = random.choice(unvisited_neighbors)
            maze[(x + nx) // 2][(y + ny) // 2] = 1
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze

# 初始化地圖和玩家位置
maze = generate_maze()
player_a_pos = [1, 1]
player_b_pos = [MAP_SIZE - 2, MAP_SIZE - 2]

# 初始化Pygame視窗
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Maze Game")

# 初始化計時器
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

def play_maze_game():
    global maze, player_a_pos, player_b_pos, start_ticks

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        remaining_seconds = max(60 - elapsed_seconds, 0)

        keys_a = pygame.key.get_pressed()
        if keys_a[pygame.K_w] and player_a_pos[1] > 0 and maze[player_a_pos[0]][player_a_pos[1] - 1] == 1:
            player_a_pos[1] -= 1
        elif keys_a[pygame.K_s] and player_a_pos[1] < MAP_SIZE - 1 and maze[player_a_pos[0]][player_a_pos[1] + 1] == 1:
            player_a_pos[1] += 1
        elif keys_a[pygame.K_a] and player_a_pos[0] > 0 and maze[player_a_pos[0] - 1][player_a_pos[1]] == 1:
            player_a_pos[0] -= 1
        elif keys_a[pygame.K_d] and player_a_pos[0] < MAP_SIZE - 1 and maze[player_a_pos[0] + 1][player_a_pos[1]] == 1:
            player_a_pos[0] += 1

        keys_b = pygame.key.get_pressed()
        if keys_b[pygame.K_UP] and player_b_pos[1] > 0 and maze[player_b_pos[0]][player_b_pos[1] - 1] == 1:
            player_b_pos[1] -= 1
        elif keys_b[pygame.K_DOWN] and player_b_pos[1] < MAP_SIZE - 1 and maze[player_b_pos[0]][player_b_pos[1] + 1] == 1:
            player_b_pos[1] += 1
        elif keys_b[pygame.K_LEFT] and player_b_pos[0] > 0 and maze[player_b_pos[0] - 1][player_b_pos[1]] == 1:
            player_b_pos[0] -= 1
        elif keys_b[pygame.K_RIGHT] and player_b_pos[0] < MAP_SIZE - 1 and maze[player_b_pos[0] + 1][player_b_pos[1]] == 1:
            player_b_pos[0] += 1

        window.fill(WHITE)

        for y in range(MAP_SIZE):
            for x in range(MAP_SIZE):
                color = GREEN if (x, y) == tuple(player_a_pos) else RED if (x, y) == tuple(player_b_pos) else BLACK if maze[x][y] == 0 else WHITE
                pygame.draw.rect(window, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(window, GREEN, (player_a_pos[0] * CELL_SIZE, player_a_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(window, RED, (player_b_pos[0] * CELL_SIZE, player_b_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        if player_a_pos == [MAP_SIZE - 2, MAP_SIZE - 2]:
            display_winner_message("Player A Wins!")
            return

        elif player_b_pos == [1, 1]:
            display_winner_message("Player B Wins!")
            return

        font = pygame.font.Font(None, 36)
        timer_text = font.render(f"Time: {remaining_seconds}", True, COFFEE)
        window.blit(timer_text, (WINDOW_SIZE - timer_text.get_width() - 10, 10))

        pygame.display.flip()
        clock.tick(30)

def display_winner_message(message):
    pygame.display.set_caption(message)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(WHITE)
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, (0, 0, 0))
        window.blit(text, (WINDOW_SIZE // 2 - text.get_width() // 2, WINDOW_SIZE // 2 - text.get_height() // 2))
        pygame.display.flip()

if __name__ == "__main__":
    play_maze_game()

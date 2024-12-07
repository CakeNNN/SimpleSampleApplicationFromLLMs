import pygame
import random
import math

# 初期化
pygame.init()

# 画面サイズ
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 色の定義
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# プレイヤーの設定
player_size = 50
player_pos = [screen_width // 2, screen_height // 2]
player_speed = 5

# 敵の設定
enemy_size = 50
enemy_pos = [random.randint(0, screen_width - enemy_size), random.randint(0, screen_height - enemy_size)]
enemy_speed = 2

# ゲームループ
game_over = False
clock = pygame.time.Clock()

def detect_collision(player_pos, enemy_pos):
    p_x, p_y = player_pos
    e_x, e_y = enemy_pos
    distance = math.sqrt((e_x - p_x) ** 2 + (e_y - p_y) ** 2)
    return distance < (player_size + enemy_size) / 2

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # 画面の端に到達した場合の処理
    player_pos[0] = max(0, min(player_pos[0], screen_width - player_size))
    player_pos[1] = max(0, min(player_pos[1], screen_height - player_size))

    # 敵の移動
    enemy_direction = [player_pos[0] - enemy_pos[0], player_pos[1] - enemy_pos[1]]
    distance = math.sqrt(enemy_direction[0] ** 2 + enemy_direction[1] ** 2)
    enemy_direction = [enemy_direction[0] / distance, enemy_direction[1] / distance]
    enemy_pos[0] += enemy_direction[0] * enemy_speed
    enemy_pos[1] += enemy_direction[1] * enemy_speed

    # 衝突判定
    if detect_collision(player_pos, enemy_pos):
        game_over = True

    # 画面の描画
    screen.fill(black)
    pygame.draw.rect(screen, white, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, red, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.display.flip()

    clock.tick(30)

pygame.quit()

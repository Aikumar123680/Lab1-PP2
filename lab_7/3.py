import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed = 20

running = True
while running:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - ball_speed - ball_radius >= 0:
                ball_y -= ball_speed
            elif event.key == pygame.K_DOWN and ball_y + ball_speed + ball_radius <= HEIGHT:
                ball_y += ball_speed
            elif event.key == pygame.K_LEFT and ball_x - ball_speed - ball_radius >= 0:
                ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT and ball_x + ball_speed + ball_radius <= WIDTH:
                ball_x += ball_speed

pygame.quit()
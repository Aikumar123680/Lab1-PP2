import pygame
import datetime

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background = pygame.image.load("clock.png")
minute_hand = pygame.image.load("first_hand.png")
second_hand = pygame.image.load("sec_hand.png")

center = (WIDTH // 2, HEIGHT // 2)

def draw_clock():
    now = datetime.datetime.now()

    minutes = now.minute
    seconds = now.second

    minutes_angle = - (minutes * 6)
    seconds_angle = - (seconds * 6)

    rotated_minute = pygame.transform.rotate(minute_hand, minutes_angle)
    rotated_second = pygame.transform.rotate(second_hand, seconds_angle)

    min_rect = rotated_minute.get_rect(center=center)
    sec_rect = rotated_second.get_rect(center=center)

    screen.blit(background, (0, 0))
    screen.blit(rotated_minute, min_rect.topleft)
    screen.blit(rotated_second, sec_rect.topleft)

    pygame.display.flip()

running = True
while running:
    screen.fill((255, 255, 255))
    draw_clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(1)

pygame.quit()
import pygame
import random

# Инициализация Pygame
pygame.init()

# Цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Размер экрана
size = (600, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snake Game")

# Параметры змейки
snake_block = 10
snake_speed = 15

# Шрифты
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# Функция отображения счета
def show_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])


# Класс для игрока (змейки)
class Snake:
    def __init__(self):
        self.snake_list = [[100, 50], [90, 50], [80, 50]]  # Начальная длина змейки
        self.snake_direction = "RIGHT"
        self.x_change = snake_block
        self.y_change = 0

    def draw_snake(self):
        for block in self.snake_list:
            pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

    def move(self):
        # Перемещение змейки
        head = self.snake_list[-1]
        new_head = [head[0] + self.x_change, head[1] + self.y_change]
        self.snake_list.append(new_head)
        self.snake_list.pop(0)

    def change_direction(self, direction):
        if direction == "UP":
            self.x_change = 0
            self.y_change = -snake_block
        elif direction == "DOWN":
            self.x_change = 0
            self.y_change = snake_block
        elif direction == "LEFT":
            self.x_change = -snake_block
            self.y_change = 0
        elif direction == "RIGHT":
            self.x_change = snake_block
            self.y_change = 0

    def grow(self):
        # Добавляем новый сегмент к змейке
        tail = self.snake_list[0]
        if self.snake_direction == "UP":
            self.snake_list.insert(0, [tail[0], tail[1] - snake_block])
        elif self.snake_direction == "DOWN":
            self.snake_list.insert(0, [tail[0], tail[1] + snake_block])
        elif self.snake_direction == "LEFT":
            self.snake_list.insert(0, [tail[0] - snake_block, tail[1]])
        elif self.snake_direction == "RIGHT":
            self.snake_list.insert(0, [tail[0] + snake_block, tail[1]])


# Класс для еды
class Food:
    def __init__(self):
        self.x = round(random.randrange(0, size[0] - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, size[1] - snake_block) / 10.0) * 10.0

    def draw(self):
        pygame.draw.rect(screen, red, [self.x, self.y, snake_block, snake_block])


# Главная игровая логика
def game_loop():
    game_over = False
    snake = Snake()
    food = Food()
    score = 0
    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.snake_direction != "RIGHT":
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT and snake.snake_direction != "LEFT":
                    snake.change_direction("RIGHT")
                elif event.key == pygame.K_UP and snake.snake_direction != "DOWN":
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN and snake.snake_direction != "UP":
                    snake.change_direction("DOWN")

        # Проверка на столкновение с границами
        if snake.snake_list[-1][0] >= size[0] or snake.snake_list[-1][0] < 0 or snake.snake_list[-1][1] >= size[1] or snake.snake_list[-1][1] < 0:
            game_over = True

        # Проверка на столкновение с собой
        if snake.snake_list[-1] in snake.snake_list[:-1]:
            game_over = True

        # Проверка на поедание еды
        if snake.snake_list[-1][0] == food.x and snake.snake_list[-1][1] == food.y:
            food = Food()  # Генерируем новую еду
            score += 10  # Увеличиваем счет
            snake.grow()  # Увеличиваем змейку

        # Обновляем состояние змейки
        snake.move()

        # Заполняем экран фоном
        screen.fill(blue)

        # Рисуем еду и змейку
        food.draw()
        snake.draw_snake()

        # Отображаем счет
        show_score(score)

        # Обновляем экран
        pygame.display.update()

        # Контролируем скорость игры
        clock.tick(snake_speed)

    pygame.quit()


# Запуск игры
game_loop()
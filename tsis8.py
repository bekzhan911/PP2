import pygame

pygame.init()  # Инициализация библиотеки pygame

W, H = 600, 400  # Ширина и высота окна
WHITE = (255, 255, 255)  # Цвет фона
BLUE = (0, 0, 255)  # Цвет синего прямоугольника
RED = (255, 0, 0)  # Цвет красного прямоугольника
BLACK = (0, 0, 0)

# Создание окна игры
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Мой первый проект на pygame!")  # Название окна

clock = pygame.time.Clock()  # Таймер для контроля FPS
FPS = 60  # Количество кадров в секунду

# Свойства прямоугольников
width = 50  # Ширина
height = 20  # Высота
speed = 5  # Скорость перемещения
jump_height = 10  # Высота прыжка
gravity = 0.5  # Гравитация

# Свойства синего прямоугольника
x_blue = W // 2  # Начальная позиция X
y_blue = H - height  # Начальная позиция Y (внизу окна)
flLeft_blue = flRight_blue = flUp_blue = False
on_ground_blue = True
jump_speed_blue = jump_height

# Свойства красного прямоугольника
x_red = W // 2 - width  # Начальная позиция X (чуть левее синего)
y_red = H - height  # Начальная позиция Y (внизу окна)
flLeft_red = flRight_red = flUp_red = False
on_ground_red = True
jump_speed_red = jump_height

# Свойства стен
wall_width = 18
wall_height = 35
wall1_x = 100  # Позиция первой стены по X
wall2_x = 500  # Позиция второй стены по X
wall_y = H - wall_height  # Позиция стен по Y (внизу окна)

# Функция для проверки столкновения прямоугольника с препятствием
def check_collision(x, y, width, height, wall_x, wall_y, wall_width, wall_height):
    if (x < wall_x + wall_width and x + width > wall_x and
        y < wall_y + wall_height and y + height > wall_y):
        return True
    return False

# Функция для проверки столкновения между двумя прямоугольниками
def check_collision(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x1 < x2 + w2 and x1 + w1 > x2 and
        y1 < y2 + h2 and y1 + h1 > y2):
        return True
    return False

while True:  # Главный игровой цикл
    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT:  # Закрытие окна
            quit()
        elif event.type == pygame.KEYDOWN:  # Нажатие клавиш
            # Управление синим прямоугольником
            if event.key == pygame.K_LEFT:
                flLeft_blue = True
            elif event.key == pygame.K_RIGHT:
                flRight_blue = True
            if event.key == pygame.K_UP and on_ground_blue:
                flUp_blue = True
                on_ground_blue = False
            # Управление красным прямоугольником
            if event.key == pygame.K_a:
                flLeft_red = True
            elif event.key == pygame.K_d:
                flRight_red = True
            if event.key == pygame.K_w and on_ground_red:
                flUp_red = True
                on_ground_red = False
        elif event.type == pygame.KEYUP:  # Отпускание клавиш
            # Управление синим прямоугольником
            if event.key == pygame.K_LEFT:
                flLeft_blue = False
            elif event.key == pygame.K_RIGHT:
                flRight_blue = False
            # Управление красным прямоугольником
            if event.key == pygame.K_a:
                flLeft_red = False
            elif event.key == pygame.K_d:
                flRight_red = False
   

    # Движение и прыжки прямоугольников
    if flLeft_blue and x_blue > 0:
        x_blue -= speed
        speed += 0.2  # Ускорение
    else:
        speed = 5  # Сброс скорости до начального значения
    if flRight_blue and x_blue < W - width:
        x_blue += speed
        speed += 0.2  # Ускорение
    else:
        speed = 5  # Сброс скорости до начального значения
    if flUp_blue:
        y_blue -= jump_speed_blue
        jump_speed_blue -= gravity
        if jump_speed_blue < -jump_height:  # Если достигнута вершина прыжка
            flUp_blue = False
            jump_speed_blue = jump_height
    else:
        if y_blue < H - height:
            y_blue += gravity * 2
        else:
            y_blue = H - height
            on_ground_blue = True

    if flLeft_red and x_red > 0:
        x_red -= speed
        speed += 0.1  # Ускорение
    else:
        speed = 5  # Сброс скорости до начального значения
    if flRight_red and x_red < W - width:
        x_red += speed
        speed += 0.1  # Ускорение
    else:
        speed = 5  # Сброс скорости до начального значения
    if flUp_red:
        y_red -= jump_speed_red
        jump_speed_red -= gravity
        if jump_speed_red < -jump_height:  # Если достигнута вершина прыжка
            flUp_red = False
            jump_speed_red = jump_height
    else:
        if y_red < H - height:
            y_red += gravity * 2
        else:
            y_red = H - height
            on_ground_red = True
 # Проверка столкновения синего прямоугольника со стенами
    if check_collision(x_blue, y_blue, width, height, wall1_x, wall_y, wall_width, wall_height):
        if flLeft_blue:
            x_blue = wall1_x + wall_width
        elif flRight_blue:
            x_blue = wall1_x - width
    if check_collision(x_blue, y_blue, width, height, wall2_x, wall_y, wall_width, wall_height):
        if flLeft_blue:
            x_blue = wall2_x + wall_width
        elif flRight_blue:
            x_blue = wall2_x - width
    # Проверка столкновения красного прямоугольника со стенами
    if check_collision(x_red, y_red, width, height, wall1_x, wall_y, wall_width, wall_height):
        if flLeft_red:
            x_red = wall1_x + wall_width
        elif flRight_red:
            x_red = wall1_x - width
    if check_collision(x_red, y_red, width, height, wall2_x, wall_y, wall_width, wall_height):
        if flLeft_red:
            x_red = wall2_x + wall_width
        elif flRight_red:
            x_red = wall2_x - width
     # Проверка столкновения между синим и красным прямоугольником
    if check_collision(x_blue, y_blue, width, height, x_red, y_red, width, height):
        # Здесь вы можете добавить код, который будет выполняться при столкновении
        # Например, остановить движение обоих прямоугольников
        flLeft_blue = flRight_blue = flUp_blue = False
        flLeft_red = flRight_red = flUp_red = False
    
    sc.fill(WHITE)  # Заливка фона
    pygame.draw.rect(sc, BLUE, (x_blue, y_blue, width, height))  # Рисование синего прямоугольника
    pygame.draw.rect(sc, RED, (x_red, y_red, width, height))  # Рисование красного прямоугольника
    # Отрисовка стен
    pygame.draw.rect(sc, BLACK, (wall1_x, wall_y, wall_width, wall_height))
    pygame.draw.rect(sc, BLACK, (wall2_x, wall_y, wall_width, wall_height))
    pygame.display.update()  # Обновление содержимого всего экрана
    clock.tick(FPS)  # Поддержание заданного FPS

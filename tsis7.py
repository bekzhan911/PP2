import pygame
pygame.init()  # Инициализация библиотеки pygame

W, H = 600, 400  # Ширина и высота окна
WHITE = (255, 255, 255)  # Цвет фона
BLUE = (0, 0, 255)  # Цвет прямоугольника

# Создание окна игры
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Мой первый проект на pygame!")  # Название окна

clock = pygame.time.Clock()  # Таймер для контроля FPS
FPS = 60  # Количество кадров в секунду

# Свойства прямоугольника
x = W // 2  # Начальная позиция X
y = H - 20  # Начальная позиция Y (внизу окна)
width = 50  # Ширина
height = 20  # Высота
speed = 5  # Скорость перемещения
jump_height = 10  # Высота прыжка
gravity = 0.5  # Гравитация

# Флаги для управления движением
flLeft = flRight = flUp = False  # Начальное состояние: стоим на месте
on_ground = True  # Флаг, находится ли прямоугольник на земле

while True:  # Главный игровой цикл
    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT:  # Закрытие окна
            quit()
        elif event.type == pygame.KEYDOWN:  # Нажатие клавиш
            if event.key == pygame.K_LEFT:  # Если нажата стрелка влево
                flLeft = True
            elif event.key == pygame.K_RIGHT:  # Если нажата стрелка вправо
                flRight = True
            if event.key == pygame.K_UP and on_ground:  # Если нажата стрелка вверх и мы на земле
                flUp = True
                on_ground = False
        elif event.type == pygame.KEYUP:  # Отпускание клавиш
            if event.key == pygame.K_LEFT:  # Если отпущена стрелка влево
                flLeft = False
            elif event.key == pygame.K_RIGHT:  # Если отпущена стрелка вправо
                flRight = False

    # Движение прямоугольника
    if flLeft and x > 0:  # Движение влево
        x -= speed
    if flRight and x < W - width:  # Движение вправо
        x += speed

    # Прыжок и падение
    if flUp:  # Если начат прыжок
        y -= jump_height
        jump_height -= gravity
        if jump_height < 0:  # Если достигнута вершина прыжка
            flUp = False
    else:  # Если персонаж не в прыжке
        if y < H - height:  # Если не на земле, падаем
            y += gravity * 2
        else:  # Если достигнута земля
            y = H - height  # Останавливаемся у нижнего края
            on_ground = True
            jump_height = 10  # Сброс высоты прыжка

    # Сброс флага прыжка
    if on_ground:
        flUp = False
        jump_height = 10

    sc.fill(WHITE)  # Заливка фона
    pygame.draw.rect(sc, BLUE, (x, y, width, height))  # Рисование прямоугольника
    pygame.display.update()  # Обновление содержимого всего экрана
    clock.tick(FPS)  # Поддержание заданного FPS

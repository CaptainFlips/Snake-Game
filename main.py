import pygame
import random
pygame.init()

# Classes

class Window():
    def __init__(self, height, width, caption):
        self.height = height
        self.width = width
        self.caption = caption

        self.call = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)


class Snake():
    global c_mode
    global fruit_eten

    moves = []
    parts = []

    x_his = []
    y_his = []

    def __init__(self, x, y, width, height, black_images, white_images, coloured_images, python_images, is_first = False):
        self.pos = fruit_eten
        self.is_first = is_first

        if not self.is_first:
            self.x = Snake.parts[self.pos -1].prev_x
            self.y = Snake.parts[self.pos -1].prev_y

        else:
            self.x = x
            self.y = y

        self.prev_x = self.x
        self.prev_y = self.y

        self.width = width
        self.height = height

        self.black_images = black_images
        self.white_images = white_images
        self.colour_images = coloured_images
        self.python_images = python_images

        self.vel = 24

        if not self.is_first:
            self.dir = Snake.parts[self.pos -1].last_dir
        else:
            self.dir = 'right'

        self.last_dir = self.dir
        self.prev_dir = self.dir

        self.selected_image = white_images[0]
        self.current_image = self.selected_image
        self.image_pos = 0

    def check_mode(self):

        if len(Snake.parts) > 1:
            if self.pos == 0:
                self.image_pos = 1
            elif self.pos == len(Snake.parts) -1:
                self.image_pos = 3
            elif self.dir != Snake.parts[self.pos -1].dir:
                self.image_pos = 4
            else:
                self.image_pos = 2
            
        if c_mode == 'Black':
            self.selected_image = self.white_images[self.image_pos]
        elif c_mode == 'White':
            self.selected_image = self.black_images[self.image_pos]
        elif c_mode == 'Colour':
            self.selected_image = self.colour_images[self.image_pos]
        elif c_mode == 'Python':
            self.selected_image = self.python_images[self.image_pos]            

    def call(self, window):

        if self.dir == 'right':
            window.call.blit(self.current_image, (self.x, self.y))
        elif self.dir == 'left':
            window.call.blit(self.current_image, (self.x, self.y))
        elif self.dir == 'down':
            window.call.blit(self.current_image, (self.x, self.y))
        elif self.dir == 'up':
            window.call.blit(self.current_image, (self.x, self.y))

    def update(self):

        if not self.is_first:
            self.dir = Snake.parts[self.pos -1].prev_dir

        self.check_mode()

        if self.image_pos == 4:

            if self.dir == 'right' and Snake.parts[self.pos -1].dir == 'up':
                self.current_image = self.selected_image
            elif self.dir == 'down' and Snake.parts[self.pos -1].dir == 'left':
                self.current_image = self.selected_image

            elif self.dir == 'left' and Snake.parts[self.pos -1].dir == 'up':
                self.current_image = pygame.transform.rotate(self.selected_image, -90)
            elif self.dir == 'down' and Snake.parts[self.pos -1].dir == 'right':
                self.current_image = pygame.transform.rotate(self.selected_image, -90)

            elif self.dir == 'right' and Snake.parts[self.pos -1].dir == 'down':
                self.current_image = pygame.transform.rotate(self.selected_image, 90)
            elif self.dir == 'up' and Snake.parts[self.pos -1].dir == 'left':
                self.current_image = pygame.transform.rotate(self.selected_image, 90)

            elif self.dir == 'left' and Snake.parts[self.pos -1].dir == 'down':
                self.current_image = pygame.transform.rotate(self.selected_image, 180)
            elif self.dir == 'up' and Snake.parts[self.pos -1].dir == 'right':
                self.current_image = pygame.transform.rotate(self.selected_image, 180)

        else:
                
            if self.image_pos == 3 and self.dir != Snake.parts[self.pos -1].dir:
                if Snake.parts[self.pos -1].dir == 'up':
                    self.current_image = pygame.transform.rotate(self.selected_image, 90)
                elif Snake.parts[self.pos -1].dir == 'down':
                    self.current_image = pygame.transform.rotate(self.selected_image, -90)
                elif Snake.parts[self.pos -1].dir == 'right':
                    self.current_image = self.selected_image
                elif Snake.parts[self.pos -1].dir == 'left':
                    self.current_image = pygame.transform.rotate(self.selected_image, 180)
            else:
                        
                if self.dir == 'right':
                    self.current_image = self.selected_image

                elif self.dir == 'down':
                    self.current_image = pygame.transform.rotate(self.selected_image, -90)

                elif self.dir == 'left':
                    self.current_image = pygame.transform.rotate(self.selected_image, 180)

                elif self.dir  == 'up':
                    self.current_image = pygame.transform.rotate(self.selected_image, 90)

                if self.selected_image == self.colour_images[2]:
                    if random.randint(1,2) == 2:
                        self.current_image = pygame.transform.rotate(self.current_image, 180)

    def move(self):

        self.prev_x = self.x
        self.prev_y = self.y
        self.prev_dir = self.dir

        if len(keyQueue) != 0:
            if self.is_first:
                self.dir = keyQueue[0]
                keyQueue.pop(0)

        if not self.is_first:
            self.x = Snake.parts[self.pos -1].prev_x
            self.y = Snake.parts[self.pos -1].prev_y

        if self.is_first:
            if self.dir == 'right':
                self.x += self.vel

            elif self.dir == 'down':
                self.y += self.vel

            elif self.dir == 'left':
                self.x -= self.vel

            elif self.dir  == 'up':
                self.y -= self.vel

        if self.image_pos != 3:
            Snake.x_his.append(self.prev_x)
            Snake.y_his.append(self.prev_y)

        self.update()


class Fruit:
    global c_mode
    global prev_mode

    def __init__(self, white_images, black_images, colour_images):
        self.white_images = white_images
        self.black_images = black_images
        self.colour_images = colour_images

        self.selected_image = self.white_images[random.randint(0, len(self.white_images) -1)]

    def call(self, window):
        window.call.blit(self.selected_image, (self.x, self.y))
 
    def check_mode(self):
        global prev_mode

        if c_mode == 'White':
            if prev_mode == 'Black':
                self.selected_image = self.black_images[self.white_images.index(self.selected_image)]
            elif prev_mode == 'Colour' or prev_mode == 'Python':
                self.selected_image = self.black_images[self.colour_images.index(self.selected_image)]

        elif c_mode == 'Black':
            if prev_mode == 'White':
                self.selected_image = self.white_images[self.black_images.index(self.selected_image)]
            elif prev_mode == 'Colour' or prev_mode == 'Python':
                self.selected_image = self.white_images[self.colour_images.index(self.selected_image)]

        elif c_mode == 'Colour':
            if prev_mode == 'White':
                self.selected_image = self.colour_images[self.black_images.index(self.selected_image)]
            elif prev_mode == 'Black':
                self.selected_image = self.colour_images[self.white_images.index(self.selected_image)]

        prev_mode = c_mode

    def place(self, window, call = True):

        if c_mode == 'White':
            self.selected_image = self.black_images[random.randint(0, len(self.white_images) -1)]
        elif c_mode == 'Black':
            self.selected_image = self.white_images[random.randint(0, len(self.white_images) -1)]
        elif c_mode == 'Colour':
            self.selected_image = self.colour_images[random.randint(0, len(self.white_images) -1)]

        self.x = int(random.randrange(0, gameWindow.width, 24))
        self.y = int(random.randrange(0, gameWindow.height, 24))

        if call:
            self.call(window)

# Window

gameWindow = Window(600, 816, 'Snake')

# Files

black_snake_images = [
    pygame.image.load('Images/Snakes/Black - Single.png'),
    pygame.image.load('Images/Snakes/Black - Head.png'), 
    pygame.image.load('Images/Snakes/Black - Body.png'),
    pygame.image.load('Images/Snakes/Black - Tail.png'),
    pygame.image.load('Images/Snakes/Black - Bent.png')
]

white_snake_images = [
    pygame.image.load('Images/Snakes/White - Single.png'),
    pygame.image.load('Images/Snakes/White - Head.png'), 
    pygame.image.load('Images/Snakes/White - Body.png'),
    pygame.image.load('Images/Snakes/White - Tail.png'),
    pygame.image.load('Images/Snakes/White - Bent.png')
]

coloured_snake_images = [
    pygame.image.load('Images/Snakes/Coloured - Single.png'),
    pygame.image.load('Images/Snakes/Coloured - Head.png'), 
    pygame.image.load('Images/Snakes/Coloured - Body.png'),
    pygame.image.load('Images/Snakes/Coloured - Tail.png'),
    pygame.image.load('Images/Snakes/Coloured - Bent.png')
]

python_snake_images = [
    pygame.image.load('Images/Snakes/Python - Single.png'),
    pygame.image.load('Images/Snakes/Python - Head.png'), 
    pygame.image.load('Images/Snakes/Python - Body.png'),
    pygame.image.load('Images/Snakes/Python - Tail.png'),
    pygame.image.load('Images/Snakes/Python - Bent.png')
]

white_fruit_images = [
    pygame.image.load('Images/Fruit/White - Apple.png'),
    pygame.image.load('Images/Fruit/White - Cherry.png'), 
    pygame.image.load('Images/Fruit/White - Pear.png'),
    pygame.image.load('Images/Fruit/White - Banana.png')
]

black_fruit_images = [
    pygame.image.load('Images/Fruit/Black - Apple.png'),
    pygame.image.load('Images/Fruit/Black - Cherry.png'), 
    pygame.image.load('Images/Fruit/Black - Pear.png'),
    pygame.image.load('Images/Fruit/Black - Banana.png')
]

coloured_fruit_images = [
    pygame.image.load('Images/Fruit/Coloured - Apple.png'),
    pygame.image.load('Images/Fruit/Coloured - Cherry.png'), 
    pygame.image.load('Images/Fruit/Coloured - Pear.png'),
    pygame.image.load('Images/Fruit/Coloured - Banana.png')
]

# Variables

clock = pygame.time.Clock()

running = True

ready = False

keyQueue = []

c_mode = 'Black'
prev_mode = c_mode

fruit_is_eaten = False

c_press = 0

points_toggle = False

fruit_pos_check = False

chew_sound = pygame.mixer.Sound('Sound/chew.wav')
go_sound = pygame.mixer.Sound('Sound/game_over.wav')

mute = False

dev_mode = False

diff_mode = 'Normal'

speed = 10

fruit_eten = 0

# Text Variables

text_font = pygame.font.Font('freesansbold.ttf', 18)

pre_font = pygame.font.Font('freesansbold.ttf', 16)
pre_text = pre_font.render('press SPACE to begin', True, (128, 128, 128), (0, 0, 0))
pre_text_rect = pre_text.get_rect()
pre_text_rect.center = (gameWindow.width // 2, gameWindow.height - 64)

    # controls

ctrls_text = text_font.render(' C - Colour  Theme              ', True, (180, 180, 180), (50, 50, 50))
ctrls_text_rect = ctrls_text.get_rect()
ctrls_text_rect.center = (gameWindow.width -50, 9)

ctrls2_text = text_font.render(' P - Show  Points              ', True, (180, 180, 180), (50, 50, 50))
ctrls2_text_rect = ctrls_text.get_rect()
ctrls2_text_rect.center = (gameWindow.width -50, 28)

ctrls3_text = text_font.render(' M - Toggle Mute              ', True, (180, 180, 180), (50, 50, 50))
ctrls3_text_rect = ctrls_text.get_rect()
ctrls3_text_rect.center = (gameWindow.width -50, 47)

    # dev mode

dev_font = pygame.font.Font('freesansbold.ttf', 25)
dev_text = dev_font.render('Developer Mode', True, (128, 128, 128), (255, 255, 255))
dev_text_rect = dev_text.get_rect()
dev_text_rect.center = (gameWindow.width // 2, gameWindow.height // 2)

    # difficulty

dif_rect = pygame.Rect(0, 0, 150, 80)

dif0_text = text_font.render('    Game Difficulty ', True, (200, 200, 200), (50, 50, 50))
dif0_text_rect = dif0_text.get_rect()
dif0_text_rect.center = (65, 9)

dif1_text = text_font.render(' 1 - Easy ', True, (200, 200, 200), (50, 50, 50))
dif1_text_rect = dif1_text.get_rect()
dif1_text_rect.center = (45, 28)

dif2_text = text_font.render(' 2 - Normal ', True, (200, 200, 200), (50, 50, 50))
dif2_text_rect = dif2_text.get_rect()
dif2_text_rect.center = (56, 47)

dif3_text = text_font.render(' 3 - Hard ', True, (200, 200, 200), (50, 50, 50))
dif3_text_rect = dif3_text.get_rect()
dif3_text_rect.center = (45, 66)

    # selected

dif0s_font = pygame.font.Font('freesansbold.ttf', 18)
dif0s_text = dif0s_font.render('    Game Difficulty ', True, (200, 200, 200), (150, 150, 50))
dif0s_text_rect = dif0s_text.get_rect()
dif0s_text_rect.center = (65, 9)

dif1s_font = pygame.font.Font('freesansbold.ttf', 18)
dif1s_text = dif1s_font.render(' 1 - Easy ', True, (200, 200, 200), (100, 100, 50))
dif1s_text_rect = dif1s_text.get_rect()
dif1s_text_rect.center = (45, 28)

dif2s_font = pygame.font.Font('freesansbold.ttf', 18)
dif2s_text = dif2s_font.render(' 2 - Normal ', True, (200, 200, 200), (100, 100, 50))
dif2s_text_rect = dif2s_text.get_rect()
dif2s_text_rect.center = (56, 47)

dif3s_font = pygame.font.Font('freesansbold.ttf', 18)
dif3s_text = dif3s_font.render(' 3 - Hard ', True, (200, 200, 200), (100, 100, 50))
dif3s_text_rect = dif3s_text.get_rect()
dif3s_text_rect.center = (45, 66)

# Points

points = 0

def points_update():
    global text
    global text_rect

    font = pygame.font.Font('freesansbold.ttf', 16)
    if c_mode == 'Black':
        text = font.render(' Points: ' + str(points) + ' ', True, (128, 128, 128), (255, 255, 255))
    elif c_mode == 'White':
        text = font.render(' Points: ' + str(points) + ' ', True, (128, 128, 128), (0, 0, 0))
    elif c_mode == 'Colour' or c_mode == 'Python':
        text = font.render(' Points: ' + str(points) + ' ', True, (128, 128, 128), (255, 255, 255))

    text_rect = text.get_rect()
    text_rect.center = (35, 8)

def add_points():
    global diff_mode

    if diff_mode == 'Easy':
        return 1
    elif diff_mode == 'Normal':
        return 2
    elif diff_mode == 'Hard':
        return 3

# Objects

snake_0 = Snake(192, 192, 24, 24, black_snake_images, white_snake_images, coloured_snake_images, python_snake_images, True)

Snake.parts.append(globals()['snake_' + str(points)])      

fruit = Fruit(white_fruit_images, black_fruit_images, coloured_fruit_images)
fruit.place(gameWindow, False)

# Draw

def redrawWindow():
    if c_mode == 'Black':
        gameWindow.call.fill((0,0,0))
    elif c_mode == 'White':
        gameWindow.call.fill((255,255,255))
    elif c_mode == 'Colour':
        gameWindow.call.fill((150,64,64))
    elif c_mode == 'Python':
        gameWindow.call.fill((128,150,32))

    if points_toggle == True:
        gameWindow.call.blit(text, text_rect)

    fruit.call(gameWindow)

    for snake in Snake.parts:
        snake.call(gameWindow)

    Snake.x_his.clear()
    Snake.y_his.clear()

    pygame.display.update()


# - Pre Loop -

while not ready:

    gameWindow.call.fill((0,0,0))

    snake_0.call(gameWindow)

    gameWindow.call.blit(pre_text, pre_text_rect)

    gameWindow.call.blit(ctrls_text, ctrls_text_rect)
    gameWindow.call.blit(ctrls2_text, ctrls2_text_rect)
    gameWindow.call.blit(ctrls3_text, ctrls3_text_rect)

    pygame.draw.rect(gameWindow.call, (50,50,50), dif_rect)
    gameWindow.call.blit(dif0_text, dif0_text_rect)

    if diff_mode == 'Easy':
        gameWindow.call.blit(dif1s_text, dif1s_text_rect)
        gameWindow.call.blit(dif2_text, dif2_text_rect)
        gameWindow.call.blit(dif3_text, dif3_text_rect)
    elif diff_mode == 'Normal':
        gameWindow.call.blit(dif1_text, dif1_text_rect)
        gameWindow.call.blit(dif2s_text, dif2s_text_rect)
        gameWindow.call.blit(dif3_text, dif3_text_rect)
    else:
        gameWindow.call.blit(dif1_text, dif1_text_rect)
        gameWindow.call.blit(dif2_text, dif2_text_rect)
        gameWindow.call.blit(dif3s_text, dif3s_text_rect)

    if dev_mode:
        gameWindow.call.blit(dev_text, dev_text_rect)


    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            ready = True

        # Key Detection

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ready = True

            if event.key == pygame.K_RCTRL:
                dev_mode = not dev_mode

            if event.key == pygame.K_1:
                diff_mode = 'Easy'
                speed = 4
            if event.key == pygame.K_2:
                diff_mode = 'Normal'
                speed = 10
            if event.key == pygame.K_3:
                diff_mode = 'Hard'
                speed = 16

# ----- Main Loop -----

if dev_mode:
    for i in range(10):
            fruit_eten += 1
            points += add_points()
            fruit.place(gameWindow)

            globals()['snake_' + str(fruit_eten)] = Snake(Snake.parts[-1].x, Snake.parts[-1].y, 24, 24, black_snake_images, white_snake_images, coloured_snake_images, python_snake_images)
            Snake.parts.append(globals()['snake_' + str(fruit_eten)])

            for snake in Snake.parts:
                snake.check_mode()
            Snake.parts[-2].update()
            globals()['snake_' + str(fruit_eten)].update()

while running:
    clock.tick(speed)

    # Main Events 

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Key Detection

        if event.type == pygame.KEYDOWN:
            if snake_0.dir != 'right' and snake_0.dir != 'left' and snake_0.last_dir != 'right' and snake_0.last_dir != 'left':
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    keyQueue.append('left')
                    snake_0.last_dir = 'left'
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    keyQueue.append('right')
                    snake_0.last_dir = 'right'

            if snake_0.dir != 'down' and snake_0.dir != 'up' and snake_0.last_dir != 'down' and snake_0.last_dir != 'up':
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    keyQueue.append('up')
                    snake_0.last_dir = 'up'
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    keyQueue.append('down')
                    snake_0.last_dir = 'down'

            if event.key == pygame.K_c: # Change colour theme
                if c_mode == 'Black':
                    c_mode = 'White'
                elif c_mode == 'White':
                    c_mode = 'Colour'
                elif c_mode == 'Colour':
                    c_mode = 'Python'
                elif c_mode == 'Python':
                    c_mode = 'Black'

            if event.key == pygame.K_p:
                points_toggle = not points_toggle

            if event.key == pygame.K_m:
                mute = not mute

            for snake in Snake.parts:
                snake.check_mode()

            fruit.check_mode()

    # Direction Check/Set

    for snake in Snake.parts:
        snake.move()

    # Border Detection

    for snake in Snake.parts:
        if snake.x == -(snake.width):
            snake.x = gameWindow.width - snake.width
        elif snake.x >= gameWindow.width:
            snake.x = 0
        elif snake.y == -(snake.height):
            snake.y = gameWindow.height - snake.height
        elif snake.y >= gameWindow.height:
            snake.y = 0

    # Snake Collision

    for i in range(len(Snake.x_his)):

        if snake_0.x == Snake.x_his[i] and snake_0.y == Snake.y_his[i]:

            go_font = pygame.font.Font('freesansbold.ttf', 50)
            end_points_font = pygame.font.Font('freesansbold.ttf', 16)
            if c_mode == 'Black':
                go_text = go_font.render('Game Over', True, (128, 128, 128), (255, 255, 255))
                end_points_text = end_points_font.render('Points: ' + str(points), True, (128, 128, 128), (255, 255, 255))
            elif c_mode == 'White':
                go_text = go_font.render('Game Over', True, (128, 128, 128), (0, 0, 0))
                end_points_text = end_points_font.render('Points: ' + str(points), True, (128, 128, 128), (0, 0, 0))
            elif c_mode == 'Colour' or c_mode == 'Python':
                go_text = go_font.render('Game Over', True, (128, 128, 128), (255, 255, 255))
                end_points_text = end_points_font.render('Points: ' + str(points), True, (128, 128, 128), (255, 255, 255))

            go_text_rect = go_text.get_rect()
            go_text_rect.center = (gameWindow.width // 2, gameWindow.height // 2)

            end_points_text_rect = end_points_text.get_rect()
            end_points_text_rect.center = (gameWindow.width // 2, gameWindow.height // 2 + 33)

            gameWindow.call.blit(go_text, go_text_rect)
            gameWindow.call.blit(end_points_text, end_points_text_rect)
            pygame.display.update()

            if not mute:
                go_sound.play()

            pygame.time.delay(3000)

            running = False

    # Fruit Collision

    if snake_0.x == fruit.x and snake_0.y == fruit.y:
        fruit_eten += 1
        points += add_points()
        fruit.place(gameWindow)

        if not mute:
            chew_sound.play()
        
        fruit_pos_check = False

        globals()['snake_' + str(fruit_eten)] = Snake(Snake.parts[-1].x, Snake.parts[-1].y, 24, 24, black_snake_images, white_snake_images, coloured_snake_images, python_snake_images)
        Snake.parts.append(globals()['snake_' + str(fruit_eten)])

        for snake in Snake.parts:
            snake.check_mode()
        Snake.parts[-2].update()
        globals()['snake_' + str(fruit_eten)].update()

    # Fruit Placement Control

    while not fruit_pos_check:
        fruit_pos_check = True
        for i in range(len(Snake.x_his)):
            if fruit.x == Snake.x_his[i] and fruit.y == Snake.y_his[i]:
                fruit.place(gameWindow)
                fruit_pos_check = False
                

    points_update()
    

    redrawWindow()

pygame.quit()
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
    global points

    moves = []
    parts = []

    x_his = []
    y_his = []

    def __init__(self, x, y, width, height, black_images, white_images, coloured_images, python_images, is_first = False):
        self.pos = points
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

        self.len = 1
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
        self.check_mode()

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
            self.prev_dir = self.dir
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

# Text Variables

pre_font = pygame.font.Font('freesansbold.ttf', 16)
pre_text = pre_font.render('press SPACE to begin', True, (128, 128, 128), (0, 0, 0))
pre_text_rect = pre_text.get_rect()
pre_text_rect.center = (gameWindow.width // 2, gameWindow.height - 64)

ctrls_font = pygame.font.Font('freesansbold.ttf', 18)
ctrls_text = ctrls_font.render(' C - Colour  Theme              ', True, (180, 180, 180), (50, 50, 50))
ctrls_text_rect = ctrls_text.get_rect()
ctrls_text_rect.center = (gameWindow.width -50, 9)

ctrls2_font = pygame.font.Font('freesansbold.ttf', 18)
ctrls2_text = ctrls_font.render(' P - Show  Points              ', True, (180, 180, 180), (50, 50, 50))
ctrls2_text_rect = ctrls_text.get_rect()
ctrls2_text_rect.center = (gameWindow.width -50, 28)

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

# Objects

snake_0 = Snake(192, 192, 24, 24, black_snake_images, white_snake_images, coloured_snake_images, python_snake_images, True)
snake_0.call(gameWindow)

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

    gameWindow.call.blit(pre_text, pre_text_rect)
    gameWindow.call.blit(ctrls_text, ctrls_text_rect)
    gameWindow.call.blit(ctrls2_text, ctrls2_text_rect)

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            ready = True

        # Space Detection

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ready = True

# ----- Main Loop -----

while running:
    clock.tick(8)

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
                if points_toggle == False:
                    points_toggle = True
                else:
                    points_toggle = False

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

    his_dict = dict(zip(Snake.x_his, Snake.y_his))

    for x_pos, y_pos in his_dict.items():

        if snake_0.x == x_pos and snake_0.y == y_pos:

            go_font = pygame.font.Font('freesansbold.ttf', 50)
            if c_mode == 'Black':
                go_text = go_font.render('Game Over', True, (128, 128, 128), (255, 255, 255))
            elif c_mode == 'White':
                go_text = go_font.render('Game Over', True, (128, 128, 128), (0, 0, 0))
            elif c_mode == 'Colour' or c_mode == 'Python':
                go_text = go_font.render('Game Over', True, (128, 128, 128), (255, 255, 255))

            go_text_rect = go_text.get_rect()
            go_text_rect.center = (gameWindow.width // 2, gameWindow.height // 2)

            gameWindow.call.blit(go_text, go_text_rect)
            pygame.display.update()

            pygame.time.delay(2500)

            running = False

    # Fruit Collision

    if snake_0.x == fruit.x and snake_0.y == fruit.y:
        points += 1
        fruit.place(gameWindow)
        
        fruit_pos_check = False

        globals()['snake_' + str(points)] = Snake(Snake.parts[-1].x, Snake.parts[-1].y, 24, 24, black_snake_images, white_snake_images, coloured_snake_images, python_snake_images)
        Snake.parts.append(globals()['snake_' + str(points)])

        for snake in Snake.parts:
            snake.check_mode()
        Snake.parts[-2].update()
        globals()['snake_' + str(points)].update()

    # Fruit Placement Control

    while not fruit_pos_check:
        for x_pos, y_pos in his_dict.items():
            if fruit.x == x_pos and fruit.y == y_pos:
                fruit.place(gameWindow)
            else:
                fruit_pos_check = True

    points_update()
    

    redrawWindow()

pygame.quit()
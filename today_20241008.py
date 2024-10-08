from pico2d import *
import random

class Grass:
    # 생성자 함수 : 객체의 초기 상태를 설정
    def __init__(self):
        self.image = load_image('grass.png')
        # 모양 없는 납작한 붕어빵 초기 모습 결정
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,40)
        pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
        pass

    def update(self):
        frame = (self.frame + 1) % 8
        self.frame = frame
        self.x += 5
        pass

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(10, 700), 599
        self.speed = random.randint(10, 50)
        random_size = random.randint(0, 1)
        if random_size == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
    def update(self):
        if self.y > 40: self.y -= self.speed
    def draw(self):
        self.image.draw(self.x,self.y)

def reset_world():
    global running
    global grass
    global team
    global world
    global ball
    running = True
    world = []
    grass = Grass()
    world.append(grass)
    team = [Boy() for i in range(10)]
    ball = [Ball() for i in range(20)]
    world += team
    pass

def update_world():
    grass.update()
    for boy in team:
        boy.update()
    for b in ball:
        b.update()

    pass

def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for b in ball:
        b.draw()
    update_canvas()
    pass

def handle_events():
    running = False

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()

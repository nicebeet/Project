from pygame import*

clock = time.Clock()
move_up = False
move_down = False
move_left = False
move_right = False
back =((0,0,0))
win = display.set_mode((1080,720))
win.fill((back))

class Wall():
    def __init__(self,x,y,w,h,color ):
        self.rect = Rect(x,y,w,h)

        self.fill_color = back
        if color:
            self.fill_color = color
    
    def color(self,new_color):
        self.fill_color = new_color

    def fill(self):
        draw.rect(win,self.fill_color,self.rect)

    

class Player():
    def __init__(self,x,y,w,h,color,speed):
        rect = Rect
        self.fill_color = color
        self.rect = Rect(x,y,w,h)
        self.rect.x = x
        self.rect.y = y
        
    def color(self,new_color):
        self.fill_color = new_color

    def fill(self):
        draw.rect(win,self.fill_color,self.rect)

wall = Wall(400,100,200,800,(0, 255, 255))
player = Player(400,100,20,20,(255,0,0),3)
while True:
    wall.fill()
    player.fill()
    for e in event.get():
        if e.type == QUIT:
            game = False

        
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                move_up = True
            if e.key == K_DOWN:
                move_down = True
            if e.key == K_LEFT:
                move_left = True
            if e.key == K_RIGHT:
                move_right = True
        elif e.type == KEYUP:
            if e.key == K_UP:
                move_up = False
            if e.key == K_DOWN:
                move_down = False
            if e.key == K_LEFT:
                move_left = False
            if e.key == K_RIGHT:
                move_right = False
                        




    if move_up:
        player.rect.y -= 3
    if move_down:
        player.rect.y += 3    
    if move_right:
        player.rect.x += 3
    if move_left:
        player.rect.x -= 3



    display.update()
    clock.tick(50)
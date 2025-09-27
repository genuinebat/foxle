from tkinter import PhotoImage

class Fox():
    def __init__(self, name:str, width:int, height:int):
        self.name = name

        self.mx = 900
        self.my = 500

        self.x_speed = 4
        self.y_speed = 3

        self.clicked = False

        self._w = width
        self._h = height

        self._left = "./fox/l.gif"
        self._right = "./fox/r.gif" 
        self._forward = "./fox/f.gif"
        self._idle = "./fox/f1.jpg"

        self._move_buffer = 2
        self._anim_buffer = 5
        self._stop_buffer = 8
        self._curr_state = self._right

        self._x = 0
        self._y = 0
    
    def update(self):
        # checking for idle animation conditions (near to target position)
        if self.mx - self._w/2 in [i for i in range(self._x - self.x_speed*self._stop_buffer, self._x + self.x_speed*self._stop_buffer)] and self.my - self._h/2 in [i for i in range(self._y - self.x_speed*self._stop_buffer, self._y + self.x_speed*self._stop_buffer)]:
                self._curr_state = self._idle
                return
        
        # checking for vertical movement animation or one of two horizontal movement animations
        if self.mx - self._w/2 in [i for i in range(self._x - self.x_speed*self._anim_buffer, self._x + self.x_speed*self._anim_buffer)]:
            self._curr_state = self._forward
        else:
            if self.mx - self._w/2+ self.x_speed * self._anim_buffer < self._x:
                self._curr_state = self._left
            elif self.mx - self._w/2 - self.x_speed * self._anim_buffer > self._x:
                self._curr_state = self._right
        
        # movement towards target position (in this case its the last dragged mouse position coordinates)
        if self.mx - self._w/2 + self.x_speed * self._move_buffer < self._x:
            self._curr_state = self._left
            self._x -= self.x_speed
        elif self.mx - self._w/2 - self.x_speed * self._move_buffer > self._x:
            self._curr_state = self._right
            self._x += self.x_speed
        
        if self.my - self._h/2 + self.y_speed * self._move_buffer< self._y:
            self._y -= self.y_speed
        elif self.my - self._h/2 + self.y_speed * self._move_buffer> self._y:
            self._y += self.y_speed

    def get_coordinates(self) -> tuple:
        return (self._x, self._y)

    def get_curr_anim(self) -> list:
        if self._curr_state == self._idle:
            return [PhotoImage(file= self._curr_state)]
        else:
            return [PhotoImage(file=self._curr_state, format=f"gif -index {i}") for i in range(3)]
    
    # range is defined by the horizontal / vertical speed multiplied by the stopping buffer amount
    def within_range(self, x, y) -> bool:
        if x < self._x + self._w + self.x_speed * self._stop_buffer and x > self._x - self.x_speed * self._stop_buffer and y < self._y + self._h + self.y_speed * self._stop_buffer and y > self._y - self.y_speed * self. _stop_buffer:
            return True
        else:
            return False
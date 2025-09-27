import pyautogui
from tkinter import Tk, Label
from fox import Fox

class Window():
    def __init__(self, width:int, height:int):
        self.w = width
        self.h = height

        self._win = Tk()

        self._win.overrideredirect(True)
        self._win.config(highlightbackground='black')
        self._win.wm_attributes('-transparentcolor', 'black')
        self._win.attributes('-topmost', True)
    
    def start(self):
        self.update()
        self._win.mainloop()
    
    def update(self):
        self._win.after(50, self.update)

    def destroy(self):
        self._win.destroy()


class FoxWindow(Window):
    def __init__(self, width:int, height:int, name:str, ):
        super().__init__(width, height)

        self._pet = Fox(name, self.w, self.h)

        self._anim = self._pet.get_curr_anim()
        self._frame = 0

        self._label = Label(self._win, bd=0, bg="black")
        self._label.image = self._anim
    
    def update(self):
        m_coord = pyautogui.position()
        if self._pet.clicked:
            self._pet.mx = m_coord[0]
            self._pet.my = m_coord[1]
        
        self._pet.update()

        self._anim = self._pet.get_curr_anim()

        if self._frame >= len(self._anim): self._frame = 0
        next_f = self._anim[self._frame]
        self._frame += 1
        self._label.configure(image=next_f)
        self._label.pack()

        pet_coord = self._pet.get_coordinates()
        self._win.geometry(f'{self.w}x{self.h}+{pet_coord[0]}+{pet_coord[1]}')

        super().update()        

    def m_click(self, x, y, pressed):
        if pressed and self._pet.within_range(x, y):
            self._pet.clicked = True
        else:
            self._pet.clicked = False

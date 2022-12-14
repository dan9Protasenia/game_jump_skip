from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Lose_window:
    def __init__(self, canvas, font, color):
        self.canvas = canvas
        self.id = canvas.create_text(250, 100,
                                     text='ВЫ ПРОИГРАЛИ!',
                                     font=font,
                                     fill=color)
        # self.canvas.move(self.id, 245, 100)
        # starts = [-3, -2, -1, 1, 2, 3]
        # random.shuffle(starts)
        # self.x = starts[0]

    def draw(self):
        self.canvas.move(self.id, 0, 0)



class Start_window:
    def __init__(self, canvas, font, color):
        self.canvas = canvas
        self.id = canvas.create_text(265, 350,
                                     text='                 нажмите ЛКМ\n'
                                          'для управления используйте ⬅️⬆️⬇️➡️' ,
                                     font=font,
                                     fill=color)


    def draw(self):
        self.canvas.move(self.id, 0, 0)

    def delete(self):
        self.canvas.move(self.id, 500, 500)


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 4
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[3] >= self.canvas_height:
            self.y = -4
        if self.hit_paddle(pos) == True:
            self.y = -4
        if pos[0] <= 0:
            self.x = 4
        if pos[2] >= self.canvas_width:
            self.x = -4

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -4

    def turn_right(self, evt):
        self.x = 4



    start = Start_window(canvas, "'Bold' 10", 'black')



def starting_game(event):
    while 1:
        if ball.hit_bottom == False:
            start = Start_window(canvas, "'Bold' 10", 'white')

            ball.draw()
            paddle.draw()
        elif ball.hit_bottom == True:
            lose = Lose_window(canvas, "'Archangelsk' 30", 'red')

        tk.update_idletasks()
        tk.update()
        # lose.draw()
        time.sleep(0.0001)






paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

canvas.bind_all('<Button-1>', starting_game)
canvas.mainloop()

from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("maze_solver")
        self.canvas = Canvas(self.__root, bg="white", width=self.width,height=self.height)
        self.canvas.pack(fill=BOTH,expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    def close(self):
        self.running = False

    def draw_line(self,line,fill_color="black"):
        line.draw(self.canvas,fill_color)


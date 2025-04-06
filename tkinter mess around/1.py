import tkinter as tk

class draggableWidget:
    def __init__(self, widget):
        self.widget = widget
        self.widget.bind("<ButtonPress-1>", self.start_drag)
        self.widget.bind("<B1-Motion>",self.drag)

    def start_drag(self, event):
        self.x = event.x
        self.y = event.y

    def drag(self, event):
        dx = event.x - self.x
        dy = event.y - self.y
        self.updateX = self.widget.winfo_x() + dx
        self.updateY = self.widget.winfo_y() + dy
        self.widget.place(x=self.updateX, y=self.updateY)


        centerX = self.widget.winfo_x() + self.widget.winfo_width() // 2
        centerY = self.widget.winfo_y() + self.widget.winfo_height() // 2
        print(f'{centerX, centerY=}')
        self.widget.config(text=f'{centerX}, {centerY}')

def drawGrid(canvas, spacing=100):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    for x in range(0,width,spacing):
        canvas.create_line(x,0, x, height, fill="black",width=1)
    for y in range(0,height, spacing):
        canvas.create_line(0,y,width,y, fill="black",width=1)


root = tk.Tk()

canvas = tk.Canvas(root,width=600, height=400)
canvas.pack(expand=True, fill="both")
drawGrid(canvas)


label = tk.Label(root,text="0, 0",bg="lightblue",padx=10,pady=5)
label.place(x=0,y=20)

draggableWidget(label)


root.mainloop()

from tkinter import Tk, Frame, Button, Label

class Window():
    def __init__(self, logic):
        self.tk = Tk()
        self.tk.title("Snake M122")
        self.tk.minsize()
        self.tk.resizable(False, False)

        self.tk.bind("<KeyPress>", self.__onKeyPress)

        self.logic = logic

        self.isRunning = False

        self.__build()
        self.draw()

    def __onKeyPress(self, ev):
        if(ev.keysym == "Up"):
            self.logic.onDirectionChange("u")
        elif(ev.keysym == "Right"):
            self.logic.onDirectionChange("r")
        elif(ev.keysym == "Down"):
            self.logic.onDirectionChange("d")
        elif(ev.keysym == "Left"):
            self.logic.onDirectionChange("l")

    def __build(self):
        f = Frame(self.tk)
        self.tiles = dict()
        self.canvas = self.__getCanvas(f)
        self.canvas.grid(row=0, column=0, sticky="NESW", padx=10, pady=10)
        self.btns = self.__getBtns(f)
        self.btns.grid(row=1, column=0, sticky="NESW", padx=10, pady=10)

        f.pack()

    def __getCanvas(self, master):
        f = Frame(master)

        for t in self.logic.grid.getTiles1D():
            tile = Frame(f, height=25, width=25)
            self.__colorTile(t, tile)
            tile.grid(row=t.y, column=t.x)
            self.tiles[t.getKey()] = tile

        return f

    def startBtnClick(self):
        if(not self.logic.isRunning):
            self.draw()
            self.setCountLabel(self.logic.countApple)
            self.elStartBtn.config(text="Abbrechen", fg="red")
            self.__loop()
        else:
            self.logic.reset()
            self.elStartBtn.config(text="Start", fg="green")

    def __loop(self):
        if(self.logic.loop()):
            self.draw()
            self.tk.after(200, self.__loop)
        else:
            self.elStartBtn.config(text="Start", fg="green")

    def setCountLabel(self, val):
        self.elCountLabel.config(text=val)

    def __getBtns(self, master):
        f = Frame(master)
        self.elStartBtn = Button(f, text="Start", command=lambda: self.tk.after(0, self.startBtnClick), fg="green", width=20)
        self.elStartBtn.grid(row=0, column=0)

        self.elCountLabel = Label(f, text="", fg="green", padx=10)
        self.elCountLabel.grid(row=0, column=1)
        return f

    def draw(self):
        self.setCountLabel(self.logic.countApple)
        for e in self.logic.grid.getTiles1D():
            self.__colorTile(e, self.tiles[e.getKey()])

    def __colorTile(self, tileObj, tileEl):
        if(tileObj.isApple):
            tileEl.config(bg="red")
        elif(tileObj.isSnake):
            tileEl.config(bg="green")
        else:
            tileEl.config(bg="white")

    def mainloop(self):
        self.tk.mainloop()

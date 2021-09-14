import tkinter as jra


class Application(jra.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.hi_there = jra.Button(self)
        self.hi_there["text"] = "Tên nút"
        self.hi_there["command"] = self.PressCheck
        self.hi_there.pack()

        self.quit = jra.Button(self, text="QUIT", command=root.destroy)
        self.quit.pack()

        self.pack()

    def PressCheck(self, event=None):
        print("hellu")


root = jra.Tk()
app = Application(master=root)
app.master.title("Dự đoán")
app.master.minsize(300, 200)
app.mainloop()
import tkinter as jra
from tkinter import messagebox
from tkinter import font
from tkinter.filedialog import askopenfilename, askdirectory

class Application(jra.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("Simple UI")

        master.configure(bg="pink")
        self.configure(bg="pink")

        rong = 500
        dai = 500
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()

        x = int(ws / 2 - (rong / 2))
        y = int((hs / 2) - (dai / 2))
        
        master.geometry(f'{rong}x{dai}+{x}+{y}')
        
        self.font = font.Font(family='Helvetica', size=14, weight="bold")

        jra.Label(self,bg="pink").pack()

        giatrimacdinh = "Mac dinh"
        DATA = ["NAM", "NU", "LESS", "GAY"]
        self.option_menu = jra.OptionMenu(self, giatrimacdinh,*DATA)
        self.option_menu.pack()

        jra.Label(self,bg="pink").pack()

        self.label = jra.Label(self,bg="pink", font=self.font,text="Chu' Thi'ch")

        self.label.pack()


        self.hi_there = jra.Button(self,text="Tên nút",bg="#B0F5AB",width=20,font=self.font)
        self.hi_there["command"] = self.lenh_xin_chao
        self.hi_there.pack()

        jra.Label(self,bg="pink").pack()
        self.nut2 = jra.Button(self,text="Nút 2",font=self.font)
        self.nut2["command"] = self.lenh_xin_chao
        self.nut2.pack()

        jra.Label(self,bg="pink").pack()
        self.o_nhap_du_lieu1 = jra.Entry(self,font=self.font)
        self.o_nhap_du_lieu1.pack()

        jra.Label(self,bg="pink").pack()
        self.o_nhap_du_lieu2 = jra.Entry(self,font=self.font)
        self.o_nhap_du_lieu2.pack()

        jra.Label(self,bg="pink").pack()
        self.o_nhap_du_lieu3 = jra.Entry(self,font=self.font)
        self.o_nhap_du_lieu3.pack()

        jra.Label(self,bg="pink").pack()
        self.o_nhap_du_lieu4 = jra.Entry(self,font=self.font)
        self.o_nhap_du_lieu4.pack()

        jra.Label(self,bg="pink").pack()
        self.o_nhap_du_lieu5 = jra.Entry(self,font=self.font)
        self.o_nhap_du_lieu5.pack()

        self.quit = jra.Button(self, text="QUIT", command=root.destroy)
        self.quit.pack()

        self.pack()

        self.mainloop()

    def lenh_xin_chao(self):
        duongdan =  askopenfilename()
        messagebox.showinfo("Duong dan",duongdan)
        # try:
        #     giatri = int(self.o_nhap_du_lieu.get())
        # except Exception as e:
        #     messagebox.showerror('Loi gia tri')
        #     return

        # messagebox.showinfo(giatri + 10)


root = jra.Tk()
app = Application(master=root)

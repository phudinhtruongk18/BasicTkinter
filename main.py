import os
import tkinter as jra
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import font as tkfont


def openThuMuc(link=""):
    os.startfile(f'{os.path.realpath("") + link}')


class Application(jra.Frame):
    def __init__(self, master=None, api_key=None):
        super().__init__(master)
        self.api_key = api_key
        master.title("KeyWordCrawler")
        master.iconbitmap("logo.ico")
        w = 555
        h = 500
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()
        x = ws / 2 - (w / 2)
        y = (hs / 2) - (h / 2)
        master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # self.value_of_check = True
        # self.check_box = jra.Checkbutton(self, text="Tải toàn bộ chapter", variable=self.value_of_check)
        # self.check_box.grid(row=0, column=0)

        self.font = tkfont.Font(family='Helvetica', size=12, weight="bold")

        self.string_selected_session = "Mac dinh"
        self.session_option_menu = jra.OptionMenu(self, self.string_selected_session,
                                                  ["MAC DINH 0", "MAC DINH 2", "MAC DINH 3", "MAC DINH 4"])
        self.session_option_menu.configure(font=self.font, width=18, anchor=jra.CENTER, bd=5)
        self.session_option_menu.grid(row=0, column=0)

        self.canvas_batdau = jra.Frame(self)

        self.labelllll = jra.Label(self.canvas_batdau, text="Num of Threads")
        self.labelllll.grid(row=1, column=0)

        self.entry_link = jra.Text(self.canvas_batdau, font=tkfont.Font(family='Helvetica', size=14, weight="bold"),
                                   fg="#000000",
                                   bg="#B0F5AB", width=50, height=10)
        self.entry_link.grid(row=4, column=0)

        jra.Label(self.canvas_batdau, text="Your link").grid(row=3, column=0)

        self.entry_api = jra.Entry(self.canvas_batdau, font=tkfont.Font(family='Helvetica', size=14, weight="bold"),
                                   fg="#000000",
                                   bg="#B0F5AB", width=50)
        self.entry_api.grid(row=2, column=0)

        self.entry_api.insert(1, self.api_key)

        jra.Label(self.canvas_batdau).grid(row=5, column=0)
        self.buttonSoSanh = jra.Button(self.canvas_batdau, text="Thực thi", font=self.font, fg="#ffffff",
                                       bg="#263942",
                                       width=20,
                                       height=2)
        self.buttonSoSanh["command"] = self.kiem_tra_va_thuc_thi
        self.buttonSoSanh.grid(row=6, column=0)

        jra.Label(self.canvas_batdau).grid(row=10, column=0)

        self.buttonThuMuc = jra.Button(self.canvas_batdau, text="Mở Thư Mục Hiện Hành ", font=self.font, fg="#ffffff",
                                       bg="#263942",
                                       width=20, height=2)
        self.buttonThuMuc["command"] = openThuMuc
        self.buttonThuMuc.grid(row=11, column=0)

        # self.buttonThuMuc = jra.Button(self, text="Clear", font=self.font, fg="#ffffff", bg="#263942",
        #                                width=20, height=1)
        # self.buttonThuMuc["command"] = self.clear_taptruyen
        # self.buttonThuMuc.grid(row=7, column=0)

        # self.bool_show = False
        # self.show = jra.Button(self, text="Show Process", font=self.font, fg="#ffffff", bg="#263942",
        #                        width=20, height=1)
        # self.show["command"] = self.show_tientrinh
        # self.show.grid(row=8, column=0)
        self.label_trang_thai = jra.Label(self.canvas_batdau, text="Downloading and uploading your files")

        self.progress_bar = ttk.Progressbar(self.canvas_batdau, orient=jra.HORIZONTAL, length=100, mode="determinate")

        self.huongDan = jra.Label(self.canvas_batdau, text="\nBất kì vấn đề nào \n phudinhtruongk18@gmail.com",
                                  width=60)
        self.huongDan.grid(row=12, column=0)

        # jra.Label(self.canvas_batdau).grid(row=9, column=0)

        # self.canvas_button = jra.Canvas(self.canvas_batdau)
        # self.canvas_button.grid(row=12, column=0)
        self.column = 0
        self.row = 0
        self.danh_sach_button = []
        self.danhsach_chap = []
        self.tentruyen = ""

        # new_window = jra.Toplevel(self)
        # self.DetectedWindow = TienTrinhCuaSo(new_window, self, w, h, y)
        self.canvas_batdau.grid()
        self.canvas_batdau.grid_forget()

        self.canvas_ketuqua = jra.Frame(self)

        # self.label_trang_thai = jra.Label(self.canvas_ketuqua, text="Downloading your file")
        # self.label_trang_thai.grid(row=1, column=0)
        jra.Label(self.canvas_ketuqua).grid(row=2, column=0)
        # self.button_reload = jra.Button(self.canvas_ketuqua, text="Reload", font=self.font, fg="#ffffff", bg="#263942",
        #                                 width=20, height=2)
        # self.button_reload["command"] = self.reload_tool
        # self.button_reload.grid(row=3, column=0)
        jra.Label(self.canvas_ketuqua).grid(row=4, column=0)
        self.Text_ketqua = jra.Text(self.canvas_ketuqua, font=tkfont.Font(family='Helvetica', size=14, weight="bold"),
                                    fg="#000000",
                                    bg="#B0F5AB", width=50, height=10)
        self.Text_ketqua.grid(row=5, column=0)
        jra.Label(self.canvas_ketuqua).grid(row=6, column=0)
        # self.button_copy = jra.Button(self.canvas_ketuqua, text="Copy", font=self.font, fg="#ffffff", bg="#263942",
        #                               width=20,
        #                               height=2)
        # self.button_copy["command"] = self.saochep_text_box
        # self.button_copy.grid(row=7, column=0)
        self.huongDan2 = jra.Label(self.canvas_ketuqua, text="\nBất kì vấn đề nào \n phudinhtruongk18@gmail.com",
                                   width=60)
        self.huongDan2.grid(row=8, column=0)

        self.canvas_batdau.grid()

        # self.value_of_check.trace("w", self.hide_and_show)
        self.grid()
        self.mainloop()

    def kiem_tra_va_thuc_thi(self):
        if not os.path.exists("Output"):
            os.mkdir("Output")
        try:
            api_key = int(self.entry_api.get())
        except Exception as e:
            messagebox.showinfo("Check threads number ", e)
            return
        if api_key < 0:
            messagebox.showinfo("Check threads number", "Check threads number")
            return
        print("Your thread", api_key)
        link_tonghop = self.entry_link.get('1.0', 'end')
        list_link = []
        for temp in str(link_tonghop).split("\n"):
            list_link.append(temp.strip())
        print(list_link)

        # thuc_thi_cong_viec(api_key, list_link)
        messagebox.showinfo("Done", "Complete! Thank for using my tool")

    # def show_tientrinh(self):
    #     if self.bool_show:
    #         self.bool_show = False
    #         self.DetectedWindow.hide()
    #         self.show.configure(text="Show")
    #     else:
    #         self.bool_show = True
    #         self.DetectedWindow.show()
    #         self.show.configure(text="Hide")

    # def tao_nut_theo_chapter(self):
    # def tao_nut_theo_chapter(self):
    #     for temp in self.danhsach_chap:
    #         nutchapter = jra.Button(self.canvas_button, bg="pink", text=str(temp[0]), font=self.font, width=8)
    #         nutchapter.configure(command=lambda btn=nutchapter: self.tai_truyen_theo_chap(button_temp=btn))
    #         nutchapter.grid(row=self.row, column=self.column)
    #
    #         self.danh_sach_button.append(nutchapter)
    #         if self.column == 4:
    #             self.row += 1
    #             self.column = 0
    #         else:
    #             self.column += 1

    # def clear_taptruyen(self):
    #     self.column = 0
    #     self.row = 0
    #     self.danhsach_chap.clear()
    #     for temp in self.danh_sach_button:
    #         temp.grid_forget()
    #     self.danh_sach_button.clear()
    def thuc_thi_khi_hoantat(self, ten_file):
        self.canvas_batdau.grid_forget()
        self.canvas_ketuqua.grid()
        self.Text_ketqua.delete('1.0', jra.END)
        self.entry_link.delete('1.0', jra.END)
        fileCanMo = open(ten_file, "r")
        dulieu = fileCanMo.read()
        fileCanMo.close()
        self.Text_ketqua.insert('1.0', dulieu)


print("Hello")
# ketqua = requests.get("https://caythuearam.com")
# if ">phudinhtruongk18@gmail.com</a>" in ketqua.text:
giaoDien = jra.Tk()

# fileCanMo = open("setting.txt", "r")
# apikey = fileCanMo.read()
# fileCanMo.close()
apikey = ""

app = Application(master=giaoDien, api_key=str(apikey.strip()))

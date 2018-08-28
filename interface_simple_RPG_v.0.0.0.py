import tkinter
from tkinter import messagebox

class Window(tkinter.Frame):

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master) # daje mozliwosc wywolania  okien

        self.master = master

        self.init_window3()
        self.init_window()
        self.init_window2()
        self.init_image()

    def init_window(self):

        self.master.title("Simple RPG")
        labelframe1 = tkinter.LabelFrame(text="Action", relief="raised", height=10, width=10)

        MainMenu = tkinter.Menu(self.master)    # dodanie głownego menu do okna
        self.master.config(menu=MainMenu)       # konfiguracja glownjego menu w oknie


        file = tkinter.Menu(MainMenu)
        MainMenu.add_cascade(label='File', menu=file)
        file.add_command(label='Save - not work')
        file.add_command(label='Exit', command=self.client_exit)

        edit = tkinter.Menu(MainMenu)
        MainMenu.add_cascade(label='Edit', menu=edit)
        edit.add_command(label='Undo', state="disabled")

        about = tkinter.Menu(MainMenu)
        MainMenu.add_cascade(label='About', menu=about)
        about.add_command(label='About',  command=self.about_x)

        north = tkinter.Button(labelframe1, text="\'NORTH\'", fg="blue", height=4, width=25, bd=4)
        north.place(x=170, y=10)

        south = tkinter.Button(labelframe1, text="\'SOUTH\'", fg="blue", cursor="dot", height=4, width=25, bd=4)
        south.place(x=170, y=310)

        east = tkinter.Button(labelframe1, text="\'EAST\'", fg="blue", height=10, width=10, bd=4)
        east.place(x=20, y=110)

        west = tkinter.Button(labelframe1, text="\'WEST\'", fg="blue", height=10, width=10, bd=4)
        west.place(x=420, y=110)

        walcz = tkinter.Button(labelframe1, text="\'FIGHT!\'", fg="red", height=10, width=10, bd=4)
        walcz.place(x=170, y=110)

        uciekaj = tkinter.Button(labelframe1, text="\'RUN AWAY\'", fg="green", height=10, width=10, bd=4)
        uciekaj.place(x=270, y=110)

        # quitButton = tkinter.Button(self, text="QUIT\'", command=self.client_exit)
        # quitButton.place(x=10, y=10)

        labelframe1.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1, anchor=tkinter.CENTER)
        # self.pack()

    def init_window2(self):

        labelframe2 = tkinter.LabelFrame(text="Map", relief="flat", height=10, width=10)
        labelframe2.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        img = tkinter.PhotoImage(file="Pusta_Mapa.png").zoom(x=4, y=4)
        imgLabel = tkinter.Label(image=img, relief="flat")
        imgLabel.image = img
        imgLabel.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=1, padx=50, pady=20)

    def init_image(self):
        pass

    def init_window3(self):

        labelframe3 = tkinter.LabelFrame(text="Event", relief="raised", height=350, width=100)
        zmienna = tkinter.StringVar()
        zmienna.set("That WORKS!!!!!!!!!!!!!!!!!!!!!!! \n That WORKS VERY WELL :D  TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST\n :D")
        frame3 = tkinter.Message(labelframe3, textvariable=zmienna, width=500)
        labelframe3.pack(side=tkinter.BOTTOM, fill=tkinter.X, expand=0)
        frame3.pack(padx=150, pady=130)

    def client_exit(self):
        answer=messagebox.askquestion("Game Over ?", 'Are U sure?')
        if answer == "yes":
            exit()

    def about_x(self):
        messagebox.showinfo("Simple RPG - Creator: Paqul", "This is Interface to my first Text RPG Game \n Have Fun ^^")

root = tkinter.Tk()
root.resizable(width=False, height=False)
root.geometry("1024x768")

app = Window(root)

root.mainloop()

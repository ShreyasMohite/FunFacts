from tkinter import *
import randfacts


class Fact:
    def __init__(self,root):
        self.root=root
        self.root.title("Facts")
        self.root.iconbitmap("logo1.ico")
        self.root.geometry("400x300")
        self.root.resizable(0,0)


        def rand():
            x = randfacts.getFact(True)
            lab.config(text=x)



#===========================================================
        
        mainframe=Frame(self.root,width=400,height=300,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        button=Button(mainframe,text="Random Facts",width=13,font=('times new roman',13),cursor="hand2",command=rand)
        button.place(x=130,y=30)

        lab=Label(mainframe,text="",font=('times new roman',13),wraplength=390)
        lab.place(x=0,y=160)




if __name__=="__main__":
    root=Tk()
    Fact(root)
    root.mainloop()


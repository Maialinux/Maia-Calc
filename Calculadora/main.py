from tkinter import *
import calculadora


class Main():
    def __init__(self) -> None:
        print("Projeto Iniciado")
        self.janelaMain = Tk()
        self.janelaMain.title("Maia calc")
        self.janelaMain.geometry("325x500")
        self.favicon = PhotoImage(file="icones/favicon.png")
        self.janelaMain.iconphoto(True, self.favicon)
        self.janelaMain.resizable(False, False)
        self.painelMain = Frame(self.janelaMain,background="#232323")
        self.painelMain.pack(side=TOP, fill=BOTH, expand=1, ipady=53)
        self.painelMain2 = Frame(self.janelaMain,background="#131313")
        self.painelMain2.pack(side=TOP, fill=BOTH, expand=1)
        self.calaculadora = calculadora.Calculadora(self.painelMain,self.painelMain2)
        self.janelaMain.mainloop()
        pass
    

if __name__ == "__main__":
    Main()
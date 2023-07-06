from tkinter import *
import math


todos_valores = ""
botaoToggle = False

class Calculadora():
    def __init__(self,painelMain,painelMain2) -> None:
        print("Calculadora Inicializada")
        self.painelCalculadora = painelMain
        self.painelCalculadora.configure(bg="#232333")  #ccc
        self.MenuCalculadora()
        self.DisplayCalculadora()
        self.painelBotoes = painelMain2
        self.painelBotoes.configure(bg="#232333")  #bbb
        self.BotoesDaCalculadora()
        pass


    def MenuCalculadora(self):
        self.pressionei = True
        self.imgMenu_On = PhotoImage(file="icones/16x16/menu_humburguer16.png")
        self.imgMenu_Off = PhotoImage(file="icones/16x16/menu_humburguer16Hover.png")
        self.btnMenu = Button(self.painelCalculadora, image=self.imgMenu_On, command=self.TrocarIcone)
        self.btnMenu.place(width="32", height="32", x=5, y=5)
        self.tituloCalculadora = Label(self.painelCalculadora,text="Menu Fechado",bg="#232333", fg="#e7e7e7", font=("impact",16))
        self.tituloCalculadora.place(x=100, y=5)
        pass

    def TrocarIcone(self):
        if self.pressionei:
            self.btnMenu.config(image=self.imgMenu_Off)
            self.pressionei = False
            self.tituloCalculadora["text"] = "Menu Aberto"
        
        else:
             self.btnMenu.config(image=self.imgMenu_On)
             self.pressionei = True
             self.tituloCalculadora["text"] = "Menu Fechado"
        pass


    def DisplayCalculadora(self):
        self.textoVariado = StringVar()
        self.displayCalculadora = Entry(self.painelCalculadora, textvariable=self.textoVariado, font=("Arial", 30), fg="#000",justify="right", bg="cyan",highlightbackground="#0000D2", highlightcolor="#0000c2", highlightthickness=2, relief="flat", state="readonly", readonlybackground="cyan")
        self.displayCalculadora.place(width=315, height=55, x=5, y=45)
        self.displayCalculadora.focus_set()
        self.textoVariado.set(0)
        self.displayCalculadora.bind("<Return>", self.TeclaCalculo)
        self.displayCalculadora.bind("<Key>", self.TeclasDaCalculadora)
        self.displayCalculadora.bind("<Escape>", lambda e:self.Limpar(e))
        self.displayCalculadora.bind("<BackSpace>", lambda e:self.Apagar(e))
        


    def BotoesDaCalculadora(self):
        largura = "69"
        altura = "55"
        #largura = "32"
        #altura = "32"
        self.imgPorcentagem = PhotoImage(file="icones/32x32/por-cento.png")
        self.btnPorcentagem = Button(self.painelBotoes,image=self.imgPorcentagem,width=largura, height=altura, command=lambda:self.Porcentagem(" % "))
        self.btnPorcentagem.grid(row=0, column=0, padx=2, pady=2)

        self.imgLimpar = PhotoImage(file="icones/32x32/limpar.png")
        self.btnLimpar = Button(self.painelBotoes,image=self.imgLimpar,width=largura, height=altura, command=lambda:self.Limpar(True))
        self.btnLimpar.grid(row=0, column=1, columnspan=2, ipadx=44, padx=2, pady=2)

        self.imgApagar = PhotoImage(file="icones/32x32/apagar.png")
        self.btnApagar = Button(self.painelBotoes,image=self.imgApagar,width=largura, height=altura, command=lambda:self.Apagar(True))
        self.btnApagar.grid(row=0, column=3, padx=2, pady=2)

        self.imgNumAoQuadrado = PhotoImage(file="icones/32x32/num-ao-quadrado.png")
        self.btnNumAoQuadrado = Button(self.painelBotoes,image=self.imgNumAoQuadrado,width=largura, height=altura, command=lambda:self.NumeroAoQuadrado(" * "))
        self.btnNumAoQuadrado.grid(row=1, column=0, padx=2, pady=2)

        self.imgRaizQuadrada = PhotoImage(file="icones/32x32/raiz-quadrada.png")
        self.btnRaizQuadrada = Button(self.painelBotoes,image=self.imgRaizQuadrada,width=largura, height=altura, command=lambda:self.RaizQuadrada(" / "))
        self.btnRaizQuadrada.grid(row=1, column=1, columnspan=2, ipadx=44, padx=2, pady=2)

        self.imgDivisao = PhotoImage(file="icones/32x32/divisao.png")
        self.btnDivisao = Button(self.painelBotoes,image=self.imgDivisao,width=largura, height=altura, command=lambda:self.EntraValor(" / "))
        self.btnDivisao.grid(row=1, column=3, padx=2, pady=2)


        self.imgNum7 = PhotoImage(file="icones/32x32/7.png")
        self.btnNum7 = Button(self.painelBotoes,image=self.imgNum7,width=largura, height=altura, command=lambda:self.EntraValor("7"))
        self.btnNum7.grid(row=2, column=0, padx=2, pady=2)

        self.imgNum8 = PhotoImage(file="icones/32x32/8.png")
        self.btnNum8 = Button(self.painelBotoes,image=self.imgNum8,width=largura, height=altura, command=lambda:self.EntraValor("8"))
        self.btnNum8.grid(row=2, column=1, padx=2, pady=2)

        self.imgNum9 = PhotoImage(file="icones/32x32/9.png")
        self.btnNum9 = Button(self.painelBotoes,image=self.imgNum9,width=largura, height=altura, command=lambda:self.EntraValor("9"))
        self.btnNum9.grid(row=2, column=2, padx=2, pady=2)

        self.imgMultiplicacao = PhotoImage(file="icones/32x32/multiplicacao.png")
        self.btnMultiplicacao = Button(self.painelBotoes,image=self.imgMultiplicacao,width=largura, height=altura, command=lambda:self.EntraValor(" * "))
        self.btnMultiplicacao.grid(row=2, column=3, padx=2, pady=2)

        self.imgNum4 = PhotoImage(file="icones/32x32/4.png")
        self.btnNum4 = Button(self.painelBotoes,image=self.imgNum4,width=largura, height=altura, command=lambda:self.EntraValor("4"))
        self.btnNum4.grid(row=3, column=0, padx=2, pady=2)

        self.imgNum5 = PhotoImage(file="icones/32x32/5.png")
        self.btnNum5 = Button(self.painelBotoes,image=self.imgNum5,width=largura, height=altura, command=lambda:self.EntraValor("5"))
        self.btnNum5.grid(row=3, column=1, padx=2, pady=2)

        self.imgNum6 = PhotoImage(file="icones/32x32/6.png")
        self.btnNum6 = Button(self.painelBotoes,image=self.imgNum6,width=largura, height=altura, command=lambda:self.EntraValor("6"))
        self.btnNum6.grid(row=3, column=2, padx=2, pady=2)

        self.imgMenus = PhotoImage(file="icones/32x32/menus.png")
        self.btnMenus = Button(self.painelBotoes,image=self.imgMenus,width=largura, height=altura, command=lambda:self.EntraValor(" - "))
        self.btnMenus.grid(row=3, column=3, padx=2, pady=2)

        self.imgNum1 = PhotoImage(file="icones/32x32/1.png")
        self.btnNum1 = Button(self.painelBotoes,image=self.imgNum1,width=largura, height=altura, command=lambda:self.EntraValor("1"))
        self.btnNum1.grid(row=4, column=0, padx=2, pady=2)

        self.imgNum2 = PhotoImage(file="icones/32x32/2.png")
        self.btnNum2 = Button(self.painelBotoes,image=self.imgNum2,width=largura, height=altura, command=lambda:self.EntraValor("2"))
        self.btnNum2.grid(row=4, column=1, padx=2, pady=2)

        self.imgNum3 = PhotoImage(file="icones/32x32/3.png")
        self.btnNum3 = Button(self.painelBotoes,image=self.imgNum3,width=largura, height=altura, command=lambda:self.EntraValor("3"))
        self.btnNum3.grid(row=4, column=2, padx=2, pady=2)

        self.imgMais = PhotoImage(file="icones/32x32/mais.png")
        self.btnMais = Button(self.painelBotoes,image=self.imgMais,width=largura, height=altura, command=lambda:self.EntraValor(" + "))
        self.btnMais.grid(row=4, column=3, padx=2, pady=2)


        self.imgMaisOuMenos = PhotoImage(file="icones/32x32/mais-ou-menos.png")
        self.btnMaisOuMenos = Button(self.painelBotoes,image=self.imgMaisOuMenos,width=largura, height=altura, command=lambda:self.MaisOuMenos(" * -1 "))
        self.btnMaisOuMenos.grid(row=5, column=0, padx=2, pady=2)

        self.imgNum0 = PhotoImage(file="icones/32x32/0.png")
        self.btnNum0 = Button(self.painelBotoes,image=self.imgNum0,width=largura, height=altura, command=lambda:self.EntraValor("0"))
        self.btnNum0.grid(row=5, column=1, padx=2, pady=2)

        self.imgVirgula = PhotoImage(file="icones/32x32/virgula.png")
        self.btnVirgula = Button(self.painelBotoes,image=self.imgVirgula,width=largura, height=altura, command=lambda:self.EntraValor("."))
        self.btnVirgula.grid(row=5, column=2, padx=2, pady=2)

        self.imgIgual = PhotoImage(file="icones/32x32/igual.png")
        self.btnIgual = Button(self.painelBotoes,image=self.imgIgual,width=largura, height=altura, command=lambda:self.Calcular())
        self.btnIgual.grid(row=5, column=3, padx=2, pady=2)

        pass


    def Porcentagem(self,parametro):
        global todos_valores

        if parametro == " % ":
            parametro = " / "

        todos_valores = todos_valores + str(parametro) + str(float(100))
        resultado = str(eval(todos_valores)) 
        self.textoVariado.set(resultado)
        pass

    def Limpar(self, parametro):
        global todos_valores
        todos_valores = ""
        self.textoVariado.set(0)
        pass

    def Apagar(self,parametro):
        global todos_valores
        todos_valores = todos_valores[:-1]   
        self.textoVariado.set(todos_valores)
       
    def NumeroAoQuadrado(self, parametro):
        global todos_valores
        todos_valores = todos_valores + str(parametro) + str(math.pow(eval(todos_valores),1))
        resultado = str(eval(todos_valores))
        self.textoVariado.set(resultado)
        pass


    def RaizQuadrada(self, parametro):
        global todos_valores
        todos_valores = todos_valores + str(parametro) + str(math.sqrt(eval(todos_valores)))   
        resultado = str(eval(todos_valores))
        self.textoVariado.set(resultado)


    def MaisOuMenos(self, parametro):
        global todos_valores
        global botaoToggle

        botaoToggle = not botaoToggle

        if botaoToggle == True:
            todos_valores = todos_valores + str(parametro)
            resultado = str(eval(todos_valores))
            todos_valores = todos_valores[:-1]
            self.textoVariado.set(resultado)
        else:
            todos_valores = todos_valores + str(parametro)
            resultado = str(eval(todos_valores))
            todos_valores = todos_valores[:-1]
            self.textoVariado.set(resultado)


    def EntraValor(self,parametro):
        global todos_valores
        todos_valores = todos_valores + str(parametro)
        self.textoVariado.set(todos_valores)
        pass

    def Calcular(self):
        global todos_valores
        self.resultado = str(eval(todos_valores))
        self.textoVariado.set(self.resultado)
        todos_valores = ""
        pass


    def TeclaCalculo(self, event):
        try:
            self.Calcular()
        except:
            print("Digite alguma coisa")
        
    
    def TeclasDaCalculadora(self, event):
        tecla = event.char
        
        if tecla.isnumeric() or tecla.isdigit() or tecla == "/" or tecla == "*" or tecla == "-" or tecla == "+" or tecla == ".":
            self.EntraValor(tecla)

        if tecla == ",":
            self.EntraValor(".")

        if tecla == "%":
            self.Porcentagem(" % ")
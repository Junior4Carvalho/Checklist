from tkinter import *
from time import sleep

janela = Tk()

janela.title("Chekclist")
janela.geometry("390x320+630+200")
janela.configure(bg="darkgray")


cl1 = IntVar()
cl2 = IntVar()
cl3 = IntVar()
cl4 = IntVar()
cl5 = IntVar()
cl6 = IntVar()
cl7 = IntVar()


def todo():
        
    c1 = Checkbutton(text="1 - Arrumar a cama", variable=cl1, onvalue= 1, offvalue= 0, pady=10, bg= "darkgray", fg="black", font=("helvetica", 10, "bold"))
    c2 = Checkbutton(text="2 - Escovar os dentes", variable=cl2, onvalue= 1, offvalue= 0, pady=10, bg= "darkgray", fg="black", font=("helvetica", 10, "bold"))
    c3 = Checkbutton(text="3 - Fazer os trabalhos domésticos", variable=cl3, onvalue= 1, offvalue= 0, bg= "darkgray", fg="black", font=("helvetica", 10, "bold"))
    c4 = Checkbutton(text="4 - Matabichar", variable=cl4, onvalue= 1, offvalue= 0, pady=10, bg= "darkgray", fg="black", font=("helvetica", 10, "bold"))
    c5 = Checkbutton(text="5 - Tomar Banho", variable=cl5, onvalue= 1, offvalue= 0, bg= "darkgray", fg="black", font=("helvetica", 10, "bold"))
    c6 = Checkbutton(text="6 - Estudar", variable=cl6, onvalue= 1, offvalue= 0, pady=10, bg= "darkgray", fg="black", font=("helvetica", 10, "bold"))
    c7 = Checkbutton(text="7 - Ir para Escola", variable=cl7, onvalue= 1, offvalue= 0, bg= "darkgray", fg="black", font=("helvetica", 10, "bold"))
 
    
    c1.place(x=20, y= 20)
    c2.place(x=20, y= 50)
    c3.place(x=20, y= 90)
    c4.place(x=20, y= 110)
    c5.place(x=20, y= 150)
    c6.place(x=20, y= 170)
    c7.place(x=20, y= 205)

    btn = Button(text="Confirmar", bg="green", fg="white", width=10, height=2, border=3, borderwidth=4, font=("verdana", 10, "bold"), command=confirmar)
    btn.place(x=250, y=250)


def confirmar():
    
    print("CONFIRMAR - Passa para a próxima janela.")
    g1 = cl1.get()   
    g2 = cl2.get()
    g3 = cl3.get()
    g4 = cl4.get()
    g5 = cl5.get()
    g6 = cl6.get()
    g7 = cl7.get()
    
    sleep(.3)
    janela.withdraw()
    
    sleep(.3)
    global janela2
    janela2 = Toplevel()
    janela2.title("Chekclist")
    janela2.geometry("490x420+630+200")
    janela2.configure(bg="lightgray")
    tarefa = Label(janela2, text="Tarefas Concluídas ⬇️", pady=5, bg="lightgray", fg="blue", font=("helvetica", 12, "bold"))
    tarefa.place(x=170, y=20)
    vlt = Button(janela2, text="Voltar", bg="green", fg="white", width=10, height=2, border=3, borderwidth=4, font=("verdana", 10, "bold"), command=voltar)
    vlt.place(x=220, y=350)
    
    sr = Button(janela2, text="Sair", bg="Red", fg="white", width=10, height=2, border=3, borderwidth=4, font=("verdana", 10, "bold"), command=sair)
    sr.place(x=350, y=350)
         
    
        
    if g1  == 1:
        print("1 - Feito")
        f1 = Label(janela2, text="Arrumar a cama ✅", pady=10, bg="lightgray", fg="green", font=("helvetica", 10, "bold"))
        f1.place(x=50, y= 50)
    else:
        print("1 - Não feito")
        
    if g2  == 1:
        print("2 - Feito")
        f2 = Label(janela2, text="Escovar os dentes ✅", pady=10, bg="lightgray", fg="green", font=("helvetica", 10, "bold"))
        f2.place(x=50, y= 80)
        
    else:
        print("2 - Não feito")
        
    if g3  == 1:
        print("3 - Feito")
        f3 = Label(janela2, text="Fazer os trabalhos domésticos ✅", pady=10, bg="lightgray", fg="green", font=("helvetica", 10, "bold"))
        f3.place(x=50, y= 110)
    else:
        print("3 - Não feito")
        
    if g4  == 1:
        print("4 - Feito")
        f4 = Label(janela2, text="Matabichar ✅", pady=10, bg="lightgray", fg="green", font=("helvetica", 10, "bold"))
        f4.place(x=50, y= 140)
        
    else:
        print("4 - Não feito")
        
    if g5  == 1:
        print("5 - Feito")
        f5 = Label(janela2, text="Tomar Banho ✅", pady=10, bg="lightgray", fg="green", font=("helvetica", 10, "bold"))
        f5.place(x=50, y= 170)
    else:
        print("5 - Não feito")
        
    if g6  == 1:
        print("6 - Feito")
        f6 = Label(janela2, text="Estudar ✅", pady=10, bg="lightgray", fg="green", font=("helvetica", 10, "bold"))
        f6.place(x=50, y= 200)
    else:
        print("6 - Não feito")
        
    if g7  == 1:
        print("7 - Feito")
        f5 = Label(janela2, text="Ir para Escola ✅", pady=10, bg="lightgray", fg="green", font=("helvetica", 10, "bold"))
        f5.place(x=50, y= 230)
    else:
        print("7 - Não feito")
        
        
        
    if g1 and g2 and g3 and g4 and g5 and g6 and g7 == 1:
        done = Label(janela2, text="Parabéns, Todas as Tarefas foram Feitas ✅", pady=5, bg="lightgray", fg="green", font=("helvetica", 12, "bold"))
        done.place(x=90, y=280)

def sair():
    
    sleep(.3)
    janela2.destroy()
    print("SAIR - Programa FINALIZADO!")


def voltar():
    
    sleep(.3)
    janela2
    janela2.withdraw()
    
    sleep(.3)
    janela.deiconify()
    
    print("VOLTAR - Voltou para a primeira janela!")
    

todo()
janela.mainloop()

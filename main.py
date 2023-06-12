import tkinter
from tkinter import *
from tkinter.ttk import *

question = Tk()
question.geometry("500x500")
question.title("Ao meu amor!")
labelQ = Label(question, text="Como eu escreveria 'jealousy' em português um ano atras?")

labelQ.grid(column=0, row=0)
answer = Entry(question, width=10)
answer.grid(column=1, row=0)


def clicked():
    if answer.get().lower() == "ciúmes":
        res = "Hoje em dia, sim! Então não! Tenta de novo!"
        labelQ.configure(text=res)

    elif answer.get().lower() == "suimes":
        root = Toplevel(question)
        root.geometry("750x420")
        root.title("Feliz aniversario a nos! Com um ano do nosso amor!")
        res = "Certo! Aqui o meu presente pra você! Te amo!"
        lebelres = Label(root, text=res)
        lebelres.pack()

        data1 = "Quero beber o seu sorriso, afogar no seu beijo, cair no seu abraço"
        data2 = "E perder a minha realidade lá"
        data3 = "Viajando no calor do seu corpo"
        data4 = "Perder e achar de novo como eu sou e de onde venho "
        data5 = "Quero perder controle, deixar você tocar em mim e fazer música do meu gemido"
        data6 = "Quero que você feche o sol dos meus olhos, deixe eu olhar você "
        data7 = "Quero a sua atenção, sua conquista e a minha rendição"
        data8 = 'Para que ce entre pra onde sou pelado'
        data9 = 'Esperando você'
        data10 = 'Quero a bruxaria pra te virar um animal do jeito eu queira, do jeito ce me mete até quase matar e revitalizar'
        data11 = 'Quero você, seu doce, seu salgado, seu amargo, seu tal'
        data12 = 'Quero que você satisfaça o meu desejo satisfazendo o seu'
        data13 = 'Quero que você feche as portas, apague a luz, para que fiquemos de dois no escuro sentindo nosso calor, cheiro, como nossos corações batem'
        data14 = 'Quero que achemos a luz nos olhos do outro e portas abertas.'

        label1 = Label(root, text=data1, wraplength=300, justify="center")
        label2 = Label(root, text=data2, wraplength=300, justify="center")
        label3 = Label(root, text=data3, wraplength=300, justify="center")
        label4 = Label(root, text=data4, wraplength=300, justify="center")
        label5 = Label(root, text=data5, wraplength=300, justify="center")
        label6 = Label(root, text=data6, wraplength=300, justify="center")
        label7 = Label(root, text=data7, wraplength=300, justify="center")
        label8 = Label(root, text=data8, wraplength=300, justify="center")
        label9 = Label(root, text=data9, wraplength=300, justify="center")
        label10 = Label(root, text=data10, wraplength=300, justify="center")
        label11 = Label(root, text=data11, wraplength=300, justify="center")
        label12 = Label(root, text=data12, wraplength=300, justify="center")
        label13 = Label(root, text=data13, wraplength=300, justify="center")
        label14 = Label(root, text=data14, wraplength=300, justify="center")
        label1.pack()
        label2.pack()
        label3.pack()
        label4.pack()
        label5.pack()
        label6.pack()
        label7.pack()
        label8.pack()
        label9.pack()
        label10.pack()
        label11.pack()
        label12.pack()
        label13.pack()
        label14.pack()

    else:
        res = "Ne não, meu amor! Faz de novo, se quiser desistir, me chama!:P"
        labelQ.configure(text=res)


bttn = Button(question, text="Give me the answer, Rafael!", command=clicked)
bttn.grid(column=0, row=1)

question.mainloop()
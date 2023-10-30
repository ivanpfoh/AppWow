from tkinter import *


raiz = Tk()


myFrame = Frame(raiz, width=800, height=1000)
myFrame.config(bg="#567268")
myFrame.pack()

#-- Formulario --------------------------------------------------------------

cuadroUsuario = Entry(myFrame)
cuadroUsuario.grid(row=0, column=1, padx=3, pady=3)
cuadroUsuario.config(fg="black")

textoUsuario = Label(myFrame, text="Usuario: ")
textoUsuario.grid(row=0, column=0, sticky="w")
textoUsuario.config(bg="#567268")

cuadroContraseña = Entry(myFrame)
cuadroContraseña.grid(row=1, column=1)
cuadroContraseña.config(fg="black")

textocontraseña = Label(myFrame, text="Contraseña: ")
textocontraseña.grid(row=1, column=0, sticky="w")
textocontraseña.config(bg="#567268")

cuadroEmail = Entry(myFrame)
cuadroEmail.grid(row=2, column=1)
cuadroEmail.config(fg="black")

textoEmail = Label(myFrame, text="Email: ")
textoEmail.grid(row=2, column=0, sticky="w")
textoEmail.config(bg="#567268")

cuadroPersonaje = Entry(myFrame)
cuadroPersonaje.grid(row=3, column=1)
cuadroPersonaje.config(fg="black")

textoPersonaje = Label(myFrame, text="Personaje: ")
textoPersonaje.grid(row=3, column=0, sticky="w")
textoPersonaje.config(bg="#567268")

#---------------------------------------------------------------------------------

varOpcion = IntVar()
newframe = Frame(raiz, width=800, height=1000)
newframe.config(bg="#567268")
newframe.pack()

def imprimir():
    print(varOpcion.get())

    if varOpcion.get()==1:
        etiqueta.config(text="ahh! Tienes  buena punteria eh?")
    elif varOpcion.get()==2:
        etiqueta.config(text="Con precisión!")
    elif varOpcion.get()==3:
        etiqueta.config(text="Lok'Tar camarada!")
    elif varOpcion.get()==4:
        etiqueta.config(text="ohh! Espero que este afilada!")
    else:
        etiqueta.config(text="Acaso... eres Hechizero?")




Radiobutton(newframe, text="Arco", variable=varOpcion, value=1, command=imprimir, bg="#567268", width=25, height=1).pack()

Radiobutton(newframe, text="Ballesta", variable=varOpcion, value=2, command=imprimir, bg="#567268").pack()

Radiobutton(newframe, text="Maza", variable=varOpcion, value=3, command=imprimir, bg="#567268").pack()

Radiobutton(newframe, text="Espada", variable=varOpcion, value=4, command=imprimir, bg="#567268").pack()

Radiobutton(newframe, text="Baston", variable=varOpcion, value=5, command=imprimir, bg="#567268").pack()



etiqueta=Label(newframe)
etiqueta.config(bg="#567268")
etiqueta.pack()





#---------------------------------------------------------------------------------

    
Button(newframe, text="Submit").pack()


#---------------------------------------------------------------------------------





raiz.mainloop()
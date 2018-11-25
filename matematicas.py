from tkinter import *
a=1
b=2
c=3
d=4

raiz=Tk()

miframe=Frame(raiz,width=1000,height=500)

miframe.pack()

#------------pantalla----------------

pantalla=Entry(miframe)
#pantallla visual (fila , columna , tamaño , espacio que ocupa por comlumna)
pantalla.grid(row=1,column=1 , padx=10 , pady=10,columnspan=4)
pantalla.config(background="white",fg="#AE4C0A",justify="right")

#-------------fila 1 , columna 1 --------------------
boton7=Button(miframe,text=a,width=3,padx=20 , pady=10)
#pantallla visual(fila , columna )
boton7.grid(row=2 ,column=2)
#-------------fila 1 , columna 2 --------------------
boton8=Button(miframe,text=b,width=3,padx=20 , pady=10)
#pantallla visual(fila , columna )
boton8.grid(row=3 ,column=2)
#-------------fila 2 , columna 1 --------------------
boton9=Button(miframe,text=c,width=3,padx=20 , pady=10)
#pantallla visual(fila , columna )
boton9.grid(row=2 ,column=1)
#-------------fila 2 , columna 2 --------------------
botonMul=Button(miframe,text=d,width=3,padx=20 , pady=10)
#pantallla visual(fila , columna )
botonMul.grid(row=3 ,column=1)




raiz.mainloop()

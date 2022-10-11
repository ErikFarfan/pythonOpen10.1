import tkinter
from tkinter import ttk

window=tkinter.Tk()

def reinicio(event):
    print('reinicio')
    window.quit()
    window.mainloop()

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)
seleccionado=tkinter.StringVar()
r1=ttk.Radiobutton(window,text='si',value=1,variable=seleccionado)
r2=ttk.Radiobutton(window,text='no',value=2,variable=seleccionado)
r3=ttk.Radiobutton(window,text='Quizas',value=3,variable=seleccionado)

r1.grid(column=0,row=1,padx=5,pady=5)
r2.grid(column=0,row=2,padx=5,pady=5)
r3.grid(column=0,row=3,padx=5,pady=5)

r4=tkinter.Button(window,text='Reinicio')
r4.grid(column=1,row=4,padx=5,pady=5)
r4.bind('<Button-1>',reinicio)
window.mainloop()



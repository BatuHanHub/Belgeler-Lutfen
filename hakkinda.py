from tkinter import *

hakkinda = Tk()
hakkinda.geometry('600x600')
hakkinda.title('Belgeler, Lütfen')
hakkinda.configure(bg='#4F4F4F')
hakkinda.resizable(width=False, height=False)

baslikFrame = Frame(hakkinda, bg='#4F4F4F')
yaziFrame = Frame(hakkinda, bg='#4F4F4F')

baslikFrame.place(relx = 0 , rely = 0.1, relheight= 0.2, relwidth= 0.9+0.1)
yaziFrame.place(relx = 0 , rely = 0.3, relheight= 0.5, relwidth= 0.9+0.1)

merhabaYazi = Label(baslikFrame, text='Merhaba Yoldaş!', font='Arial 55 bold', bg='#4F4F4F').pack()
yaziFrame = Label(yaziFrame, text='''Bu oyun Papers,Please oyunun kendimce yapılmış halidir.
Programlanırken Python dili kullanılmıştır. Müzikler Papers,Please oyununa aittir.\n\nGithub:https://github.com/BatuHanHub\nBloğum:https://tatliyazilimci.blogspot.com''', 
font='Arial 12 italic' ,bg='#4F4F4F').pack()

hakkinda.mainloop()
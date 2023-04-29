from tkinter import *
import subprocess
import pygame
import time
import sys

def yenidenDene():
    subprocess.call(['python','acilis.py'])
    time.sleep(3)
    kanal.stop()
    kov.destroy()
    
def masaustuneDon():
    sys.exit()

pygame.init()

sarki2 = pygame.mixer.Sound('kovulma.mp3')

kanal = pygame.mixer.Channel(0)  
pygame.time.delay(500)
kanal.play(sarki2, loops= 1) 

kov = Tk()
kov.attributes('-fullscreen', True)
kov.title('Belgeler, Lütfen')
kov.configure(bg='red')

yenidenDeneButtonFrame = Frame(kov, bg='red')
kovuldunBaslikFrame = Frame(kov, bg='red')
sebepYaziFrame = Frame(kov, bg='red')

yenidenDeneButtonFrame.place(relx= 0.1, rely=0.8,relwidth=0.8, relheight=0.09)
kovuldunBaslikFrame.place(relx= 0, rely=0.1,relwidth=1, relheight=0.3)
sebepYaziFrame.place(relx= 0.05, rely=0.5,relwidth=0.9, relheight=0.2)

kovuldunBaslikYazi = Label(kovuldunBaslikFrame, text='KOVULDUN!', font='arial 80 bold', bg='red', fg='white').pack()
sebepYazi = Label(sebepYaziFrame, text=f'Sizi 3 defa uyardık ama bizi dinlemediğiniz için sizi kovuyoruz. Hayatta başarılar.',
                bg='red', fg='white', font='arial 23 bold italic').pack(side=LEFT)

yenidenDeneButton = Button(yenidenDeneButtonFrame, text='Yeniden dene', font='arial 25 bold', bg='#FF2B2B',
activebackground='#B12828', fg='white', activeforeground='#828282', command=yenidenDene)
yenidenDeneButton.pack(side=LEFT)

masaustuneDonButton = Button(yenidenDeneButtonFrame, text='Masaüstüne dön', font='arial 25 bold', bg='#FF2B2B',
activebackground='#B12828', fg='white', activeforeground='#828282', command=masaustuneDon) 

masaustuneDonButton.pack(side=RIGHT)

kov.mainloop()
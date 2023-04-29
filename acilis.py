from tkinter import *
import subprocess
import time
import pygame

pygame.init()

sarki = pygame.mixer.Sound('baslangic.mp3')

kanal = pygame.mixer.Channel(0)  
pygame.time.delay(500)
kanal.play(sarki, loops=1)  

def baslatOyun():
    kanal.stop()
    subprocess.call(["python","main.py"])
    time.sleep(3)
    acilis.destroy()

def hakkinda():
    subprocess.call(["python","hakkinda.py"])

acilis = Tk()
acilis.title('Belgeler, Lütfen')
acilis.configure(bg='#4F4F4F')
acilis.resizable(height=False, width=False)
acilis.geometry('300x400')

baslatFrame = Frame(acilis, bg='#4F4F4F')
hakkindaFrame = Frame(acilis, bg='#4F4F4F')
surumFrame = Frame(acilis, bg='#4F4F4F')

baslatFrame.place(relx = 0 , rely = 0.4, relheight= 0.2, relwidth= 0.9+0.1)
hakkindaFrame.place(relx = 0 , rely = 0.7, relheight= 0.2, relwidth= 0.9+0.1)
surumFrame.place(relx = 0.3 , rely = 0.9+0.02, relheight= 0.05, relwidth= 0.4)

Button(baslatFrame, text ="Başlat", font='arial 30 bold italic',command=baslatOyun).pack(side=BOTTOM)
Button(hakkindaFrame, text ="Hakkında", font='arial 30 bold italic',command=hakkinda).pack(side=BOTTOM)

Label(surumFrame, text='Ver: Açık Beta', font='bold', bg='#4F4F4F').pack()

acilis.mainloop()
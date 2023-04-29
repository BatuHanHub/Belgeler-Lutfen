from tkinter import *
from tkinter import messagebox # Eğer pasaport konusunda yanlışı olursa uyarı verecek
import pygame as ses # Sesler müzikler
import subprocess
from config import *
import random # Pasaport numarası
import time # Yeni kişi için bekletmek için

uyari = 0
skor = 0            
    
def yenile(): # Pasaport bilgileri yenileniyor...
    # Yolcunun pasaportu
    global adSoyad, adSoyadGercek, pasaportNo, pasaport, pasaportGercek, sicil, sicilGercek, ulke, ulkeGercek, pasaportAdSoyadYazi, pasaportNumarasiYazi, pasaportSicilYazi, pasaportUlkeYazi, gercekPasaportAdSoyadYazi, gercekPasaportNumarasiYazi, gercekPasaportSicilYazi, gercekPasaportUlkeYazi
    
    kisiSecim = random.randint(0,100)
    
    adSoyadSecim = random.randint(0,100)
    
    uzunlukSecim = random.randint(0,100) 
    
    sicilSecim = random.randint(0,100)
    
    ulkeSecim = random.randint(0,100)
    
    # Ad soyad oluşturuluyor {
    if kisiSecim > 50:
        adDegiskeni = random.choice(ad)
        soyadDegiskeni = random.choice(soyad)

        adSoyad = adDegiskeni + " " + soyadDegiskeni
        pass

    elif kisiSecim <= 50:
        adSoyad = random.choice(onemli)
    
    if adSoyadSecim > 20:
        adSoyadGercek = adSoyad
        
    else:
        adDegiskeni = random.choice(ad)
        soyadDegiskeni = random.choice(soyad)

        adSoyadGercek = adDegiskeni + " " + soyadDegiskeni
        pass
    # } 
       
    # Pasaport numarası oluşturuluyor {
    pasaportNo = "".join(random.sample(karakterler, 10))
    if uzunlukSecim > 20:
        pasaport = (f"{pasaportNo[0:5]}-{pasaportNo[5:]}")
    
    else:
        pasaport = (f"{pasaportNo[0:4]}-{pasaportNo[4:]}")

    pasaportGercek = (f"{pasaportNo[0:5]}-{pasaportNo[5:]}")
    
    # }
    
    # Sicil oluşturuluyor {
    sicilGercek = random.choice(siciller)
    if sicilSecim > 30:
        sicil = sicilGercek 
    
    else: 
        sicil = random.choice(siciller)
    
    # }
    
    # Ülke oluşturuluyor {
    ulke = random.choice(ulkeler)
    
    if ulkeSecim > 12:
        ulkeGercek = ulke
        
    else:
        ulkeGercek = random.choice(ulkeler)   
        
    pasaportAdSoyadYazi.configure(text=f'Ad ve Soyad : {adSoyad}')
    pasaportNumarasiYazi.configure(text=f'Pasaport No : {pasaport}')
    pasaportSicilYazi.configure(text=f'Sicil : {sicil}')
    pasaportUlkeYazi.configure(text=f'Ülke : {ulke}')
    
    gercekPasaportAdSoyadYazi.configure(text=f'Ad ve Soyad : {adSoyadGercek}')
    gercekPasaportNumarasiYazi.configure(text=f'Pasaport No : {pasaportGercek}')
    gercekPasaportSicilYazi.configure(text=f'Sicil : {sicilGercek}')
    gercekPasaportUlkeYazi.configure(text=f'Ülke : {ulkeGercek}')  
    # } 

def onay():
    global skor, uyari
    redButton.configure(state='disabled')
    onayButton.configure(state='disabled')
    if adSoyadGercek == adSoyad and pasaportGercek == pasaport and "Temiz" == sicil and ulkeGercek == ulke:
        skor += 5
        skorYazi.configure(text=f'Skor : {skor}')
    else:
        if uyari != 3:
            if adSoyadGercek != adSoyad:
                messagebox.showerror('Uyarı!','Yolcunun adı ve soyadı yanlış!')    
            if pasaportGercek != pasaport:
                messagebox.showerror('Uyarı!','Yolcunun pasaport numarası yanlış!')        
            if "Temiz" != sicilGercek:
                messagebox.showerror('HATA!','Sicil kayıdı kirli yolcu alamazsın!')
            if ulkeGercek != ulke:
                messagebox.showerror('HATA!','Yolcunun geldiği ülke yanlış!')
            uyari += 1
            kovulmakYazi.configure(text=f'Kovulma uyarılarınız : {uyari}')
        else:
            subprocess.call(['python','kovuldu.py'])
            time.sleep(3)
            pencere.destroy()
    time.sleep(2)
    yenile()
    redButton.configure(state='normal')
    onayButton.configure(state='normal')

def red():
    global skor, uyari
    redButton.configure(state='disabled')
    onayButton.configure(state='disabled')
    if adSoyadGercek != adSoyad or pasaportGercek != pasaport or "Temiz değil" == sicil or ulkeGercek != ulke:
        skor += 5
        skorYazi.configure(text=f'Skor : {skor}')
    else:
        if uyari != 3:
            if adSoyadGercek == adSoyad:
                messagebox.showerror('Uyarı!','Yolcunun adı ve soyadı doğru!') 
            if pasaportGercek == pasaport:
                messagebox.showerror('Uyarı!','Yolcunun pasaport numarası doğru!')        
            if "Temiz" == sicilGercek:
                messagebox.showerror('HATA!','Yolcunun sicili temiz!')
            if ulkeGercek == ulke:
                messagebox.showerror('HATA!','Yolcunun geldiği ülke doğru!')
            uyari += 1
            kovulmakYazi.configure(text=f'Kovulma uyarılarınız : {uyari}')
        else:
            subprocess.call(['python','kovuldu.py'])
            time.sleep(3)
            pencere.destroy()
            
    time.sleep(2)
    yenile()
    redButton.configure(state='normal')
    onayButton.configure(state='normal')

pencere = Tk()
pencere.attributes('-fullscreen', True)
pencere.title('Belgeler, Lütfen')

# ===Frameler===
pasaportBilgiFrame = Frame(pencere, bg='#666666')
skorFrame = Frame(pencere)
kaseFrame = Frame(pencere)

pasaportBilgiFrame.place(relx = 0.03 , rely = 0.04, relheight= 0.8, relwidth= 0.3)
skorFrame.place(relx = 0.3+0.04 , rely = 0.04, relheight= 0.2, relwidth= 0.3)
kaseFrame.place(relx = 0.6+0.06 , rely = 0.04, relheight= 0.2, relwidth= 0.3+0.04)
# ======

# ===Pasaport=== 
pasaportBaslikYazi = Label(pasaportBilgiFrame, text='PASAPORT BİLGİLERİ', font='Arial 20 italic', bg='#666666', fg='blue')

pasaportAdSoyadYazi = Label(pasaportBilgiFrame, text=f'Ad ve Soyad : ', font='Arial 15 italic', bg='#666666')
pasaportNumarasiYazi = Label(pasaportBilgiFrame, text=f'Pasaport No : ', font='Arial 15 italic', bg='#666666')
pasaportSicilYazi = Label(pasaportBilgiFrame, text=f'Sicil : ', font='Arial 15 italic', bg='#666666')
pasaportUlkeYazi = Label(pasaportBilgiFrame, text=f'Ülke : ', font='Arial 15 italic', bg='#666666')

pasaportBaslikYazi.pack(side=TOP, anchor=N)

pasaportAdSoyadYazi.place(rely= 0.07)
pasaportNumarasiYazi.place(rely= 0.1+0.03)
pasaportSicilYazi.place(rely= 0.1+0.09)
pasaportUlkeYazi.place(rely= 0.2+0.05)
# ======

# ===Gerçek Pasaport===
gercekPasaportBaslikYazi = Label(pasaportBilgiFrame, text='  GERÇEK PASAPORT BİLGİLERİ', font='Arial 19 italic', fg='#FF1A1A' , bg='#666666')

gercekPasaportAdSoyadYazi = Label(pasaportBilgiFrame, text=f'Ad ve Soyad : ', font='Arial 15 italic', bg='#666666')
gercekPasaportNumarasiYazi = Label(pasaportBilgiFrame, text=f'Pasaport No : ', font='Arial 15 italic', bg='#666666')
gercekPasaportSicilYazi = Label(pasaportBilgiFrame, text=f'Sicil : ', font='Arial 15 italic', bg='#666666')
gercekPasaportUlkeYazi = Label(pasaportBilgiFrame, text=f'Ülke : ', font='Arial 15 italic', bg='#666666')

gercekPasaportBaslikYazi.place(rely=0.5)

gercekPasaportAdSoyadYazi.place(rely= 0.5+0.07)
gercekPasaportNumarasiYazi.place(rely= 0.6+0.03)
gercekPasaportSicilYazi.place(rely= 0.7-0.01)
gercekPasaportUlkeYazi.place(rely= 0.7+0.05)
# ======

# ===Skor===
skorYazi = Label(skorFrame, text=f'Skor : {skor}', font='arial 50 bold')
kovulmakYazi = Label(skorFrame, text=f'Kovulma uyarılarınız : {uyari}', font='arial 25 bold')

skorYazi.pack(side=LEFT, anchor=NW)
kovulmakYazi.place(rely= 0.6)
# ======

# ===Kaşe===
onayButton = Button(kaseFrame, text='ONAY',font = 'arial 50 bold', borderwidth=10, fg='green', bg='LIGHTGREEN', 
                    activeforeground='LIGHTGREEN', activebackground='green', command=onay)

redButton = Button(kaseFrame, text='RED',font = 'arial 50 bold', borderwidth=10, fg='DARKRED', bg='red', 
                    activeforeground='red', activebackground='DARKRED', command=red)

onayButton.pack(side= LEFT)
redButton.pack(side=LEFT)
# ======

yenile()

pencere.mainloop()
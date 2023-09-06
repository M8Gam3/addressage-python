from tkinter import *
fen = Tk()

saisie=StringVar()   #cree la 1 fenetre
fen.geometry("500x400")
fen.title("Décodeur IP")

##___________________________________________________________________________________________________##

IP=saisie.get() # initialise chaque variables et fonctions
Classe=''
Ad_bin=''
Ad_masque=''
Reseau_bin=''
Reseau_dec=''
classe_var=''
Ad_IP=[]
Ad_IP_bin=[]
masque=[]
ad_reseau_bin=[]
classe=''
conv=0


##___________________________________________________________________________________________________##

L60=Label(fen,text='',fg='red', width=39, borderwidth=1)
L60.place(x=110,y=250)

def valider(): #permet de diviser l'adresse ip en 4 et d'appeler les differentes fonctions
    global IP
    global Ad_IP
    global masque

    IP=saisie.get()
    Ad_IP = IP.split(".")
    if len(Ad_IP)==4: #test si l'adresse est bien en IPv4
        test=0
        for i in Ad_IP:
            if int(i)>255: # test si chaque nombre est compris entre 0 et 255
                test=1
                L60.configure(text="les nombres de l'adresse doivent etre entre 0 et 255")
        if test!=1: #active les fonctions si dessous
            L60.configure(text="")
            fonction_classe()
            fonction_ad_bin()
            fonction_reseau_bin()
            fonction_reseau_dec()
    else:
        L60.configure(text="entrez une adresse IPv4")

def fonction_classe():   # permet de selectionnez la classe correspondante a l'adresse ip
    global classe_var
    global masque
    global binaire
    global classe
    classe_var=bin(int(Ad_IP[0]))
    classe_var=classe_var[2:]
    nombre=len(classe_var)
    nombre = 8-int(nombre)
    for i in range(nombre):
        classe_var='0'+classe_var
    e=0
    test_classe=0
    for i in classe_var:
        e+=1
        if e==1:
            if i == '1':
                test_classe+=1
        if e==2:
            if i == '1':
                if test_classe==1:
                    test_classe+=1

    if test_classe==0:
        L7.configure(text="Classe A")
        masque=['11111111','00000000','00000000','00000000']
        classe='A'
        L9.configure(text=masque)
    elif test_classe==1:
        L7.configure(text="Classe B")
        masque=['11111111','11111111','00000000','00000000']
        classe='B'
        L9.configure(text=masque)
    elif test_classe==2:
        L7.configure(text="Classe C")
        masque=['11111111','11111111','11111111','00000000']
        classe='C'
        L9.configure(text=masque)

def fonction_ad_bin(): #permet de rajouter des 0 a chaque nombres en binaires pour qu'ils soient tous sur 8 bits
    global Ad_IP
    global Ad_IP_bin
    global masque
    global binaire
    binaire=[]
    ajout=''
    for i in range(4):
        ajout=''
        ajout=bin(int(Ad_IP[i]))
        ajout=ajout[2:]
        nombre=len(ajout)
        nombre = 8-int(nombre)
        for i in range(nombre):
            ajout='0'+str(ajout)
        Ad_IP_bin.append(ajout)
        binaire.append(ajout)
    L8.configure(text=binaire)

def fonction_reseau_bin():
    global ad_reseau_bin  #permet d'appliquer le masque a l'adresse ip
    global binaire
    global masque
    ad_reseau_bin=[]
    bin=''
    for i in range(4):
        for e in range(8):
            if binaire[i][e] == '1':
                if masque[i][e] =='1':
                    bin+='1'
                else:
                    bin+='0'
            else:
                bin+='0'
        ad_reseau_bin.append(bin)
        bin=''
    L10.configure(text=ad_reseau_bin)

def fonction_reseau_dec(): #permet d'assembler la partie adresse reseau en binaire
    global ad_reseau_bin
    ad_reseau_dec=[]
    for i in range(4):
        ad_reseau_dec.append(str(int(ad_reseau_bin[i],2)))
    adresse_r_d=".".join(ad_reseau_dec)
    L11.configure(text=adresse_r_d)

    B3=Button(fen,text='2nd page',width=15,command=new_page)
    B3.place(x=180,y=220)

##___________________________________________________________________________________________________##

L1=Label(fen,text='Entrez Une Adresse IP:', width=20)  # crée des labels de la premiere page
L1.place(x=25,y=30)
L2=Label(fen,text='Classe:', width=20)
L2.place(x=25,y=60)
L3=Label(fen,text='Adresse Binaire', width=20)
L3.place(x=25,y=90)
L4=Label(fen,text='Adresse Masque', width=20)
L4.place(x=25,y=120)
L5=Label(fen,text='Adresse Réseau Binaire', width=20)
L5.place(x=25,y=150)
L6=Label(fen,text='Adresse Réseau Decimal', width=20)
L6.place(x=25,y=180)

L7=Label(fen,text=Classe,fg='black', width=39, relief="groove", borderwidth=1)
L7.place(x=180,y=60)
L8=Label(fen,text=Ad_bin,fg='black', width=39, relief="groove", borderwidth=1)
L8.place(x=180,y=90)
L9=Label(fen,text=Ad_masque,fg='black', width=39, relief="groove", borderwidth=1)
L9.place(x=180,y=120)
L10=Label(fen,text=Reseau_bin,fg='black', width=39, relief="groove", borderwidth=1)
L10.place(x=180,y=150)
L11=Label(fen,text=Reseau_dec,fg='black', width=39, relief="groove", borderwidth=1)
L11.place(x=180,y=180)

##___________________________________________________________________________________________________##

E=Entry(fen,textvariable=saisie, width=46) # crée entry de la premiere page
E.place(x=180,y=30)

##___________________________________________________________________________________________________##
 #___________________________________________________________________________________________________#
##___________________________________________________________________________________________________##



##___________________________________________________________________________________________________##

def new_page(): # supprime la premiere page et en crée une nouvelle
    global fen
    global saisie1
    global IP
    global masque
    global Ad_IP_bin
    global Ad_IP
    global classe
    IP=saisie.get()
    fen.destroy()
    fen = Tk()
    saisie1=StringVar()

    fen.geometry("1000x900") # inntialise la taille de la fenetre
    fen.title('Sous Réseaux') # nomme la feneter


    def Conversion(): # avec l'adresse ip et la classe. crée le nombre de sous reseaux demander par l'utilisateur
        global classe
        global conv
        e=90
        k=60
        h=0
        for i in range(25):
            k+=30
            L=Label(fen,text='',fg='black',width=39)
            L.place(x=180,y=k)
            L=Label(fen,text='',fg='black',width=39)
            L.place(x=300,y=k)
            L=Label(fen,text='',fg='black',width=13)
            L.place(x=30,y=k)
            L=Label(fen,text='',fg='black',width=39)
            L.place(x=530,y=k)
            L=Label(fen,text='',fg='black',width=39)
            L.place(x=650,y=k)
            L=Label(fen,text='',fg='black',width=13)
            L.place(x=380,y=k)

        if classe=='A':
            Ad_IP[1]=0
            Ad_IP[2]=0
            Ad_IP[3]=0
            L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
            L.place(x=180,y=90)
            x=1
            L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
            L.place(x=30,y=90)
            if 0<int(saisie1.get()) and int(saisie1.get())<3:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1]+127,Ad_IP[2]+255,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                for i in range(int(saisie1.get())-1):
                    e+=30
                    Ad_IP[1]+=128
                    L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=180,y=e)
                    L=Label(fen,text=(Ad_IP[0],Ad_IP[1]+127,Ad_IP[2]+255,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=300,y=e)
                    x+=1
                    L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                    L.place(x=30,y=e)
                    L25.configure(text=('nombre de machines: 8 388 605'),fg='black')
            elif 2<int(saisie1.get()) and int(saisie1.get())<5:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1]+63,Ad_IP[2]+255,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                for i in range(int(saisie1.get())-1):
                    e+=30
                    Ad_IP[1]+=64
                    L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=180,y=e)
                    L=Label(fen,text=(Ad_IP[0],Ad_IP[1]+63,Ad_IP[2]+255,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=300,y=e)
                    x+=1
                    L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                    L.place(x=30,y=e)
                    L25.configure(text=('nombre de machines: 4 194 301'),fg='black')
            elif 4<int(saisie1.get()) and int(saisie1.get())<9:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1]+31,Ad_IP[2]+255,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                for i in range(int(saisie1.get())-1):
                    e+=30
                    Ad_IP[1]+=32
                    L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=180,y=e)
                    L=Label(fen,text=(Ad_IP[0],Ad_IP[1]+31,Ad_IP[2]+255,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=300,y=e)
                    x+=1
                    L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                    L.place(x=30,y=e)
                    L25.configure(text=('nombre de machines: 2 097 152'),fg='black')
            elif 8<int(saisie1.get()) and int(saisie1.get())<17:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1]+15,Ad_IP[2]+255,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                for i in range(int(saisie1.get())-1):
                    e+=30
                    Ad_IP[1]+=16
                    L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=180,y=e)
                    L=Label(fen,text=(Ad_IP[0],Ad_IP[1]+15,Ad_IP[2]+255,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=300,y=e)
                    x+=1
                    L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                    L.place(x=30,y=e)
                    L25.configure(text=('nombre de machines: 1 048 573'),fg='black')
            elif 16<int(saisie1.get()) and int(saisie1.get())<33:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1]+7,Ad_IP[2]+255,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                h=0
                for i in range(int(saisie1.get())-1):
                    if h < 24:
                        h+=1
                        e+=30
                        Ad_IP[1]+=8
                        L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=180,y=e)
                        L=Label(fen,text=(Ad_IP[0],Ad_IP[1]+7,Ad_IP[2]+255,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=300,y=e)
                        x+=1
                        L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                        L.place(x=30,y=e)
                    if h == 24:
                        e=60
                    if h >= 24:
                        h+=1
                        e+=30
                        Ad_IP[1]+=8
                        L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=600,y=e)
                        L=Label(fen,text=(Ad_IP[0],Ad_IP[1]+7,Ad_IP[2]+255,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=720,y=e)
                        x+=1
                        L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                        L.place(x=450,y=e)
                    L25.configure(text=('nombre de machines: 524 285'),fg='black')

            elif 32<int(saisie1.get()) and int(saisie1.get())<51:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1]+3,Ad_IP[2]+255,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                h=0
                for i in range(int(saisie1.get())-2):
                    if h < 24:
                        h+=1
                        e+=30
                        Ad_IP[1]+=4
                        L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=180,y=e)
                        L=Label(fen,text=(Ad_IP[0],Ad_IP[1]+3,Ad_IP[2]+255,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=300,y=e)
                        x+=1
                        L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                        L.place(x=30,y=e)
                    if h == 24:
                        e=60
                    if h >= 24:
                        h+=1
                        e+=30
                        Ad_IP[1]+=4
                        L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=600,y=e)
                        L=Label(fen,text=(Ad_IP[0],Ad_IP[1]+3,Ad_IP[2]+255,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=720,y=e)
                        x+=1
                        L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                        L.place(x=450,y=e)
                L25.configure(text=('nombre de machines: 262 143'),fg='black')

        elif classe=='B':
            Ad_IP[2]=0
            Ad_IP[3]=0
            L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
            L.place(x=180,y=90)
            x=1
            L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
            L.place(x=30,y=90)
            if 0<int(saisie1.get()) and int(saisie1.get())<3:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2]+127,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                for i in range(int(saisie1.get())-1):
                    e+=30
                    Ad_IP[2]+=128
                    L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=180,y=e)
                    L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2]+127,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=300,y=e)
                    x+=1
                    L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                    L.place(x=30,y=e)
                    L25.configure(text=('nombre de machines: 32 765'),fg='black')
            elif 2<int(saisie1.get()) and int(saisie1.get())<5:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2]+63,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                for i in range(int(saisie1.get())-1):
                    e+=30
                    Ad_IP[2]+=64
                    L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=180,y=e)
                    L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2]+63,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=300,y=e)
                    x+=1
                    L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                    L.place(x=30,y=e)
                    L25.configure(text=('nombre de machines: 16 381'),fg='black')
            elif 4<int(saisie1.get()) and int(saisie1.get())<9:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2]+31,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                for i in range(int(saisie1.get())-1):
                    e+=30
                    Ad_IP[2]+=32
                    L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=180,y=e)
                    L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2]+31,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=300,y=e)
                    x+=1
                    L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                    L.place(x=30,y=e)
                    L25.configure(text=('nombre de machines: 8 189'),fg='black')
            elif 8<int(saisie1.get()) and int(saisie1.get())<17:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2]+15,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                for i in range(int(saisie1.get())-1):
                    e+=30
                    Ad_IP[2]+=16
                    L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=180,y=e)
                    L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2]+15,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=300,y=e)
                    x+=1
                    L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                    L.place(x=30,y=e)
                    L25.configure(text=('nombre de machines: 2 045'),fg='black')
            elif 16<int(saisie1.get()) and int(saisie1.get())<33:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2]+7,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                h=0
                for i in range(int(saisie1.get())-1):
                    if h < 24:
                        h+=1
                        e+=30
                        Ad_IP[2]+=8
                        L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=180,y=e)
                        L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2]+7,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=300,y=e)
                        x+=1
                        L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                        L.place(x=30,y=e)
                    if h == 24:
                        e=60
                    if h >= 24:
                        h+=1
                        e+=30
                        Ad_IP[2]+=8
                        L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=600,y=e)
                        L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2]+7,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=720,y=e)
                        x+=1
                        L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                        L.place(x=450,y=e)
                    L25.configure(text=('nombre de machines: 1 023'),fg='black')

            elif 32<int(saisie1.get()) and int(saisie1.get())<51:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2]+3,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                h=0
                for i in range(int(saisie1.get())-2):
                    if h < 24:
                        h+=1
                        e+=30
                        Ad_IP[2]+=4
                        L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=180,y=e)
                        L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2]+3,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=300,y=e)
                        x+=1
                        L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                        L.place(x=30,y=e)
                    if h == 24:
                        e=60
                    if h >= 24:
                        h+=1
                        e+=30
                        Ad_IP[2]+=4
                        L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=600,y=e)
                        L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2]+3,Ad_IP[3]+255),fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=720,y=e)
                        x+=1
                        L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                        L.place(x=450,y=e)
                L25.configure(text=('nombre de machines: 511'),fg='black')

        elif classe=='C':
            Ad_IP[3]=0
            L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
            L.place(x=180,y=90)
            x=1
            L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
            L.place(x=30,y=90)
            if 0<int(saisie1.get()) and int(saisie1.get())<3:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2],Ad_IP[3]+127),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                for i in range(int(saisie1.get())-1):
                    e+=30
                    Ad_IP[3]+=128
                    L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=180,y=e)
                    L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2],Ad_IP[3]+127),fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=300,y=e)
                    x+=1
                    L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                    L.place(x=30,y=e)
                    L25.configure(text=('nombre de machines: 125'),fg='black')
            elif 2<int(saisie1.get()) and int(saisie1.get())<5:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2],Ad_IP[3]+63),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                for i in range(int(saisie1.get())-1):
                    e+=30
                    Ad_IP[3]+=64
                    L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=180,y=e)
                    L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2],Ad_IP[3]+63),fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=300,y=e)
                    x+=1
                    L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                    L.place(x=30,y=e)
                    L25.configure(text=('nombre de machines: 61'),fg='black')
            elif 4<int(saisie1.get()) and int(saisie1.get())<9:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2],Ad_IP[3]+31),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                for i in range(int(saisie1.get())-1):
                    e+=30
                    Ad_IP[3]+=32
                    L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=180,y=e)
                    L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2],Ad_IP[3]+31),fg='black',width=31, relief="groove", borderwidth=1)
                    L.place(x=300,y=e)
                    x+=1
                    L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                    L.place(x=30,y=e)
                    L25.configure(text=('nombre de machines: 29'),fg='black')
            elif 8<int(saisie1.get()) and int(saisie1.get())<17:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2],Ad_IP[3]+15),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                for i in range(int(saisie1.get())-1):
                    e+=30
                    Ad_IP[3]+=16
                    L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=180,y=e)
                    L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2],Ad_IP[3]+15),fg='black',width=19, relief="groove", borderwidth=1)
                    L.place(x=300,y=e)
                    x+=1
                    L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                    L.place(x=30,y=e)
                    L25.configure(text=('nombre de machines: 13'),fg='black')
            elif 16<int(saisie1.get()) and int(saisie1.get())<33:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2],Ad_IP[3]+7),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                h=0
                for i in range(int(saisie1.get())-1):
                    if h < 24:
                        h+=1
                        e+=30
                        Ad_IP[3]+=8
                        L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=180,y=e)
                        L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2],Ad_IP[3]+7),fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=300,y=e)
                        x+=1
                        L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                        L.place(x=30,y=e)
                    if h == 24:
                        e=60
                    if h >= 24:
                        h+=1
                        e+=30
                        Ad_IP[3]+=8
                        L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=600,y=e)
                        L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2],Ad_IP[3]+7),fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=720,y=e)
                        x+=1
                        L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                        L.place(x=450,y=e)
                    L25.configure(text=('nombre de machines: 5'),fg='black')
            elif 32<int(saisie1.get()) and int(saisie1.get())<51:
                L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2],Ad_IP[3]+3),fg='black',width=19, relief="groove", borderwidth=1)
                L.place(x=300,y=e)
                h=0
                for i in range(int(saisie1.get())-2):
                    if h < 24:
                        h+=1
                        e+=30
                        Ad_IP[3]+=4
                        L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=180,y=e)
                        L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2],Ad_IP[3]+3),fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=300,y=e)
                        x+=1
                        L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                        L.place(x=30,y=e)
                    if h == 24:
                        e=60
                    if h >= 24:
                        h+=1
                        e+=30
                        Ad_IP[3]+=4
                        L=Label(fen,text=Ad_IP,fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=600,y=e)
                        L=Label(fen,text=(Ad_IP[0],Ad_IP[1],Ad_IP[2],Ad_IP[3]+3),fg='black',width=19, relief="groove", borderwidth=1)
                        L.place(x=720,y=e)
                        x+=1
                        L=Label(fen,text=('sous réseau ',str(x)),fg='black',width=13, borderwidth=1)
                        L.place(x=450,y=e)
                L25.configure(text=('nombre de machines: 1'),fg='black')


    def verif(): # verifie si le nombre de sous reseaux est compris entre 0 et 20
        global saisie1
        if saisie1.get()!='':
            if int(saisie1.get())>50:
                L25.configure(text='Le nombre de sous reseau doivent etre inferieur a 50',fg='red')
            else:
                L25.configure(text='')
                Conversion()
        else:
            L25.configure(text='renseigner un nombre de sous reseau',fg='red')

    E3=Entry(fen,textvariable=saisie1, width=46)
    E3.place(x=180,y=40)

    L19=Label(fen,text=IP,fg='black',width=39, relief="groove", borderwidth=1)
    L19.place(x=180,y=10)
    L20=Label(fen,text='Entrez Une Adresse IP:', width=20)
    L20.place(x=25,y=10)
    L20=Label(fen,text='Nombre sous réseaux:', width=20)
    L20.place(x=25,y=40)

    L25=Label(fen,fg='red',text='', width=50)
    L25.place(x=100,y=60)

    B2=Button(fen,text='Quitter',width=15,command=fen.destroy)
    B2.place(x=750,y=30)
    B10=Button(fen,text='Conversion',width=15,command=verif)
    B10.place(x=600,y=30)


##___________________________________________________________________________________________________##
 #___________________________________________________________________________________________________#
##___________________________________________________________________________________________________##

B1=Button(fen,text='Valider',width=15,command=valider)
B1.place(x=50,y=220)
B2=Button(fen,text='Quitter',width=15,command=fen.destroy)
B2.place(x=310,y=220)


##___________________________________________________________________________________________________##

E.focus()

fen.mainloop()
print(saisie.get())

##___________________________________________________________________________________________________##

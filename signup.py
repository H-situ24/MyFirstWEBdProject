from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector as sql
win=Tk()
mycon=sql.connect(host="localhost",user="root",password="situ9144",database="situproject1")
mycur=mycon.cursor()
unm=StringVar()
emi=StringVar()
pas=StringVar()
def signup():
    unn=unm.get()
    eml=emi.get()
    paa=pas.get()
    q="insert into login values('{}','{}','{}')".format(unn,eml,paa)
    mycur.execute(q)
    mycon.commit()
    messagebox.showinfo("signup","successfull")

def lgn():
    un=unm.get()
    em=emi.get()
    pa=pas.get()
    q="select * from login where email='{}' and password='{}'".format(em,pa)
    mycur.execute(q)
    mycur.fetchall()
    mycon.commit()
    messagebox.showinfo("login","successfull")

    def newadm():
        import mysql.connector as sql
        winn=Toplevel(win)
        winn.title("student form")
        winn.geometry("500x600")
        winn.resizable(0,0)
        winn.config(background="yellow")
        mycon=sql.connect(host="localhost",user="root",password="situ9144",database="situproject1")
        mycur=mycon.cursor()
        sid=StringVar()
        sn=StringVar()
        sphn=StringVar()
        sc=StringVar()
        sd=StringVar()
        sfee=IntVar()
        def sub():
            i=sid.get()
            n=sn.get()
            p=sphn.get()
            c=sc.get()
            d=sd.get()
            f=sfee.get()
            q="insert into addmissionchart values('{}','{}','{}','{}','{}','{}')".format(i,n,p,c,d,f)
            mycur.execute(q)
            mycon.commit()
            messagebox.showinfo("addmission","successfull")
        l1=Label(winn,text="addmission form",bg="yellow",fg="black",font=("algerian",22,"bold"))
        l1.place(x=130,y=10)
        l2=Label(winn,text="clarity",bg="yellow",fg="red",font=("monotype corsiva",22,"bold"))
        l2.place(x=30,y=70)
        e1=Entry(winn,bg="white",fg="blue",font=("algerian",16,"bold"),bd=5,textvariable=sid)
        e1.place(x=180,y=70)
        l3=Label(winn,text="S_NAME",bg="yellow",fg="red",font=("monotype corsiva",22,"bold"))
        l3.place(x=30,y=130)
        e2=Entry(winn,bg="white",fg="blue",font=("algerian",16,"bold"),bd=5,textvariable=sn)
        e2.place(x=180,y=130)
        l3=Label(winn,text="S_PHONE",bg="yellow",fg="red",font=("monotype corsiva",22,"bold"))
        l3.place(x=30,y=200)
        e2=Entry(winn,bg="white",fg="blue",font=("algerian",16,"bold"),bd=5,textvariable=sphn)
        e2.place(x=180,y=200)
        l4=Label(winn,text="S_COR",bg="yellow",fg="red",font=("monotype corsiva",22,"bold"))
        l4.place(x=30,y=270)
        e3=Entry(winn,bg="white",fg="blue",font=("algerian",16,"bold"),bd=5,textvariable=sc)
        e3.place(x=180,y=270)
        l5=Label(winn,text="S_DUR",bg="yellow",fg="red",font=("monotype corsiva",22,"bold"))
        l5.place(x=30,y=340)
        e4=Entry(winn,bg="white",fg="blue",font=("algerian",16,"bold"),bd=5,textvariable=sd)
        e4.place(x=180,y=340)
        l6=Label(winn,text="S_FEE",bg="yellow",fg="red",font=("monotype corsiva",22,"bold"))
        l6.place(x=30,y=410)
        e5=Entry(winn,bg="white",fg="blue",font=("algerian",16,"bold"),bd=5,textvariable=sfee)
        e5.place(x=180,y=410)
        b1=Button(winn,text="submmit",bg="black",fg="white",font=("algerian",19,"bold"),bd=5,command=sub)
        b1.place(x=30,y=500)
        b1=Button(winn,text="cancel",bg="black",fg="white",font=("algerian",19,"bold"),bd=5)
        b1.place(x=300,y=500)   
    

    def cancel():
        pass

    def updt():
        import mysql.connector as sql
        wind=Toplevel(win)
        wind.title("update profile")
        wind.geometry("500x450")
        wind.resizable(0,0)
        wind.config(background="blue")
        mycon=sql.connect(host="localhost",user="root",password="situ9144",database="situproject1")
        mycur=mycon.cursor()

        
        ph=IntVar()
        idd=StringVar()
        def update():
            pp=ph.get()
            ide=idd.get()
            q="update addmissionchart set sphn='{}' where id='{}'".format(pp,ide)
            mycur.execute(q)
            mycon.commit()
            messagebox.showinfo("update","successfull")

        l1=Label(wind,text="UPDATEINFO",bg="blue",fg="red",font=("algerian",22,"bold"))
        l1.place(x=130,y=10)
        l2=Label(wind,text="SPHN",bg="blue",fg="black",font=("monotype corsiva",22,"bold"))
        l2.place(x=30,y=70)
        e1=Entry(wind,bg="white",fg="blue",font=("algerian",16,"bold"),bd=5,textvariable=ph)
        e1.place(x=180,y=70)
        l3=Label(wind,text="ID",bg="blue",fg="black",font=("monotype corsiva",22,"bold"))
        l3.place(x=30,y=130)
        e2=Entry(wind,bg="white",fg="blue",font=("algerian",16,"bold"),bd=5,textvariable=idd)
        e2.place(x=180,y=135)
        b1=Button(wind,text="update",bg="black",fg="white",font=("algerian",19,"bold"),bd=5,command=update)
        b1.place(x=60,y=250)
    
    def dlte():
        import mysql.connector as sql
        windo=Toplevel(win)
        windo.title("delete somthing")
        windo.geometry("500x450")
        windo.resizable(0,0)
        windo.config(background="green")
        mycon=sql.connect(host="localhost",user="root",password="situ9144",database="situproject1")
        mycur=mycon.cursor()

        l1=Label(windo,text="DELETEINFO",bg="yellow",fg="red",font=("algerian",22,"bold"))
        l1.place(x=130,y=10)
        l2=Label(windo,text="SPHN",bg="green",fg="black",font=("monotype corsiva",22,"bold"))
        l2.place(x=30,y=70)
        e1=Entry(windo,bg="white",fg="blue",font=("algerian",16,"bold"),bd=5,textvariable=sph)
        e1.place(x=180,y=70)
        l3=Label(windo,text="SCOR",bg="green",fg="black",font=("monotype corsiva",22,"bold"))
        l3.place(x=30,y=130)
        e2=Entry(windo,bg="white",fg="blue",font=("algerian",16,"bold"),bd=5,textvariable=sc)
        e2.place(x=180,y=135)
        l4=Label(windo,text="SDUR",bg="green",fg="black",font=("monotype corsiva",22,"bold"),bd=5)
        l4.place(x=30,y=190)
        e3=Entry(windo,bg="white",fg="blue",font=("algerian",16,"bold"),bd=5,textvariable=sd)
        e3.place(x=180,y=205)
        b1=Button(windo,text="delete",bg="black",fg="white",font=("algerian",19,"bold"),bd=5,command=delete)
        b1.place(x=60,y=270)
         
    sph=IntVar()
    sc=StringVar()
    sd=StringVar()
    def delete():
            spp=sph.get()
            scc=sc.get()
            sdd=sd.get()
            q="delete from addmissionchart where sphn='{}' and sc='{}' and sd='{}'".format(spp,scc,sdd)
            mycur.execute(q)
            mycon.commit()
            messagebox.showinfo("delete","successfull")

        
    '''def find():
        awin=Toplevel(win)
        import mysql.connector as sql
        awin.title("delete somthing")
        awin.geometry("500x450")
        awin.resizable(0,0)
        awin.config(background="green")
        mycon=sql.connect(host="localhost",user="root",password="situ9144",database="situproject1")
        mycur=mycon.cursor()

        l1=Label(awin,text="FINDINFO",bg="yellow",fg="red",font=("algerian",22,"bold"))
        l1.place(x=130,y=10)
        l2=Label(awin,text="S__ID",bg="green",fg="black",font=("monotype corsiva",22,"bold"))
        l2.place(x=30,y=70)
        e1=Entry(awin,bg="white",fg="blue",font=("algerian",16,"bold"),bd=5,textvariable=fnd)
        e1.place(x=180,y=70)
        b1=Button(awin,text="search",bg="black",fg="white",font=("algerian",19,"bold"),bd=5,command=search)
        b1.place(x=60,y=200)
        
    fnd=StringVar()
    def search():
        f=fnd.get()
        q="select * from addmissionchart"
        mycur.execute(q)
        messagebox.showinfo("find","successfull")
    mwin=Toplevel(win)
    import mysql.connector as sql
    mwin.title("delete somthing")
    mwin.geometry("500x450")
    mwin.resizable(0,0)
    mwin.config(background="green")
    mycon=sql.connect(host="localhost",user="root",password="situ9144",database="situproject1")
    mycur=mycon.cursor()'''

            
    wind=Toplevel(win)
    wind.title("for addmission")
    wind.geometry("500x400")
    wind.resizable(0,0)
    wind.config(background="pink")
    l1=Label(wind,text="TYPES OF BUTTON FOR USE",bg="pink",fg="darkgreen",font=("monotype corsiva",19,"bold"))
    l1.place(x=80,y=10)
    b1=Button(wind,text="new addmision",bg="black",fg="white",font=("algerian",14,"bold"),bd=5,command=newadm)
    b1.place(x=250,y=70)
    b2=Button(wind,text="update",bg="black",fg="white",font=("algerian",14,"bold"),bd=5,command=updt)
    b2.place(x=250,y=130)
    b3=Button(wind,text="delete",bg="black",fg="white",font=("algerian",14,"bold"),bd=5,command=dlte)
    b3.place(x=250,y=190)
    b4=Button(wind,text="find",bg="black",fg="white",font=("algerian",14,"bold"),bd=5,command=find)
    b4.place(x=250,y=250)
        
    
def fpas():
    e=emi.get()
    p=pas.get()
    q="update login set password='{}' where email='{}'".format(p,e)
    mycur.execute(q)
    mycon.commit()
    messagebox.showinfo("update","successfull")
    
win.title("login")
win.geometry("500x600")
win.resizable(0,0)
win.config(background="black")
image=Image.open("c:\\Users\\Alfa\\Desktop\\hub.png")
imm=image.resize((110,110))
img=ImageTk.PhotoImage(imm)
l1=Label(win,image=img)
l1.pack()
l2=Label(win,text="HUBNET STUDENT MENAGEMENT SYSTEM",bg="black",fg="white",font=("algerin",16,"bold"))
l2.place(x=30,y=120)
l3=Label(win,text="USERNAME",bg="black",fg="green",font=("monotype corsiva",20,"bold"))
l3.place(x=170,y=170)
e1=Entry(win,bg="white",fg="blue",font=("algerian",20,"bold"),bd=5,textvariable=unm)
e1.place(x=100,y=220)
l4=Label(win,text="EMAILID",bg="black",fg="green",font=("monotype corsiva",20,"bold"))
l4.place(x=170,y=270)
e2=Entry(win,bg="white",fg="blue",font=("algerian",20,"bold"),bd=5,textvariable=emi)
e2.place(x=100,y=320)
l5=Label(win,text="PASSWORD",bg="black",fg="green",font=("monotype corsiva",20,"bold"))
l5.place(x=170,y=370)
e3=Entry(win,bg="white",fg="blue",font=("algerian",20,"bold"),bd=5,textvariable=pas)
e3.place(x=100,y=420)
b1=Button(win,text="signup",bg="red",fg="black",font=("algerian",16,"bold"),bd=5,command=signup)
b1.place(x=20,y=520)
b2=Button(win,text="login",bg="red",fg="black",font=("algerian",16,"bold"),bd=5,command=lgn)
b2.place(x=160,y=520)
b3=Button(win,text="Fpassword",bg="red",fg="black",font=("algerian",16,"bold"),bd=5,command=fpas)
b3.place(x=300,y=520)
c1=Checkbutton(win,text="all the term and condition are accepted",bg="black",fg="white",font=("mototype corsiva",12,"bold"))
c1.place(x=90,y=480)

    

win.mainloop()

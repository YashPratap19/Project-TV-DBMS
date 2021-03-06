#=================IMPORTING LIBRARIES=================
import sys
import mysql.connector as con
from tkinter import *
import  clipboard as cp
from functools import partial
from time import strftime
from PIL import Image, ImageTk
#=============================================


#=================DEFINING COLOURS=================
bgcol = 'white'
fgcol='black'
fg='{}'.format(fgcol)
#=============================================


splash= Tk()                                                                    #splash screen window

#=================IMPORTING & RESIZING IMAGES=================
p1 = PhotoImage(file = 'path135.png')
p1 = p1.subsample(10,10)
p2= PhotoImage(file = 'path137.png')
p2= p2.subsample(20,20)

p3 = Image.open('path138.png')
resize_imagepanel = p3.resize((600, 120))
p3=ImageTk.PhotoImage(resize_imagepanel)

p4= PhotoImage(file='path140.png')
p4=p4.subsample(2,2)

bimg=Image.open('cable.png')
resize_imagebg = bimg.resize((600, 598))
bimg = ImageTk.PhotoImage(resize_imagebg)

p6=Image.open("userimg.png")
resize_image1 = p6.resize((70, 60))
p6 = ImageTk.PhotoImage(resize_image1)

p7=Image.open("serviceimg.png")
resize_image2= p7.resize((60, 60))
p7 = ImageTk.PhotoImage(resize_image2)

p8=Image.open("mailimg.png")
resize_image3 =p8.resize((70, 60))
p8 = ImageTk.PhotoImage(resize_image3)

p9=Image.open("adduserimg.png")
resize_image4 =p9.resize((60, 60))
p9 = ImageTk.PhotoImage(resize_image4)

p10=Image.open("addserviceimg.png")
resize_image5 =p10.resize((60, 60))
p10 = ImageTk.PhotoImage(resize_image5)

p13=Image.open("centimg.png")
resize_imagecent =p13.resize((70, 60))
p13 = ImageTk.PhotoImage(resize_imagecent)

p11=Image.open("searchimg.png")
resize_imagep11 = p11.resize((163, 163))
p11=ImageTk.PhotoImage(resize_imagep11)

bckimg=Image.open("backimg.png")
resize_imageback = bckimg.resize((30, 23))
bckimg=ImageTk.PhotoImage(resize_imageback)

delimg=Image.open("delete.png")
resize_imagedel = delimg.resize((50, 50))
delimg=ImageTk.PhotoImage(resize_imagedel)

editimg=Image.open("edit.png")
resize_imageedit = editimg.resize((50, 50))
editimg=ImageTk.PhotoImage(resize_imageedit)

Y132 = PhotoImage(file='32Y1.png')
Y132=Y132.subsample(2,2)

Q155 = PhotoImage(file='Q1.png')
Q155=Q155.subsample(2,2)

Q1Pro55 = PhotoImage(file='Q1Pro.png')
Q1Pro55=Q1Pro55.subsample(2,2)

Y140 = PhotoImage(file='40Y1.png')
Y140=Y140.subsample(2,2)

Y143 = PhotoImage(file='43Y1.png')
Y143=Y143.subsample(2,2)

U155 = PhotoImage(file='55U1.png')
U155=U155.subsample(2,2)

U1S50 = PhotoImage(file='50U1S.png')
U1S50=U1S50.subsample(2,2)

U1S55 = PhotoImage(file='55U1S.png')
U1S55=U1S55.subsample(2,2)

U1S65 = PhotoImage(file='65U1S.png')
U1S65=U1S65.subsample(2,2)

p12= PhotoImage(file='email.png')
#=============================================


#connecting to mySQL
SNo = '0'
mycon = con.connect (host = "localhost", user = "root", passwd = "2371", database = "Project")
cursor = mycon.cursor()
#=============================================


#=================BACK=================
def back():
    window()

def exiting():
    print("Exit")

#FUNCTION 1================================================================
#=================SEARCH WINDOW=================
def database():
    global p1
    search = Toplevel()
    search.geometry("600x500")
    search.configure(bg='{}'.format(bgcol))    
    global SNo
    search.resizable(True, True)

    lbl=Label(search, text="Search User Data", fg='red', bg='{}'.format(bgcol), font=("Arial", 18))
    lbl.pack(side='top')

    searchimg = Label(search, image = p11, bg='white')
    searchimg.pack(side = "top")

    SNo = 100
    SNo_label = Label(search, text = 'Enter Serial No.', font = ('Calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
    SNo_label.place(x=120, y=250)
    
    SNo_entry = Entry (search,textvariable = SNo, font=('calibre',10,'normal'))
    SNo_entry.place(x = 250, y = 250)
    
    sub_btn= Button(search,text = 'Submit', command = lambda: [submit(), lbl.destroy()])
    sub_btn.place(x=500, y=250)

    back_btn = Button(search, image = bckimg, compound="top", command = lambda: [search.withdraw(), back()])
    back_btn.pack(side='bottom')
    
    search.iconphoto(False, p1)
    search.title('Search User Data')

#=================RESULT WINDOW=================
    def submit():
        global SNo
        SNo = int(SNo_entry.get())
        SNo_label.destroy()
        SNo_entry.destroy()
        lbl.destroy()
        searchimg.destroy()
        sub_btn.destroy()
        
        lbl2=Label(search, text="User Data", fg='red', bg='{}'.format(bgcol), font=("Arial", 18))
        lbl2.pack(side='top')
        
        cursor.execute("Select * from Customer where SN = %s", (SNo,))
        data = cursor
        for row in data:
            sn = row[0]
            mod = row[1]
            loc = row[2]
            cont = row[3]
            name = row[4]
            date = row[5]
            channel = row[6]
            act = row[7]

        #=================DISPLAYING DATA=================
        name_lbl = Label(search, text="Name - {}".format(name), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
        name_lbl.place(x=10, y = 40)
        
        mod_lbl = Label(search, text="Model of the OnePlus TV - {}".format(mod), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
        mod_lbl.place(x=10, y = 60)
        
        loc_lbl = Label(search, text="Location - {}".format(loc), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
        loc_lbl.place(x=10, y = 80)
        
        cont_lbl = Label(search, text="Contact Number - {}".format(cont), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
        cont_lbl.place(x=10, y = 100)
        
        date_lbl = Label(search, text="Purchase Date - {}".format(date), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
        date_lbl.place(x=10, y = 120)
        
        channel_lbl = Label(search, text="Purchase Channel - {}".format(channel), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
        channel_lbl.place(x=10, y = 140)
        
        act_lbl = Label(search, text="Number of Active Requests - {}".format(act), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
        act_lbl.place(x=10, y = 160)

        #________________________________________
        if mod =="55Q1":
            imguse=Q155
        if mod =="55Q1 Pro":
            imguse=Q1Pro55
        if mod =="32Y1":
            imguse=Y132
        if mod =="40Y1":
            imguse=Y140
        if mod =="43Y1":
            imguse=Y143
        if mod =="50U1S":
            imguse=U1S50
        if mod =="55U1S":
            imguse=U1S55
        if mod =="65U1S":
            imguse=U1S65
        if mod =="55U1":
            imguse=U155
        #----------------------------------------------------
            
        tv_imglbl = Label(search, image=imguse, bg="white")
        tv_imglbl.place(x=300, y=50)

        edit_bt = Button(search, text = "Edit User Details", image = editimg, compound="top", bg="white", command = lambda: update())
        edit_bt.place(x=10, y=190)

        delete_bt = Button(search, text = "Delete User Data", image = delimg, compound="top", bg="white", command = lambda: delete())
        delete_bt.place(x=150, y=190)

        def delete():
            edit_bt.destroy()
            delete_bt.destroy()
            cursor.execute("Delete from DupCust where SN = %s", (SNo,))
            delete2_bt = Label(search, text = "---- Deleted User Data Successfully ----", bg='{}'.format(bgcol), fg='{}'.format(fgcol), font=("Arial", 14))
            delete2_bt.place(x=150, y=190)
            
            mycon.commit()

        def update():
            print("Updating")

            sn3_label = Label(search, text = 'Enter Serial Number  ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            sn3_label.place(x=10, y=430)

            name3_label = Label(search, text = 'Enter Customer Name  ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            name3_label.place(x=10, y=220)

            Type3_label = Label(search, text = 'Enter TV Model Name ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            Type3_label.place(x=10, y=250)

            loc3_label = Label(search, text = 'Enter Customer Location. ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            loc3_label.place(x=10, y=280)

            CN3_label = Label(search, text = 'Enter Contact No ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            CN3_label.place(x=10, y=310)

            date3_label = Label(search, text = 'Enter Purchase Date', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            date3_label.place(x=10, y=340)

            Channel3_label = Label(search, text = 'Enter TV Purchase Channel  ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            Channel3_label.place(x=10, y=370)

            req3_label = Label(search, text = 'Enter Requests Active  ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            req3_label.place(x=10, y=400)

            #entries

            sn3_entry= Entry(search,font=('calibre',10,'normal') )
            sn3_entry.place(x = 200, y = 430)
            
            name3_entry = Entry (search,font=('calibre',10,'normal') )
            name3_entry.place(x = 200, y = 220)

            Type3_entry = Entry (search,font=('calibre',10,'normal'))
            Type3_entry.place(x = 200, y = 250)

            loc3_entry = Entry (search, font=('calibre',10,'normal'))
            loc3_entry.place(x = 200, y = 280)

            CN3_entry = Entry(search,font=('calibre',10,'normal'))
            CN3_entry.place(x=200, y=310)

            date3_entry = Entry (search, font=('calibre',10,'normal') )
            date3_entry.place(x = 200, y = 340)

            Channel3_entry = Entry(search,font=('calibre',10,'normal'))
            Channel3_entry.place(x=200, y=370)

            req3_entry = Entry(search,font=('calibre',10,'normal'))
            req3_entry.place(x=200, y=400)

            bttn = Button(search, text="Submit Changes", command = lambda: [sub2()])
            bttn.pack(side='bottom') 
            
            def sub2():
                bttn.destroy()
                edit_bt.destroy()
                bttn2 = Label(search, text = 'User Details Changed', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
                bttn2.pack(side = 'bottom')
                
                model = str(Type3_entry.get())
                loc = str(loc3_entry.get())
                CN= int(CN3_entry.get())
                name = str(name3_entry.get())
                date = date3_entry.get()
                channel = str(Channel3_entry.get())
                req = int(req3_entry.get())

                cursor.execute("Update dupcust set Model_Name = {}, Cust_Location = {}, Cust_CN = {}, Cust_Name = {}, Purchase_Date = {}, Purchase_Channel= {}, Requests_Active = {} where SN = {}".format(f'"{model}"', f'"{loc}"', f'"{CN}"', f'"{name}"', f'"{date}"', f'"{channel}"', f'"{req}"', f'"{SNo}"'))
                mycon.commit()
                
                print(SNo, model, loc, CN, name, date, channel, req)
        
                
#FUNCTION 2================================================================
def requests():
      
    request=Toplevel()
    request.title('Requests Manager')
    request.configure(bg='{}'.format(bgcol))
    request.iconphoto(False, p1)
    request.resizable(True, True)
    
    frame = Frame(request, height = 50, width = 400, bg='{}'.format(bgcol))
    
    ttlbl=Label(request, text= "List Of Active Requests", fg='red', font=("Arial", 18), bg='{}'.format(bgcol))
    ttlbl.place(x=150, y=10)

    back_btn = Button(request, image = bckimg, compound="top", command = lambda: [request.withdraw(), back()])
    back_btn.pack(side='bottom')
    
    cursor.execute("Select * from Requests")
    data = cursor.fetchall()

    listbox = Listbox(request, width = 50, height =15, bg='{}'.format(bgcol) , font=("Arial", 14), selectmode=SINGLE, fg='{}'.format(fgcol))
    x=0
    for row in data:
        x=x+1
        Req_ID = row[0]
        Req_Date = row[1]
        Req_Type= row[2]
        Req_Notes = row[3]
        SN = row[4]
        listbox.insert(x, row[0])

    def resolve():
        for i in listbox.curselection():
            x=listbox.get(i)
            cursor.execute("Select * from Requests where Req_ID = %s", (x,))
            data=cursor.fetchall()
            for row in data:
                ID= row[0]
                print(ID)
                label = ID
                idx = listbox.get(0,    END).index(label)
                listbox.delete(idx)
                ted = Toplevel()
                ted.title('Resolved')
                ted.configure(bg='{}'.format(bgcol))
                ted.iconphoto(False, p1)
                ted.geometry("400x100+10+20")
                ted.resizable(True, True)
                ted.overrideredirect(True)
                
                lbldel = Label(ted, text="- Marked Case ID {} as resolved -".format(ID), bg='{}'.format(bgcol), fg='red'.format(fgcol), font=("Arial", 15) )
                lbldel.place(x=15, y=25)
                request.after(2000, ted.destroy)

    #=================RESULT WINDOW=================
    def selected_item():
        select=Toplevel()
        select.title('Request Details')
        select.iconphoto(False, p1)
        frame = Frame(select, height = 400, width = 450, bg='{}'.format(bgcol))
        
        select.resizable(True, True)
        frame.pack()
        date_list = []
        ttlbl.destroy()
        btn.destroy()
        titlb = Label(select, text= "Request Details", fg='red', font=("Arial", 18), bg='{}'.format(bgcol))
        titlb.place(x=150, y=5)
        for i in listbox.curselection():
            x=listbox.get(i)
            cursor.execute("Select * from Requests where Req_ID = %s", (x,))
            data=cursor.fetchall()
            for row in data:
                ID= row[0]
                date= row[1]
                req = row[2]
                comment= row[3]
                ser = row[4]
                date_list.append(ID)
                print(date_list)

            request.destroy()
            
            name_lbl = Label(select, text="ID - {}".format(ID), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            name_lbl.place(x=10, y = 40)

            date_lbl = Label(select, text="Request raised on - {}".format(date), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            date_lbl.place(x=10, y = 60)

            req_lbl = Label(select, text="Type of request - {}".format(req), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            req_lbl.place(x=10, y = 80)

            comm_lbl = Label(select, text="Comments - {}".format(comment), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            comm_lbl.place(x=10, y = 100)

            serv_lbl = Label(select, text="Serial Number - {}".format(ser), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            serv_lbl.place(x=10, y = 120)

            btn1= Button(select, text='Escalate to Customer Support', command= lambda: escalate(), bg='{}'.format(bgcol))
            btn1.place(x=5, y=160)

            back_btn = Button(select, image = bckimg, compound="top", command = lambda: [select.destroy(), back()], fg='{}'.format(fgcol))
            back_btn.pack(side='bottom')

            def escalate():
                btn1.destroy()
                btn2= Label(select, text='Escalated to Customer Support', bg='{}'.format(bgcol))
                btn2.place(x=5, y=160)
                
                print("Escalated to CS")
                cursor.execute("Insert into Priority values ({}, {}, {}, {})".format(f'"{ID}"', f'"{date}"', f'"{req}"', f'"{ser}"'))
                mycon.commit()
            
    btn = Button(request, text='Show Details', command=selected_item)
    btn.place(x=10, y=398)

    btn2 = Button(request, text='Mark As Resolved', command=resolve)
    btn2.place(x=440, y=398)
    
    frame.pack()
    listbox.pack()
    request.mainloop



#FUNCTION 3================================================================
def add():
      
    manual = Toplevel()
    manual.title('Raise a Service Request')
    manual.iconphoto(False, p1)
    frame = Frame(manual, height = 400, width = 450, bg='{}'.format(bgcol))
    frame.pack()

    Req_label = Label(manual, text = 'Enter Request ID. ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
    Req_label.place(x=20, y=50)

    date_label = Label(manual, text = 'Enter Date', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
    date_label.place(x=20, y=80)

    Type_label = Label(manual, text = 'Enter Type of Request ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
    Type_label.place(x=20, y=110)

    note_label = Label(manual, text = 'Enter Request Notes ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
    note_label.place(x=20, y=140)

    SN_label = Label(manual, text = 'Enter Serial No ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
    SN_label.place(x=20, y=170)

    #entries ----
    
    ReqID_entry = Entry (manual, font=('calibre',10,'normal'))
    ReqID_entry.place(x = 200, y = 50)

    date_entry = Entry (manual, font=('calibre',10,'normal') )
    date_entry.place(x = 200, y = 80)

    Type_entry = Entry (manual,font=('calibre',10,'normal'))
    Type_entry.place(x = 200, y = 110)

    note_entry = Entry (manual,font=('calibre',10,'normal') )
    note_entry.place(x = 200, y = 140)

    SN_entry = Entry (manual,font=('calibre',10,'normal'))
    SN_entry.place(x = 200, y = 170)

    btn3 = Button(manual, text="Submit", fg='red', bg='{}'.format(bgcol), command=lambda: sub())
    btn3.place(x=100, y=200)

    back_btn = Button(manual, image = bckimg, compound="top", command = lambda: [manual.withdraw(), back()])
    back_btn.pack(side='bottom')
    
    def sub():
        ID = str(ReqID_entry.get())
        date = date_entry.get()
        Type = str(Type_entry.get())
        note = str(note_entry.get())
        SN = SN_entry.get()

        print(ID, date, Type, note, SN)
        cursor.execute("INSERT INTO DupTest values ({}, {}, {}, {}, {})".format(f'"{ID}"', f'"{date}"', f'"{Type}"', f'"{note}"', f'"{SN}"'))
        mycon.commit()
        
    manual.mainloop
    


#FUNCTION 4================================================================
def cust():
      
    custo = Toplevel()
    custo.title('Manually Add User')
    custo.iconphoto(False, p1)
    frame = Frame(custo, height = 400, width = 450, bg='{}'.format(bgcol))
    frame.pack()

    loc2_label = Label(custo, text = 'Enter Customer Location. ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
    loc2_label.place(x=10, y=50)

    date2_label = Label(custo, text = 'Enter Purchase Date', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
    date2_label.place(x=10, y=80)

    Type2_label = Label(custo, text = 'Enter TV Model Name ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
    Type2_label.place(x=10, y=110)

    name2_label = Label(custo, text = 'Enter Customer Name  ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
    name2_label.place(x=10, y=140)

    SN2_label = Label(custo, text = 'Enter Serial No ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
    SN2_label.place(x=10, y=170)

    Channel2_label = Label(custo, text = 'Enter TV Purchase Channel  ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
    Channel2_label.place(x=10, y=200)

    req2_label = Label(custo, text = 'Enter Requests Active  ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
    req2_label.place(x=10, y=230)

    CN2_label = Label(custo, text = 'Enter Contact No ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
    CN2_label.place(x=10, y=260)

    #entries ----
    
    loc2_entry = Entry (custo, font=('calibre',10,'normal'))
    loc2_entry.place(x = 200, y = 50)

    date2_entry = Entry (custo, font=('calibre',10,'normal') )
    date2_entry.place(x = 200, y = 80)

    Type2_entry = Entry (custo,font=('calibre',10,'normal'))
    Type2_entry.place(x = 200, y = 110)

    name2_entry = Entry (custo,font=('calibre',10,'normal') )
    name2_entry.place(x = 200, y = 140)

    SN2_entry = Entry (custo,font=('calibre',10,'normal'))
    SN2_entry.place(x = 200, y = 170)

    Channel2_entry = Entry(custo,font=('calibre',10,'normal'))
    Channel2_entry.place(x=200, y=200)

    req2_entry = Entry(custo,font=('calibre',10,'normal'))
    req2_entry.place(x=200, y=230)

    CN2_entry = Entry(custo,font=('calibre',10,'normal'))
    CN2_entry.place(x=200, y=260)

    btn3 = Button(custo, text="Submit", fg='red', bg='{}'.format(bgcol), font=("Calibri", 12), command=lambda: sub())
    btn3.place(x=150, y=300)

    back_btn = Button(custo, image = bckimg, compound="top", command = lambda: [custo.withdraw(), back()])
    back_btn.pack(side='bottom')
    
    def sub():
        SN = int(SN2_entry.get())
        model = str(Type2_entry.get())
        loc = str(loc2_entry.get())
        CN= int(CN2_entry.get())
        name = str(name2_entry.get())
        date = date2_entry.get()
        channel = str(Channel2_entry.get())
        req = int(req2_entry.get())

        print(SN, model, loc, CN, name, date, channel, req)

        cursor.execute("INSERT INTO DupCust values ({}, {}, {}, {}, {}, {}, {}, {})".format(f'"{SN}"', f'"{model}"', f'"{loc}"', f'"{CN}"', f'"{name}"', f'"{date}"', f'"{channel}"', f'"{req}"'))
        mycon.commit()
        
    custo.mainloop

#FUNCTION 5================================================================
def mail():
    mailgen = Toplevel()
    mailgen.geometry("600x500")
    mailgen.configure(bg='{}'.format(bgcol))
    mailgen.title('Email Customer')
    mailgen.iconphoto(False, p1)
    titlbl= Label(mailgen, text='Email Generator and Sender', font=('arial', 15), bg='{}'.format(bgcol))
    titlbl.pack(side='top')
    
    snowlbl = Label(mailgen, text = 'Enter Serial No.', font = ('calibre',10,'bold'), bg='{}'.format(bgcol))
    snowlbl.place(x=20, y=300)

    titimg=Label(mailgen, image=p12, bg='white')
    titimg.pack(side='top')
    sno='1'
    snowent = Entry (mailgen,textvariable = sno, font=('calibre',10,'normal'))
    snowent.place(x = 200, y = 300)

    sub_btn= Button(mailgen,text = 'Submit', command = lambda: [gen()])
    sub_btn.place(x=50, y=330)

    def gen():
        sno = int(snowent.get())
        cursor.execute("Select * from Customer where SN = %s", (sno,))
        data = cursor
        for row in data:
            sn = row[0]
            mod = row[1]
            loc = row[2]
            cont = row[3]
            name = row[4]
            date = row[5]
            channel = row[6]
            act = row[7]

            mail1 = ('''Hey {},
Hope your {} meets all your expectations and enhances your entertainment experience.
Please rate delivery by our e-commerce partner {}, and let us know if you need help, or are facing any issues with your device.

Your satisfaction is our top priority and we are always reachable via official  support channels

Our service centres in {} will respond to any request regarding installation or repair services.

Thank you, looking forward to your feedback!'''.format(name, mod, channel, loc))

            sub_btn.destroy()
            snowent.destroy()
            titimg.destroy()
            snowlbl.destroy()
            msg = Message( mailgen, text = "{}".format(mail1), font=('calibre',11,'normal'))
            msg.place(x=50, y=120)
            snowlbl2 = Label(mailgen, text = 'Email Text Generated.', font = ('calibre',10,'bold'), bg='{}'.format(bgcol))
            snowlbl2.place(x=20, y=100)
            copbut = Button(mailgen,text = ' Copy ', command = lambda: [cop()])
            copbut.place(x=50, y=400)
            back_btn = Button(mailgen,  image = bckimg, compound="top", command = lambda: [mailgen.destroy(), back()], fg='{}'.format(fgcol))
            back_btn.pack(side='bottom')
            def cop():
                cp.copy(mail1)
                copbut.destroy()
                coptxt = Label(mailgen,text = ' Copied ', font = ('calibre',10,'bold'), bg='{}'.format(bgcol))
                coptxt.place(x=50, y=400)
    mailgen.mainloop()

#FUNCTION 6================================================================
def centre():
      
    centre=Toplevel()
    centre.title('Centre Manager')
    centre.configure(bg='{}'.format(bgcol))
    centre.iconphoto(False, p1)
    centre.resizable(True, True)
    
    frame = Frame(centre, height = 50, width = 400, bg='{}'.format(bgcol))
    
    ttlbl=Label(centre, text= "List Of Active Centres", fg='red', font=("Arial", 18), bg='{}'.format(bgcol))
    ttlbl.place(x=150, y=10)

    back_btn = Button(centre,  image = bckimg, compound="top", command = lambda: [centre.withdraw()])
    back_btn.pack(side='bottom')
    
    cursor.execute("Select * from centre")
    data = cursor.fetchall()

    listbox = Listbox(centre, width = 50, height =15, bg='{}'.format(bgcol) , font=("Arial", 14), selectmode=SINGLE, fg='{}'.format(fgcol))
    x=0
    for row in data:
        x=x+1
        Cent_Name = row[0]
        Cent_Loc = row[1]
        Cent_ID= row[2]
        listbox.insert(x, row[0])

    #=================RESULT WINDOW=================
    def selected_item():
        select=Toplevel()
        select.title('centre Details')
        select.iconphoto(False, p1)
        frame = Frame(select, height = 400, width = 450, bg='{}'.format(bgcol))
        select.resizable(True, True)
        frame.pack()
        date_list = []
        ttlbl.destroy()
        btn.destroy()
        titlb = Label(select, text= "Centre Details", fg='red', font=("Arial", 18), bg='{}'.format(bgcol))
        titlb.place(x=150, y=5)
        for i in listbox.curselection():
            x=listbox.get(i)
            cursor.execute("Select * from centre where Name = %s", (x,))
            data=cursor.fetchall()
            for row in data:
                Name= row[0]
                Loc= row[1]
                ID = row[2]
                date_list.append(ID)
                print(date_list)

            centre.destroy()

            date_lbl = Label(select, text="Centre Name - {}".format(Name), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            date_lbl.place(x=10, y = 60)

            req_lbl = Label(select, text="Centre Location - {}".format(Loc), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            req_lbl.place(x=10, y = 80)

            name_lbl = Label(select, text="ID - {}".format(ID), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
            name_lbl.place(x=10, y = 40)

            btn1= Button(select, text='Mark Centre as Non-Operational', command= lambda: [nonop()], bg='{}'.format(bgcol))
            btn1.place(x=5, y=120)

            btn2=Button(select, text='Check Available Technicians', command= lambda: techie(), bg='{}'.format(bgcol))
            btn2.place(x=200, y=120)

            back_btn = Button(select,  image = bckimg, compound="top", command = lambda: [select.destroy(), back()], fg='{}'.format(fgcol))
            back_btn.pack(side='bottom')

            def nonop():
                btn1.destroy()
                btn2= Label(select, text='Marked Centre as Non-Operational', bg='{}'.format(bgcol))
                btn2.place(x=5, y=160)
                cursor.execute("Insert into non_func_cent values ({}, {}, {})".format(f'"{Name}"', f'"{Loc}"', f'"{ID}"'))
                mycon.commit()

            def techie():
                 btn1.destroy()
                 btn2.destroy()
                 cursor.execute("Select * from technic where Tx_Centre=%s",(ID,))
                 data = cursor.fetchall()
                 names=[]
                 ids=[]
                 for row in data:
                     Tech_ID= row[0]
                     Name= row[1]
                     names.append(Name)
                     ids.append(Tech_ID)

                 hete=Label(select, text="Available Technicians", bg='{}'.format(bgcol), fg='red', font=("Arial", 13))
                 hete.place(x=10, y = 120)
                 
                 tx_name_lbl = Label(select, text="Technician ID - {}".format(ids[0]), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
                 tx_name_lbl.place(x=10, y = 150)

                 tx_id_lbl = Label(select, text="Technician Name - {}".format(names[0]), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
                 tx_id_lbl.place(x=10, y = 170)

                 tx_name2_lbl = Label(select, text="Technician ID - {}".format(ids[1]), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
                 tx_name2_lbl.place(x=10, y = 200)

                 tx_id2_lbl = Label(select, text="Technician Name - {}".format(names[1]), bg='{}'.format(bgcol), fg='{}'.format(fgcol))
                 tx_id2_lbl.place(x=10, y = 220)

    btn = Button(centre, text='Show Details', command=selected_item)
    btn.place(x=10, y=398)

    frame.pack()
    listbox.pack()
    centre.mainloop

#=================START WINDOW=================
def login():
    splash.withdraw()
    tkWindow = Toplevel()
    tkWindow.iconphoto(False, p1)
    
    p5= PhotoImage(file='path141.png')
    
    def validateLogin(username, password):
        userID=[]
        passWd=[]
        data=cursor.execute("SELECT * FROM Profile")
        data=cursor.fetchall()
        usnm= username.get()
        pswd = password.get()
        for row in data:
            userid=row[0]
            name=row[1]
            passw=row[2]
            userID.append(userid)
            passWd.append(passw)
        tkWindow.withdraw()
        if usnm in userID:
            if pswd in passWd:
                window()
                
            else:
                print("Password wrong")#SHIFT TO TKINTER
        else:
            print("Try Again")#SHIFT TO TKINTER

    global usnm

    imgg= Label(tkWindow, image = p5, bg='black')
    imgg.place(x=0,y=0)
    
    btmlbl=Label(tkWindow, text="Made by Yash Pratap Singh | Logos are property of OnePlus VI ??? 2021", bg='black', fg='white', font=('Helvetica', 9))
    btmlbl.pack(side='bottom')
    
    tkWindow.geometry('500x500')
    tkWindow.configure(bg='black')
    tkWindow.title('Login Form')

    usernameLabel = Label(tkWindow, text="User Name", font=("Arial", 15),bg='black', fg='white' )
    usernameLabel.place(x=100, y=300)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username)
    usernameEntry.place(x=250, y=307)

    passwordLabel = Label(tkWindow,text="Password", font=("Arial", 15),bg='black', fg='white' )
    passwordLabel.place(x=100, y=340)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*')
    passwordEntry.place(x=250, y=347)

    validateLogin = partial(validateLogin, username, password)
    loginButton = Button(tkWindow, text="   Login   ", font=("Arial", 12) , command=validateLogin)
    loginButton.place(x=200, y=390)

    tkWindow.mainloop()

    
log = Label(splash, image = p1, bg='black')
log.place(x=170, y=40)
splash.configure(bg='black')
splash_lbl=Label(splash, text="Starting...", fg='red', bg='black'.format(bgcol), font=("Arial", 18))
splash_lbl.place(x=150, y=130)
splash.geometry("400x200+120+50")
splash.overrideredirect(True)

usnm='demo'
def window():
    global usnm
    window=Toplevel()
    bglbl=Label(window, image=bimg, bg='white')
    bglbl.place(x=0,y=5)
    panel = Label(window, image = p3, bg='white')
    panel.pack(side = "bottom")
    background_label = Label(window, image=p4, bg='white')
    background_label.pack(side = 'bottom')

    def time():
        string = strftime('%H:%M:%S %p')
        lbltm.config(text = string)
        lbltm.after(1000, time)
     
    lbltm = Label(window, font = ('calibri', 11), fg='black', bg='{}'.format(bgcol))
     
    lbltm.place(x=520, y=15)
    time()
    lblgreet = Label(window,  text="Welcome, {}".format(usnm), fg='black', bg='#F07E89'.format(bgcol))
    lblgreet.place(x=1,y=15)
    lbl=Label(window, text="OnePlus TV Database System", fg='red', bg='{}'.format(bgcol), font=("Arial", 16))
    lbl.pack(side='top')
    
    btn=Button(window, text="        Check User Data         ", fg='red', bg='{}'.format(bgcol), image = p6, compound="top",  command= lambda: [window.withdraw()  , database()])
    btn.place(x=60, y=100)

    btn2=Button(window, text="      Check Active Requests      ", fg='red', bg='{}'.format(bgcol), image = p7, compound="top", command= lambda: [window.withdraw()  ,requests()])
    btn2.place(x=350, y=100)

    btn3 = Button(window, text="      Manually Raise Request    ", fg='red', bg='{}'.format(bgcol), image = p10, compound="top", command=  lambda: [window.withdraw()  ,add()])
    btn3.place(x=350, y=200)

    btn4 = Button(window, text="      Manually Add User      ", fg='red', bg='{}'.format(bgcol), image = p9, compound="top", command=  lambda: [window.withdraw()  ,cust()])
    btn4.place(x=60, y=200)

    btn5= Button(window, text="        E-Mail Generator        ", fg='red', bg='{}'.format(bgcol), image = p8, compound="top", command=  lambda: [window.withdraw()  ,mail()])
    btn5.place(x=60, y=300)

    btn6= Button(window, text="          Service Centre Info         ", fg='red', bg='{}'.format(bgcol), image = p13, compound="top", command=  lambda: [window.withdraw()  ,centre()])
    btn6.place(x=350, y=300)

    exbut=Button(window, text="Exit", fg='red', bg='{}'.format(bgcol), command=lambda: [window.withdraw(), exiting()])
    #PLACE EXIT BUTTON
    
    window.title('TV Database Management System')
    window.iconphoto(False, p1)

    window.geometry("620x600")
    window.configure(bg='{}'.format(bgcol))
    window.mainloop()

splash.after(2000,  login)
splash.mainloop()

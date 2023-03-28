from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import scrolledtext
import tkinter
import DataStructureFile as DSfile
disttotal=DSfile.totaldist()


def PrintOrder():
    screen1 = Toplevel(root)
    screen1.title("Traversal Details")
    screen1.geometry("1920x1080+0+0")
    screen1["background"]="light blue"
    # lbd1 = Label(screen1, text="NAME", background='black', fg='White', font=("Times New Roman", 16, 'bold'))
    # lbd1.place(x="240", y="120")
    # myFrame = Frame(screen1).place(x=50, y=100)
    # for i in li11:
    #     Label(myFrame, text="● " + i).pack()  # you can use a bullet point emoji.
    ts1 = Label(screen1,text="Optimal order to visit the shops",font=("Times New Roman",25, 'bold'))
    ts1.configure(foreground="blue")
    ts1.place(x="70",y="14")
    ShopBox=Listbox(screen1,width=30, height=10,font=6)
    ShopBox.place(x="170",y="90")
    for shops in li11:
        ShopBox.insert(END,shops)
    ts2 = Label(screen1, text="Distance between Each shop", font=("Times New Roman", 25, 'bold'))
    ts2.configure(foreground="blue")
    ts2.place(x="630", y="14")
    DistBox = Listbox(screen1,width=30, height=10,font=6)
    DistBox.place(x="650", y="90")
    print(li22)
    for dist in li22:
        DistBox.insert(END,"%s :    %s"%(dist,li22[dist]))
    disttotal = DSfile.totaldist()
    labeler=Label(screen1,text=f"The Total Distance to Travel :  {disttotal}",font="19")
    labeler.configure(foreground="blue")
    labeler.place(x="150",y="400")









def GetShops():
    global li11,li22
    CompleteList =text_area.get(1.0,END)
    # CompleteList=text_area.get(1.0, "end-1c")
    # print("complete")
    # print(CompleteList)
    # print("ctext")
    # print(Ctext)
    print(CompleteList)
    print(CompleteList[0])
    if (CompleteList == "\n"):
        messagebox.showerror("Error", "Shopping list is empty")
        return

    s =CompleteList.upper()
    print(s)
    li2 = []
    s1 = ""
    for i in range(len(s) - 1):
        if (i == 0):
            while (s[i] != '\n' and i<len(s)-1):
                s1 = s1 + s[i]
                i = i + 1
            li2.append(s1)
        s1 = ""
        if (i<len(s)-1 and s[i] == '\n'):
            i = i + 1
            s1 = s[i]
            i = i + 1
            while (s[i] != '\n'):
                s1 = s1 + s[i]
                i = i + 1
            li2.append(s1)
    if(len(li2)>1):
        li2.pop(1)

    for i in range(len(li2)):
        if(li2.count(li2[i])>1):
            messagebox.showerror("Error",f"{li2[i]} is repeated")
            return''
        elif(DSfile.Mall.count(li2[i])==0):
            messagebox.showerror("Error", f"Currently {li2[i]} is not available in the mall")
            return ''

    li11=DSfile.FirstOrder(li2)
    li22=DSfile.OrderWithDistance()
    PrintOrder()


def main_screen():
    global root,Et1,Et2,imgg3,labeler,text_area
    root=Tk()
    root.title("Mall")
    root.geometry("1920x1080+0+0")

    frame = Frame(root, width=100, height=100)
    frame.pack()
    frame.place(anchor='center', relx=0.25, rely=0.55)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("mallmap.png"))
    # larger_image = img.zoom(2, 2)  # create a new image twice as large as the original
    # smaller_image = img.subsample(2, 2)
    # Create a Label Widget to display the text or Image
    label = Label(frame, image=img)
    label.pack()




    # image1 = Image.open(r"C:\Users\mithr\PycharmProjects\pythonProject3\ADSProjectSem-4\mallmap.png")
    # image1 = image1.resize((50, 50), Image.ANTIALIAS)




    # imgg2=ImageTk.PhotoImage(Image.open(r"C:\Users\mithr\PycharmProjects\pythonProject3\TkinterProject\img1Project.png"))
    # mylabel1=Label(root,image=imgg2)
    # imgg3 = ImageTk.PhotoImage(Image.open(r"C:\Users\mithr\PycharmProjects\pythonProject3\TkinterProject\img2Project.png"))
    # mylabel1.place(x=0,y=0,relwidth=1,relheight=1)
    title=Label(text="WELCOME TO MALL",width="600",bg='white',height="2",background='Black',fg='White',font=("Times New Roman",36,'bold'))
    title.pack()
    title2= Label(text="Map of the mall",font=("Times New Roman", 26, 'bold'))
    title2.place(x="180",y="140")
    title3 = Label(text="Enter the shops/Places to visit",font=("Times New Roman",24, 'bold'))
    title3.place(x="660",y="200")
    # imgg2=ImageTk.PhotoImage(
    #         Image.open(r"C:\Users\mithr\PycharmProjects\pythonProject3\ADSProjectSem-4\mallmap.png"))
    # mylabel1 = Label(root, image=imgg2)
    text_area =Text(root,height=10,width=40,font=10)


    text_area.place(x="690",y="260")
    # text_area = scrolledtext.ScrolledText(root, wrap=tkinter.WORD,
    #                                       width=40, height=8,
    #                                       font=("Times New Roman", 15))
    #
    # text_area.place(x="300",y="200")

    # placing cursor in text area
    # text_area.focus()
    # #
    # # # text_area = Text(root, wrap=WORD, width=40, height=8, font=("Times New Roman", 15))
    # # # # text_area.grid(column=0, row=2, pady=10, padx=45)
    # # # text_area.place(x=200, y=350)
    # # # text_area.focus()
    # labeler = Label(root, text='')
    # labeler.place(x="300", y="200")
    def clear():
        text_area.delete("1.0","end")
    Bt1=Button(text="FIND THE ROUTE",bg="#808080",fg="black",command=GetShops,width=13,height=2)
    Bt1.place(x="780",y="520")
    Bt2 = Button(text="CLEAR", bg="#808080", fg="black", command=clear, width=13, height=2)
    Bt2.place(x="920", y="520")

    root.mainloop()
# db = DataBase("DataDb.db")
main_screen()
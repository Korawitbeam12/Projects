import customtkinter
from tkinter import *
from tkinter import messagebox
from subprocess import call

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.title("Multi-Calculator")
app.geometry("400x430")
app.resizable(0,0)


font1 = ('Arial',20,'bold')

i = 0
equation=""

#Tabview
tabView = customtkinter.CTkTabview(app,
                                   width=500,height=800)
tabView.pack(padx=20,pady=10)

#create Tabs
tabView.add("Calculator")
tabView.add("Grade")
tabView.add("Currency Changer")


#set Deafult Windows when start
tabView.set("Calculator")

#--------------------------------------------

def open_py_file():
    call(["Grade_Calculator.exe"])

#--------------------------------------------
def button_func1():
    print("but 1 pressed")

def button_func2():
    print("but 2 pressed")

def button_func3():
    print("but 3 pressed")

def about_win():
    messagebox.showinfo("About","*This Program is as a Project* \n Made By M.5/5 SWK Student:\n Korawit Wongkhamlue (นายกรวิชญ์ วงศ์คำลือ) No.10 \n Tharathep Boonmak (ธราเทพ บุญมาก) No.14\n Jirapat Kaewprom (จิรพัฒน์ แก้วพรม) No.18 \n Teerawat Kaewthipnet (ธีรวัชร เเก้วทิพเนตร) No.19 \n Nitipoom Sannork (นิติภูมิ แสนนอก) No.21 \n Setvisut Sornjareankul (เศรษฐวิสุทธิ์ สอนเจริญกุล) No.23")


#Calculator Functions-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def show(value):
    global i
    global equation
    if(value=="%"):
        value="/100"
    equation+=value
    result_entry.insert(i,value)
    i = i+1

def clear():
    global equation
    result_entry.delete(0,END)
    equation=""

def calculate():
    try:
        global equation
        result=""
        result = eval(equation)
        clear()
        result_entry.insert(0,result)
    except:
        messagebox.showerror(title="Error",message="Please enter a valid number")

result_entry = customtkinter.CTkEntry(tabView.tab("Calculator"),placeholder_text=" ",
                                      fg_color = "black",width=235,height=40)
result_entry.place(x=58,y=10)

Button1 = customtkinter.CTkButton(tabView.tab("Calculator"),command=clear,text="C",font=font1,width=50,height=50,fg_color="orange",text_color="black")
Button1.place(x=60,y=60)
Button2 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("%"),text="%",font=font1,width=50,height=50,fg_color="orange",text_color="black")
Button2.place(x=120,y=60)

Button3 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("/"),text="/",font=font1,width=50,height=50,fg_color="orange",text_color="black")
Button3.place(x=180,y=60)

Button4 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("*"),text="x",font=font1,width=50,height=50,fg_color="orange",text_color="black")
Button4.place(x=240,y=60)

Button5 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("7"),text="7",font=font1,width=50,height=50,fg_color="#4F4C45")
Button5.place(x=60,y=120)

Button6 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("8"),text="8",font=font1,width=50,height=50,fg_color="#4F4C45")
Button6.place(x=120,y=120)

Button7 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("9"),text="9",font=font1,width=50,height=50,fg_color="#4F4C45")
Button7.place(x=180,y=120)

Button8 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("-"),text="-",font=font1,width=50,height=50,fg_color="orange")
Button8.place(x=240,y=120)

Button9 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("4"),text="4",font=font1,width=50,height=50,fg_color="#4F4C45")
Button9.place(x=60,y=180)

Button10 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("5"),text="5",font=font1,width=50,height=50,fg_color="#4F4C45")
Button10.place(x=120,y=180)

Button11 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("6"),text="6",font=font1,width=50,height=50,fg_color="#4F4C45")
Button11.place(x=180,y=180)

Button12 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("+"),text="+",font=font1,width=50,height=110,fg_color="orange")
Button12.place(x=240,y=180)

Button13 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("1"),text="1",font=font1,width=50,height=50,fg_color="#4F4C45")
Button13.place(x=60,y=240)

Button14 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("2"),text="2",font=font1,width=50,height=50,fg_color="#4F4C45")
Button14.place(x=120,y=240)

Button15 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("3"),text="3",font=font1,width=50,height=50,fg_color="#4F4C45")
Button15.place(x=180,y=240)

Button16 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("0"),text="0",font=font1,width=50,height=50,fg_color="#4F4C45")
Button16.place(x=60,y=300)

Button17 = customtkinter.CTkButton(tabView.tab("Calculator"),command=lambda:show("."),text=".",font=font1,width=50,height=50,fg_color="#4F4C45")
Button17.place(x=120,y=300)

Button18 = customtkinter.CTkButton(tabView.tab("Calculator"),command=calculate,text="=",font=font1,width=115,height=50,fg_color="orange")
Button18.place(x=175,y=300)

#Currency Changer-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

money = IntVar()

#input
label1 = customtkinter.CTkLabel(tabView.tab("Currency Changer"),text="Amount (THB): ",font=font1)
label1.place(x=0,y=50)
label3 = customtkinter.CTkLabel(tabView.tab("Currency Changer"),text = "(The price is based on 11/02/2024)",font =("font1",11),text_color="#FF4848")
label3.place(x=85,y=230)

entry1 = customtkinter.CTkEntry(tabView.tab("Currency Changer"),font=font1,width=100,textvariable=money)
entry1.place(x=150,y=50)

#input currency choice
curr = customtkinter.StringVar(value="Choose currency")
label2 = customtkinter.CTkLabel(tabView.tab("Currency Changer"),text="Currency: ",font=font1)
label2.place(x=46,y=90)
combo = customtkinter.CTkComboBox(tabView.tab("Currency Changer"),values=["EUR","JPY","USD","GBP"],variable=curr)
#combobox = CTkComboBox(app,values=["EUR","JPY"])
combo.place(x=150,y=90)

#Output
outputLabel = customtkinter.CTkLabel(tabView.tab("Currency Changer"),text="Result: ",font=font1)
outputLabel.place(x=73,y=130)
et2=Entry(tabView.tab("Currency Changer"),font=font1,width=10)
et2.place(x=150,y=130)


def calculate_cur():
    amount = money.get()
    currency = (curr.get())

    if currency == "EUR":
        et2.delete(0,END)
        result = ((amount*0.026),"EUR")
        et2.insert(0,result)
    elif currency == "JPY":
        et2.delete(0,END)
        result = ((amount*4.16),"JPY")
        et2.insert(0,result)
    elif currency == "USD":
        et2.delete(0,END)
        result = ((amount*0.028),"USD")
        et2.insert(0,result)
    elif currency == "GBP":
        et2.delete(0,END)
        result = ((amount*0.022),"GBP")
        et2.insert(0,result)
    else:
        et2.delete(0,END)
        result = "Error"
        et2.insert(0,result)


def deletetext():
        entry1.delete(0,END)
        et2.delete(0,END)

btn1 = customtkinter.CTkButton(tabView.tab("Currency Changer"),text="Convert",font=font1,command=calculate_cur)
btn1.place(x=70,y=190)
btn2 = customtkinter.CTkButton(tabView.tab("Currency Changer"),text="Clear",font=font1,width=40,fg_color="#FF5F5F",command=deletetext)
btn2.place(x=220,y=190)

#-------------------------------------------------------------------------------------------------------------------------------------------------
btn3 = customtkinter.CTkButton(tabView.tab("Grade"),text="Launch Grade Calculator",font=font1,command=open_py_file)
btn3.place(x=50,y=100)
btn4 = customtkinter.CTkButton(app,text="About",font=("font1",12),width=23,height=5,command=about_win,fg_color="green")
btn4.place(x=320,y=23)
app.mainloop()
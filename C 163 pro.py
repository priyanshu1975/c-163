from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("fever ")
root.minsize(600, 600)
root.maxsize(600, 600)
root.configure(bg="gray")

radio1=StringVar(value="0")
lab_1=Label(root,text="do you experience shortness of breath during routine activities ? ")
lab_1.pack()
radio1_yes=Radiobutton(root,text="yes",variable=radio1,value="yes")
radio1_yes.pack()
radio1_no=Radiobutton(root,text="no",variable=radio1,value="no")
radio1_no.pack()



radio2=StringVar(value="0")
lab_2=Label(root,text="do you swelling in feel / ankles /legs (shoes feel tighter )or abdomen ? ")
lab_2.pack()
radio2_yes=Radiobutton(root,text="yes",variable=radio2,value="yes")
radio2_yes.pack()
radio2_no=Radiobutton(root,text="no",variable=radio2,value="no")
radio2_no.pack()



radio3=StringVar(value="0")
lab_3=Label(root,text="do you feel any of these symptoms-confusion , disorientation or loss of memory ? ")
lab_3.pack()
radio3_yes=Radiobutton(root,text="yes",variable=radio3,value="yes")
radio3_yes.pack()
radio3_no=Radiobutton(root,text="no",variable=radio3,value="no")
radio3_no.pack()



radio4=StringVar(value="0")
lab_4=Label(root,text="do you experience shortness of breath while at rest/lying down ? ")
lab_4.pack()
radio4_yes=Radiobutton(root,text="yes",variable=radio4,value="yes")
radio4_yes.pack()
radio4_no=Radiobutton(root,text="no",variable=radio4,value="no")
radio4_no.pack()



radio5=StringVar(value="0")
lab_5=Label(root,text="do you experience persistent wheezing / coughing that produce white or pink blood tinged mucus ? ")
lab_5.pack()
radio5_yes=Radiobutton(root,text="yes",variable=radio5,value="yes")
radio5_yes.pack()
radio5_no=Radiobutton(root,text="no",variable=radio5,value="no")
radio5_no.pack()



def score_1():
    score=0
    if radio1.get()=="yes":
        score=score+20
    if radio2.get()=="yes":
        score=score+20
    if radio3.get()=="yes":
         score=score+20
    if radio4.get()=="yes":
         score=score+20 
    if radio5.get()=="yes":
        score=score+20      
    if score <=20:
       messagebox.showinfo("report"," you do not visit a doctor")
    elif score >20 and score <=60:
        messagebox.showinfo("report","you might perhaps have to visit a doctor")
    else :
        messagebox.showinfo("report","I advise you visit a doctor ")
        
        
    
button=Button(root,text="click me",command=score_1)
button.pack()















root.mainloop()
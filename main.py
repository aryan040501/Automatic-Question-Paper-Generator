import fpdf
from tkinter import *
import csv

pdf = fpdf.FPDF(format='letter')


q = []
q1= []
q2= []

s1 = []
s2 = []
s3 = []


def ques1():
    global q1
    with open('question.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
                ques1 = row["s2"]
                q1.append(ques1)

def ques2():
    global q2
    with open('question.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
                ques2 = row["s3"]
                q2.append(ques2)

def ques():
    with open('question.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            ques = row["s1"]
            q.append(ques)

ques()
ques1()
ques2()



def pdf_gen():
    pdf.add_page()
    pdf.set_font("Times", size=20)

    pdf.cell(200,15,"Examination", ln=1, align="C")
    pdf.set_font("Times",'i', size=17)
    pdf.cell(200,15,"Generated using an automated paper generation system", ln=1, align="C")
    pdf.set_font("Times",'i', size=14)
    pdf.cell(167,15,"Max Marks : 100", align="left")
    pdf.cell(100,15,"Time : 3 Hours",ln=1, align="right")
    pdf.set_font("Arial",'b', size=16)
    pdf.cell(134,15,"Section A", align="left")
    pdf.set_font("Times",'i', size=13)
    pdf.cell(100,15,"Max marks for this section are 4",ln=1, align="left")


    pdf.set_font("Times", size=12)
    for i in range(5):
        pdf.cell(170,6,"Q"+str(i+1)+": "+q[i],ln=1,align="left")

    pdf.set_font("Arial",'b', size=16)
    pdf.cell(134,15,"Section B", align="left")
    pdf.set_font("Times",'i', size=13)
    pdf.cell(100,15,"Max marks for this section are 6",ln=1, align="left")

    pdf.set_font("Times", size=12)
    for i in range(5,10):
        pdf.cell(170,6,"Q"+str(i+1)+": "+q1[i],ln=1,align="left")

    pdf.set_font("Arial",'b', size=16)
    pdf.cell(133,15,"Section C", align="left")
    pdf.set_font("Times",'i', size=13)
    pdf.cell(100,15,"Max marks for this section are 10",ln=1, align="left")

    pdf.set_font("Times", size=12)
    for i in range(10,15):
        pdf.cell(170,6,"Q"+str(i+1)+": "+q2[i],ln=1,align="left")

    pdf.output("file.pdf")

def mainwin():
    window = Tk()
    window.title("Question Paper Generator")
    window.configure(background='#ECECEC')
    window.geometry('600x500')

    lbl = Label(window, font="SF\Mono 36 bold", text = "Question Paper\nGenerator\n\n To Upload: replace csv\n  in the same folder \n    'question.csv'",background='#ECECEC',justify='left')
    lbl.grid(column=0, row=0,padx=20,pady=10)

    frame=Frame(window)
    frame.grid(column=0,row=3,padx=0,pady=10)

    addbutton=Button(frame,text="Add Question",)
    addbutton.config(height = 2, width = 15,bg='#ECECEC',justify='left',bd='0',relief='raised',command=addQwin)
    addbutton.grid(column=0,row=2)

    genbutton=Button(frame,text="Generate PDF",)
    genbutton.config(height = 2, width = 15,bg='#ECECEC',justify='left',bd='0',relief='raised',command=genpdf)
    genbutton.grid(column=1,row=2)

    window.mainloop()

def addQwin():
    window = Tk()
    window.title("Add Questions")
    window.configure(background='#ECECEC')
    window.geometry('500x500')

    txt2 = StringVar(window)

    def clicked():

        section = txt2.get()

        with open('question.csv') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=("s1","s2","s3"))
            header = next(reader)  # skip header row
            qs = txt1.get()

        with open('question.csv', mode='w') as f:
            fieldnames = ["s1", "s2", "s3"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(header)

            if (section == "Section A"):
                s1.append(qs)
                for i in range(len(s1)):
                    writer.writerow({'s1': s1[i]})
                for i in range(len(s2)):
                    writer.writerow({'s2': s2[i]})
                for i in range(len(s3)):
                    writer.writerow({'s3': s3[i]})
            elif (section == "Section B"):
                s2.append(qs)
                for i in range(len(s1)):
                    writer.writerow({'s1': s1[i]})
                for i in range(len(s2)):
                    writer.writerow({'s2': s2[i]})
                for i in range(len(s3)):
                    writer.writerow({'s3': s3[i]})
            elif (section == "Section C"):
                s3.append(qs)
                for i in range(len(s1)):
                    writer.writerow({'s1': s1[i]})
                for i in range(len(s2)):
                    writer.writerow({'s2': s2[i]})
                for i in range(len(s3)):
                    writer.writerow({'s3': s3[i]})


        f.close()




    lbl1 = Label(window, font="SF\Mono 36 bold", text="Add\nQuestions", background='#ECECEC', justify='left')
    lbl1.grid(column=0, row=0, padx=20, pady=10)
    frame1 = Frame(window)
    frame1.grid(column=0, row=2, padx=0, pady=10)
    txt1 = Entry(frame1, width=20, bg='#ECECEC')
    txt1.grid(column=0, row=0)

    lbl2 = Label(window, font="SF\Mono 28 bold", text="Enter Marks", background='#ECECEC', justify='left')
    lbl2.grid(column=0, row=3, padx=20, pady=10)
    frame2 = Frame(window)
    frame2.grid(column=0, row=4, padx=0, pady=10)
    optionm = OptionMenu(frame2, txt2, "Section A", "Section B", "Section C")
    optionm.grid(column=0, row=0)

    frame4 = Frame(window)
    frame4.grid(column=0, row=7, padx=0, pady=10)
    btn = Button(frame4, text="Submit", command=clicked)
    btn.grid(column=0, row=0)



def genpdf():
    pdf_gen()


mainwin()
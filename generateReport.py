import tkinter
from tkinter import *
from tkinter import ttk
from reportlab.pdfgen.canvas import Canvas
# from reportlab.lib.pagesizes import letter
from reportlab.lib import colors


###################################################################
# FUNCTIONS
###################################################################

# Creates actual report
def createReport():
    # Get user input
    firstName = firstNameInput.get()
    lastName = lastNameInput.get()
    score1 = score1Input.get()
    score2 = score2Input.get()


    fileName = lastName + "_Report.pdf"
    documentTitle = "sample"
    title = "Report for " + firstName + lastName
    subTitle = "this better be centered"
    textLines = [
        "this is line one",
        "and this is line two",
        "this is score 1: " + score1,
        "and this is score 2: " + score2
    ]

    pdf = Canvas(fileName)
    pdf.setTitle(documentTitle)

    # Title
    pdf.setFont("Helvetica-Bold", 30)
    pdf.drawCentredString(300, 770, title)
    pdf.drawCentredString(290, 720, subTitle)

    # Intro
    pdf.line(30, 710, 550, 710)
    text = pdf.beginText(40, 680)
    for line in textLines:
        text.textLine(line)
    pdf.drawText(text)

    pdf.save()

# For tabbing through intput boxes
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

###################################################################
# MAIN
###################################################################

window = tkinter.Tk()
window.title("Report Generator")
window.geometry("750x500")
window.resizable(0, 0)

space = tkinter.Label(window, height=2, ).pack()

firstNameLabel = Label(window, text="Student First Name").place(x=40, y=60)
firstNameInput = Entry(window, width = 20)
firstNameInput.place(x=200, y=60)

lastNameLabel = Label(window, text="Student Last Name").place(x=40, y=80)
lastNameInput = Entry(window, width = 20)
lastNameInput.place(x=200, y=80)

score1Label = Label(window, text="Student First Score").place(x=40, y=100)
score1Input = Entry(window, width = 20)
score1Input.place(x=200, y=100)

score2Label = Label(window, text="Student Second Score").place(x=40, y=120)
score2Input = Entry(window, width = 20)
score2Input.place(x=200, y=120)

button = tkinter.Button(text=" Generate Report PDF ", command=createReport).place(x=40, y=420)

window.mainloop()

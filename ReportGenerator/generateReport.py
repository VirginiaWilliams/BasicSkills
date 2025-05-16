import tkinter
from tkinter import *
from tkinter import ttk
from reportlab.pdfgen.canvas import Canvas
# from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
# from reportlab.lib.colors import HexColor
from reportlab.graphics import shapes


###################################################################
# FUNCTIONS
###################################################################

# Creates actual report
def createReport():
    # Get user input // Remove me?  Just use the getters?
    firstName = firstNameInput.get()
    lastName = lastNameInput.get()
    dateOfBirth = "00/00/0000"
    testNorm = "END OF GRADE BLAH BLAH BLAH IS THIS USER INPUT???"
    testDate = "11/11/1111"
    levelMaybe = "CAT 6 LEVEL 18 - SURVEY FORM C"
    score1 = score1Input.get()
    score2 = score2Input.get()

    # Other Values
    fileName = lastName + "_Report.pdf"
    documentTitle = "sample"
    title = "BasicSkills"
    subTitle = "Assesment & Educational Services"
    address = [
        "19146 Molalla Avenue",
        "Oregon City, Oregon 97045-8975",
        "Phone: (503) 650-5282"
    ]
    testName = "California Achievement Test 6, Terra Nova 2 Test Report"

    pdf = Canvas(fileName)
    pdf.setTitle(documentTitle)
    y = 750

    ##### Header #####

    # Title
    pdf.setFillColor(colors.navy)
    pdf.setFont("Times-Bold", 60)
    pdf.drawCentredString(300, y, title)

    # Subtitle
    y = y - 25
    pdf.setFont("Times-Bold", 20)
    pdf.drawCentredString(300, y, subTitle)

    # Address
    pdf.setFillColor(colors.black)
    pdf.setFont("Helvetica", 12)
    y = y - 25
    for line in address:
        pdf.drawCentredString(300, y, line)
        y = y - 15
    
    # Test Name
    y = 630
    pdf.drawCentredString(300, y, testName)

    ##### Student Info #####

    # Student Name
    y = 600
    pdf.drawString(50, y, "STUDENT'S NAME:")
    pdf.drawString(200, y, firstName + " " + lastName)

    # Student Date of Birth
    y = y - 20
    pdf.drawString(50, y, "DATE OF BIRTH:")
    pdf.drawString(200, y, dateOfBirth)

    # Test Norm?
    y = y - 20
    pdf.drawString(50, y, "TEST NORM:")
    pdf.drawString(200, y, testNorm)

    # Test Date
    y = y - 20
    pdf.drawString(50, y, "TEST DATE:")
    pdf.drawString(200, y, testDate)

    # Level?
    y = y - 20
    pdf.drawString(50, y, levelMaybe)

    # Horizontal Lines
    y = y - 20
    pdf.line(50, y, 540, y)
    y = y - 5
    pdf.line(50, y, 540, y)

    ##### Scores #####

    # Headers
    y = y - 25
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Subtest Title")
    pdf.drawString(250, y, "RS")
    pdf.drawString(300, y, "NP")
    pdf.drawString(350, y, "NCE")
    pdf.drawString(400, y, "S9")
    pdf.drawString(450, y, "GE")
    pdf.drawString(500, y, "SS")

    # Reading
    y = y - 25
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, "READING")
    pdf.drawString(250, y, "RS")
    pdf.drawString(300, y, "NP")
    pdf.drawString(350, y, "NCE")
    pdf.drawString(400, y, "S9")
    pdf.drawString(450, y, "GE")
    pdf.drawString(500, y, "SS")

    # Language
    y = y - 25
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, "LANGUAGE")
    pdf.drawString(250, y, "RS")
    pdf.drawString(300, y, "NP")
    pdf.drawString(350, y, "NCE")
    pdf.drawString(400, y, "S9")
    pdf.drawString(450, y, "GE")
    pdf.drawString(500, y, "SS")

    # Mathematics
    y = y - 25
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, "MATHEMATICS")
    pdf.drawString(250, y, "RS")
    pdf.drawString(300, y, "NP")
    pdf.drawString(350, y, "NCE")
    pdf.drawString(400, y, "S9")
    pdf.drawString(450, y, "GE")
    pdf.drawString(500, y, "SS")

    # Total Score
    y = y - 25
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, "TOTAL SCORE")
    pdf.drawString(250, y, "RS")
    pdf.drawString(300, y, "NP")
    pdf.drawString(350, y, "NCE")
    pdf.drawString(400, y, "S9")
    pdf.drawString(450, y, "GE")
    pdf.drawString(500, y, "SS")


    ##### Footer #####
    y = y - 100
    pdf.drawString(50, y, "Note: Examiner Qualification: This test was administered by [Name Name] who is qualified")
    y = y - 15
    pdf.drawString(50, y, "and neutral in regard to the above named child.")
    y = y - 30
    pdf.drawString(50, y, "The Total Score is based on an average of the Scale Scores for the Reading, Language, and")
    y = y - 15
    pdf.drawString(50, y, "Mathematics subtests.")

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

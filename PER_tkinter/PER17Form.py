import tkinter
from tkinter import *
from tkinter import ttk

###################################################################
# PER 17
###################################################################       

def open_per_17_form():
    window = tkinter.Tk()
    window.title("Report Generator")
    window.geometry("1000x750")
    window.resizable(True, True)

    canv = Canvas(window, relief=SUNKEN)
    canv.config(width=900, height=450)

    ##---------- scrollregion has to be larger than canvas size
    ##           otherwise it just stays in the visible canvas
    canv.config(scrollregion=(0,700,0,2000))
    canv.config(highlightthickness=0)

    ybar = Scrollbar(window)
    ybar.config(command=canv.yview)                   
    ## connect the two widgets together
    canv.config(yscrollcommand=ybar.set)              
    ybar.grid(column=1, row=0, sticky='NS')               
    canv.grid(column=0, row=0)

    frm = Frame(window, width=900, height=450, bd=2) # reduse height to scroll more IDK
    frm.grid(row= 0, column=0, padx=20, pady=10)

    ###################################################################
    # Student Info
    ###################################################################

    rowValue = 0

    tkinter.Label(frm, text="Student's Name:").grid(sticky="w", row=rowValue, column=0)
    tkinter.Label(frm, text="Test Date:").grid(sticky="w", row=rowValue+1, column=0)

    tkinter.Entry(frm).grid(row=0, column=1)
    tkinter.Entry(frm).grid(row=rowValue+1, column=1)

    for widget in frm.winfo_children():
        widget.grid_configure(padx=10, pady=5)
    
    ###################################################################
    # Reading Objectives
    ###################################################################

    rowValue = rowValue + 2
    tkinter.Label(frm, text="Reading Objectives ------------------", font='Helvetica 15').grid(sticky="w", row=rowValue, column=0, columnspan=3)
    rowValue = rowValue + 1

    tkinter.Label(frm, text="Can answer questions at the following levels of understanding:", wraplength=250, font='Helvetica 10 bold').grid(sticky="w", row=rowValue, column=0, columnspan=3)

    tkinter.Label(frm, text="Knowledge").grid(sticky="w", row=rowValue+1, column=0)
    tkinter.Label(frm, text="Comprehension").grid(sticky="w", row=rowValue+2, column=0)
    tkinter.Label(frm, text="Analysis").grid(sticky="w", row=rowValue+3, column=0)
    tkinter.Label(frm, text="Application").grid(sticky="w", row=rowValue+4, column=0)
    tkinter.Label(frm, text="Synthesis").grid(sticky="w", row=rowValue+5, column=0)
    tkinter.Label(frm, text="Evaluation").grid(sticky="w", row=rowValue+6, column=0)

    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+1, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+2, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+3, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+4, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+5, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+6, column=1)

    tkinter.Label(frm, text="/4").grid(row=rowValue+1, column=2)
    tkinter.Label(frm, text="/8").grid(row=rowValue+2, column=2)
    tkinter.Label(frm, text="/7").grid(row=rowValue+3, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+4, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+5, column=2)
    tkinter.Label(frm, text="/3").grid(row=rowValue+6, column=2)

    tkinter.Label(frm, text="Vocabulary", wraplength=250, font='Helvetica 10 bold').grid(sticky="w", row=rowValue+7, column=0, columnspan=3)

    tkinter.Label(frm, text="Can identify the orrect use or meaning of a word or phrase", wraplength=175).grid(sticky="w", row=rowValue+8, column=0)
    tkinter.Label(frm, text="Undersatnds the meaning of common prefixes and suffixes", wraplength=175).grid(sticky="w", row=rowValue+9, column=0)
    tkinter.Label(frm, text="Can identify the correct definition of a word", wraplength=175).grid(sticky="w", row=rowValue+10, column=0)
    
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+8, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+9, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+10, column=1)
    
    tkinter.Label(frm, text="/7").grid(row=rowValue+8, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+9, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+10, column=2)

    ###################################################################
    # Language Objectives
    ###################################################################


    tkinter.Label(frm, text="Language Objectives ------------------", font='Helvetica 15').grid(sticky="w", row=rowValue-1, column=3, columnspan=3)
    rowValue = rowValue + 1

    tkinter.Label(frm, text="Can recognize a correctly-constructed sentence", wraplength=200).grid(sticky="w", row=rowValue + 0, column=3)
    tkinter.Label(frm, text="Can identify sentences that do not support the topic sentence", wraplength=200).grid(sticky="w", row=rowValue + 1, column=3)
    tkinter.Label(frm, text="Can identify nouns, pronouns, determiners, conjunctions, or verbs that agee in number, or tesnse or function.", wraplength=200).grid(sticky="w", row=rowValue + 2, column=3)
    tkinter.Label(frm, text="Can combine sentences for clarity", wraplength=200).grid(sticky="w", row=rowValue + 3, column=3)
    tkinter.Label(frm, text="Can choose the best topic sentence for a paragraph", wraplength=200).grid(sticky="w", row=rowValue + 4, column=3)
    tkinter.Label(frm, text="Can organize or sequence sentences to make a paragraph", wraplength=200).grid(sticky="w", row=rowValue + 5, column=3)
    tkinter.Label(frm, text="Can idenitify and /or correct run-on sentences", wraplength=200).grid(sticky="w", row=rowValue + 6, column=3)
    tkinter.Label(frm, text="Can predict the usefulness of potential source Material", wraplength=200).grid(sticky="w", row=rowValue + 7, column=3)
    tkinter.Label(frm, text="Can identify and/or correct a sentence fragment", wraplength=200).grid(sticky="w", row=rowValue + 8, column=3)

    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue + 0, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue + 1, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue + 2, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue + 3, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue + 4, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue + 5, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue + 6, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue + 7, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue + 8, column=4)

    tkinter.Label(frm, text="/4").grid(row=rowValue + 0, column=5)
    tkinter.Label(frm, text="/4").grid(row=rowValue + 1, column=5)
    tkinter.Label(frm, text="/7").grid(row=rowValue + 2, column=5)
    tkinter.Label(frm, text="/4").grid(row=rowValue + 3, column=5)
    tkinter.Label(frm, text="/3").grid(row=rowValue + 4, column=5)
    tkinter.Label(frm, text="/1").grid(row=rowValue + 5, column=5)
    tkinter.Label(frm, text="/2").grid(row=rowValue + 6, column=5)
    tkinter.Label(frm, text="/1").grid(row=rowValue + 7, column=5)
    tkinter.Label(frm, text="/1").grid(row=rowValue + 8, column=5)

    ###################################################################
    # Math Problem Solving
    ###################################################################

    rowValue = rowValue + 9
    tkinter.Label(frm, text="Math Problem Solving -------------------------------------------------------------------------", font='Helvetica 15').grid(sticky="w", row=rowValue, column=0, columnspan=6)
    rowValue = rowValue + 1

    
    ###################################################################
    # Col 1 

    tkinter.Label(frm, text="Math computation", wraplength=250, font='Helvetica 10 bold').grid(sticky="w", row=rowValue+0, column=0, columnspan=3)

    tkinter.Label(frm, text="Can multiply and divide decimals", wraplength=200).grid(sticky="w", row=rowValue+1, column=0)
    tkinter.Label(frm, text="Can subtract mixed numbers with different denominators", wraplength=200).grid(sticky="w", row=rowValue+2, column=0)
    tkinter.Label(frm, text="Can find the precent of a number", wraplength=200).grid(sticky="w", row=rowValue+3, column=0)

    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+1, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+2, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+3, column=1)

    tkinter.Label(frm, text="/2").grid(row=rowValue+1, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+2, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+3, column=2)

    tkinter.Label(frm, text="Math Problem Solving", wraplength=250, font='Helvetica 10 bold').grid(sticky="w", row=rowValue+4, column=0, columnspan=3)

    tkinter.Label(frm, text="Can find solutions to story problems involving meoney", wraplength=175).grid(sticky="w", row=rowValue+5, column=0)
    tkinter.Label(frm, text="Can use subtractin of decimals to solve story problems", wraplength=175).grid(sticky="w", row=rowValue+6, column=0)
    tkinter.Label(frm, text="Can estimate solutions to subtraction problems involving whole numbers", wraplength=175).grid(sticky="w", row=rowValue+7, column=0)
    tkinter.Label(frm, text="Can estimate solutions to subtraction problems involving money", wraplength=175).grid(sticky="w", row=rowValue+8, column=0)
    tkinter.Label(frm, text="Can select the correct operation required to solve a story problem", wraplength=175).grid(sticky="w", row=rowValue+9, column=0)
    tkinter.Label(frm, text="Can read, understand, and apply graph data and other forms of data", wraplength=175).grid(sticky="w", row=rowValue+10, column=0)
    tkinter.Label(frm, text="Can use factoring and multiples to solve story problems", wraplength=175).grid(sticky="w", row=rowValue+11, column=0)
    tkinter.Label(frm, text="Can write numers using expanded notatin and exponents", wraplength=175).grid(sticky="w", row=rowValue+12, column=0)
    tkinter.Label(frm, text="Can apply concepts of lines, line segments, and rays", wraplength=175).grid(sticky="w", row=rowValue+13, column=0)
    tkinter.Label(frm, text="Can determine mode, median, or mean for a set of data", wraplength=175).grid(sticky="w", row=rowValue+14, column=0)
    tkinter.Label(frm, text="Understands and can apply place value concepts", wraplength=175).grid(sticky="w", row=rowValue+15, column=0)
    tkinter.Label(frm, text="Can read and recognize numbers", wraplength=175).grid(sticky="w", row=rowValue+16, column=0)
    tkinter.Label(frm, text="Can apply simple algebra concepts to solve story problems and equations", wraplength=175).grid(sticky="w", row=rowValue+17, column=0)
    tkinter.Label(frm, text="Can distinguish between parallel and perpendicular lines", wraplength=175).grid(sticky="w", row=rowValue+18, column=0)
    tkinter.Label(frm, text="Can use reasoning to find soltions to problmes involving time", wraplength=175).grid(sticky="w", row=rowValue+19, column=0)
    
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+5, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+6, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+7, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+8, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+9, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+10, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+11, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+12, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+13, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+14, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+15, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+16, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+17, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+18, column=1)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+19, column=1)
    
    tkinter.Label(frm, text="/2").grid(row=rowValue+5, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+6, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+7, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+8, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+9, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+10, column=2)
    tkinter.Label(frm, text="/3").grid(row=rowValue+11, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+12, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+13, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+14, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+15, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+16, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+17, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+18, column=2)
    tkinter.Label(frm, text="/1").grid(row=rowValue+19, column=2)

    ###################################################################
    # Col 2
    tkinter.Label(frm, text="Can use reasoning to find solutions to problems involving area", wraplength=200).grid(sticky="w", row=rowValue+5, column=3)
    tkinter.Label(frm, text="Can solve measurement problems involving scaled drawings", wraplength=200).grid(sticky="w", row=rowValue+6, column=3)
    tkinter.Label(frm, text="Can identify missing information required to solve story problems", wraplength=200).grid(sticky="w", row=rowValue+7, column=3)
    tkinter.Label(frm, text="Can identify common geometric shapes", wraplength=200).grid(sticky="w", row=rowValue+8, column=3)
    tkinter.Label(frm, text="Can identify solution patterns necessary to solve sotry problems", wraplength=200).grid(sticky="w", row=rowValue+8, column=3)
    tkinter.Label(frm, text="Can solve story problems involving distance, rate, and time", wraplength=200).grid(sticky="w", row=rowValue+9, column=3)
    tkinter.Label(frm, text="Can identify parts of geometrical solids", wraplength=200).grid(sticky="w", row=rowValue+10, column=3)
    tkinter.Label(frm, text="Cand etermine probablitiy", wraplength=200).grid(sticky="w", row=rowValue+11, column=3)
    tkinter.Label(frm, text="Can solve two-step story problems", wraplength=200).grid(sticky="w", row=rowValue+12, column=3)

    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+5, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+6, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+7, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+8, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+9, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+10, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+11, column=4)
    tkinter.Entry(frm, width=5).grid(sticky="e", row=rowValue+12, column=4)

    tkinter.Label(frm, text="/1").grid(row=rowValue+5, column=5)
    tkinter.Label(frm, text="/1").grid(row=rowValue+6, column=5)
    tkinter.Label(frm, text="/1").grid(row=rowValue+7, column=5)
    tkinter.Label(frm, text="/1").grid(row=rowValue+8, column=5)
    tkinter.Label(frm, text="/2").grid(row=rowValue+9, column=5)
    tkinter.Label(frm, text="/1").grid(row=rowValue+10, column=5)
    tkinter.Label(frm, text="/1").grid(row=rowValue+11, column=5)
    tkinter.Label(frm, text="/1").grid(row=rowValue+12, column=5)


    ###################################################################
    for widget in frm.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    canv.create_window(10,700,anchor=NW, window=frm)
    window.mainloop()

# For tabbing through intput boxes
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")
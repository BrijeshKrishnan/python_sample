from tkinter import *
ROW_SPACER = 25
class MyWindow:
    i=ROW_SPACER
    checkListItem = ["Use meaningful names in the code (Variables:class:function etc.)",
        "Follow the coding guideline (like Classes should be small! : Functions should be small!)",
        "Explain yourself in code: Comments",
        "Make sure the code formatting is applied",
        "Use Exceptions rather than Return codes",
        "Do not return Null",
        "Lint errors and warnings are checked and fixed",
        "Code duplication check is run and duplication is made minimum",
        "Do not log highly sensitive information (password: user id etc)",
        "Avoid excessive consol prints",
        "Adiquate logging is added in the code",
        "Validate inputs",
        "Do not hardcode the path",
        "Exceptions are not ignored",
        "Favor the use of standard exceptions",
        "Check parameters for validity",
        "Does the code work? Does it perform its intended function. the logic is correct etc.",
        "Do loops have a set length and correct termination conditions?",
        "Is there any commented out code?",
        "Is the code as modular as possible?",
        "Can any global variables be replaced?",
        "Is the Manual Test/ Requirement is tagged to automated Test",
        "Is the test integrated to CI pipeline in Dev branch and executed ~3 cycle",
        "Report -(Execution: Lint: Copy paste detection: Static analysis: code coverage) attached along with code review files",
        "All the steps mentioned in the test cases are automated",
        "Pre and Post conditions are automated??",
        "Is reusable methods are moved to common class??",
        "Copyright and Audit trial info is added to file",
        "Unit tests of the library /generic framework developed is carried out?"
        ]

    def __init__(self, win):
        
        for item in range(len(self.checkListItem)):
            self.lbl_item=Label(win, text=self.checkListItem[item])
            self.lbl_item.place(x=10, y= ROW_SPACER+self.i)
            globals()['V0_%s' %item] = None
            globals()['V0_%s' %item]=IntVar()
            globals()['V0_%s' %item].set(2)
            r1_item=Radiobutton(window, text="Yes", variable=globals()['V0_%s' %item],value=1)
            r2_item=Radiobutton(window, text="No", variable=globals() ['V0_%s' %item],value=2)
            r1_item.place(x=650, y= ROW_SPACER+self.i)
            r2_item.place(x=700, y= ROW_SPACER+self.i)
            self.i = self.i+ROW_SPACER
        self.b1=Button(win, text='Submit', command=self.submit)
        self.b1.place(x=350, y=2*ROW_SPACER+ROW_SPACER*(len(self.checkListItem)))

    def submit(self):
        RESULT = {1: "Yes", 2: "No"}
        try:
            with open("ReviewChecklist.csv", 'w') as file:
                file.write("Review checklist item ,")
                file.write("Status"+"\n")
                for item in range(len(self.checkListItem)):
                    file.write(self.checkListItem[item]+",")
                    file.write(RESULT[globals()['V0_%s' %item].get()]+"\n")
        except:
            print('Error')



window=Tk()
mywin=MyWindow(window)
window.title('CodeReviewChecklist')
window.geometry("800x800+10+10")
window.mainloop()

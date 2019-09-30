import re, math
from collections import Counter
from tkinter import *
from tkinter import filedialog
# Reading an excel file using Python 
import xlrd 
WORD = re.compile(r'\w+')
# Give the location of the file 
ROW_SPACER = 25
class MyWindow:

    i=ROW_SPACER  
    def __init__(self, win):
        self.path=Label(win, text="InputFilePath")
        self.path.place(x=10, y= ROW_SPACER)
        self.path_t = Entry(win, width=30)
        self.path_t.place(x=200, y= ROW_SPACER)

        self.browsebutton = Button(win, text="Browse", command=self.browsefunc)
        self.browsebutton.place(x=450, y= ROW_SPACER)

        self.sin_index=Label(win, text="Similatity Index")
        self.sin_index.place(x=10, y= ROW_SPACER*2)
        self.sin_index_t = Entry(win, width=10)
        self.sin_index_t.place(x=200, y= ROW_SPACER*2)
        self.sin_index_t.delete(0, END)

        self.tc_id=Label(win, text="TestCase ID Index")
        self.tc_id.place(x=10, y= ROW_SPACER*3)
        self.tc_id_t = Entry(win, width=10)
        self.tc_id_t.place(x=200, y= ROW_SPACER*3)
        self.tc_id_t.delete(0, END)

        self.ts_id=Label(win, text="TestCase Steps Index")
        self.ts_id.place(x=10, y= ROW_SPACER*4)
        self.ts_id_t = Entry(win, width=10)
        self.ts_id_t.place(x=200, y= ROW_SPACER*4)
        self.ts_id_t.delete(0, END)

        # self.te_id=Label(win, text="TestCase Expected Index")
        # self.te_id.place(x=10, y= ROW_SPACER*5)
        # self.te_id_t = Entry(win, width=10)
        # self.te_id_t.place(x=200, y= ROW_SPACER*5)
        # self.te_id_t.delete(0, END)
        self.submit=Button(win, text ="Process", command = self.submit)
        self.submit.place(x=250, y= ROW_SPACER*7)
        

    def browsefunc(self):
      self.filename = filedialog.askopenfilename()
      self.path_t.delete(0, END)
      self.path_t.insert(0,str(self.filename))
      return
    def validate_input(self):
        if not (self.path_t.get() and self.sin_index_t.get() and 
          self.tc_id_t.get() and self.ts_id_t.get()):#and 
        #   self.te_id_t.get()):
            print ("Enter values in field")
            return
    def submit(self):        
        try:
            self.validate_input()
            # self.process_file()
            self.process_cosine()
        except:
            print('Error')

    def get_cosine(self, vec1, vec2):
    
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])

        sum1 = sum([vec1[x]**2 for x in vec1.keys()])
        sum2 = sum([vec2[x]**2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

    def text_to_vector(self, text):
        words = WORD.findall(text)
        return Counter(words)
        
    def check_tolarance(self, actual_val=100, exp_val=100):
        return abs(actual_val - exp_val) <= 1

    def process_cosine(self):
        file = open("C:\\SimilarityIndexProcessor\\SimilarityIndexProcessor.csv","w") 
    # To open Workbook 
        if (int(self.sin_index_t.get()) >= 98):
             file.write("Testcase ID,Duplicates\n")
        else:
            file.write("Testcase ID,Potential Merge\n")
        wb = xlrd.open_workbook(self.path_t.get()) 
        sheet = wb.sheet_by_index(0) 
        for i in range(1, sheet.nrows):
            test_case_id = sheet.cell_value(i, int(self.tc_id_t.get())) 
            master_text = sheet.cell_value(i, int(self.ts_id_t.get())) 
            vector1 = self.text_to_vector(str(master_text))
            for j in range (i+1, sheet.nrows):
                match_text = sheet.cell_value(j, int(self.ts_id_t.get()))
                vector2 = self.text_to_vector(str(match_text))
                cosine = self.get_cosine(vector1, vector2)
                if self.check_tolarance(cosine*100, int(self.sin_index_t.get())):
                    print(cosine*100)
                    file.write(str(test_case_id)+","+str(sheet.cell_value(j, int(self.tc_id_t.get())))+"\n")
def process_file():
    wb = xlrd.open_workbook("C:\\Projects\\PythonRepo\\python_sample\\nlp\\sample.xlsx") 
    sheet = wb.sheet_by_index(0) 
    for i in range(1, sheet.nrows):
        row_to_merge = 1
        print("i=%s"%i)
        # print(sheet.cell_value(i,0))
        for j in range(i+1, sheet.nrows):
            if (sheet.cell_value(i,0) == sheet.cell_value(j,0) or (sheet.cell_value(j,0) is "")):
                row_to_merge+=1
            else:
                print(row_to_merge)
                print("j=%s"%(j-1))
                print("*************")
                i=j-1
                break



window=Tk()
mywin=MyWindow(window)
window.title('Text Similarity Index Processor')
window.geometry("550x250+10+10")
window.mainloop()
# process_file()

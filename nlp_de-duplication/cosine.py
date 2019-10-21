import re, math
from collections import Counter
from tkinter import *
from tkinter import filedialog
from collections import defaultdict
# Reading an excel file using Python 
import xlrd
import sys
import os
WORD = re.compile(r'\w+')
import xlsxwriter 
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

        self.ts_id=Label(win, text="Column of interest")
        self.ts_id.place(x=10, y= ROW_SPACER*4)
        self.ts_id_t = Entry(win, width=10)
        self.ts_id_t.place(x=200, y= ROW_SPACER*4)
        self.ts_id_t.delete(0, END)

        self.submit=Button(win, text ="Process", command = self.submit)
        self.submit.place(x=250, y= ROW_SPACER*7)
        self.row_merge_dict =defaultdict(str)
        

    def browsefunc(self):
        """
        Function used for providing the Browse to file path in the GUI
        """
        self.filename = filedialog.askopenfilename()
        self.path_t.delete(0, END)
        self.path_t.insert(0,str(self.filename))
        return

    def validate_input(self):
        """
        Function used for validating whether all the mandatory input fields are provided or not
        """
        if not (self.path_t.get() and self.sin_index_t.get() and 
          self.tc_id_t.get() and self.ts_id_t.get()):
            return
    def submit(self):
        """
        Function which is the entry for all the processing activity. 
        """        
        try:
            self.validate_input()
            self.process_file()
            self.create_temp_file()
            self.process_cosine()
        except:
            print('Error')

    def get_file_path(self):
        """
        Function used for getting the file path where the results can be stored
        """
        return str(os.path.dirname(self.path_t.get()))
    
    def get_file_name(self):
        """
        Function used for getting the file name which can be used for naming the result
        """
        file_path = self.path_t.get().split("/")
        return(os.path.splitext(file_path[-1])[0])

    def get_cosine(self, vec1, vec2):
        """
        Function used for getting the cosine value
        vec1, vec2: Input vector from the texts to be compared
        """
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
        """
        Function used for converting the text to vector
        text: Input text 
        """
        words = WORD.findall(text)
        return Counter(words)
        
    def check_tolarance(self, actual_val=100, exp_val=100):
        """
        Function used for checking the tolarance value (defaulted to 100)
        actual_val: what is the actual value after processing the cosine
        exp_val: what is the expected value for the cosine
        """
        if actual_val >= exp_val:
            return abs(actual_val - exp_val) <= 1
        else:
            return 0

    def process_cosine(self):
        """
        Function which process the cosine from the merged input data and generate a recomendation after processing
        """
        file = open(os.path.join(self.get_file_path(),self.get_file_name()+"_recomendation_%s.csv"%self.sin_index_t.get()),"w")
        print(os.path.join(self.get_file_path(),self.get_file_name()+"_recomendation_%s.csv"%self.sin_index_t.get()))
        # To open Workbook 
        if (int(self.sin_index_t.get()) >= 98):
             file.write("Testcase ID,Duplicates\n")
        else:
            file.write("Testcase ID,Potential Merge\n")
        wb = xlrd.open_workbook(os.path.join(self.get_file_path(),self.get_file_name()+"_merged.xlsx"))

        sheet = wb.sheet_by_index(0) 
        for i in range(1, sheet.nrows):
            test_case_id = sheet.cell_value(i, 0) 
            master_text = sheet.cell_value(i, 1) 
            vector1 = self.text_to_vector(str(master_text))
            for j in range (i+1, sheet.nrows):
                match_text = sheet.cell_value(j, 1)
                vector2 = self.text_to_vector(str(match_text))
                cosine = self.get_cosine(vector1, vector2)
                if self.check_tolarance(cosine*100, int(self.sin_index_t.get())):
                    print(cosine*100)
                    file.write(str(test_case_id)+","+str(sheet.cell_value(j, 0))+"\n")

    def get_tc_id(self, row_num, sheet):
        """
        Function used for getting the testcase id from the input sheet
        row_num : row number on which testcase id need to be fetched
        steet : sheet of interest
        """
        return str(sheet.cell_value(row_num, int(self.tc_id_t.get())))
    def create_temp_file(self):
        """
        Function used for creating the temporary file which has just 2 columns 1: testcase id,2: all interested cells merged to form the steps
        """
        workbook = xlsxwriter.Workbook(os.path.join(self.get_file_path(),self.get_file_name()+"_merged.xlsx")) 
        worksheet = workbook.add_worksheet() 
        xls_row = 1
        worksheet.write(0, 0, "Testcase ID") 
        worksheet.write(0, 1, "Merged_Steps")
        wb = xlrd.open_workbook(self.path_t.get())
        sheet = wb.sheet_by_index(0)
        int_colum = (str(self.ts_id_t.get())).split(",")
        skip_count = 0
        for i in range(1,sheet.nrows):
            processed_text = ''
            id = self.get_tc_id(i, sheet)
            if skip_count:
                skip_count-=1
                continue
            if ((self.row_merge_dict[id] > 1)):
                worksheet.write(xls_row, 0, "%s"%str(id)) 
                for row in range (i, i+self.row_merge_dict[id]):
                    skip_count = int(self.row_merge_dict[id])-1
                    for j in int_colum:
                        processed_text += sheet.cell_value(row, int(j))
                worksheet.write(xls_row, 1, "%s"%str(processed_text)) 
               
            else:
                worksheet.write(xls_row, 0, "%s"%str(id)) 
                for j in int_colum:
                    processed_text += sheet.cell_value(i, int(j))
                worksheet.write(xls_row, 1, "%s"%str(processed_text)) 
            xls_row+=1
            print("row=%s"%xls_row)
        workbook.close()

    def process_file(self):
        """
        Function used for identifying the cells to be merged and create a dictionary which will help the further processing during the creating of 
        consolidated steps in create_temp_file()
        """
        wb = xlrd.open_workbook(self.path_t.get())
        sheet = wb.sheet_by_index(0)
        jump_flag = None
        row_to_merge = 1
        for i in range(1,sheet.nrows):
            if (row_to_merge> 1):
                if (jump_flag):            
                        row_to_merge-=1
                        continue
                if (not row_to_merge):
                    jump_flag = 0
                    row_to_merge = 1
            self.row_merge_dict[str(sheet.cell_value(i,0))]=1
            for j in range(i+1, sheet.nrows):
                if not (sheet.cell_value(j,int(self.tc_id_t.get())) == ''):
                    if (str(sheet.cell_value(i,int(self.tc_id_t.get()))) == str(sheet.cell_value(j,int(self.tc_id_t.get())))):
                        row_to_merge=row_to_merge+1
                        jump_flag = 1
                        self.row_merge_dict[str(sheet.cell_value(i,int(self.tc_id_t.get())))]=row_to_merge
                        continue
                    else:
                        break
                else:
                    row_to_merge=row_to_merge+1
                    jump_flag = 1
                    self.row_merge_dict[str(sheet.cell_value(i,int(self.tc_id_t.get())))]=row_to_merge
                    continue
        print(self.row_merge_dict)
        print("Number of records analysed:%s"%len(self.row_merge_dict))
        return self.row_merge_dict

window=Tk()
mywin=MyWindow(window)
window.title('Text Similarity Index Processor')
window.geometry("550x250+10+10")
window.mainloop()
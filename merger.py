import os
from PyPDF2 import PdfMerger
from tkinter import Tk, filedialog

merger = PdfMerger()

root = Tk()
root.withdraw()
pdf_files = filedialog.askopenfilenames(filetypes=[('PDF Files', '*.pdf')])

for pdf in pdf_files:
    if os.path.exists(pdf):
        merger.append(pdf)
    else:
        print(f'Error: File "{pdf}" not found.')

if merger.inputs:
    output_path = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[('PDF Files', '*.pdf')])
     
    merger.write(output_path)
    print(f'PDF files merged successfully. Output saved to "{output_path}".')
else:
    print('No PDF files to merge.')


merger.close()
import os
import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import docx

root = Tk()
root.withdraw()
pdf_path = askopenfilename(filetypes=[("PDF Files", "*.pdf")])

with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)

    doc = docx.Document()

    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        doc.add_paragraph(text)

    doc_path = asksaveasfilename(defaultextension='.docx', filetypes=[("Word Document", "*.docx")])
    doc.save(doc_path)
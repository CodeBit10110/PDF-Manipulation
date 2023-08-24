import PyPDF2
import tkinter as tk
from tkinter import filedialog, simpledialog

def get_filename():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    return file_path

def get_page_range():
    root = tk.Tk()
    root.withdraw()
    first_page = simpledialog.askinteger(title="First Page", prompt="Enter the first page to extract (e.g. 1)")
    last_page = simpledialog.askinteger(title="Last Page", prompt="Enter the last page to extract (e.g. 10)")
    return first_page, last_page

def demerge_pdf():
    input_filename = get_filename()

    first_page, last_page = get_page_range()

    with open(input_filename, "rb") as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)

        for page_num in range(first_page-1, last_page):
            output_filename = input_filename.replace(".pdf", f"_page{page_num+1}.pdf")
            with open(output_filename, "wb") as output_file:
                pdf_writer = PyPDF2.PdfWriter()
                pdf_writer.add_page(pdf_reader.pages[page_num])
                pdf_writer.write(output_file)

            print(f"Extracted page {page_num+1} to {output_filename}")


if __name__ == '__main__':
    demerge_pdf()
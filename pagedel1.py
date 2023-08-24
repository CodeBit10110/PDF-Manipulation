import PyPDF2
import easygui

pdf_file_path = easygui.fileopenbox(title="Select PDF file to remove pages", default="*.pdf")

pdf_file = open(pdf_file_path, 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)

delete_pages_str = easygui.enterbox("Enter the page number(s) to be deleted (separated by commas): ")
delete_pages = [int(p.strip()) for p in delete_pages_str.split(',')]

pdf_writer = PyPDF2.PdfWriter()

for page_num in range (len(pdf_reader.pages)):
    if page_num + 1 not in delete_pages:
        page_obj = pdf_reader.pages[page_num - 1]
        pdf_writer.add_page(page_obj)

output_file_path = easygui.filesavebox(default=".pdf", title="Save the modified PDF file as", filetypes=["*.pdf"])

if output_file_path:

    output_file = open(output_file_path, 'wb')
    pdf_writer.write(output_file)

    pdf_file.close()
    output_file.close()
else:
    pdf_file.close()
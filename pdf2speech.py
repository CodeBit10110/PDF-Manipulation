import os
import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from gtts import gTTS

Tk().withdraw()
filelocation= askopenfilename()

with open(filelocation  , "rb") as f:
    pdf = PyPDF2.PdfReader(f)
    myText =""
    for PageNum in range (len(pdf.pages)):
     pageObj= pdf.pages[PageNum]
     myText+= pageObj.extract_text()
print(myText)   

final_output = gTTS(text=myText,lang='en')
print("Generating speech..........")
final_output.save("Generated_speech.mp3")
os.system("start Generated_Speech.mp3")
print("Succesfully Generated ........")
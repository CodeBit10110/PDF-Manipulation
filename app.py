from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_script_1', methods=['POST'])
def run_script_1():
    subprocess.run(['python', 'C:/Users/Vivek sharma/Desktop/Project/merger.py'])
    return "Your PDF's has been Merged Successfully in your respective folder!!!"

@app.route('/run_script_2', methods=['POST'])
def run_script_2():
    subprocess.run(['python', 'C:/Users/Vivek sharma/Desktop/Project/demerge.py'])
    return "Your PDF's has been De-merged Successfully in your respective folder!!!"

@app.route('/run_script_3', methods=['POST'])
def run_script_3():
    subprocess.run(['python', 'C:/Users/Vivek sharma/Desktop/Project/pdf2doc.py'])
    return "Your PDF's has been converted to Doc file Successfully in your respective folder!!!"

@app.route('/run_script_4', methods=['POST'])
def run_script_4():
    subprocess.run(['python', 'C:/Users/Vivek sharma/Desktop/Project/pdf2speech.py'])
    return "Your PDF's has been converted to Speech Successfully in your respective folder!!!"

@app.route('/run_script_5', methods=['POST'])
def run_script_5():
    subprocess.run(['python', 'C:/Users/Vivek sharma/Desktop/Project/pagedel1.py'])
    return "The provided Page Numbers has been removed successfully from the PDF!!!"

if __name__ == '__main__':
    app.run(debug=True, port=5200)
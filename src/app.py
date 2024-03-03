from flask import Flask, render_template, request, make_response, redirect
from funciones.funciones import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'pdf' in request.files:
        pdf_file = request.files['pdf']
        guardar_archivo(pdf_file)
    if 'mp4' in request.files:
        mp4_file = request.files['mp4']
        guardar_archivo(mp4_file)
    return redirect('/archivos')

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    file = fs.find_one({'filename': filename})
    if file:
        response = make_response(file.read())
        response.headers.set('Content-Disposition', 'attachment', filename=filename)
        return response
    else:
        return 'El archivo no existe'

@app.route('/archivos', methods=['GET'])
def get_files():
    pdf_files = obtener_archivos('pdf')
    mp4_files = obtener_archivos('mp4')
    return render_template('download.html', pdf_files=pdf_files, mp4_files=mp4_files)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1', threaded=True)
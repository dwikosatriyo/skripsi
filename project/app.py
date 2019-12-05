from flask import Flask, render_template, redirect, request, url_for
from werkzeug.utils import secure_filename
import test, timeit, proses

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html', coba=['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'])

@app.route('/enc_waktu_text', methods=['POST', 'GET'])
def enc_waktu_text():
    error = None
    if (request.method == 'POST'):
        pesan = request.form['pesan']
        len_pesan = len(pesan)
        kunci = request.form['kunci']
        time_encrypt, time_decrypt, algoritma, ciphertext = proses.input_small(pesan, kunci)
        
        return render_template('enc_waktu_text.html', algoritma = algoritma, time_encrypt = time_encrypt, time_decrypt = time_decrypt, len_plaintext = len_pesan, ciphertext = ciphertext, plaintext = pesan)

    return render_template('input_waktu_text.html', error=error)


@app.route('/enc_waktu_file', methods=['POST', 'GET'])
def enc_waktu_file():
    error = None
    if (request.method == 'POST'):
        f = request.files['pesan']
        f.save(app.root_path + '\\upload\\' + secure_filename(f.filename))
        with open(app.root_path + '\\upload\\' + secure_filename(f.filename), "r") as x:
            plaintext = x.read().replace('\n','') 
        len_plaintext = len(plaintext)
        kunci = request.form['kunci']
        time_encrypt, time_decrypt, algoritma = proses.input(plaintext, kunci)
        
        return render_template('enc_waktu_file.html', algoritma = algoritma, time_encrypt = time_encrypt, time_decrypt = time_decrypt, len_plaintext = len_plaintext)

    return render_template('input_waktu_file.html', error=error)

@app.route('/enc_waktu_size_all')
def enc_waktu_size_all():
    error = None
    kunci = "kuncirahasia"
    plaintext = []
    size = ["1 KB", "2 KB", "4 KB", "8 KB", "16 KB", "32 KB", "64 KB", "128 KB", "256 KB"]
    with open(app.root_path + '\\files\\dummy\\1kb.txt' , "r") as x:
        text1kb = x.read().replace('\n','')
    with open(app.root_path + '\\files\\dummy\\2kb.txt' , "r") as x:
        text2kb = x.read().replace('\n','')
    with open(app.root_path + '\\files\\dummy\\4kb.txt' , "r") as x:
        text4kb = x.read().replace('\n','')
    with open(app.root_path + '\\files\\dummy\\8kb.txt' , "r") as x:
        text8kb = x.read().replace('\n','')
    with open(app.root_path + '\\files\\dummy\\16kb.txt' , "r") as x:
        text16kb = x.read().replace('\n','')
    with open(app.root_path + '\\files\\dummy\\32kb.txt' , "r") as x:
        text32kb = x.read().replace('\n','')
    with open(app.root_path + '\\files\\dummy\\64kb.txt' , "r") as x:
        text64kb = x.read().replace('\n','')
    with open(app.root_path + '\\files\\dummy\\128kb.txt' , "r") as x:
        text128kb = x.read().replace('\n','')
    with open(app.root_path + '\\files\\dummy\\256kb.txt' , "r") as x:
        text256kb = x.read().replace('\n','')
    plaintext = [text1kb,text2kb,text4kb,text8kb,text16kb,text32kb,text64kb,text128kb,text256kb]
    time_encrypt, time_decrypt, algoritma = proses.input_many(plaintext, kunci)
    # time_encrypt1, time_decrypt1, algoritma = proses.input(text1kb, kunci)
    # time_encrypt2, time_decrypt2, algoritma = proses.input(text2kb, kunci)
    # time_encrypt4, time_decrypt4, algoritma = proses.input(text4kb, kunci)
    # time_encrypt8, time_decrypt8, algoritma = proses.input(text8kb, kunci)
    # time_encrypt16, time_decrypt16, algoritma = proses.input(text16kb, kunci)
    # time_encrypt = [time_encrypt1,time_encrypt2,time_encrypt4,time_encrypt8,time_encrypt16]
    # time_decrypt = [time_decrypt1,time_decrypt2,time_decrypt4,time_decrypt8,time_decrypt16]
    return render_template('enc_waktu_size_all.html', algoritma = algoritma,  size = size, time_encrypt = time_encrypt, time_decrypt = time_decrypt )


@app.route('/hello')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)

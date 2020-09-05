from flask import Flask, render_template, redirect, request, url_for, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import test, timeit, proses, steganographyDNA, os
from proces import dna
app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html', coba=['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'])

@app.route('/files/img/<path:filename>')
def download_image(filename):
    path = os.path.dirname(os.path.abspath(__file__))+('/files/img/')

    return send_from_directory(path,
                               filename, as_attachment=True)

@app.route('/all/<input>', methods=['POST','GET'])
def encode_stegano(input):
    error = None
    if (request.method == 'POST'):
        pesan = request.form['pesan']
        kunci = request.form['kunci']
        media = request.form['media']
        media_dna = dna.string_to_DNA(media)
        
        pesan_ascii, pesan_binary, pesan_dna, pesan_protein, tabel_kunci, hasil_enkripsi = proses.input_detail (pesan, kunci)
        input_binary, hasil_steganografi, random_number = steganographyDNA.subtitution_embed_detail(hasil_enkripsi, media_dna)
        
        hasil_ekstraksi = steganographyDNA.subtitution_extract_detail(hasil_steganografi, media_dna)

        return render_template('all_text.html', pesan=pesan, kunci=kunci, media=media, pesan_ascii=pesan_ascii, pesan_binary=pesan_binary, pesan_dna=pesan_dna, pesan_protein=pesan_protein, tabel_kunci=tabel_kunci, hasil_enkripsi=hasil_enkripsi,  media_dna=media_dna, input_binary=input_binary, random_number=random_number, hasil_steganografi=hasil_steganografi, hasil_ekstraksi=hasil_ekstraksi)
    
    return render_template('input_all_text.html', error=error)
    

@app.route('/enc_waktu_text', methods=['POST','GET'])
def enc_waktu_text():
    error = None
    if (request.method == 'POST'):
        pesan = request.form['pesan']
        len_pesan = len(pesan)
        kunci = request.form['kunci']
        time_encrypt, time_decrypt, algoritma, ciphertext, plaintex_protein, tabel_kunci = proses.input_small(pesan, kunci)
        
        return render_template('enc_waktu_text.html', algoritma = algoritma, time_encrypt = time_encrypt, time_decrypt = time_decrypt, len_plaintext = len_pesan, ciphertext = ciphertext, plaintext = pesan, plaintex_protein = plaintex_protein, kunci = kunci, tabel_kunci = tabel_kunci)

    return render_template('input_waktu_text.html', error=error)

@app.route('/steg_waktu_text', methods=['POST','GET'])

def steg_waktu_text():
    error = None
    if (request.method == 'POST'):
        f = request.files['reference']
        f.save(app.root_path + '\\upload\\' + secure_filename(f.filename))
        with open(app.root_path + '\\upload\\' + secure_filename(f.filename), "r") as x:
            reference = x.read().replace('\n','') 
        plaintext = request.form['pesan']
        algorithm, stego, time_s, time_e, img_path = steganographyDNA.steganography_all(plaintext, reference)
        
        # time_e = ["0.02698099999997794", "0.004854699999896184", "0.37416030000008504"]
        # time_s = ["0.02698099999997794", "0.004854699999896184", "0.37416030000008504"]
        return render_template('steg_waktu_text.html', algoritma = algorithm, stego = stego, time_s = time_s, time_e = time_e, img_path= img_path)

    return render_template('steg_input_text.html', error=error)

@app.route('/steg_waktu_text_method', methods=['POST','GET'])
def steg_waktu_text_method():
    error = None
    if (request.method == 'POST'):
        f = request.files['reference']
        f.save(app.root_path + '\\upload\\' + secure_filename(f.filename))
        with open(app.root_path + '\\upload\\' + secure_filename(f.filename), "r") as x:
            reference = x.read().replace('\n','') 
        plaintext = request.form['pesan']
        method = request.form['metode']
        return render_template('steg_waktu_text_method.html')
        # stego, time_s, time_e = steganographyDNA.steganography_method(plaintext, reference, method)
        
        # time_e = ["0.02698099999997794", "0.004854699999896184", "0.37416030000008504"]
        # time_s = ["0.02698099999997794", "0.004854699999896184", "0.37416030000008504"]
        # return render_template('steg_waktu_text_method.html',  stego = stego, time_s = time_s, time_e = time_e)

    return render_template('steg_input_text_method.html', error=error)

@app.route('/steg_waktu_all_process', methods =['GET'])
def steg_waktu_all_process():   
    if (request.method == 'GET'): 
        plaintext = "PESAN RAHASIA"
        size = ["32 KB", "64 KB", "128 KB", "256 KB", "512 KB", "1024 KB", "2048 KB", "4096 KB"]
        with open(app.root_path + '\\files\\dummy_ref\\32kb.txt' , "r") as x:
            text32kb = x.read().replace('\n','')
        with open(app.root_path + '\\files\\dummy_ref\\64kb.txt' , "r") as x:
            text64kb = x.read().replace('\n','')
        with open(app.root_path + '\\files\\dummy_ref\\128kb.txt' , "r") as x:
            text128kb = x.read().replace('\n','')
        with open(app.root_path + '\\files\\dummy_ref\\256kb.txt' , "r") as x:
            text256kb = x.read().replace('\n','')
        with open(app.root_path + '\\files\\dummy_ref\\512kb.txt' , "r") as x:
            text512kb = x.read().replace('\n','')
        with open(app.root_path + '\\files\\dummy_ref\\1024kb.txt' , "r") as x:
            text1024kb = x.read().replace('\n','')
        with open(app.root_path + '\\files\\dummy_ref\\2048kb.txt' , "r") as x:
            text2048kb = x.read().replace('\n','')
        with open(app.root_path + '\\files\\dummy_ref\\4096kb.txt' , "r") as x:
            text4096kb = x.read().replace('\n','')
        reference = [text32kb,text64kb,text128kb,text256kb,text512kb,text1024kb,text2048kb,text4096kb]
        stego = {0 : [],1 : [],2 : []}
        time_s = {0 : [],1 : [],2 : []}
        time_e = {0 : [],1 : [],2 : []}
        img_path = {0 : [],1 : [],2 : []}
        num_size = 0
        try:
            for x in reference:
                algorithm, stegoTemp, time_sTemp, time_eTemp, img_pathTemp = steganographyDNA.steganography_all(plaintext, x)
                for i in range(len(algorithm)):
                    stego[i].append(stegoTemp[i])
                    time_s[i].append(time_sTemp[i])
                    time_e[i].append(time_eTemp[i])
                    img_path[i].append(img_pathTemp[i])
                print(size[num_size])
                num_size+=1
        except:
            return("An exception occurred") 
            
        # time_e = ["0.02698099999997794", "0.004854699999896184", "0.37416030000008504"]
        # time_s = ["0.02698099999997794", "0.004854699999896184", "0.37416030000008504"]
        return render_template('steg_waktu_all.html', algoritma = algorithm, stego = stego, time_embedding = time_s, time_extract = time_e, img_path= img_path, size = size)


@app.route('/steg_waktu_all', methods=['GET','POST'])

def steg_waktu_all():
    error = None
    if (request.method == 'POST'):
    # if request.form["pesan"] in globals():
        plaintext = "PESAN RAHASIA"
        # size = ["32 KB", "64 KB", "128 KB", "256 KB", "512 KB", "1024 KB", "2048 KB"]
        size = ["32 KB", "64 KB", "128 KB", "256 KB", "512 KB", "1024 KB"]
        with open(app.root_path + '\\files\\dummy_ref\\32kb.txt' , "r") as x:
            text32kb = x.read().replace('\n','')
        with open(app.root_path + '\\files\\dummy_ref\\64kb.txt' , "r") as x:
            text64kb = x.read().replace('\n','')
        with open(app.root_path + '\\files\\dummy_ref\\128kb.txt' , "r") as x:
            text128kb = x.read().replace('\n','')
        with open(app.root_path + '\\files\\dummy_ref\\256kb.txt' , "r") as x:
            text256kb = x.read().replace('\n','')
        with open(app.root_path + '\\files\\dummy_ref\\512kb.txt' , "r") as x:
            text512kb = x.read().replace('\n','')
        with open(app.root_path + '\\files\\dummy_ref\\1024kb.txt' , "r") as x:
            text1024kb = x.read().replace('\n','')
        # with open(app.root_path + '\\files\\dummy_ref\\2048kb.txt' , "r") as x:
        #     text2048kb = x.read().replace('\n','')

        # reference = [text32kb,text64kb,text128kb,text256kb,text512kb,text1024kb,text2048kb]
        reference = [text32kb,text64kb,text128kb,text256kb,text512kb,text1024kb]

        stego = {0 : [],1 : [],2 : []}
        time_s = {0 : [],1 : [],2 : []}
        time_e = {0 : [],1 : [],2 : []}
        img_path = {0 : [],1 : [],2 : []}
        num_size = 0
        try:
            for x in reference:
                algorithm, stegoTemp, time_sTemp, time_eTemp, img_pathTemp = steganographyDNA.steganography_all(plaintext, x)
                for i in range(len(algorithm)):
                    stego[i].append(stegoTemp[i])
                    time_s[i].append(time_sTemp[i])
                    time_e[i].append(time_eTemp[i])
                    img_path[i].append(img_pathTemp[i])
                print(size[num_size])
                num_size+=1
        except:
            return("An exception occurred") 
            
        # time_e = ["0.02698099999997794", "0.004854699999896184", "0.37416030000008504"]
        # time_s = ["0.02698099999997794", "0.004854699999896184", "0.37416030000008504"]
        return render_template('steg_waktu_all.html', algoritma = algorithm, stego = stego, time_embedding = time_s, time_extract = time_e, img_path= img_path, size = size)

    return render_template('steg_input_all.html', error=error)

@app.route('/enc_waktu_file', methods=['POST','GET'])
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
        # return jsonify({
        #     "algoritma"     : algoritma, 
        #     "time_encrypt"  : time_encrypt, 
        #     "time_decrypt"  : time_decrypt, 
        #     "len_plaintext" : len_plaintext,
        # })
        return render_template('enc_waktu_file.html', algoritma = algoritma, time_encrypt = time_encrypt, time_decrypt = time_decrypt, len_plaintext = len_plaintext)
    return render_template('input_waktu_file.html', error=error)

@app.route('/enc_waktu_size_all', methods=['POST','GET'])
def enc_waktu_size_all():
    error = None
    if (request.method == 'POST'):
        kunci = "kuncirahasia"
        plaintext = []
        size = ["1 KB", "2 KB", "4 KB", "8 KB", "16 KB", "32 KB", "64 KB", "128 KB", "256 KB"]
        with open(app.root_path + '\\files\\dummy\\1024kb.txt' , "r") as x:
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
    return render_template('input_waktu_all.html', error=error)

@app.route('/hello')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    
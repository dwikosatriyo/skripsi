import test
import timeit
from proces import playfair_dna, dna, playfair



def input_detail (plaintext, kunci) :
    pesan_ascii =  dna.string_to_ascii(plaintext)
    pesan_binary = dna.ascii_to_binary(pesan_ascii)
    pesan_binary += "0"*(6-(len(pesan_binary)%6))
    pesan_dna= dna.binary_to_DNA(pesan_binary)
    pesan_protein = playfair_dna.DNA_to_protein(pesan_dna)
    tabel_kunci = playfair.create_table(kunci)
    hasil_enkripsi = test.encrypt_dna(pesan_protein.protein.lower(), kunci.lower(), 1)
    
    return pesan_ascii, pesan_binary, pesan_dna, pesan_protein.protein, tabel_kunci, hasil_enkripsi   
def input_small (plaintext, kunci) : 
    pesan = dna.string_to_binary(plaintext)
    pesan += "0"*(6-(len(pesan)%6))
    pesan = dna.binary_to_DNA(pesan)
    plaintex_protein = playfair_dna.DNA_to_protein(pesan) 
    tabel_kunci = playfair.create_table(kunci)
    time_encrypt = []
    time_decrypt = []
    ciphertext = []
    algoritma = ["Playfair-DNA", "Porta-DNA", "Vigenere-DNA", "AES"]
    a, ambiguity, time_x = test.encrypt_dna_time(plaintext, kunci, 1)
    b, time_y = test.decrypt_dna(a, kunci, ambiguity, 1)
    time_encrypt.append(time_x)
    time_decrypt.append(time_y)
    ciphertext.append(a)
    a, ambiguity, time_x = test.encrypt_dna_time(plaintext, kunci, 2)
    b, time_y = test.decrypt_dna(a, kunci, ambiguity, 2)
    time_encrypt.append(time_x)
    time_decrypt.append(time_y)
    ciphertext.append(a)
    a, ambiguity, time_x = test.encrypt_dna_time(plaintext, kunci, 3)
    b, time_y = test.decrypt_dna(a, kunci, ambiguity, 3)
    time_encrypt.append(time_x)
    time_decrypt.append(time_y)
    ciphertext.append(a)
    a, time_x = test.encrypt_regular(plaintext, kunci, 1)
    b, time_y = test.decrypt_regular(a, kunci, 1)
    time_encrypt.append(time_x)
    time_decrypt.append(time_y)
    ciphertext.append(a)
    return time_encrypt, time_decrypt, algoritma, ciphertext, plaintex_protein.protein.lower(), tabel_kunci

def input (plaintext, kunci) :  
    time_encrypt = []
    time_decrypt = []
    algoritma = ["Playfair-DNA", "Porta-DNA", "Vigenere-DNA", "AES"]
    a, ambiguity, time_x = test.encrypt_dna_time(plaintext, kunci, 1)
    b, time_y = test.decrypt_dna(a, kunci, ambiguity, 1)
    time_encrypt.append(time_x)
    time_decrypt.append(time_y)
    a, ambiguity, time_x = test.encrypt_dna_time(plaintext, kunci, 2)
    b, time_y = test.decrypt_dna(a, kunci, ambiguity, 2)
    time_encrypt.append(time_x)
    time_decrypt.append(time_y)
    a, ambiguity, time_x = test.encrypt_dna_time(plaintext, kunci, 3)
    b, time_y = test.decrypt_dna(a, kunci, ambiguity, 3)
    time_encrypt.append(time_x)
    time_decrypt.append(time_y)
    a, time_x = test.encrypt_regular(plaintext, kunci, 1)
    b, time_y = test.decrypt_regular(a, kunci, 1)
    time_encrypt.append(time_x)
    time_decrypt.append(time_y)
    return time_encrypt, time_decrypt, algoritma
def input_many (plaintext, kunci) :          
    
    time_encrypt = [[] for y in range(4)] 
    time_decrypt = [[] for y in range(4)] 
    algoritma = ["Playfair-DNA", "Porta-DNA", "Vigenere-DNA", "AES"]
    count = 0
    for i in range(1,4) :
        for x in plaintext :
            a, ambiguity, time_x = test.encrypt_dna_time(x, kunci, i)
            time_encrypt[count].append(time_x)
            b, time_y = test.decrypt_dna(a, kunci, ambiguity, i)
            time_decrypt[count].append(time_y)
        count = count+1
    for x in plaintext :
        a, time_x = test.encrypt_regular(x, kunci, 1)
        time_encrypt[count].append(time_x)
        b, time_y = test.decrypt_regular(a, kunci,  1)
        time_decrypt[count].append(time_y)
    return time_encrypt, time_decrypt, algoritma


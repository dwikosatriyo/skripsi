import test
import timeit

def input_small (plaintext, kunci) :          
    time_encrypt = []
    time_decrypt = []
    ciphertext = []
    algoritma = ["Playfair", "Porta", "Vigenre", "AES"]
    a, ambiguity, time_x = test.encrypt_dna(plaintext, kunci, 1)
    b, time_y = test.decrypt_dna(a, kunci, ambiguity, 1)
    time_encrypt.append(time_x)
    time_decrypt.append(time_y)
    ciphertext.append(a)
    a, ambiguity, time_x = test.encrypt_dna(plaintext, kunci, 2)
    b, time_y = test.decrypt_dna(a, kunci, ambiguity, 2)
    time_encrypt.append(time_x)
    time_decrypt.append(time_y)
    ciphertext.append(a)
    a, ambiguity, time_x = test.encrypt_dna(plaintext, kunci, 3)
    b, time_y = test.decrypt_dna(a, kunci, ambiguity, 3)
    time_encrypt.append(time_x)
    time_decrypt.append(time_y)
    ciphertext.append(a)
    a, time_x = test.encrypt_regular(plaintext, kunci, 1)
    b, time_y = test.decrypt_regular(a, kunci, 1)
    time_encrypt.append(time_x)
    time_decrypt.append(time_y)
    ciphertext.append(a)
    return time_encrypt, time_decrypt, algoritma, ciphertext

def input (plaintext, kunci) :          
    time_encrypt = []
    time_decrypt = []
    algoritma = ["Playfair", "Porta", "Vigenre", "AES"]
    a, ambiguity, time_x = test.encrypt_dna(plaintext, kunci, 1)
    b, time_y = test.decrypt_dna(a, kunci, ambiguity, 1)
    time_encrypt.append(time_x)
    time_decrypt.append(time_y)
    a, ambiguity, time_x = test.encrypt_dna(plaintext, kunci, 2)
    b, time_y = test.decrypt_dna(a, kunci, ambiguity, 2)
    time_encrypt.append(time_x)
    time_decrypt.append(time_y)
    a, ambiguity, time_x = test.encrypt_dna(plaintext, kunci, 3)
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
    algoritma = ["Playfair", "Porta", "Vigenre", "AES"]
    count = 0
    for i in range(1,4) :
        for x in plaintext :
            a, ambiguity, time_x = test.encrypt_dna(x, kunci, i)
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


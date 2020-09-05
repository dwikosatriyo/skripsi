from proces import playfair_dna, pyaes, dna, playfair
from secretpy import Playfair
from secretpy import Vigenere
from secretpy import Porta
import timeit


class proteinp :
    def __init__ (self, protein, ambiguity):
        self.protein = protein
        self.ambiguity = ambiguity

def encrypt_dna (message, key, algorithm):
    if (algorithm==1):
        cipher = playfair
    elif(algorithm==2):
        cipher = Porta()
    elif (algorithm==3):
        cipher = Vigenere()
    else :
        return None
    result = cipher.encrypt(message.lower(), key.lower())
    return result
def encrypt_dna_time (message, key, algorithm):
    if (algorithm==1):
        cipher = playfair
    elif(algorithm==2):
        cipher = Porta()
    elif (algorithm==3):
        cipher = Vigenere()
    else :
        return None
    start = timeit.default_timer()
    a = dna.string_to_binary(message)
    a += "0"*(6-(len(a)%6))
    a = dna.binary_to_DNA(a)
    #melakukan encode dari biner ke dna sequence
    b = playfair_dna.DNA_to_protein(a) 
    result = cipher.encrypt(b.protein.lower(), key.lower())

    stop = timeit.default_timer()
    time = str(stop - start)
    return result, b.ambiguity, time

def decrypt_dna(chippertext, key, ambiguity, algorithm): 
    
    # print ("chippertext = ")
    # print (chippertext, end="")
    if (algorithm==1):
        cipher = playfair
    elif(algorithm==2):
        cipher = Porta()
    elif (algorithm==3):
        cipher = Vigenere()
    else :
        return None
    start = timeit.default_timer()  
    decrypt = cipher.decrypt(chippertext.lower(), key.lower())
    
    protein = proteinp(decrypt,ambiguity)
    a = playfair_dna.protein_to_DNA_amb (protein)
    b = dna.DNA_to_binary (a)
    b = b[:-(len(b)%8)]
    c = int(b, base =2)
    result = c.to_bytes((c.bit_length() + 7) // 8, 'big').decode()
    stop = timeit.default_timer()
    time = str(stop - start)
    return result, time

def encrypt_regular(plaintext, key, algorithm):
    if (algorithm == 1):
        if (len(key)<32):
            key = key+("a"*(32-len(key)))
    
    start = timeit.default_timer()
    key = str.encode(key)

    aes = pyaes.AESModeOfOperationCTR(key)
    plaintext = plaintext
    plaintext = str.encode(plaintext)
    ciphertext = aes.encrypt(plaintext)
    stop = timeit.default_timer()
    time = str(stop - start)
    return ciphertext, time
def decrypt_regular(ciphertext, key, algorithm):
    if (algorithm == 1):
        if (len(key)<32):
            key = key+("a"*(32-len(key)))
    start = timeit.default_timer()
    key = str.encode(key)

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted = aes.decrypt(ciphertext)
    stop = timeit.default_timer()
    time = str(stop - start)
    return decrypted, time
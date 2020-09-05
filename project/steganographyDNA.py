from proces import dna
import random, math
import binascii
import timeit
import os
from PIL import Image
ProteinLib = {'A': ['GCU', 'GCC', 'GCA', 'GCG'], 'B': ['UAA', 'UAG', 'UGA'], 'C': ['UGU', 'UGC'], 'D': ['GAU', 'GAC'], 'E': ['GAA', 'GAG'], 'F': ['UUU', 'UUC'], 'G': ['GGU', 'GGC', 'GGA', 'GGG'], 'H': ['CAU', 'CAC'], 'I': ['AUU', 'AUC', 'AUA'], 'K': ['AAA', 'AAG'], 'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], 'M': ['AUG'], 'N': ['AAU', 'AAC'], 'O': ['UUA', 'UUG'], 'P': ['CCU', 'CCC', 'CCA', 'CCG'], 'Q': ['CAA', 'CAG'], 'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'T': ['ACU', 'ACC', 'ACA', 'ACG'], 'U': ['AGA', 'AGG'], 'V': ['GUU', 'GUC', 'GUA', 'GUG'], 'W': ['UGG'], 'X': ['AGU', 'AGC'], 'Y': ['UAU', 'UAC'], 'Z': ['UAC']}
DNALib = {'GCU': ['A'], 'GCC': ['A'], 'GCA': ['A'], 'GCG': ['A'], 'UAA': ['B'], 'UAG': ['B'], 'UGA': ['B'], 'UGU': ['C'], 'UGC': ['C'], 'GAU': ['D'], 'GAC': ['D'], 'GAA': ['E'], 'GAG': ['E'], 'UUU': ['F'], 'UUC': ['F'], 'GGU':
['G'], 'GGC': ['G'], 'GGA': ['G'], 'GGG': ['G'], 'CAU': ['H'], 'CAC': ['H'], 'AUU': ['I'], 'AUC': ['I'], 'AUA': ['I'], 'AAA': ['K'], 'AAG': ['K'], 'UUA': ['L', 'O'], 'UUG': ['L', 'O'], 'CUU': ['L'], 'CUC': ['L'], 'CUA': ['L'], 'CUG': ['L'], 'AUG': ['M'], 'AAU': ['N'], 'AAC': ['N'], 'CCU': ['P'], 'CCC': ['P'], 'CCA': ['P'], 'CCG': ['P'], 'CAA': ['Q'], 'CAG': ['Q'], 'CGU': ['R'], 'CGC': ['R'], 'CGA': ['R'], 'CGG': ['R'], 'AGA': ['R',
'U'], 'AGG': ['R', 'U'], 'UCU': ['S'], 'UCC': ['S'], 'UCA': ['S'], 'UCG': ['S'], 'AGU': ['S', 'X'], 'AGC': ['S', 'X'], 'ACU': ['T'], 'ACC': ['T'], 'ACA': ['T'], 'ACG': ['T'], 'GUU': ['V'], 'GUC': ['V'], 'GUA': ['V'], 'GUG': ['V'], 'UGG': ['W'], 'UAU': ['Y'], 'UAC': ['Y', 'Z']}
dna = dna


def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

def subtitution_embed_detail(input, reference):
    input = input.encode()
    input_binary = "".join([bin(x)[2:].zfill(8) for x in input])
    #menkonversi plaintext ke binary
    plaintext_length = len(input_binary)
    reference_length = len(reference)
    dna_pair = {}
    dna_pair ["A"] = "U"
    dna_pair ["C"] = "A"
    dna_pair ["G"] = "C"
    dna_pair ["U"] = "G"
    
    rand_number = random.sample(range(1, reference_length), plaintext_length)
    rand_number.sort()
    hasil_steganografi = ""
    i = 1
    for dna in reference:
        # print(i)
        try:
            a = rand_number.index(i)
            pn = input_binary[a]
            if(pn == "1"):
                hasil_steganografi+=dna_pair[dna]
            else:
                hasil_steganografi+=dna
        except:
            c = dna_pair[dna]
            hasil_steganografi+=dna_pair[c[0]][0]
        i= i+1
    
    return input_binary, hasil_steganografi, rand_number

def subtitution_extract_detail(steganograph, reference):
    
    dna_pair = {}
    dna_pair ["A"] = "U"
    dna_pair ["C"] = "A"
    dna_pair ["G"] = "C"
    dna_pair ["U"] = "G"
    s = len(reference)
    r = len(steganograph)
    # print ("s = " + str(s))
    # print ("r = "+ str(r))
    m = ""
    for i in range(s):
        if (steganograph[i] == reference[i]):
            m = m+("0")
        elif (steganograph[i] == dna_pair[reference[i]]):
            m = m+("1")
        
        
    # int_m = int(m, base =2)
    result = bitstring_to_bytes(m)
    # bin_m = int_m.to_bytes((int_m.bit_length() + 7) // 8, 'big').decode()
    return result

def subtitution_embed(plaintext, reference):
    start = timeit.default_timer()
    bin_plaintext = "".join([bin(x)[2:].zfill(8) for x in plaintext])
    #menkonversi plaintext ke binary
    plaintext_length = len(bin_plaintext)
    reference_length = len(reference)
    dna_pair = {}
    dna_pair ["A"] = "U"
    dna_pair ["C"] = "A"
    dna_pair ["G"] = "C"
    dna_pair ["U"] = "G"
    
    rand_number = random.sample(range(1, reference_length), plaintext_length)
    rand_number.sort()
    final_dna = ""
    i = 1
    for dna in reference:
        # print(i)
        try:
            a = rand_number.index(i)
            pn = bin_plaintext[a]
            if(pn == "1"):
                final_dna+=dna_pair[dna]
            else:
                final_dna+=dna
        except:
            c = dna_pair[dna]
            final_dna+=dna_pair[c[0]][0]
        i= i+1
    
    stop = timeit.default_timer()
    time = str(stop - start)
    return final_dna, time



def subtitution_extract(steganograph, reference):
    start = timeit.default_timer()
    dna_pair = {}
    dna_pair ["A"] = "U"
    dna_pair ["C"] = "A"
    dna_pair ["G"] = "C"
    dna_pair ["U"] = "G"
    s = len(reference)
    r = len(steganograph)
    # print ("s = " + str(s))
    # print ("r = "+ str(r))
    m = ""
    for i in range(s):
        if (steganograph[i] == reference[i]):
            m = m+("0")
        elif (steganograph[i] == dna_pair[reference[i]]):
            m = m+("1")
        
        
    # int_m = int(m, base =2)
    result = bitstring_to_bytes(m)
    # bin_m = int_m.to_bytes((int_m.bit_length() + 7) // 8, 'big').decode()

    stop = timeit.default_timer()
    time = str(stop - start)
    return result, time


def insertion_embed(plaintext, reference):
    start = timeit.default_timer()
    bin_plaintext = "".join([bin(x)[2:].zfill(8) for x in plaintext])
    # print(bin_plaintext)
    bin_dna = dna.DNA_to_binary(reference)
    # print(bin_dna)
    plaintext_length = len(bin_plaintext)
    
    bin_dna_array = []
    num = 0
    for i in [bin_dna[i:i+3] for i in range(0, len(bin_dna), 3)]:
        bin_dna_array.append(bin_plaintext[num]+i)
        num+=1
        if(num == plaintext_length):
            break
    bin_stego_dna = "".join(bin_dna_array)
    stego_dna = dna.binary_to_DNA(bin_stego_dna)
    stop = timeit.default_timer()
    time = str(stop - start)
    return stego_dna, time


def insertion_extract(steganograph):
    start = timeit.default_timer()
    bin_steganograph = dna.DNA_to_binary(steganograph)
    bin_plaintext_array = []
    for i in [bin_steganograph[i:i+4] for i in range(0, len(bin_steganograph), 4)]:
        bin_plaintext_array.append(i[0])

    bin_plaintext = "".join(bin_plaintext_array)
    result = bitstring_to_bytes(bin_plaintext)
    stop = timeit.default_timer()
    time = str(stop - start)    
    return result, time

def get_pair (seq):
    dna_pair = {}
    dna_pair ["A"] = "U"
    dna_pair ["C"] = "A" 
    dna_pair ["G"] = "C"
    dna_pair ["U"] = "G"
    result_array = []
    for i in seq :
        result_array.append(dna_pair[i])
    result = "".join(result_array)
    return result
def get_longest_pair_length (sequence):
    x = 2
    # print(sequence)
    while True:
        check_final = {}
        check = {}
        exist = 0
        num = 0
        for i in [sequence[i:i+x] for i in range(0, len(sequence), 1)]:
            # i = AD
            if (len(i)<x):
                break
            check[i] = num
            num+=1
            
        for i in check:
            if get_pair(i) in check:
                # print ("%s [%s] , %s [%s]" % (i, check[i] , get_pair(i), check[get_pair(i)]))
                x+=1
                exist = 1
                break
        if exist == 0:
            # print("longest pair = %s" % str(x-1))
            break
    return (x-1)
def get_longest_pair (sequence):
    # print(sequence)
    longest_pair_length = get_longest_pair_length(sequence)
    longest_pair = []
    check_final = {}
    check = {}
    exist = 0
    num = 0
    
    for i in [sequence[i:(i+longest_pair_length)] for i in range(0, len(sequence), 1)]:
        # i = AD
        if (len(i)<longest_pair_length):
            break
            
        if (i in check):
            check[i].append(num)
        else:
            check[i] = []
            check[i].append(num)

        num+=1
        
        
    for i in check:
        if get_pair(i) in check:
            # print ("%s [%s] , %s [%s]" % (i, check[i] , get_pair(i), check[get_pair(i)]))
            longest_pair.extend(check[i])
            longest_pair.extend(check[get_pair(i)])
            break
    longest_pair.sort()
    # print(longest_pair)
    # print(longest_pair)
    # x = 2
    # # print(sequence)
    # while True:
    #     longest_pair = []
    #     check_final = {}
    #     check = {}
    #     exist = 0
    #     num = 0
        
    #     for i in [sequence[i:i+x] for i in range(0, len(sequence), 1)]:
    #         # i = AD
    #         if (len(i)<x):
    #             break
    #         check[i] = num
    #         num+=1
            
    #     for i in check:
    #         if get_pair(i) in check:
    #             # print ("%s [%s] , %s [%s]" % (i, check[i] , get_pair(i), check[get_pair(i)]))
    #             x+=1
    #             longest_pair.append(i)
    #             longest_pair.append(get_pair(i))
    #             exist = 1
    #             break
    #     if exist == 0:
    #         # print("longest pair = %s" % str(x-1))
    #         break
            
            
    # longest_pair_length = get_longest_pair_length(sequence)
    # print(longest_pair_length)
    # num = 0
    # check = {}
    # for i in [sequence[i:(i+longest_pair_length)] for i in range(0, len(sequence), 1)]:
    #     # i = AD
    #     if (len(i)<longest_pair_length):
    #         break
    #     check[i] = []
    #     check[i].append(num)
    #     num+=1    
    # position = []
    # for i in check:
    #     if get_pair(i) in check:
    #         print(i)
    #         for j in check[i]:
    #             position.append(j)
    #         for j in check[get_pair(i)]:
    #             position.append(j)
    # print(position)
    return longest_pair
    
def complementary_embed(plaintext, reference):
    # print(reference)
    start = timeit.default_timer()
    binary_dna = ['A', 'C', 'G', 'U']
    longest_pair = get_longest_pair_length(reference)
    # print(longest_pair)
    bin_plaintext = "".join([bin(x)[2:].zfill(8) for x in plaintext])
    dna_plaintext = dna.binary_to_DNA(bin_plaintext)
    len_dna_plaintext = len(dna_plaintext)
    insert_range = int((len(reference)-3)/len_dna_plaintext)
    loop = True
    
    while loop:
        padding_array = []
        temp_array = []
        for j in range (longest_pair+1):
            temp_1 = random.choice(binary_dna)
            temp_array.append(temp_1)
        temp = "".join(temp_array)
        padding_array.append(temp)
        padding_array.append(get_pair(temp))
        # print(padding_array[0])
        x = 3
        steganograph_array = []
        steganograph_array.append(reference[0:3])
        num = 0
        for i in dna_plaintext:
            # print(i,end="")
            steganograph_array.append(i)
            steganograph_array.append("U")
            steganograph_array.append(padding_array[num])
            steganograph_array.append("U")
            steganograph_array.append(reference[x:x+insert_range])
            num+=1
            if(num == 2):
                num = 0
            x+=insert_range
        # print()
        if(x<(len(dna_plaintext))):
            steganograph_array.append(reference[x:(len(reference))])
        # for i in A:
        #     # print(dna_plaintext[num],end="")
        #     steganograph_array.append(dna_plaintext[num])
        #     steganograph_array.append("U")
        #     steganograph_array.append(padding)
        #     steganograph_array.append("U")
        #     steganograph_array.append(reference[x:x+insert_range])
        #     num+=1
        #     x+=insert_range+1
        stego_dna = "".join(steganograph_array)
        # print(stego_dna)
        longest_pair_stego = get_longest_pair_length(stego_dna)
        if longest_pair_stego==longest_pair+1:
            loop = False

    stop = timeit.default_timer()
    time = str(stop - start)
    return stego_dna,time


def complementary_extract(steganograph):
    # print(steganograph)
    start = timeit.default_timer()
    position = get_longest_pair(steganograph)
    # print(steganograph[position[0]:position[0]+8])
    # print(steganograph[position[2]:position[2]+8])
    # print(len(position))
    # print(len(position))
    plaintext_array = []
    for i in position:
        plaintext_array.append(steganograph[(i-2)])
    # print(plaintext_array)
    # print(len(plaintext_array))
    plaintext_dna = "".join(plaintext_array)

    plaintext_binary = dna.DNA_to_binary(plaintext_dna)
    plaintext = bitstring_to_bytes(plaintext_binary)
    stop = timeit.default_timer()
    time = str(stop - start)
    return plaintext,time


def dna_to_img(seq, path):
    # dimension = ([640,360],[800,600],[1024,768],[1280,720],[1360,768])
    dimension = int(round(math.sqrt(len(seq)))+1)
    # print(dimension)
    img_size = [dimension,dimension]
    
    img = Image.new("RGB", img_size)
    pixels = img.load()
    num = 0
    temp = (0,0,0)
    i = 0
    j = 0
    for char in seq:
        # print(char)
        if char == "A" :
            temp = (255, 0, 0)
        elif char == "G" :
            temp = (0, 255, 0)
        elif char == "C" :
            temp = (0, 0, 255)
        elif char == "U" :
            temp = (255, 255, 0)
        pixels[i,j] = temp
        i+=1
        num+=1
        if(i==img_size[0]):
            j+=1
            i=0
    img.save(path)
    # for i in range(x):
    #     for j in range(y):
    #         # print(num)
    #         # print(seq[num])
    #         # break
    #         if seq[num] == "A" :
    #             temp = (0, 0, 100)
    #             print("dasd")
    #         elif seq[num] == "G" :
    #             temp = (0, 0, 2)
    #         elif seq[num] == "C" :
    #             temp = (0, 0, 3)
    #         elif seq[num] == "U" :
    #             temp = (0, 0, 4)
    #         pixels[i,j] = temp
    #         num+=1
    return img



def steganography_all(plaintext, reference):
    algorithm = ['Subtitution', 'Insertion', 'Complementary Rule']
    bin_plaintext = plaintext.encode()
    stego1s, time1s = subtitution_embed(bin_plaintext, reference)
    stego1e, time1e = subtitution_extract(stego1s, reference)
    stego2s, time2s = insertion_embed(bin_plaintext, reference)
    stego2e, time2e = insertion_extract(stego2s)
    stego3s, time3s = complementary_embed(bin_plaintext, reference)
    stego3e, time3e = complementary_extract(stego3s)


    # print(bin_plaintext)
    if(stego1e==bin_plaintext and stego2e==bin_plaintext and stego3e==bin_plaintext):
        pass
    else:
        print("False")
        return False
    stego = []
    time_s = [] 
    time_e = []
    img = []
    stego.extend((stego1s,stego2s,stego3s))
    time_s.extend((time1s,time2s,time3s))
    time_e.extend((time1e,time2e,time3e))
    img.append(reference)
    img.extend(stego)
    # img.append((dna_to_img(reference),dna_to_img(stego1s),dna_to_img(stego2s),dna_to_img(stego3s)))
    path = os.path.dirname(os.path.abspath(__file__))
    num = 0
    img_path = []
    for i in img:
        dna_to_img(i,path+"\\files\\img\\image"+str(num)+".jpg")
        img_path.append("image"+str(num)+".jpg")
        num+=1

    return algorithm, stego, time_s, time_e, img_path



def steganography_method(plaintext, reference, method):
    algorithm = ['Subtitution', 'Insertion', 'Complementary Rule']
    bin_plaintext = plaintext.encode()
    if (method==1):
        stego_s, time_s = subtitution_embed(bin_plaintext, reference)
        stego_e, time_e = subtitution_extract(stego_s, reference)
    elif(method==2):
        stego_s, time_s = insertion_embed(bin_plaintext, reference)
        stego_e, time_e = insertion_extract(stego_s)
    elif (method==3):
        stego_s, time_s = complementary_embed(bin_plaintext, reference)
        stego_e, time_e = complementary_extract(stego_s)
    else :
        return None
    algorithm_select = algorithm[method]
   
    
    stego_s, time_s = subtitution_embed(bin_plaintext, reference)
    stego_e, time_e = subtitution_extract(stego_s, reference)

    # print(bin_plaintext)
    if(stego_e==bin_plaintext):
        pass
    else:
        return False


    return stego_s, time_s, time_e



# with open("project/in.txt", "r") as f:
#     plaintext = f.read()
#     #membaca plaintext
# plaintext = "pesan"
# with open("project/1kb.dna", "r") as f2:
    reference = f2.read().replace('\n','') 


# algorithm, stego, time_s, time_e, img_path = steganography_all(plaintext, reference)

# stego_dna,time = complementary_embed(plaintext, reference)





# print(stego[1])
# print(stego[1])
# #membaca media penyembunyian
# path = os.path.dirname(os.path.abspath(__file__))
# img = dna_to_img(stego[1], path+"\\files\\img\\image"+str(999)+".jpg")
# img.show()
# steganograph, time = complementary_embed(plaintext,reference)

# extracted_message, time = complementary_extract(steganograph)
# # print ("extracted_message = %s" % extracted_message)
# if (plaintext == extracted_message ):
#     print("same")
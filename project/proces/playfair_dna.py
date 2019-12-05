from secretpy import Playfair
from secretpy import Vigenere
from secretpy import Porta
import timeit
ProteinLib = {}
ProteinLib["A"] = ["GCU","GCC","GCA","GCG"]
ProteinLib["B"] = ["UAA","UAG","UGA"]
ProteinLib["C"] = ["UGU","UGC"]
ProteinLib["D"] = ["GAU","GAC"]
ProteinLib["E"] = ["GAA","GAG"]
ProteinLib["F"] = ["UUU","UUC"]
ProteinLib["G"] = ["GGU","GGC","GGA","GGG"]
ProteinLib["H"] = ["CAU","CAC"]
ProteinLib["I"] = ["AUU","AUC","AUA"]
ProteinLib["K"] = ["AAA","AAG"]
ProteinLib["L"] = ["UUA","UUG","CUU","CUC","CUA","CUG"]
ProteinLib["M"] = ["AUG"]
ProteinLib["N"] = ["AAU","AAC"]
ProteinLib["O"] = ["UUA","UUG"]
ProteinLib["P"] = ["CCU","CCC","CCA","CCG"]
ProteinLib["Q"] = ["CAA","CAG"]
ProteinLib["R"] = ["CGU","CGC","CGA","CGG","AGA","AGG"]
ProteinLib["S"] = ["UCU","UCC","UCA","UCG","AGU","AGC"]
ProteinLib["T"] = ["ACU","ACC","ACA","ACG"]
ProteinLib["U"] = ["AGA","AGG"]
ProteinLib["V"] = ["GUU","GUC","GUA","GUG"]
ProteinLib["W"] = ["UGG"]
ProteinLib["X"] = ["AGU","AGC"]
ProteinLib["Y"] = ["UAU","UAC"]
ProteinLib["Z"] = ["UAC"]


DNALib = {'GCU': {'A': 0}, 'GCC': {'A': 1}, 'GCA': {'A': 2}, 'GCG': {'A': 3}, 'UAA': {'B': 0}, 'UAG': {'B': 1}, 'UGA': {'B': 2}, 'UGU': {'C': 0}, 'UGC': {'C': 1}, 'GAU': {'D': 0}, 'GAC': {'D': 1}, 'GAA': {'E': 0}, 'GAG': {'E':
1}, 'UUU': {'F': 0}, 'UUC': {'F': 1}, 'GGU': {'G': 0}, 'GGC': {'G': 1}, 'GGA': {'G': 2}, 'GGG': {'G': 3}, 'CAU': {'H': 0}, 'CAC': {'H': 1}, 'AUU': {'I': 0}, 'AUC': {'I': 1}, 'AUA': {'I': 2}, 'AAA': {'K': 0}, 'AAG': {'K': 1}, 'UUA': {'L': 0, 'O': 0}, 'UUG': {'L': 1, 'O': 1}, 'CUU': {'L': 2}, 'CUC': {'L': 3}, 'CUA': {'L': 4}, 'CUG': {'L': 5}, 'AUG': {'M': 0}, 'AAU': {'N': 0}, 'AAC': {'N': 1}, 'CCU': {'P': 0}, 'CCC': {'P': 1}, 'CCA': {'P': 2}, 'CCG': {'P': 3}, 'CAA': {'Q': 0}, 'CAG': {'Q': 1}, 'CGU': {'R': 0}, 'CGC': {'R': 1}, 'CGA': {'R': 2}, 'CGG': {'R': 3}, 'AGA': {'R': 4, 'U': 0}, 'AGG': {'R': 5, 'U': 1}, 'UCU': {'S': 0}, 'UCC': {'S': 1}, 'UCA': {'S': 2}, 'UCG': {'S': 3}, 'AGU': {'S': 4, 'X': 0}, 'AGC': {'S': 5, 'X': 1}, 'ACU': {'T': 0}, 'ACC': {'T': 1}, 'ACA': {'T': 2}, 'ACG': {'T': 3}, 'GUU': {'V': 0}, 'GUC': {'V': 1}, 'GUA': {'V': 2}, 'GUG': {'V': 3}, 'UGG': {'W': 0}, 'UAU': {'Y': 0}, 'UAC': {'Y': 1, 'Z': 0}}


class proteinp :
    def __init__ (self, protein, ambiguity):
        self.protein = protein
        self.ambiguity = ambiguity

def protein_to_DNA_amb (protein):
    seq = ""
    seqarray = []
    for i in range(len(protein.ambiguity)):
        # seq+=ProteinLib[protein.protein[i].upper()][protein.ambiguity[i]]
        seqarray.append(ProteinLib[protein.protein[i].upper()][protein.ambiguity[i]])
    seq = "".join(seqarray)
    return seq
def protein_to_DNA (protein):
    seq = ""
    for i in range(len(protein)):
        seq+=ProteinLib[protein.protein[i].upper()][0]
    return seq
def DNA_to_protein (seq):
    protein = ""
    proteinarray = []
    ambiguity = []
    for i in [seq[i:i+3] for i in range(0, len(seq), 3)]:
        for j in DNALib[i]:
            # protein=protein+j
            proteinarray.append(j)
            ambiguity.append(DNALib[i][j])
    protein = "".join(proteinarray)
    result = proteinp(protein,ambiguity)
    return result
def add_prefix(message):
    
    message += "0"*(6-(len(message)%6))
    return message
# def encrypt (message, key, algorithm):
    
#     a = dna.encode(message)
#     a += "0"*(6-(len(a)%6))
#     a = dna.binary_to_DNA(a)
#     #melakukan encode dari biner ke dna sequence
#     b = DNA_to_protein(a)
    
#     if (algorithm==1):
#         cipher = Playfair()
#     elif(algorithm==2):
#         cipher = Porta()
#     elif (algorithm==3):
#         cipher = Vigenere()
#     else :
#         return None
       
#     result = cipher.encrypt(b.protein.lower(), key.lower())
    
#     # result = protein_to_DNA(chippertext)
# #     return result, b.ambiguity
# def decrypt(chippertext, key, ambiguity, algorithm): 
     
#     if (algorithm==1):
#         cipher = Playfair()
#     elif(algorithm==2):
#         cipher = Porta()
#     elif (algorithm==3):
#         cipher = Vigenere()
#     else :
#         return None  
    
#     decrypt = cipher.decrypt(chippertext.lower(), key.lower())
#     start = timeit.default_timer()  
#     protein = proteinp(decrypt,ambiguity)
#     a = protein_to_DNA_amb (protein)
#     b = dna.DNA_to_binary (a)
#     b = b[:-(len(b)%8)]
#     c = int(b, base =2)
#     c = c.to_bytes((c.bit_length() + 7) // 8, 'big').decode()
#     stop = timeit.default_timer()
#     print("Vigenre : ")
#     print('Time: ', stop - start)  
#     return c
# def attach_ambiguity(seq, ambiguity):
#     result = ""
#     x = 0
#     # print (seq)
#     for i in ([seq[i:i+3] for i in range(0, len(seq), 3)]):
#         result = result+i+dna.binary_to_DNA(decimal_to_binary(ambiguity[x]))
#         x=x+1
#     return result
# def detach_ambiguity(seq):
#     result = ""
#     ambiguity = []
#     for i in [seq[i:i+4] for i in range(0, len(seq), 4)]:
#         result = result+(i[:-1])
#         x = i[-1]
#         x = dna.DNA_to_binary(x)
#         x = int(x, 2)
#         ambiguity.append(x)
#     print(ambiguity)
#     return result,ambiguity
def decimal_to_binary(dec):
    binary = bin(dec).replace("0b", "")
    if(len(binary)<2):
        binary = "0"+binary
    return binary
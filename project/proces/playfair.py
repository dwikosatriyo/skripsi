import re

def create_table(key):
    kunci = clean_key(key)
    alphabetlist = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in kunci:
        if i in alphabetlist:
            alphabetlist.remove(i)
    kunci.extend(alphabetlist)
    rows, cols = (5, 5) 
    kunci_box = {}
    x,y = (0,0)
    for i in kunci:
        kunci_box[i]=[x,y]
        y=y+1
        if y == 5:
            y = 0
            x = x+1
    # kunci_box = [[] for j in range(rows)] 
    # x=0
    # for i in range(rows):
    #     for j in range(cols):
    #         kunci_box[i].append(kunci[x])
    #         x=x+1
    return kunci_box

def swapSet(data):
    newSet = []
    i = 0
    tempSet = []
    for x in data: # X Y Z
        tempSet.append(x)
        i = i+1
        if i == 5:
            newSet.append(tempSet)
            tempSet = []
            i = 0
    return newSet
        
def clean_key(key):
    regex = re.compile('[^a-zA-Z]')
    kunci = regex.sub('', key)
    kunci_clean = []
    for i in kunci:
        if i not in kunci_clean:
            kunci_clean.append(i)
    return kunci_clean   

def encrypt(plaintext, key):
    plaintext = plaintext.lower()
    regex = re.compile('[^a-zA-Z]')
    plaintext = regex.sub('', plaintext)
    odd = 0
    if len(plaintext)%2!=0:
        plaintext=plaintext+"x"
        odd = 1
    kunci_box = create_table(key)
    pre_plaintext = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
    kunci_box_swap = swapSet(kunci_box)
    chippertextarray = []
    chippertext = ""
    for i in pre_plaintext:
        x1 = kunci_box[i[0]]
        x2 = kunci_box[i[1]]
        if x1 == x2 :
            c1 = kunci_box_swap[(x2[0]+1)%5][(x1[1]+1)%5]
            c2 = kunci_box_swap[(x1[0]+1)%5][(x2[1]+1)%5]
        elif x1[0] == x2[0]:
            c1 = kunci_box_swap[x2[0]][(x1[1]+1)%5]
            c2 = kunci_box_swap[x1[0]][(x2[1]+1)%5]
        elif x1[1] == x2[1]:
            c1 = kunci_box_swap[(x2[0]+1)%5][x1[1]]
            c2 = kunci_box_swap[(x1[0]+1)%5][x2[1]]
        else:
            c1 = kunci_box_swap[x1[0]][x2[1]]
            c2 = kunci_box_swap[x2[0]][x1[1]]
        chippertextarray.append(c1)
        chippertextarray.append(c2)
    chippertext = "".join(chippertextarray)
    if odd == 1:
        chippertext = chippertext+"x"
    return chippertext
    
def decrypt(chippertext, key):
    chippertext = chippertext.lower()
    regex = re.compile('[^a-zA-Z]')
    chippertext = regex.sub('', chippertext)
    odd = 0
    if(len(chippertext)%2!=0):
        chippertext=chippertext[:-1]
        odd = 1
    kunci_box = create_table(key)
    pre_chippertext = [chippertext[i:i+2] for i in range(0, len(chippertext), 2)]
    kunci_box_swap = swapSet(kunci_box)
    plaintextarray = []
    plaintext = ""
    for i in pre_chippertext:
        x1 = kunci_box[i[0]]
        x2 = kunci_box[i[1]]
        if x1 == x2 :
            c1 = kunci_box_swap[(x2[0]-1)%5][(x1[1]-1)%5]
            c2 = kunci_box_swap[(x1[0]-1)%5][(x2[1]-1)%5]
        elif x1[0] == x2[0]:
            c1 = kunci_box_swap[x2[0]][(x1[1]-1)%5]
            c2 = kunci_box_swap[x1[0]][(x2[1]-1)%5]
        elif x1[1] == x2[1]:
            c1 = kunci_box_swap[(x2[0]-1)%5][x1[1]]
            c2 = kunci_box_swap[(x1[0]-1)%5][x2[1]]
        else:
            c1 = kunci_box_swap[x1[0]][x2[1]]
            c2 = kunci_box_swap[x2[0]][x1[1]]
        plaintextarray.append(c1)
        plaintextarray.append(c2)
    plaintext = "".join(plaintextarray)
    if odd == 1:
        plaintext = plaintext[:-1]
    return plaintext
    

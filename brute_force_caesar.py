#program for brute forcing caesar cipher

cipher_text=input("Enter the cipher-text:")                                      #entering the cipher text
for j in range(1,26):                                                            #loop for brute forcing
    list_of_values=[]
    final=""
    for i in range(0,len(cipher_text)):
        cval=ord(cipher_text[i])
        cno=cval-j
        if cipher_text[i].islower():
            if cno<=96:
                cno=(cno)+26
            list_of_values.append(chr(cno))
        elif cipher_text[i].isupper():
            if cno<=64:
                cno=(cno)+26
            list_of_values.append(chr(cno))
        elif cipher_text[i].isspace:
            list_of_values.append(chr(cval))
        else:
            list_of_values.append(chr(cno))

    for i in list_of_values:
        final+=i
    print("Plain-Text, Assumption",j,final)                                      #printing all the values

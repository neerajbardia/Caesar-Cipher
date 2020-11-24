#menu driven program for encryption and decryption of plaintext
choice=int(input("Select \n 1. Encryption \n 2. Decryption \n Enter your choice:"))
if choice==1:
    plain_text=input("Enter the plain-text:")                              #input of plain text
    key=int(input("Enter the key:"))                                       #input of key
    list_of_values=[]
    final=""
    for i in range(0,len(plain_text)):
        cval=ord(plain_text[i])                                            #converting the individual letters of the plain text into ASCII
        cno=cval+key                                                       #converting into cipher text
        if plain_text[i].islower():                                        #flow if the letters are in lower case
            if cno>122:                                                    #rounding off the ASCII
                cno=(cno % 122)+96                            
            list_of_values.append(chr(cno))
        elif plain_text[i].isupper():                                      #flow if the letters are in upper case
            if cno>90:                                                     #rounding off the ASCII
                cno=(cno % 90)+64
            list_of_values.append(chr(cno))
        elif plain_text[i].isspace():                                      #ignoring the spaces
            list_of_values.append(chr(cval))
        else:
            list_of_values.append(chr(cno))

    for i in list_of_values:
        final+=i
    print("Cipher-Text:",final)                                            #printing the final cipher text
    
  
elif choice==2:
    cipher_text=input("Enter the cipher-text:")                            #input the cipher text
    key=int(input("Enter the key:"))                                       #input the key to decrypt
    list_of_values=[] 
    final=""
    for i in range(0,len(cipher_text)):
        cval=ord(cipher_text[i])
        cno=cval-key
        if cipher_text[i].islower():                                        
            if cno<=96:
                cno=(cno)+26
            list_of_values.append(chr(cno))
        elif cipher_text[i].isupper():
            if cno<=64:
                cno=(cno)+26
            list_of_values.append(chr(cno))
        elif cipher_text[i].isspace():
            list_of_values.append(chr(cval))
        else:
            list_of_values.append(chr(cno))

    for i in list_of_values:
        final+=i
    print("Plain-Text:",final)                                              #printing the final plain text after decryption

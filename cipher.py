# alfabeto
alpha = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# Cifrado Cesar
def CeasarCipher(text, jmp):
    resultado = ""
    for i in range(len(text)):
        if text[i]==" ":
            resultado += "$"
            continue
        elif text[i] not in alpha:
            resultado += text[i]
            continue

        pos = alpha.index(text[i]) + jmp
        if pos>=len(alpha) : pos -= len(alpha)
        resultado += alpha[pos]
    
    return resultado

# Cifrado Octal Code
def OctalCode(text, jmp):
    resultado = ""
    for i in range(len(text)):
        if text[i] in alpha:
            pos = alpha.index(text[i]) + jmp
            if pos>=len(alpha) : pos -= len(alpha)
            resultado += str(oct(ord(alpha[pos]))[2:]) + ' '
            continue
        resultado += str(oct(ord(text[i]))[2:]) + ' '
        
    return resultado

# Decifrado Octal Code
def Octal_Decipher_To_Ceasar(text, jmp):
    resultado = ""
    text = text.split()

    for i in range(len(text)):
        char = chr(int(text[i], 8))
        if char in alpha:
            pos = alpha.index(char) - jmp
            if pos<0 : pos += len(alpha)
            resultado += alpha[pos]
            continue

        resultado += char
        
    return resultado

# Decifrado Cesar
def Ceasar_Decipher(text, jmp):
    resultado = ""
    for i in range(len(text)):
        if text[i]=="$":
            resultado+=" "
            continue
        if text[i] in alpha:
            pos = alpha.index(text[i]) - jmp
            if pos<0 : pos += len(alpha)
            resultado += alpha[pos]
            continue
        resultado += text[i]

    return resultado
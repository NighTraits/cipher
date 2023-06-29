import streamlit as st
from cipher import *
import hydralit as hy
from streamlit_extras.stateful_button import button
from streamlit_extras.metric_cards import style_metric_cards

# components
st.set_page_config(layout='wide')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

codeCrypt = '''
ceasarCrypt = CeasarCipher(msg,ceasarJmp)
octalCrypt = OctalCode(ceasarCrypt, octalJmp)

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
'''
CodeDecrypt = '''
ceasarDecrypt = Octal_Decipher_To_Ceasar(msgCrypt, octalJmp)
msgDecrypt = Ceasar_Decipher(ceasarDecrypt, ceasarJmp)

# alfabeto
alpha = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

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
'''
# code
app = hy.HydraApp(title='Simple Multi-Page App')
@app.addapp()
def Encriptar():
    input1, input2, input3 = st.columns([2, 1, 1])
    msg = input1.text_input('Mensaje a encriptar')
    ceasarJmp = input2.number_input('Saltos Cesar', min_value=0, max_value=10, value=0, step=1)
    octalJmp = input3.number_input('Saltos OctalCode', min_value=0, max_value=10, value=0, step=1)
    if msg and ceasarJmp>=0 and octalJmp>=0:
        ceasarCrypt = CeasarCipher(msg,ceasarJmp)
        octalCrypt = OctalCode(ceasarCrypt, octalJmp)
        r1, r2 = st.columns([2,2])
        with r1:
            r1.metric(label="CESAR", value=ceasarCrypt)
            r1.metric(label="OCTALCODE", value=octalCrypt)
            style_metric_cards()
        with r2:
            if button("Mostrar codigo", key="button1"):
                st.code(codeCrypt, language='python')
    else:
        hy.info('Campos vacíos')

@app.addapp()
def Desencriptar():
    input1, input2, input3 = st.columns([2, 1, 1])
    msgCrypt = input1.text_input('Mensaje a desencriptar')
    ceasarJmp = input2.number_input('Saltos Cesar', min_value=0, max_value=10, value=0, step=1)
    octalJmp = input3.number_input('Saltos OctalCode', min_value=0, max_value=10, value=0, step=1)
    if msgCrypt and ceasarJmp>=0 and octalJmp>=0:
        ceasarDecrypt = Octal_Decipher_To_Ceasar(msgCrypt, octalJmp)
        msgDecrypt = Ceasar_Decipher(ceasarDecrypt, ceasarJmp)
        r1, r2 = st.columns([2,2])
        with r1:
            r1.metric(label="CESAR", value=ceasarDecrypt)
            r1.metric(label="OCTALCODE", value=msgDecrypt)
            style_metric_cards()
        with r2:
            if button("Mostrar codigo", key="button1"):
                st.code(CodeDecrypt, language='python')
    else:
        hy.info('Campos vacíos')

app.run()

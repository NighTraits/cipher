import streamlit as st
import hydralit_components as hc
from cipher import *

st.set_page_config(layout='wide')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.header('Parcial N°3')
menu_data = [{'label':"Encriptar"},{'label':"Desencriptar"}]

menu_id = hc.nav_bar(menu_definition=menu_data)

# st.info(f"{menu_id=}")
if menu_id=='Encriptar':
    msg = st.text_input('Mensaje a encriptar')
    ceasarJmp = st.number_input('Saltos para Cifrado Cesar', min_value=0, max_value=10, value=0, step=1)
    octalJmp = st.number_input('Saltos para Cifrado OctalCode', min_value=0, max_value=10, value=0, step=1)

    if st.button('Encriptar'):
        if msg and ceasarJmp and octalJmp:
            st.write('encriptado')
            ceasarCrypt = CeasarCipher(msg,ceasarJmp)
            octalCrypt = OctalCode(ceasarCrypt, octalJmp)
            st.write(ceasarCrypt)
            st.write(octalCrypt)
        else:
            st.write('Campos vacíos')

if menu_id=='Desencriptar': 
    msgCrypt = st.text_input('Mensaje a desencriptar')
    ceasarJmp = st.number_input('Saltos para Cifrado Cesar', min_value=0, max_value=10, value=0, step=1)
    octalJmp = st.number_input('Saltos para Cifrado OctalCode', min_value=0, max_value=10, value=0, step=1)
    if st.button('Desencriptar'):
        if msgCrypt:
            ceasarDecrypt = Octal_Decipher_To_Ceasar(msgCrypt, octalJmp)
            msgDecrypt = Ceasar_Decipher(ceasarDecrypt, ceasarJmp)
            st.write(ceasarDecrypt)
            st.write(msgDecrypt)
        else:
            st.write('Campos vacíos')


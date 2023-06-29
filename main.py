import streamlit as st
import pandas as pd
import plost
import hydralit_components as hc


st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


menu_data = [
    {'label':"Left End"},
    {'label':"Book"},
    {'label':"Component"},
    {'label':"Dashboard"},
    {'label':"Right End"},
]

menu_id = hc.nav_bar(menu_definition=menu_data)

st.info(f"{menu_id=}")

st.title('Parcial N°3')

msj = st.text_input('Mensaje a encriptar')
ceasarJmp = st.text_input('Saltos para Cifrado Cesar')
octalJmp = st.text_input('Saltos para Cifrado OctalCode')

if st.button('Encriptar'):
    if msj and ceasarJmp and octalJmp:
        st.write('encriptado')
        # have_it = animal.lower() in animal_shelter
        # 'We have that animal!' if have_it else 'We don\'t have that animal.'
    else:
        st.write('Campos vacíos')


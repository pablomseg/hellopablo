# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:36:23 2026

@author: Pablo
"""

import streamlit as st

st.set_page_config(page_title="Hello Streamlit", page_icon="👋")

st.title("Hola, mundo")
st.write("Esta es mi primera app en Streamlit.")

nombre = st.text_input("Tu nombre", value="Pablo")

if st.button("Saludar"):
    st.success(f"Hola, {nombre} 👋")

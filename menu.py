import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.title("🍴 Menú del Día - Restaurante")

nombre = st.text_input("Nombre del Cliente:")
mesa = st.selectbox("Seleccione su Mesa:", ["Mesa 1", "Mesa 2", "Mesa 3", "Mesa 4"])
entrada = st.radio("Entrada:", ["Ensalada", "Sopa del día", "Ceviche"])
segundo = st.radio("Segundo:", ["Lomo Saltado", "Pollo al Horno", "Pescado Frito"])
bebida = st.selectbox("Bebida:", ["Chicha Morada", "Limonada", "Gaseosa"])

from streamlit_gsheets import GSheetsConnection

# ... (tus selectores nombre, mesa, entrada, etc., se mantienen igual)

if st.button("Enviar Pedido"):
    if nombre:
        # 1. Crear el nuevo pedido con los datos de tu formulario
        nuevo_pedido = {
            "Fecha": datetime.now().strftime("%d/%m/%Y"),
            "Hora": datetime.now().strftime("%H:%M:%S"),
           # Código corregido para la nube
        try:
            # Conexión con los Secrets que acabas de guardar
            conn = st.connection("gsheets", type=GSheetsConnection)
            
            # Leer datos que ya existan en la hoja
            df_existente = conn.read()
            
            # Sumar el nuevo pedido
            df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)
            
            # Subir todo a tu Google Sheet
            conn.update(data=df_final)
            
            st.success(f"✅ ¡Pedido de {nombre} guardado en Google Sheets!")
            st.balloons()
            
        except Exception as e:
            st.error(f"Error: {e}. Revisa que los nombres de las columnas coincidan.")
    else:
        st.error("⚠️ Por favor, escribe el nombre del cliente.")

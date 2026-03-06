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
        # 1. Crear el nuevo pedido (Asegúrate de que todas las llaves se cierren)
        nuevo_pedido = {
            "Fecha": datetime.now().strftime("%d/%m/%Y"),
            "Hora": datetime.now().strftime("%H:%M:%S"),
            "Cliente": nombre,
            "Mesa": mesa,
            "Entrada": entrada,
            "Segundo": segundo,
            "Bebida": bebida
        } # <--- Esta es la llave que faltaba cerrar
        
        df_nuevo = pd.DataFrame([nuevo_pedido])

        try:
            # 2. Conexión con los Secrets
            conn = st.connection("gsheets", type=GSheetsConnection)
            
            # 3. Leer y actualizar
            df_existente = conn.read()
            df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)
            
            # 4. Subir a Google Sheets
            conn.update(data=df_final)
            
            st.success(f"✅ ¡Pedido de {nombre} guardado en Google Sheets!")
            st.balloons()
            
        except Exception as e:
            st.error(f"Error al guardar: {e}")
    else:
        st.error("⚠️ Por favor, escribe el nombre del cliente.")

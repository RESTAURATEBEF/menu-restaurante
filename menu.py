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

if st.button("Enviar Pedido"):
    if nombre:
        nuevo_pedido = {
            "Fecha": datetime.now().strftime("%d/%m/%Y"),
            "Hora": datetime.now().strftime("%H:%M:%S"),
            "Cliente": nombre, "Mesa": mesa,
            "Entrada": entrada, "Segundo": segundo, "Bebida": bebida
        }
        df_nuevo = pd.DataFrame([nuevo_pedido])
        # Esto lo guarda directo en tu escritorio
        ruta = os.path.join(os.path.expanduser("~"), "Desktop", "pedidos_restaurante.xlsx")

        if os.path.exists(ruta):
            df_existente = pd.read_excel(ruta)
            df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)
        else:
            df_final = df_nuevo

        df_final.to_excel(ruta, index=False)
        st.success(f"✅ ¡Pedido de {nombre} guardado en Excel!")
        st.balloons()
    else:
        st.error("⚠️ Por favor, escribe el nombre del cliente.")
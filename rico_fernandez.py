import streamlit as st
import urllib.parse

# ---------------------------------------------------------
# CONFIGURACIÓN GENERAL DEL RESTAURANTE
# ---------------------------------------------------------
NOMBRE_RESTAURANTE = "RICO FERNANDEZ"
TELEFONO_WHATSAPP = "51918539634"  # Código de país Perú (51) + Tu Número

# Configuración de página optimizada para celulares
st.set_page_config(
    page_title=f"{NOMBRE_RESTAURANTE} - Menú Digital", 
    page_icon="🍽️",
    layout="centered"
)

# Encabezado
st.title(f"🍽️ {NOMBRE_RESTAURANTE}")
st.caption("¡Haz tu pedido desde tu mesa de forma rápida y sencilla!")

st.divider()

# ---------------------------------------------------------
# 1. SELECCIÓN DE MESA (1 A 7)
# ---------------------------------------------------------
mesa_seleccionada = st.selectbox(
    "📌 Selecciona tu número de mesa:",
    ["Mesa 1", "Mesa 2", "Mesa 3", "Mesa 4", "Mesa 5", "Mesa 6", "Mesa 7"]
)

st.divider()

# ---------------------------------------------------------
# 2. CARTA / MENÚ DEL DÍA (Edita esta lista diariamente)
# ---------------------------------------------------------
entradas_disponibles = ["Ninguna", "Papa a la Huancaína", "Sopa Minestrone", "Ensalada Fresca", "Sopa de Dieta"]
segundos_disponibles = ["Ninguno", "Lomo Saltado", "Arroz con Pollo", "Milanesa de Pollo", "Seco de Res", "Chicharron de Pescado"]
bebidas_disponibles = ["Ninguna", "Chicha Morada 1L", "Inca Kola 1.5L", "Limonada 1L", "Gaseosa Personal", "Agua Mineral"]

st.subheader("📋 Selecciona tus Platos")

# Seleccionar Entrada
col_e1, col_e2 = st.columns([3, 1])
with col_e1:
    entrada = st.selectbox("1. Entrada:", entradas_disponibles)
with col_e2:
    cant_entrada = st.number_input("Cant.", min_value=1, max_value=10, value=1, key="cant_e") if entrada != "Ninguna" else 0

# Seleccionar Segundo
col_s1, col_s2 = st.columns([3, 1])
with col_s1:
    segundo = st.selectbox("2. Segundo:", segundos_disponibles)
with col_s2:
    cant_segundo = st.number_input("Cant.", min_value=1, max_value=10, value=1, key="cant_s") if segundo != "Ninguno" else 0

# Seleccionar Bebida
col_b1, col_b2 = st.columns([3, 1])
with col_b1:
    bebida = st.selectbox("3. Bebida:", bebidas_disponibles)
with col_b2:
    cant_bebida = st.number_input("Cant.", min_value=1, max_value=10, value=1, key="cant_b") if bebida != "Ninguna" else 0

# Observaciones especiales (opcional para el cliente)
observaciones = st.text_input("📝 Observaciones (Opcional):", placeholder="Ej: Sin cebolla, poco arroz, bien cocido...")

st.divider()

# ---------------------------------------------------------
# 3. PROCESAR Y GENERAR MENSAJE PARA WHATSAPP
# ---------------------------------------------------------
if st.button("📲 CONFIRMAR Y ENVIAR PEDIDO", type="primary", use_container_width=True):
    # Validación: Debe elegir al menos 1 producto
    if entrada == "Ninguna" and segundo == "Ninguno" and bebida == "Ninguna":
        st.error("⚠️ Por favor selecciona al menos un plato o bebida antes de enviar.")
    else:
        # Armar el texto estructurado del pedido
        texto_pedido = f"¡Nuevo Pedido - {NOMBRE_RESTAURANTE}!\n"
        texto_pedido += f"📌 *Mesa:* {mesa_seleccionada}\n"
        
        if entrada != "Ninguna":
            texto_pedido += f"🍲 *Entrada:* {cant_entrada}x {entrada}\n"
        if segundo != "Ninguno":
            texto_pedido += f"🥩 *Segundo:* {cant_segundo}x {segundo}\n"
        if bebida != "Ninguna":
            texto_pedido += f"🥤 *Bebida:* {cant_bebida}x {bebida}\n"
            
        if observaciones.strip():
            texto_pedido += f"📝 *Obs:* {observaciones}\n"

        # Formatear el mensaje para enlace URL de WhatsApp
        mensaje_enc = urllib.parse.quote(texto_pedido)
        url_whatsapp = f"https://wa.me/{TELEFONO_WHATSAPP}?text={mensaje_enc}"

        # Presentación al usuario
        st.success("✅ ¡Pedido listo para enviar!")
        st.link_button("👉 Clic aquí para enviar mensaje a WhatsApp", url_whatsapp, use_container_width=True)
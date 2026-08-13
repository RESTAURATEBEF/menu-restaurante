import urllib.parse
import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="RICO FERNANDEZ - Menú", page_icon="🍔", layout="centered"
)

# 2. Estilos CSS Personalizados (Diseño Dark & Neon inspirado en MENU AI)
st.markdown(
    """
    <style>
    /* Fondo general oscuro estilo Charcoal/OLED */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    
    /* Ocultar barra superior por defecto de Streamlit */
    header {visibility: hidden;}

    /* Encabezado principal estilizado */
    .main-title {
        color: #FF7A00;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        font-size: 2.2rem;
        text-align: center;
        text-shadow: 0px 0px 18px rgba(255, 122, 0, 0.5);
        margin-bottom: 0px;
    }
    
    .sub-title {
        color: #9CA3AF;
        text-align: center;
        font-size: 0.95rem;
        margin-bottom: 25px;
    }

    /* Subtítulos de secciones */
    h3 {
        color: #F3F4F6 !important;
        font-size: 1.2rem !important;
        margin-top: 15px !important;
    }

    /* Cajas de selección (Selectbox) y Textarea con borde neón al enfocar */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #161B22 !important;
        border: 1px solid #30363D !important;
        border-radius: 10px !important;
        color: #FFFFFF !important;
    }

    .stTextArea textarea {
        background-color: #161B22 !important;
        border: 1px solid #30363D !important;
        border-radius: 10px !important;
        color: #FFFFFF !important;
    }

    /* Botón Principal (Naranja Neón brillante) */
    .stButton > button {
        background: linear-gradient(135deg, #FF7A00 0%, #FF5500 100%) !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 24px !important;
        width: 100% !important;
        box-shadow: 0px 4px 20px rgba(255, 122, 0, 0.5) !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 6px 25px rgba(255, 122, 0, 0.8) !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. Encabezado de la aplicación
st.markdown(
    '<p class="main-title">🍴 RICO FERNANDEZ</p>', unsafe_allow_html=True
)
st.markdown(
    '<p class="sub-title">¡Haz tu pedido desde tu mesa de forma rápida y sencilla!</p>',
    unsafe_allow_html=True,
)

st.divider()

# 4. Datos del Menú (Puedes modificar los platillos aquí)
mesas = [f"Mesa {i}" for i in range(1, 16)]
entradas = ["Ninguna", "Sopa Wonton", "Tequeños de Queso", "Causa Rellena"]
segundos = [
    "Ninguno",
    "Lomo Saltado",
    "Pollo a la Brancha",
    "Arroz Chaufa",
    "Tallarín Saltado",
]
bebidas = ["Ninguna", "Inca Kola 500ml", "Coca Cola 500ml", "Chicha Morada 1L"]

# 5. Formulario de Pedido
st.markdown("### 📍 Selección de Mesa")
mesa = st.selectbox("Selecciona tu número de mesa:", mesas)

st.markdown("### 📋 Selección de Platillos")
entrada = st.selectbox("1. Entrada:", entradas)
segundo = st.selectbox("2. Segundo:", segundos)
bebida = st.selectbox("3. Bebida:", bebidas)

observaciones = st.text_area(
    "📝 Observaciones (Opcional):",
    placeholder="Ej: Sin cebolla, poco arroz, bien cocido...",
)

st.divider()

# 6. Botón de Confirmación y Enviar por WhatsApp
if st.button("📲 CONFIRMAR Y ENVIAR PEDIDO"):
    # Validación básica
    if (
        entrada == "Ninguna"
        and segundo == "Ninguno"
        and bebida == "Ninguna"
    ):
        st.warning("⚠️ Por favor, selecciona al menos un producto para enviar tu pedido.")
    else:
        # Construcción del mensaje para WhatsApp
        mensaje = f"*NUEVO PEDIDO - RICO FERNANDEZ*\n"
        mensaje += f"📍 *{mesa}*\n\n"
        if entrada != "Ninguna":
            mensaje += f"• *Entrada:* {entrada}\n"
        if segundo != "Ninguno":
            mensaje += f"• *Segundo:* {segundo}\n"
        if bebida != "Ninguna":
            mensaje += f"• *Bebida:* {bebida}\n"
        if observaciones.strip():
            mensaje += f"• *Obs:* {observaciones.strip()}\n"

        # Número de WhatsApp destino (Ingresa tu número aquí con código de país, ej: 519XXXXXXXX)
        numero_whatsapp = "51918539634"  # <-- REEMPLAZA ESTE NÚMERO

        mensaje_codificado = urllib.parse.quote(mensaje)
        url_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensaje_codificado}"

        st.success("✅ ¡Pedido generado con éxito!")
        st.markdown(
            f"""
            <a href="{url_whatsapp}" target="_blank">
                <button style="
                    background-color: #25D366;
                    color: white;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 10px;
                    font-weight: bold;
                    width: 100%;
                    font-size: 16px;
                    cursor: pointer;
                    margin-top: 10px;">
                    💬 Abrir WhatsApp para enviar Pedido
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )

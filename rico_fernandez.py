import urllib.parse
import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="RICO FERNANDEZ - Menú Digital",
    page_icon="🍔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Estilos CSS Personalizados (Diseño Dark & Neon Premium con Banner)
st.markdown(
    """
    <style>
    /* Fondo general oscuro Charcoal Premium */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Ocultar elementos por defecto de Streamlit */
    header {visibility: hidden;}
    [data-testid="stSidebar"] {visibility: hidden;}

    /* Contenedor principal */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
    }

    /* Header y Título principal */
    .header-container {
        text-align: center;
        margin-bottom: 0px;
    }

    .main-title {
        color: #FF7A00;
        font-weight: 800;
        font-size: 2.5rem;
        text-shadow: 0px 0px 20px rgba(255, 122, 0, 0.7);
        margin-bottom: 0px;
        letter-spacing: 1.5px;
    }
    
    .sub-title {
        color: #9CA3AF;
        font-size: 1.0rem;
        margin-top: -5px;
        margin-bottom: 20px;
        font-weight: 300;
    }

    /* Banner superior con tus platos reales */
    .food-banner-container {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-top: 10px;
        margin-bottom: 25px;
        border-radius: 20px;
        padding: 12px 5px;
        background: linear-gradient(180deg, rgba(30, 35, 45, 1) 0%, rgba(14, 17, 23, 1) 100%);
        border: 1px solid #2E3440;
    }

    .food-item {
        text-align: center;
        width: 30%;
    }

    .food-item img {
        width: 85px;
        height: 85px;
        object-fit: cover;
        border-radius: 50%;
        box-shadow: 0px 0px 15px rgba(255, 122, 0, 0.4);
        border: 3px solid rgba(255, 122, 0, 0.6);
        transition: transform 0.3s ease;
    }

    .food-item-name {
        margin-top: 8px;
        font-size: 0.8rem;
        color: #F3F4F6;
        font-weight: 600;
        text-transform: uppercase;
    }

    /* Formularios y selectores */
    h3 {
        color: #F3F4F6 !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        margin-top: 15px !important;
        margin-bottom: 10px !important;
        border-bottom: 2px solid #FF7A00;
        display: inline-block;
        padding-bottom: 3px;
    }

    .stSelectbox div[data-baseweb="select"] {
        background-color: #1A1D24 !important;
        border: 1px solid #2E3440 !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
    }

    .stTextArea textarea {
        background-color: #1A1D24 !important;
        border: 1px solid #2E3440 !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
    }

    /* Botón Principal */
    .stButton > button {
        background: linear-gradient(135deg, #FF7A00 0%, #FF5500 100%) !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 14px 24px !important;
        width: 100% !important;
        box-shadow: 0px 5px 25px rgba(255, 122, 0, 0.5) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 8px 30px rgba(255, 122, 0, 0.8) !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. Encabezado principal
st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.markdown(
    '<p class="main-title">🍴 RICO FERNANDEZ</p>', unsafe_allow_html=True
)
st.markdown(
    '<p class="sub-title">Menú Digital & Pedidos</p>', unsafe_allow_html=True
)
st.markdown("</div>", unsafe_allow_html=True)

# 4. Banner superior con tus 3 imágenes reales subidas a GitHub
st.markdown(
    """
    <div class="food-banner-container">
        <div class="food-item">
            <img src="https://raw.githubusercontent.com/RESTAURATEBEF/menu-restaurante/main/aji_de_gallina.jpg" alt="Ají de Gallina">
            <p class="food-item-name">Ají de Gallina</p>
        </div>
        <div class="food-item">
            <img src="https://raw.githubusercontent.com/RESTAURATEBEF/menu-restaurante/main/lomo_saltado.jpg" alt="Lomo Saltado">
            <p class="food-item-name">Lomo Saltado</p>
        </div>
        <div class="food-item">
            <img src="https://raw.githubusercontent.com/RESTAURATEBEF/menu-restaurante/main/veciche.jpg" alt="Ceviche">
            <p class="food-item-name">Ceviche</p>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

st.divider()

# 5. Opciones del Menú
mesas = [f"Mesa {i}" for i in range(1, 16)]
entradas = ["Ninguna", "Causa Rellena", "Tequeños de Queso", "Sopa Wonton"]
segundos = [
    "Ninguno",
    "Ají de Gallina",
    "Lomo Saltado",
    "Ceviche de Pescado",
    "Pollo a la Brasa (1/4)",
    "Arroz Chaufa de Pollo",
    "Tallarín Saltado",
]
bebidas = ["Ninguna", "Inca Kola 500ml", "Coca Cola 500ml", "Chicha Morada 1L"]

# 6. Formulario de Selección
st.markdown("### 📍 Ubicación")
mesa = st.selectbox("Selecciona tu número de mesa:", mesas)

st.markdown("### 📋 Tu Orden")
entrada = st.selectbox("1. Entrada:", entradas)
segundo = st.selectbox("2. Segundo:", segundos)
bebida = st.selectbox("3. Bebida:", bebidas)

observaciones = st.text_area(
    "📝 Observaciones (Opcional):",
    placeholder="Ej: Sin cebolla, poco arroz, ají aparte...",
    height=80,
)

st.divider()

# 7. Confirmación y Enviar a WhatsApp
if st.button("🚀 CONFIRMAR Y ENVIAR PEDIDO"):
    if entrada == "Ninguna" and segundo == "Ninguno" and bebida == "Ninguna":
        st.warning(
            "⚠️ Por favor, selecciona al menos un producto para enviar tu pedido."
        )
    else:
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

        # Recuerda cambiar por tu número real de celular (Ej: 519XXXXXXXX)
        numero_whatsapp = "51918539634"

        mensaje_codificado = urllib.parse.quote(mensaje)
        url_whatsapp = (
            f"https://wa.me/{numero_whatsapp}?text={mensaje_codificado}"
        )

        st.success("✅ ¡Pedido generado con éxito!")
        st.markdown(
            f"""
            <a href="{url_whatsapp}" target="_blank">
                <button style="
                    background-color: #25D366;
                    color: white;
                    padding: 15px 20px;
                    border: none;
                    border-radius: 12px;
                    font-weight: bold;
                    width: 100%;
                    font-size: 17px;
                    cursor: pointer;
                    margin-top: 10px;
                    text-transform: uppercase;">
                    💬 Abrir WhatsApp para Enviar Pedido
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )

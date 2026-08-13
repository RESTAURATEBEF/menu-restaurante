import urllib.parse
import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="RICO FERNANDEZ - Menú Digital",
    page_icon="🍔",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Estilos CSS Personalizados Avanzados (Diseño Dark & Neon Premium con Banner)
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

    /* Contenedor principal de la tarjeta */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
    }

    /* --- ESTILO DEL HEADER Y TITULO --- */
    .header-container {
        text-align: center;
        margin-bottom: 0px;
        position: relative;
    }

    .main-title {
        color: #FF7A00; /* Naranja Neón Base */
        font-weight: 800;
        font-size: 2.8rem;
        text-shadow: 0px 0px 20px rgba(255, 122, 0, 0.7);
        margin-bottom: 0px;
        letter-spacing: 1.5px;
    }
    
    .sub-title {
        color: #9CA3AF;
        font-size: 1.0rem;
        margin-top: -10px;
        margin-bottom: 25px;
        font-weight: 300;
    }

    /* --- ESTILO DEL BANNER DE IMÁGENES LLAMATIVAS --- */
    .food-banner-container {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-top: 15px;
        margin-bottom: 30px;
        border-radius: 20px;
        padding: 10px;
        background: linear-gradient(180deg, rgba(30, 35, 45, 1) 0%, rgba(14, 17, 23, 1) 100%);
        border: 1px solid #2E3440;
    }

    .food-item {
        text-align: center;
        width: 28%;
    }

    .food-item img {
        width: 100%;
        height: auto;
        border-radius: 50%; /* Imágenes redondas estilo insignia */
        box-shadow: 0px 0px 15px rgba(255, 122, 0, 0.3);
        border: 3px solid rgba(255, 122, 0, 0.4);
        transition: transform 0.3s ease;
    }
    
    .food-item img:hover {
        transform: scale(1.1);
        box-shadow: 0px 0px 20px rgba(255, 122, 0, 0.6);
    }

    .food-item-name {
        margin-top: 8px;
        font-size: 0.8rem;
        color: #F3F4F6;
        font-weight: 600;
        text-transform: uppercase;
    }

    /* --- ESTILO DE LOS FORMULARIOS --- */
    h3 {
        color: #F3F4F6 !important;
        font-size: 1.25rem !important;
        font-weight: 700 !important;
        margin-top: 20px !important;
        margin-bottom: 10px !important;
        border-bottom: 2px solid #FF7A00;
        display: inline-block;
        padding-bottom: 3px;
    }

    /* Estilo para las cajas de input y selectbox */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #1A1D24 !important;
        border: 1px solid #2E3440 !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
        padding: 4px;
        transition: border 0.3s ease;
    }

    .stSelectbox div[data-baseweb="select"]:hover {
        border-color: #FF7A00 !important;
    }

    /* Estilo para el Textarea */
    .stTextArea textarea {
        background-color: #1A1D24 !important;
        border: 1px solid #2E3440 !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
        padding: 12px;
    }

    /* --- BOTÓN PRINCIPAL LLAMATIVO --- */
    .stButton > button {
        background: linear-gradient(135deg, #FF7A00 0%, #FF5500 100%) !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        font-size: 19px !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 15px 30px !important;
        width: 100% !important;
        box-shadow: 0px 5px 25px rgba(255, 122, 0, 0.5) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0px 8px 30px rgba(255, 122, 0, 0.8) !important;
    }
    
    /* Footer o divisor */
    hr {
        border-color: #2E3440 !important;
        margin-top: 30px !important;
    }

    </style>
""",
    unsafe_allow_html=True,
)

# --- 3. CONSTRUCCIÓN DE LA INTERFAZ VISUAL ---

# 3.1. Header con Título
st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.markdown('<p class="main-title">🍴 RICO FERNANDEZ</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Premium Restaurant & Delivery</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# 3.2. NUEVO BANNER SUPERIOR CON IMÁGENES LLAMATIVAS
# He seleccionado imágenes vibrantes y redondas para un toque profesional.
st.markdown(
    """
    <div class="food-banner-container">
        <!-- Imagen 1: Lomo Saltado -->
        <div class="food-item">
            <img src="https://raw.githubusercontent.com/fernandoceballos7/menudigital/main/lomo_saltado_vibrante.png" alt="Lomo Saltado">
            <p class="food-item-name">Lomo Saltado</p>
        </div>
        <!-- Imagen 2: Ceviche -->
        <div class="food-item">
            <img src="https://raw.githubusercontent.com/fernandoceballos7/menudigital/main/ceviche_premium.png" alt="Ceviche">
            <p class="food-item-name">Ceviche</p>
        </div>
        <!-- Imagen 3: Pollo a la Brasa -->
        <div class="food-item">
            <img src="https://raw.githubusercontent.com/fernandoceballos7/menudigital/main/pollo_vibrante.png" alt="Pollo Brasa">
            <p class="food-item-name">Pollo Brasa</p>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

st.divider()

# 4. Datos del Menú (Modificar platillos aquí)
mesas = [f"Mesa {i}" for i in range(1, 16)]
entradas = ["Ninguna", "Ceviche de Pescado", "Tequeños de Queso", "Sopa Wonton"]
segundos = [
    "Ninguno",
    "Lomo Saltado",
    "Pollo a la Brasa (1/4)",
    "Chaufa de Pollo",
    "Tallarín Saltado Carne",
]
bebidas = ["Ninguna", "Inca Kola 500ml", "Coca Cola 500ml", "Chicha Morada 1L"]

# 5. Formulario de Pedido Estilizado
st.markdown("### 📍 Ubicación")
mesa = st.selectbox("Selecciona tu número de mesa:", mesas)

st.markdown("### 📋 Tu Orden")
entrada = st.selectbox("1. Entrada:", entradas)
segundo = st.selectbox("2. Segundo:", segundos)
bebida = st.selectbox("3. Bebida:", bebidas)

observaciones = st.text_area(
    "📝 Observaciones (Opcional):",
    placeholder="Ej: Sin cebolla, poco arroz, bien cocido...",
    height=80
)

st.divider()

# 6. Botón de Confirmación y Enviar por WhatsApp
# Hemos hecho el botón más grande y con sombra más neón.
if st.button("🚀 CONFIRMAR Y ENVIAR PEDIDO"):
    # Validación básica
    if entrada == "Ninguna" and segundo == "Ninguno" and bebida == "Ninguna":
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

        # Número de WhatsApp destino (Reemplaza aquí tu número real)
        # Ingresa tu número con código de país, ej: 519XXXXXXXX)
        numero_whatsapp = "51900000000"  # <-- REEMPLAZA ESTE NÚMERO

        mensaje_codificado = urllib.parse.quote(mensaje)
        url_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensaje_codificado}"

        st.success("✅ ¡Pedido generado con éxito!")
        # Botón secundario para WhatsApp con diseño verde brillante
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
                    transition: all 0.3s ease;
                    text-transform: uppercase;">
                    💬 Enviar ahora a WhatsApp
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )

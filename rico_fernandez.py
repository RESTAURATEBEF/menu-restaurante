import urllib.parse
import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="RESTAURANT FERNANDEZ - Menú Digital",
    page_icon="🍔",
    layout="centered",
)


# 2. BASE DE DATOS GLOBAL EN MEMORIA (Compartida entre todos los usuarios)
@st.cache_resource
def obtener_menu_global():
    return {
        "entradas": ["Causa Rellena", "Tequeños de Queso", "Sopa Wonton"],
        "segundos": [
            "Ají de Gallina",
            "Lomo Saltado",
            "Ceviche de Pescado",
            "Pollo a la Brasa (1/4)",
            "Arroz Chaufa de Pollo",
        ],
        "bebidas": ["Inca Kola 500ml", "Coca Cola 500ml", "Chicha Morada 1L"],
    }


menu_global = obtener_menu_global()


# 3. Estilos CSS Personalizados
st.markdown(
    """
    <style>
    /* Fondo general oscuro Charcoal Premium */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    header {visibility: hidden;}

    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
    }

    /* Header centrado */
    .header-container {
        text-align: center;
        margin-bottom: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .sub-title {
        color: #9CA3AF;
        font-size: 1rem;
        margin-top: -8px;
        margin-bottom: 15px;
        font-weight: 300;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* Banner superior con platos */
    .food-banner-container {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-top: 5px;
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
        width: 90px;
        height: 90px;
        object-fit: cover;
        border-radius: 50%;
        box-shadow: 0px 0px 18px rgba(255, 122, 0, 0.4);
        border: 3px solid rgba(255, 122, 0, 0.6);
        transition: transform 0.3s ease;
    }

    /* Formulario */
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

    .stTextArea textarea, .stTextInput input {
        background-color: #1A1D24 !important;
        border: 1px solid #2E3440 !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
    }

    /* Botones */
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

# 4. Encabezado Curvado
st.markdown(
    """
    <div class="header-container">
        <svg width="100%" height="80" viewBox="0 0 600 80" xmlns="http://www.w3.org/2000/svg">
            <path id="curve" d="M 40 70 Q 300 15 560 70" fill="transparent"/>
            <text font-family="'Helvetica Neue', sans-serif" font-size="28" font-weight="900" fill="#FF7A00" letter-spacing="2">
                <textPath href="#curve" startOffset="50%" text-anchor="middle">
                    🍴 RESTAURANT FERNANDEZ
                </textPath>
            </text>
        </svg>
        <p class="sub-title">Menú Digital & Pedidos</p>
    </div>
""",
    unsafe_allow_html=True,
)

# 5. Banner de Fotos Reales (Solo imágenes decorativas sin texto)
st.markdown(
    """
    <div class="food-banner-container">
        <div class="food-item">
            <img src="https://raw.githubusercontent.com/RESTAURATEBEF/menu-restaurante/main/aji_de_gallina.jpg" alt="Plato decorativo 1">
        </div>
        <div class="food-item">
            <img src="https://raw.githubusercontent.com/RESTAURATEBEF/menu-restaurante/main/lomo_saltado.jpg" alt="Plato decorativo 2">
        </div>
        <div class="food-item">
            <img src="https://raw.githubusercontent.com/RESTAURATEBEF/menu-restaurante/main/veciche.jpg" alt="Plato decorativo 3">
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

st.divider()

# 6. Formulario del Cliente (Lee la lista global)
mesas = [f"Mesa {i}" for i in range(1, 16)]
lista_entradas = ["Ninguna"] + menu_global["entradas"]
lista_segundos = ["Ninguno"] + menu_global["segundos"]
lista_bebidas = ["Ninguna"] + menu_global["bebidas"]

st.markdown("### 📍 Ubicación")
mesa = st.selectbox("Selecciona tu número de mesa:", mesas)

st.markdown("### 📋 Tu Orden")
entrada = st.selectbox("1. Entrada:", lista_entradas)
segundo = st.selectbox("2. Segundo:", lista_segundos)
bebida = st.selectbox("3. Bebida:", lista_bebidas)

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
            "⚠️ Por favor, selecciona al menos un producto para enviar tu"
            " pedido."
        )
    else:
        mensaje = f"*NUEVO PEDIDO - RESTAURANT FERNANDEZ*\n"
        mensaje += f"📍 *{mesa}*\n\n"
        if entrada != "Ninguna":
            mensaje += f"• *Entrada:* {entrada}\n"
        if segundo != "Ninguno":
            mensaje += f"• *Segundo:* {segundo}\n"
        if bebida != "Ninguna":
            mensaje += f"• *Bebida:* {bebida}\n"
        if observaciones.strip():
            mensaje += f"• *Obs:* {observaciones.strip()}\n"

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

# 8. PANEL DE ADMINISTRACIÓN (Actualiza el menú de TODOS los usuarios)
st.write("")
st.write("")
st.divider()

with st.expander("🔑 Acceso Administrador (Actualizar Menú)"):
    clave_admin = st.text_input(
        "Ingresa la clave:", type="password", key="pwd_admin"
    )

    if clave_admin == "1234":
        st.success("🔓 Acceso concedido")
        st.caption("Escribe los platos del día separados por comas:")

        nuevas_entradas = st.text_area(
            "Entradas del Día:",
            value=", ".join(menu_global["entradas"]),
            height=80,
            key="txt_ent",
        )
        nuevos_segundos = st.text_area(
            "Segundos del Día:",
            value=", ".join(menu_global["segundos"]),
            height=100,
            key="txt_seg",
        )
        nuevas_bebidas = st.text_area(
            "Bebidas:",
            value=", ".join(menu_global["bebidas"]),
            height=80,
            key="txt_beb",
        )

        if st.button("💾 Guardar Menú del Día", key="btn_guardar"):
            menu_global["entradas"] = [
                e.strip() for e in nuevas_entradas.split(",") if e.strip()
            ]
            menu_global["segundos"] = [
                s.strip() for s in nuevos_segundos.split(",") if s.strip()
            ]
            menu_global["bebidas"] = [
                b.strip() for b in nuevas_bebidas.split(",") if b.strip()
            ]
            st.success("✅ ¡Menú actualizado para todos los clientes!")
            st.rerun()

    elif clave_admin != "":
        st.error("❌ Clave incorrecta")

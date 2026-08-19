import json
import os
import re
import urllib.parse
import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="RESTAURANT FERNANDEZ - Menú Digital",
    page_icon="🍔",
    layout="centered",
)

# ARCHIVO DE BASE DE DATOS LOCAL
ARCHIVO_MENU = "menu_db.json"

# Datos por defecto
DATOS_POR_DEFECTO = {
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


# 2. FUNCIONES DE LECTURA Y ESCRITURA EN DISCO
def cargar_menu():
    if not os.path.exists(ARCHIVO_MENU):
        guardar_menu(DATOS_POR_DEFECTO)
        return DATOS_POR_DEFECTO
    try:
        with open(ARCHIVO_MENU, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return DATOS_POR_DEFECTO


def guardar_menu(datos):
    with open(ARCHIVO_MENU, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)


# Carga dinámica del menú en cada renderizado
menu_actual = cargar_menu()

# 3. Estilos CSS Personalizados con Efecto 3D
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0A1128;
        color: #FFFFFF;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    header {visibility: hidden;}

    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
    }

    .header-container {
        text-align: center;
        margin-bottom: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .sub-title {
        color: #89CFF0;
        font-size: 1rem;
        margin-top: -8px;
        margin-bottom: 15px;
        font-weight: 300;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .food-banner-container {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-top: 5px;
        margin-bottom: 25px;
        border-radius: 20px;
        padding: 12px 5px;
        background: linear-gradient(180deg, #002244 0%, #0A1128 100%);
        border: 1px solid #0055A5;
        box-shadow: inset 0px 3px 5px rgba(255, 255, 255, 0.1), 0px 10px 20px rgba(0, 0, 0, 0.6);
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
        box-shadow: 0px 5px 15px rgba(0, 150, 255, 0.8), inset 0px 2px 4px rgba(255,255,255,0.4);
        border: 3px solid #00A8FF;
    }

    h3 {
        color: #FFFFFF !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        margin-top: 15px !important;
        margin-bottom: 10px !important;
        border-bottom: 2px solid #00A8FF;
        display: inline-block;
        padding-bottom: 3px;
    }

    /* EFECTO 3D PARA TODOS LOS SELECTBOX */
    div[data-baseweb="select"] > div {
        background-color: #1A2A4A !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
        
        border-top: 2px solid #4AA3FF !important;
        border-left: 2px solid #4AA3FF !important;
        border-bottom: 3px solid #001A3D !important;
        border-right: 3px solid #001A3D !important;
        
        box-shadow: 
            0px 8px 15px rgba(0, 0, 0, 0.6), 
            inset 0px 3px 6px rgba(255, 255, 255, 0.15) !important;
        
        transition: transform 0.1s ease, box-shadow 0.1s ease;
    }
    
    div[data-baseweb="select"] > div:active {
        transform: translateY(3px);
        box-shadow: 
            0px 2px 5px rgba(0, 0, 0, 0.6), 
            inset 0px 4px 8px rgba(0, 0, 0, 0.5) !important;
        border-top: 3px solid #001A3D !important;
        border-left: 3px solid #001A3D !important;
        border-bottom: 2px solid #4AA3FF !important;
        border-right: 2px solid #4AA3FF !important;
    }

    div[data-baseweb="select"] * {
        color: #FFFFFF !important;
    }

    /* EFECTO 3D PARA CAJAS DE TEXTO Y CONTRASEÑA */
    .stTextArea textarea, .stTextInput input {
        background-color: #1A2A4A !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
        
        border-top: 2px solid #4AA3FF !important;
        border-left: 2px solid #4AA3FF !important;
        border-bottom: 3px solid #001A3D !important;
        border-right: 3px solid #001A3D !important;
        
        box-shadow: 
            0px 8px 15px rgba(0, 0, 0, 0.6), 
            inset 0px 3px 6px rgba(255, 255, 255, 0.15) !important;
    }

    /* EFECTO 3D PARA PANEL DESPLEGABLE DE ADMINISTRADOR */
    div[data-testid="stExpander"] {
        background-color: #1A2A4A !important;
        border-radius: 14px !important;
        
        border-top: 2px solid #4AA3FF !important;
        border-left: 2px solid #4AA3FF !important;
        border-bottom: 3px solid #001A3D !important;
        border-right: 3px solid #001A3D !important;
        
        box-shadow: 
            0px 10px 20px rgba(0, 0, 0, 0.7), 
            inset 0px 2px 5px rgba(255, 255, 255, 0.1) !important;
    }

    div[data-testid="stTextArea"]:has(textarea[aria-label*="Observaciones"]) textarea {
        text-transform: uppercase !important;
    }

    /* EFECTO 3D PARA BOTONES */
    .stButton > button {
        background: linear-gradient(135deg, #0066FF 0%, #003399 100%) !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border-radius: 14px !important;
        padding: 14px 24px !important;
        width: 100% !important;
        text-transform: uppercase;
        
        border-top: 2px solid #89CFF0 !important;
        border-left: 2px solid #89CFF0 !important;
        border-bottom: 4px solid #001133 !important;
        border-right: 4px solid #001133 !important;
        
        box-shadow: 
            0px 10px 15px rgba(0, 0, 0, 0.6), 
            inset 0px 4px 6px rgba(255, 255, 255, 0.3) !important;
            
        transition: all 0.1s ease;
    }
    
    .stButton > button:active {
        transform: translateY(4px);
        box-shadow: 
            0px 2px 4px rgba(0, 0, 0, 0.6), 
            inset 0px 6px 10px rgba(0, 0, 0, 0.5) !important;
        border-top: 4px solid #001133 !important;
        border-left: 4px solid #001133 !important;
        border-bottom: 2px solid #89CFF0 !important;
        border-right: 2px solid #89CFF0 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 4. Encabezado Curvado (Con cubiertos al inicio y al final)
st.markdown(
    """
    <div class="header-container">
        <svg width="100%" height="80" viewBox="0 0 600 80" xmlns="http://www.w3.org/2000/svg">
            <path id="curve" d="M 40 70 Q 300 15 560 70" fill="transparent"/>
            <text font-family="'Helvetica Neue', sans-serif" font-size="26" font-weight="900" fill="#00A8FF" letter-spacing="2">
                <textPath href="#curve" startOffset="50%" text-anchor="middle">
                    🍴 RESTAURANT FERNANDEZ 🍴
                </textPath>
            </text>
        </svg>
        <p class="sub-title">Menú Digital & Pedidos</p>
    </div>
""",
    unsafe_allow_html=True,
)

# 5. Banner de fotos
st.markdown(
    """
    <div class="food-banner-container">
        <div class="food-item">
            <img src="https://raw.githubusercontent.com/RESTAURATEBEF/menu-restaurante/main/aji_de_gallina.jpg" alt="Plato 1">
        </div>
        <div class="food-item">
            <img src="https://raw.githubusercontent.com/RESTAURATEBEF/menu-restaurante/main/lomo_saltado.jpg" alt="Plato 2">
        </div>
        <div class="food-item">
            <img src="https://raw.githubusercontent.com/RESTAURATEBEF/menu-restaurante/main/veciche.jpg" alt="Plato 3">
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

st.divider()

# 6. Formulario del Cliente
mesas = [f"Mesa {i}" for i in range(1, 16)]

lista_entradas = ["Ninguna"] + menu_actual.get("entradas", [])
lista_segundos = ["Ninguno"] + menu_actual.get("segundos", [])
lista_bebidas = ["Ninguna"] + menu_actual.get("bebidas", [])

st.markdown("### 📍 Ubicación y Personas")
col_mesa, col_personas = st.columns(2)

with col_mesa:
    mesa = st.selectbox("Mesa:", mesas)

with col_personas:
    num_personas = st.selectbox(
        "¿Cuántos menús/personas son?",
        options=list(range(1, 11)),
        index=0,
    )

st.markdown("### 📋 Tu Orden")

pedidos_realizados = []

for i in range(num_personas):
    st.markdown(
        f"""
        <div style="
            color: #00A8FF; 
            font-size: 1.1rem; 
            font-weight: 800; 
            letter-spacing: 1.5px; 
            margin-top: 15px; 
            margin-bottom: 8px;
            text-transform: uppercase;">
            👤 PERSONA {i+1}
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        ent = st.selectbox(f"Entrada:", lista_entradas, key=f"ent_{i}")
    with col2:
        seg = st.selectbox(f"Segundo:", lista_segundos, key=f"seg_{i}")
    with col3:
        beb = st.selectbox(f"Bebida:", lista_bebidas, key=f"beb_{i}")

    pedidos_realizados.append({"entrada": ent, "segundo": seg, "bebida": beb})

# Observaciones Generales
obs_input = st.text_area(
    "📝 Observaciones Generales (Opcional - Solo Letras):",
    placeholder="EJ: SIN CEBOLLA, AJI APARTE PARA LA MESA...",
    height=80,
    key="txt_obs",
)

# JavaScript para restringir números sólo en Observaciones
st.components.v1.html(
    """
    <script>
    const parentDoc = window.parent.document;
    
    function aplicarBloqueoObservaciones() {
        const textareas = parentDoc.querySelectorAll('textarea');
        textareas.forEach(textarea => {
            const label = textarea.getAttribute('aria-label') || '';
            if (label.includes('Observaciones') && !textarea.dataset.bloqueado) {
                textarea.dataset.bloqueado = "true";
                
                textarea.addEventListener('keydown', function(e) {
                    if ((e.key >= '0' && e.key <= '9') || (e.keyCode >= 96 && e.keyCode <= 105)) {
                        e.preventDefault();
                    }
                });
                
                textarea.addEventListener('input', function(e) {
                    this.value = this.value.replace(/[0-9]/g, '');
                });
            }
        });
    }

    setInterval(aplicarBloqueoObservaciones, 400);
    </script>
    """,
    height=0,
)

observaciones = re.sub(r"[0-9]", "", obs_input).upper()

st.divider()

# 7. Confirmación y Enviar a WhatsApp
if st.button("🚀 CONFIRMAR Y ENVIAR PEDIDO"):
    hay_pedido = any(
        p["entrada"] != "Ninguna"
        or p["segundo"] != "Ninguno"
        or p["bebida"] != "Ninguna"
        for p in pedidos_realizados
    )

    if not hay_pedido:
        st.warning(
            "⚠️ Por favor, selecciona al menos un producto para enviar tu"
            " pedido."
        )
    else:
        mensaje = f"*NUEVO PEDIDO - RESTAURANT FERNANDEZ*\n"
        mensaje += f"📍 *{mesa}* (Total personas: {num_personas})\n\n"

        for idx, p in enumerate(pedidos_realizados, 1):
            if (
                p["entrada"] != "Ninguna"
                or p["segundo"] != "Ninguno"
                or p["bebida"] != "Ninguna"
            ):
                mensaje += f"*— PERSONA {idx} —*\n"
                if p["entrada"] != "Ninguna":
                    mensaje += f"• *Entrada:* {p['entrada']}\n"
                if p["segundo"] != "Ninguno":
                    mensaje += f"• *Segundo:* {p['segundo']}\n"
                if p["bebida"] != "Ninguna":
                    mensaje += f"• *Bebida:* {p['bebida']}\n"

        if observaciones.strip():
            mensaje += f"\n📝 *OBS:* {observaciones.strip()}\n"

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

# 8. PANEL DE ADMINISTRACIÓN
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
            value=", ".join(menu_actual.get("entradas", [])),
            height=80,
            key="admin_ent",
        )
        nuevos_segundos = st.text_area(
            "Segundos del Día:",
            value=", ".join(menu_actual.get("segundos", [])),
            height=100,
            key="admin_seg",
        )
        nuevas_bebidas = st.text_area(
            "Bebidas:",
            value=", ".join(menu_actual.get("bebidas", [])),
            height=80,
            key="admin_beb",
        )

        if st.button("💾 Guardar Menú del Día", key="btn_guardar"):
            nuevo_menu = {
                "entradas": [
                    e.strip() for e in nuevas_entradas.split(",") if e.strip()
                ],
                "segundos": [
                    s.strip() for s in nuevos_segundos.split(",") if s.strip()
                ],
                "bebidas": [
                    b.strip() for b in nuevas_bebidas.split(",") if b.strip()
                ],
            }

            guardar_menu(nuevo_menu)

            st.success("✅ ¡Menú guardado y actualizado para todos los clientes!")
            st.rerun()

    elif clave_admin != "":
        st.error("❌ Clave incorrecta")

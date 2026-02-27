import streamlit as st

# ─────────────────────────────────────────────
# CONFIGURACIÓN DE LA PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Registro de Contactos",
    page_icon="📋",
    layout="centered"
)

st.title("📋 Registro de Contactos")
st.write("Completa el formulario para agregar un nuevo contacto a la lista.")

# ─────────────────────────────────────────────
# INICIALIZAR LA LISTA DE CONTACTOS
# (Se guarda en session_state para que no se borre al recargar)
# ─────────────────────────────────────────────
if "contactos" not in st.session_state:
    st.session_state.contactos = []

# ─────────────────────────────────────────────
# FORMULARIO DE REGISTRO
# ─────────────────────────────────────────────
with st.form("formulario_contacto", clear_on_submit=True):
    st.subheader("➕ Nuevo Contacto")

    col1, col2 = st.columns(2)

    with col1:
        nombre = st.text_input("Nombre *", placeholder="Ej: Juan")
        apellido = st.text_input("Apellido *", placeholder="Ej: García")
        edad = st.number_input("Edad", min_value=0, max_value=120, value=18)

    with col2:
        telefono = st.text_input("Teléfono", placeholder="Ej: 555-1234")
        correo = st.text_input("Correo electrónico", placeholder="Ej: juan@email.com")
        ciudad = st.text_input("Ciudad", placeholder="Ej: Ciudad de México")

    notas = st.text_area("Notas adicionales", placeholder="Escribe algo aquí si quieres...")

    # Botón para enviar el formulario
    enviado = st.form_submit_button("✅ Agregar Contacto", use_container_width=True)

    # Cuando se presiona el botón
    if enviado:
        # Validar que los campos obligatorios estén llenos
        if not nombre or not apellido:
            st.error("⚠️ Por favor ingresa al menos el nombre y el apellido.")
        else:
            # Crear un diccionario con los datos del contacto
            nuevo_contacto = {
                "Nombre": nombre,
                "Apellido": apellido,
                "Edad": edad,
                "Teléfono": telefono if telefono else "—",
                "Correo": correo if correo else "—",
                "Ciudad": ciudad if ciudad else "—",
                "Notas": notas if notas else "—",
            }
            # Agregar el contacto a la lista
            st.session_state.contactos.append(nuevo_contacto)
            st.success(f"✅ ¡Contacto '{nombre} {apellido}' agregado correctamente!")

# ─────────────────────────────────────────────
# MOSTRAR LA LISTA DE CONTACTOS
# ─────────────────────────────────────────────
st.divider()
st.subheader(f"📂 Contactos registrados: {len(st.session_state.contactos)}")

if len(st.session_state.contactos) == 0:
    st.info("Aún no hay contactos registrados. ¡Agrega el primero!")
else:
    # Mostrar cada contacto en una tarjeta expandible
    for i, contacto in enumerate(st.session_state.contactos):
        with st.expander(f"👤 {contacto['Nombre']} {contacto['Apellido']}"):
            col_a, col_b = st.columns(2)
            with col_a:
                st.write(f"**Edad:** {contacto['Edad']}")
                st.write(f"**Teléfono:** {contacto['Teléfono']}")
                st.write(f"**Correo:** {contacto['Correo']}")
            with col_b:
                st.write(f"**Ciudad:** {contacto['Ciudad']}")
                st.write(f"**Notas:** {contacto['Notas']}")

            # Botón para eliminar el contacto
            if st.button(f"🗑️ Eliminar", key=f"eliminar_{i}"):
                st.session_state.contactos.pop(i)
                st.rerun()

    # Botón para limpiar todos los contactos
    st.divider()
    if st.button("🧹 Limpiar toda la lista", type="secondary"):
        st.session_state.contactos = []
        st.rerun()
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Simulador de Comisiones", layout="centered")

st.markdown("<h1 style='text-align: center; color: #1f77b4;'>Simulador de Comisiones Dinegma</h1>", unsafe_allow_html=True)
st.markdown("Este simulador te ayudará a calcular tu comisión según tus indicadores alcanzados. 🧮")

# Nombre del asesor
asesor = st.text_input("Nombre del asesor o colaborador")

# Cargo
cargo = st.selectbox("Selecciona tu cargo", ["Asesor", "Alterno", "Administrador"])

# Lista de tiendas con clasificación
tiendas_tipo = {
    "Hurley Oakland": "A",
    "Nava Oakland": "A",
    "Nava Videre": "A",
    "Vélez Oakland 1": "A",
    "Vélez Oakland 2": "A",
    "Vélez Miraflores": "A",
    "Vélez Multiplaza": "A",
    "Hurley Naranjo": "B",
    "Hurley Antigua": "B",
    "Hurley Escuintla": "B",
    "Hurley Multiplaza": "B",
    "Nava Portales": "B",
    "Vélez Naranjo": "B",
    "Vélez Portales": "B",
    "Vélez Chimaltenango": "B",
    "Vélez Pradera Xela": "B",
    "Vélez Interplaza Xela": "B",
    "Vélez Kiosco Miraflores": "Kiosco",
    "Vélez Kiosco Oakland": "Kiosco",
    "Vélez Kiosco Decima": "Kiosco",
    "Vélez Kiosco Gran Vía": "Kiosco",
    "Vélez Kiosco Galerias": "Kiosco"
}

# Selección de tienda
tienda = st.selectbox("Selecciona tu tienda", list(tiendas_tipo.keys()))
tipo_tienda = tiendas_tipo.get(tienda, "No clasificada")
marca = "Vélez" if "Vélez" in tienda else "Hurley/Nava"

# Mostrar datos básicos
if asesor and tienda and cargo:
    st.success(f"🧑‍💼 **{asesor}** - Cargo: **{cargo}** - Tienda: **{tienda}**")
    st.info(f"📌 Esta tienda es clasificada como: **Tipo {tipo_tienda}**")

    st.markdown("---")
    st.subheader("📊 Ingreso de Datos")

    venta_total = st.number_input("Venta total lograda (Q)", min_value=0.0, format="%.2f")
    facturas_realizadas = st.number_input("Facturas realizadas", min_value=0)

    col1, col2 = st.columns(2)
    with col1:
        meta_ppto = st.number_input("Meta de PPTO (Q)", min_value=0.0, format="%.2f")
        meta_axf = st.number_input("Meta de AxF", min_value=0.0, format="%.2f")
        meta_vxf = st.number_input("Meta de VxF (Q)", min_value=0.0, format="%.2f")
        meta_tc = st.number_input("Meta de TC (%)", min_value=0.0, format="%.2f")
        meta_fidelizados = facturas_realizadas if marca != "Vélez" else st.number_input("Meta de Clientes Fidelizados", min_value=0)
    with col2:
        logro_ppto = st.number_input("Logro de PPTO (Q)", min_value=0.0, format="%.2f")
        logro_axf = st.number_input("Logro de AxF", min_value=0.0, format="%.2f")
        logro_vxf = st.number_input("Logro de VxF (Q)", min_value=0.0, format="%.2f")
        logro_tc = st.number_input("Logro de TC (%)", min_value=0.0, format="%.2f")
        clientes_fidelizados = st.number_input("Clientes Fidelizados", min_value=0)

    if st.button("Calcular Comisión"):
        def calcular_cumplimiento(meta, logro):
            return (logro / meta) * 100 if meta > 0 else 0

        cumplimiento = {
            "PPTO": calcular_cumplimiento(meta_ppto, logro_ppto),
            "AxF": calcular_cumplimiento(meta_axf, logro_axf),
            "VxF": calcular_cumplimiento(meta_vxf, logro_vxf),
            "TC": calcular_cumplimiento(meta_tc, logro_tc),
            "Fidelización": calcular_cumplimiento(meta_fidelizados, clientes_fidelizados)
        }

        st.markdown("---")
        st.subheader("📈 Resultados de Cumplimiento")
        for k, v in cumplimiento.items():
            st.write(f"**{k}:** {v:.2f}%")

        def obtener_variable(indicador, porc):
            if porc >= 120:
                return 0.02
            elif porc >= 110:
                return 0.017
            elif porc >= 100:
                return 0.015
            elif porc >= 90:
                return 0.012
            elif porc >= 85:
                return 0.01
            else:
                return 0.0

        def obtener_fijo(indicador, porc):
            if porc >= 120:
                return 198
            elif porc >= 110:
                return 176
            elif porc >= 100:
                return 154
            elif porc >= 90:
                return 132
            elif porc >= 85:
                return 110
            else:
                return 0

        comisiones = {}
        for indicador, porc in cumplimiento.items():
            variable = obtener_variable(indicador, porc) * venta_total
            fijo = obtener_fijo(indicador, porc)
            if cargo == "Asesor" and marca != "Vélez" and indicador in ["Fidelización", "TC"]:
                comisiones[indicador] = max(variable, fijo)
            else:
                comisiones[indicador] = variable

        st.markdown("---")
        st.subheader("🧾 Comisión por Indicador")
        total = 0
        for ind, valor in comisiones.items():
            st.write(f"✅ **{ind}**: Q{valor:.2f}")
            total += valor

        st.markdown("---")
        st.markdown(f"<h2 style='color:green; text-align:center;'>💰 Comisión Total: Q{total:.2f}</h2>", unsafe_allow_html=True)
else:
    st.warning("Por favor, completa todos los campos iniciales.")

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
    "Hurley Naranjo": "B",
    "Hurley Antigua": "B",
    "Hurley Escuintla": "B",
    "Hurley Multiplaza": "B",
    "Nava Portales": "B"
}

# Selección de tienda
tienda = st.selectbox("Selecciona tu tienda", list(tiendas_tipo.keys()))
tipo_tienda = tiendas_tipo.get(tienda, "No clasificada")
marca = "Hurley/Nava"

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
        meta_fidelizados = facturas_realizadas
    with col2:
        logro_ppto = st.number_input("Logro de PPTO (Q)", min_value=0.0, format="%.2f")
        logro_axf = st.number_input("Logro de AxF", min_value=0.0, format="%.2f")
        logro_vxf = st.number_input("Logro de VxF (Q)", min_value=0.0, format="%.2f")
        clientes_fidelizados = st.number_input("Clientes Fidelizados", min_value=0)

    if st.button("Calcular Comisión"):
        def calcular_cumplimiento(meta, logro):
            return (logro / meta) * 100 if meta > 0 else 0

        cumplimiento = {
            "PPTO": calcular_cumplimiento(meta_ppto, logro_ppto),
            "AxF": calcular_cumplimiento(meta_axf, logro_axf),
            "VxF": calcular_cumplimiento(meta_vxf, logro_vxf),
            "Fidelización": calcular_cumplimiento(meta_fidelizados, clientes_fidelizados)
        }

        st.markdown("---")
        st.subheader("📈 Resultados de Cumplimiento")
        for k, v in cumplimiento.items():
            st.write(f"**{k}:** {v:.2f}%")

        # Tabla de comisiones por variable
        tabla_variables = {
            "Administrador": {
                "A": {"PPTO": [0.01, 0.012, 0.015, 0.017, 0.02],
                      "AxF": [0.01, 0.012, 0.015, 0.017, 0.02],
                      "VxF": [0.01, 0.012, 0.015, 0.017, 0.02],
                      "Fidelización": [0.01, 0.012, 0.015, 0.017, 0.02]},
                "B": {"PPTO": [0.008, 0.01, 0.012, 0.014, 0.016],
                      "AxF": [0.008, 0.01, 0.012, 0.014, 0.016],
                      "VxF": [0.008, 0.01, 0.012, 0.014, 0.016],
                      "Fidelización": [0.008, 0.01, 0.012, 0.014, 0.016]}
            },
            "Alterno": {
                "A": {"PPTO": [0.006, 0.008, 0.01, 0.012, 0.014],
                      "AxF": [0.006, 0.008, 0.01, 0.012, 0.014],
                      "VxF": [0.006, 0.008, 0.01, 0.012, 0.014],
                      "Fidelización": [0.006, 0.008, 0.01, 0.012, 0.014]},
                "B": {"PPTO": [0.005, 0.007, 0.009, 0.011, 0.013],
                      "AxF": [0.005, 0.007, 0.009, 0.011, 0.013],
                      "VxF": [0.005, 0.007, 0.009, 0.011, 0.013],
                      "Fidelización": [0.005, 0.007, 0.009, 0.011, 0.013]}
            },
            "Asesor": {
                "A": {"PPTO": [0.005, 0.007, 0.009, 0.011, 0.013],
                      "AxF": [0.005, 0.007, 0.009, 0.011, 0.013],
                      "VxF": [0.005, 0.007, 0.009, 0.011, 0.013],
                      "Fidelización": [0.005, 0.007, 0.009, 0.011, 0.013]},
                "B": {"PPTO": [0.004, 0.006, 0.008, 0.01, 0.012],
                      "AxF": [0.004, 0.006, 0.008, 0.01, 0.012],
                      "VxF": [0.004, 0.006, 0.008, 0.01, 0.012],
                      "Fidelización": [0.004, 0.006, 0.008, 0.01, 0.012]}
            }
        }

        def rango_index(cumplimiento):
            if cumplimiento >= 120:
                return 4
            elif cumplimiento >= 110:
                return 3
            elif cumplimiento >= 100:
                return 2
            elif cumplimiento >= 90:
                return 1
            elif cumplimiento >= 85:
                return 0
            else:
                return -1

        comisiones = {}
        for indicador, porc in cumplimiento.items():
            idx = rango_index(porc)
            if idx >= 0:
                porcentaje_variable = tabla_variables[cargo][tipo_tienda][indicador][idx]
                comisiones[indicador] = venta_total * porcentaje_variable
            else:
                comisiones[indicador] = 0.0

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

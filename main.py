import streamlit as st

# --- TABLAS DE COMISIONES ---

# ADMINISTRADORES - TIENDA A
comisiones_admins_A = {
    "PPTO": [
        {"rango": (85, 89.99), "variable": 0.0047, "fijo": 871},
        {"rango": (90, 99.99), "variable": 0.0054, "fijo": 1005},
        {"rango": (100, 109.99), "variable": 0.0074, "fijo": 1139},
        {"rango": (110, 119.99), "variable": 0.0077, "fijo": 1273},
        {"rango": (120, 999), "variable": 0.0080, "fijo": 1340},
    ],
    "VxF": [
        {"rango": (85, 89.99), "variable": 0.0008, "fijo": 143},
        {"rango": (90, 99.99), "variable": 0.0009, "fijo": 165},
        {"rango": (100, 109.99), "variable": 0.0012, "fijo": 187},
        {"rango": (110, 119.99), "variable": 0.0013, "fijo": 209},
        {"rango": (120, 999), "variable": 0.0013, "fijo": 220},
    ],
    "AxF": [
        {"rango": (85, 89.99), "variable": 0.0008, "fijo": 143},
        {"rango": (90, 99.99), "variable": 0.0009, "fijo": 165},
        {"rango": (100, 109.99), "variable": 0.0012, "fijo": 187},
        {"rango": (110, 119.99), "variable": 0.0013, "fijo": 209},
        {"rango": (120, 999), "variable": 0.0013, "fijo": 220},
    ],
    "Fidelizacion": [
        {"rango": (85, 89.99), "variable": 0.0008, "fijo": 143},
        {"rango": (90, 99.99), "variable": 0.0009, "fijo": 165},
        {"rango": (100, 109.99), "variable": 0.0012, "fijo": 187},
        {"rango": (110, 119.99), "variable": 0.0013, "fijo": 209},
        {"rango": (120, 999), "variable": 0.0013, "fijo": 220},
    ],
}

# ADMINISTRADORES - TIENDA B
comisiones_admins_B = {
    "PPTO": [
        {"rango": (85, 89.99), "variable": 0.0067, "fijo": 737},
        {"rango": (90, 99.99), "variable": 0.0074, "fijo": 871},
        {"rango": (100, 109.99), "variable": 0.0080, "fijo": 1005},
        {"rango": (110, 119.99), "variable": 0.0084, "fijo": 1139},
        {"rango": (120, 999), "variable": 0.0087, "fijo": 1206},
    ],
    "VxF": [
        {"rango": (85, 89.99), "variable": 0.0011, "fijo": 121},
        {"rango": (90, 99.99), "variable": 0.0012, "fijo": 143},
        {"rango": (100, 109.99), "variable": 0.0013, "fijo": 165},
        {"rango": (110, 119.99), "variable": 0.0014, "fijo": 187},
        {"rango": (120, 999), "variable": 0.0014, "fijo": 198},
    ],
    "AxF": [
        {"rango": (85, 89.99), "variable": 0.0011, "fijo": 121},
        {"rango": (90, 99.99), "variable": 0.0012, "fijo": 143},
        {"rango": (100, 109.99), "variable": 0.0013, "fijo": 165},
        {"rango": (110, 119.99), "variable": 0.0014, "fijo": 187},
        {"rango": (120, 999), "variable": 0.0014, "fijo": 198},
    ],
    "Fidelizacion": [
        {"rango": (85, 89.99), "variable": 0.0011, "fijo": 121},
        {"rango": (90, 99.99), "variable": 0.0012, "fijo": 143},
        {"rango": (100, 109.99), "variable": 0.0013, "fijo": 165},
        {"rango": (110, 119.99), "variable": 0.0014, "fijo": 187},
        {"rango": (120, 999), "variable": 0.0014, "fijo": 198},
    ],
}

# ASESORES - TIENDA A
comisiones_asesores_A = {
    "PPTO": [
        {"rango": (85, 89.99), "variable": 0.0114, "fijo": 536},
        {"rango": (90, 99.99), "variable": 0.0141, "fijo": 670},
        {"rango": (100, 109.99), "variable": 0.0174, "fijo": 804},
        {"rango": (110, 119.99), "variable": 0.0181, "fijo": 938},
        {"rango": (120, 999), "variable": 0.0188, "fijo": 1072},
    ],
    "VxF": [
        {"rango": (85, 89.99), "variable": 0.0019, "fijo": 88},
        {"rango": (90, 99.99), "variable": 0.0023, "fijo": 110},
        {"rango": (100, 109.99), "variable": 0.0029, "fijo": 132},
        {"rango": (110, 119.99), "variable": 0.0030, "fijo": 154},
        {"rango": (120, 999), "variable": 0.0031, "fijo": 176},
    ],
    "AxF": [
        {"rango": (85, 89.99), "variable": 0.0019, "fijo": 88},
        {"rango": (90, 99.99), "variable": 0.0023, "fijo": 110},
        {"rango": (100, 109.99), "variable": 0.0029, "fijo": 132},
        {"rango": (110, 119.99), "variable": 0.0030, "fijo": 154},
        {"rango": (120, 999), "variable": 0.0031, "fijo": 176},
    ],
    "Fidelizacion": [
        {"rango": (85, 89.99), "variable": 0.0019, "fijo": 88},
        {"rango": (90, 99.99), "variable": 0.0023, "fijo": 110},
        {"rango": (100, 109.99), "variable": 0.0029, "fijo": 132},
        {"rango": (110, 119.99), "variable": 0.0030, "fijo": 154},
        {"rango": (120, 999), "variable": 0.0031, "fijo": 176},
    ],
}

# ASESORES - TIENDA B
comisiones_asesores_B = {
    "PPTO": [
        {"rango": (85, 89.99), "variable": 0.0121, "fijo": 469},
        {"rango": (90, 99.99), "variable": 0.0147, "fijo": 603},
        {"rango": (100, 109.99), "variable": 0.0181, "fijo": 737},
        {"rango": (110, 119.99), "variable": 0.0188, "fijo": 871},
        {"rango": (120, 999), "variable": 0.0194, "fijo": 1005},
    ],
    "VxF": [
        {"rango": (85, 89.99), "variable": 0.0020, "fijo": 77},
        {"rango": (90, 99.99), "variable": 0.0024, "fijo": 99},
        {"rango": (100, 109.99), "variable": 0.0030, "fijo": 121},
        {"rango": (110, 119.99), "variable": 0.0031, "fijo": 143},
        {"rango": (120, 999), "variable": 0.0032, "fijo": 165},
    ],
    "AxF": [
        {"rango": (85, 89.99), "variable": 0.0020, "fijo": 77},
        {"rango": (90, 99.99), "variable": 0.0024, "fijo": 99},
        {"rango": (100, 109.99), "variable": 0.0030, "fijo": 121},
        {"rango": (110, 119.99), "variable": 0.0031, "fijo": 143},
        {"rango": (120, 999), "variable": 0.0032, "fijo": 165},
    ],
    "Fidelizacion": [
        {"rango": (85, 89.99), "variable": 0.0020, "fijo": 77},
        {"rango": (90, 99.99), "variable": 0.0024, "fijo": 99},
        {"rango": (100, 109.99), "variable": 0.0030, "fijo": 121},
        {"rango": (110, 119.99), "variable": 0.0031, "fijo": 143},
        {"rango": (120, 999), "variable": 0.0032, "fijo": 165},
    ],
}
# --- FUNCIÓN PARA CALCULAR COMISIÓN ---
def calcular_comision(tabla, indicador, meta, logro, venta_total):
    if meta == 0:
        return 0, 0, 0  # evitar división por cero
    porcentaje = (logro / meta) * 100
    for tramo in tabla[indicador]:
        min_r, max_r = tramo["rango"]
        if min_r <= porcentaje <= max_r:
            comision_variable = venta_total * tramo["variable"]
            comision_final = max(comision_variable, tramo["fijo"])
            return round(comision_variable, 2), tramo["fijo"], round(comision_final, 2)
    return 0, 0, 0

# --- INTERFAZ STREAMLIT ---
st.title("💸 Simulador de Comisiones - Hurley & Nava")

cargo = st.selectbox("Cargo", ["Asesor", "Administrador"])
tipo_tienda = st.selectbox("Tipo de tienda", ["Tipo A", "Tipo B"])
venta = st.number_input("Venta total realizada (Q)", min_value=0.0)

st.subheader("Indicadores")
cols = st.columns(4)
indicadores = {}
for i, indicador in enumerate(["PPTO", "VxF", "AxF", "Fidelizacion"]):
    with cols[i]:
        meta = st.number_input(f"Meta {indicador}", min_value=0.0, key=f"meta_{indicador}")
        logro = st.number_input(f"Logrado {indicador}", min_value=0.0, key=f"logro_{indicador}")
        indicadores[indicador] = (meta, logro)

# --- SELECCIÓN DE TABLA DE COMISIONES ---
if cargo == "Asesor" and tipo_tienda == "Tipo A":
    tabla = comisiones_asesores_A
elif cargo == "Asesor" and tipo_tienda == "Tipo B":
    tabla = comisiones_asesores_B
elif cargo == "Administrador" and tipo_tienda == "Tipo A":
    tabla = comisiones_admins_A
elif cargo == "Administrador" and tipo_tienda == "Tipo B":
    tabla = comisiones_admins_B
else:
    st.error("No hay tabla definida para esta combinación.")
    st.stop()
    
st.write("Tabla usada:", tabla)

# --- CÁLCULO ---
if st.button("Calcular Comisión"):
    total = 0
    st.subheader("Detalle por Indicador")
    for indicador, (meta, logro) in indicadores.items():
        com_var, com_fijo, com_final = calcular_comision(tabla, indicador, meta, logro, venta)
        total += com_final
        st.write(f"**{indicador}** ➤ Comisión Variable: Q{com_var} | Fijo: Q{com_fijo} | **Aplica: Q{com_final}**")

    st.success(f"💰 Comisión Total Estimada: Q{round(total, 2)}")

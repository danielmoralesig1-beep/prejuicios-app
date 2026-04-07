import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Panel de Leads - PREjuicios", layout="wide")

# Título para tu panel interno
st.title("🏛️ Panel de Control PRE-juicios")
st.subheader("Base de Datos de Leads (Consultas de la Web)")

# Nombre del archivo donde se guardarán los datos
DB_FILE = "leads_prejuicios.csv"

# Función para guardar datos que vienen de la Web
def guardar_lead(datos):
    df_nuevo = pd.DataFrame([datos])
    if not os.path.isfile(DB_FILE):
        df_nuevo.to_csv(DB_FILE, index=False)
    else:
        df_nuevo.to_csv(DB_FILE, mode='a', header=False, index=False)

# --- INTERFAZ DEL PANEL ---
if os.path.isfile(DB_FILE):
    df = pd.read_csv(DB_FILE)
    st.write(f"Total de personas que han consultado: {len(df)}")
    st.dataframe(df.sort_index(ascending=False)) # Muestra los más recientes arriba
    
    # Botón para descargar tu lista en Excel/CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Descargar reporte detallado", csv, "leads.csv", "text/csv")
else:
    st.info("Aún no hay consultas registradas. ¡Tu landing está lista para recibir clientes!")

# --- ESTO ES LO QUE RECIBE LOS DATOS DE NETLIFY ---
# Nota: Streamlit Cloud maneja la recepción de datos mediante este script
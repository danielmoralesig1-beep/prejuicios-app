import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Panel PRE-juicios", layout="wide")
st.title("🏛️ Panel de Control PRE-juicios")

DB_FILE = "leads_prejuicios.csv"

# Función para guardar los datos cuando Netlify los envía
def guardar_datos(nombre, telefono, deuda, estado):
    nuevo_lead = {
        "Fecha": pd.Timestamp.now(tz='America/Santiago').strftime("%d/%m/%Y %H:%M"),
        "Nombre": nombre,
        "WhatsApp": telefono,
        "Monto Deuda": deuda,
        "Estado Legal": estado
    }
    df_nuevo = pd.DataFrame([nuevo_lead])
    if not os.path.isfile(DB_FILE):
        df_nuevo.to_csv(DB_FILE, index=False)
    else:
        df_nuevo.to_csv(DB_FILE, mode='a', header=False, index=False)

# --- ESTO RECIBE LOS DATOS DE TU WEB ---
query_params = st.query_params
if "name" in query_params:
    guardar_datos(
        query_params["name"], 
        query_params["phone"], 
        query_params["debt"], 
        query_params["status"]
    )
    st.success("¡Nuevo lead registrado!")

# --- MOSTRAR LA TABLA ---
if os.path.isfile(DB_FILE):
    df = pd.read_csv(DB_FILE)
    st.dataframe(df.sort_index(ascending=False), use_container_width=True)
else:
    st.info("Esperando clientes de la landing page...")

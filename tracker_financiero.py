import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="finOps Traker",page_icon="💹", layout="wide")

st.title("📊 Monitor de Inversiones (FinOps Dashboard)")
st.markdown("Herramienta en tiempo real conectada a la API de Yahoo Finance para monitorear el rendimiento de CEDEARs y acciones.")

st.sidebar.header("Configuracion del portafolio")
activos_disponibles = ["SPY", "MSFT", "NVDA", "AAPL", "TSLA", "AMZN", "META"]

seleccionados = st.sidebar.multiselect(
    "selecciona los activos a monitorear",
    activos_disponibles,
    default=["SPY", "MSFT","NVDA"]
)
periodo = st.sidebar.selectbox(

    "selecciona el periodo historico:",
    ["1mo", "3mo", "6mo", "1y", "ytd"], 
    index=2
)

if seleccionados:
    with st.spinner("conectando con Wall Street y descargando datos..."):
        datos = yf.download(seleccionados, period=periodo)

        if isinstance(datos.columns, pd.MultiIndex):
            df = datos['Close']
        else:
            df = datos[['Close']].rename(columns={'Close': seleccionados[0]})

    st.success("¡Datos extraidos correctamente de la API!")
    
    st.markdown("### 💰 Resumen del Último Cierre (USD)")

    cols = st.columns(len(seleccionados))

    for i, ticker in enumerate(seleccionados):

        ultimo_precio = df[ticker].iloc[-1]
        precio_anterior = df[ticker].iloc[-2]
        variacion = ((ultimo_precio - precio_anterior) / precio_anterior) * 100
        
        cols[i].metric(label=ticker, value=f"${ultimo_precio:.2f}", delta=f"{variacion:.2f}%")

    
    st.markdown("### 📈 Evolución Histórica de Precios")
    
    df_grafico = df.reset_index().melt(id_vars="Date", value_vars=seleccionados, var_name="Activo", value_name="Precio (USD)")
    
    fig = px.line(df_grafico, x="Date", y="Precio (USD)", color="Activo", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("👈 Por favor, selecciona al menos un activo en el panel izquierdo para comenzar el análisis.")


    
    

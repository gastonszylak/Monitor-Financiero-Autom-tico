# Monitor-Financiero-Autom-tico
# 📈 FinOps Dashboard | Monitor de Inversiones en Tiempo Real

¡Bienvenido al repositorio del **Monitor Financiero Automático**! 💹

Esta es una aplicación web interactiva diseñada para realizar un seguimiento en tiempo real de activos financieros (CEDEARs, Acciones, ETFs), extrayendo datos vivos directamente de la bolsa de valores (Wall Street).

## 🎯 El Problema de Negocio (Business Value)
En el sector de Finanzas y RevOps, la toma de decisiones depende de la velocidad y precisión de la información. Depender de archivos Excel estáticos que se actualizan manualmente genera retrasos críticos. 
Esta herramienta automatiza la ingesta de datos bursátiles, calcula métricas de rendimiento diario y permite visualizar la volatilidad histórica de un portfolio en segundos, facilitando estrategias de inversión ágiles (Core & Satellite).

## 🛠️ Stack Tecnológico
Este proyecto fue construido íntegramente con Python y consumo de APIs externas:
* **Interfaz Web (Frontend):** `Streamlit`
* **Conexión a API Bursátil:** `yfinance` (Yahoo Finance API)
* **Procesamiento de Datos:** `Pandas`
* **Visualización de Datos:** `Plotly`

## ⚙️ Funcionalidades Principales
1. **Extracción de Datos en Vivo:** Conexión directa a la API de Yahoo Finance para descargar precios de cierre históricos y actuales sin latencia.
2. **Dashboard Dinámico:** Interfaz lateral donde el usuario puede personalizar qué activos monitorear (Ej: SPY, MSFT, NVDA) y el horizonte temporal (1 mes, 6 meses, 1 año).
3. **Cálculo de KPIs Financieros:** Motor que evalúa automáticamente la variación porcentual del último día hábil para identificar tendencias alcistas o bajistas.
4. **Gráficos Interactivos:** Visualización de series de tiempo financieras para analizar el comportamiento y riesgo de los activos.

## 🚀 Cómo ejecutar el proyecto localmente

Si deseas correr esta aplicación en tu propia máquina, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/finops-tracker.git](https://github.com/tu-usuario/finops-tracker.git)
   cd finops-tracker

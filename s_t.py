import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Configuración de la página y estilos iniciales
st.set_page_config(page_title="Análisis de Sentimiento y Corrección", page_icon="💬")
st.markdown(
    """
    <style>
    .positive {
        background-color: #e0f7fa;
    }
    .very-positive {
        background-color: #c8e6c9;
    }
    .neutral {
        background-color: #f0f4c3;
    }
    .negative {
        background-color: #ffe0b2;
    }
    .very-negative {
        background-color: #ffcdd2;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título y subtítulo de la aplicación
st.title("💬✨ Análisis de Sentimiento y Corrección de Texto")
st.markdown("#### Detecta el sentimiento y la precisión en tus frases 📈💡")

# Configuración del traductor
translator = Translator()

# Barra lateral de explicación
with st.sidebar:
    st.header("🎯 Polaridad y Subjetividad")
    st.info("""
    **Polaridad**: Indica el sentimiento del texto: positivo, negativo o neutral.
    Va de -1 (muy negativo) a 1 (muy positivo).
    
    **Subjetividad**: Mide cuánto del contenido es subjetivo (opiniones, emociones) frente a objetivo (hechos).
    Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

# Sección de análisis de sentimiento
with st.expander("📊 Analizar Polaridad y Subjetividad en un texto"):
    st.markdown("#### Por favor escribe en el campo de texto la frase que deseas analizar:")
    text1 = st.text_area("💬 Ingresa tu texto aquí:", placeholder="Escribe algo interesante...")

    if text1:
        # Traducción al inglés para el análisis con TextBlob
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        # Mostrar polaridad y subjetividad
        polarity_score = round(blob.sentiment.polarity, 2)
        subjectivity_score = round(blob.sentiment.subjectivity, 2)
        
        st.markdown("### 📈 Resultados:")
        st.write("**Polaridad:**", f"`{polarity_score}`")
        st.write("**Subjetividad:**", f"`{subjectivity_score}`")

        # Configurar la interfaz según el sentimiento
        if polarity_score >= 0.5:
            st.markdown('<div class="very-positive">🌟 ¡Es un sentimiento muy positivo! 😊</div>', unsafe_allow_html=True)
            st.image("path/to/positive_image.jpg", use_column_width=True)
        elif 0.1 <= polarity_score < 0.5:
            st.markdown('<div class="positive">💚 Es un sentimiento positivo</div>', unsafe_allow_html=True)
        elif -0.5 < polarity_score <= -0.1:
            st.markdown('<div class="neutral">⚠️ Es un sentimiento ligeramente negativo</div>', unsafe_allow_html=True)
            st.image("path/to/neutral_image.jpg", use_column_width=True)
        elif polarity_score <= -0.5:
            st.markdown('<div class="very-negative">🚨 ¡Es un sentimiento muy negativo! 😔</div>', unsafe_allow_html=True)
            st.image("path/to/negative_image.jpg", use_column_width=True)
        else:
            st.markdown('<div class="neutral">🤔 Es un sentimiento neutral 😐</div>', unsafe_allow_html=True)
            st.image("path/to/neutral_image.jpg", use_column_width=True)

# Sección de corrección de texto
with st.expander("📝 Corrección en Inglés"):
    st.markdown("#### ¿Necesitas una pequeña ayuda con la ortografía? ¡Te ayudamos!")
    text2 = st.text_area("🔍 Ingresa el texto en inglés para corregir:", placeholder="Escribe en inglés...", key="4")

    if text2:
        blob2 = TextBlob(text2)
        st.write("**Texto corregido:**")
        st.success(blob2.correct())

# Pie de página
st.markdown("---")
st.markdown("💬 **Análisis de Sentimiento y Corrección de Texto** - Potenciado por TextBlob y Google Translate")


           


        
    






    



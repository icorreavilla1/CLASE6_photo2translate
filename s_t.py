import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Configuración de la página y estilos
st.title("💬✨ Análisis de Sentimiento y Corrección de Texto")
st.markdown("#### Detecta el sentimiento y la precisión en tus frases 📈💡")

translator = Translator()

# Barra lateral con explicación
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

        # Mostrar polaridad y subjetividad con colores
        st.markdown("### 📈 Resultados:")
        st.write("**Polaridad:**", f"`{round(blob.sentiment.polarity, 2)}`")
        st.write("**Subjetividad:**", f"`{round(blob.sentiment.subjectivity, 2)}`")
        
        # Clasificación de sentimiento y cambios de interfaz
        polarity_score = round(blob.sentiment.polarity, 2)
        
        if polarity_score >= 0.5:
            st.success("🌟 ¡Es un sentimiento muy positivo! 😊")
            st.markdown("<h1 style='text-align: center;'>😄</h1>", unsafe_allow_html=True)  # Emoji gigante para positivo
            st.markdown(
                "<style>body {background-color: #b2f7b3;}</style>", 
                unsafe_allow_html=True
            )
        elif 0.1 <= polarity_score < 0.5:
            st.info("💚 Es un sentimiento positivo")
            st.markdown("<h1 style='text-align: center;'>🙂</h1>", unsafe_allow_html=True)  # Emoji gigante para positivo
            st.markdown(
                "<style>body {background-color: #d4edda;}</style>", 
                unsafe_allow_html=True
            )
        elif -0.5 < polarity_score <= -0.1:
            st.warning("⚠️ Es un sentimiento ligeramente negativo")
            st.markdown("<h1 style='text-align: center;'>😟</h1>", unsafe_allow_html=True)  # Emoji gigante para negativo
            st.markdown(
                "<style>body {background-color: #fff3cd;}</style>", 
                unsafe_allow_html=True
            )
        elif polarity_score <= -0.5:
            st.error("🚨 ¡Es un sentimiento muy negativo! 😔")
            st.markdown("<h1 style='text-align: center;'>😡</h1>", unsafe_allow_html=True)  # Emoji gigante para negativo
            st.markdown(
                "<style>body {background-color: #f8d7da;}</style>", 
                unsafe_allow_html=True
            )
        else:
            st.write("🤔 Es un sentimiento neutral 😐")
            st.markdown("<h1 style='text-align: center;'>😐</h1>", unsafe_allow_html=True)  # Emoji gigante para neutral
            st.markdown(
                "<style>body {background-color: #e2e3e5;}</style>", 
                unsafe_allow_html=True
            )

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

           


        
    






    



import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Configuración de la página y estilos
st.set_page_config(page_title="Análisis de Sentimiento", layout="wide")
st.title("<span style='color: #4B0082;'>💬✨ Análisis de Sentimiento y Corrección de Texto</span>", unsafe_allow_html=True)
st.markdown("<h4 style='color: #6A5ACD;'>Detecta el sentimiento y la precisión en tus frases 📈💡</h4>", unsafe_allow_html=True)

translator = Translator()

# Barra lateral con explicación
with st.sidebar:
    st.header("<span style='color: #4B0082;'>🎯 Polaridad y Subjetividad</span>", unsafe_allow_html=True)
    st.info("""
    **Polaridad**: Indica el sentimiento del texto: positivo, negativo o neutral. 
    Va de -1 (muy negativo) a 1 (muy positivo).
    
    **Subjetividad**: Mide cuánto del contenido es subjetivo (opiniones, emociones) frente a objetivo (hechos).
    Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

# Sección de análisis de sentimiento
with st.expander("<span style='color: #4B0082;'>📊 Analizar Polaridad y Subjetividad en un texto</span>", unsafe_allow_html=True):
    st.markdown("<h4 style='color: #6A5ACD;'>Por favor escribe en el campo de texto la frase que deseas analizar:</h4>", unsafe_allow_html=True)
    text1 = st.text_area("💬 Ingresa tu texto aquí:", placeholder="Escribe algo interesante...", height=150)

    if text1:
        # Traducción al inglés para el análisis con TextBlob
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        # Mostrar polaridad y subjetividad con colores
        st.markdown("<h3 style='color: #4B0082;'>📈 Resultados:</h3>", unsafe_allow_html=True)
        st.write("<span style='color: #4B0082;'>**Polaridad:**</span>", f"`{round(blob.sentiment.polarity, 2)}`", unsafe_allow_html=True)
        st.write("<span style='color: #4B0082;'>**Subjetividad:**</span>", f"`{round(blob.sentiment.subjectivity, 2)}`", unsafe_allow_html=True)
        
        # Clasificación de sentimiento y cambios de interfaz
        polarity_score = round(blob.sentiment.polarity, 2)
        
        if polarity_score >= 0.5:
            st.success("<span style='color: #32CD32;'>🌟 ¡Es un sentimiento muy positivo! 😊</span>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #32CD32; font-size: 100px;'>😄</h1>", unsafe_allow_html=True)  # Emoji gigante para positivo
            st.markdown("<style>body {background-color: #E8F5E9;}</style>", unsafe_allow_html=True)
        elif 0.1 <= polarity_score < 0.5:
            st.info("<span style='color: #1E90FF;'>💚 Es un sentimiento positivo</span>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #1E90FF; font-size: 100px;'>🙂</h1>", unsafe_allow_html=True)  # Emoji gigante para positivo
            st.markdown("<style>body {background-color: #BBDEFB;}</style>", unsafe_allow_html=True)
        elif -0.5 < polarity_score <= -0.1:
            st.warning("<span style='color: #FFA500;'>⚠️ Es un sentimiento ligeramente negativo</span>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFA500; font-size: 100px;'>😟</h1>", unsafe_allow_html=True)  # Emoji gigante para negativo
            st.markdown("<style>body {background-color: #FFEB3B;}</style>", unsafe_allow_html=True)
        elif polarity_score <= -0.5:
            st.error("<span style='color: #FF4500;'>🚨 ¡Es un sentimiento muy negativo! 😔</span>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FF4500; font-size: 100px;'>😡</h1>", unsafe_allow_html=True)  # Emoji gigante para negativo
            st.markdown("<style>body {background-color: #FFCDD2;}</style>", unsafe_allow_html=True)
        else:
            st.write("<span style='color: #808080;'>🤔 Es un sentimiento neutral 😐</span>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #808080; font-size: 100px;'>😐</h1>", unsafe_allow_html=True)  # Emoji gigante para neutral
            st.markdown("<style>body {background-color: #F5F5F5;}</style>", unsafe_allow_html=True)

# Sección de corrección de texto
with st.expander("<span style='color: #4B0082;'>📝 Corrección en Inglés</span>", unsafe_allow_html=True):
    st.markdown("<h4 style='color: #6A5ACD;'>¿Necesitas una pequeña ayuda con la ortografía? ¡Te ayudamos!</h4>", unsafe_allow_html=True)
    text2 = st.text_area("🔍 Ingresa el texto en inglés para corregir:", placeholder="Escribe en inglés...", key="4", height=150)
    
    if text2:
        blob2 = TextBlob(text2)
        st.write("<span style='color: #4B0082;'>**Texto corregido:**</span>", unsafe_allow_html=True)
        st.success(blob2.correct())

# Pie de página
st.markdown("---")
st.markdown("<span style='color: #4B0082;'>💬 Análisis de Sentimiento y Corrección de Texto - Potenciado por TextBlob y Google Translate</span>", unsafe_allow_html=True)

        
    






    



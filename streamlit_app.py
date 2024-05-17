import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os

st.success('Gratulacje! uruchomiono aplikację')

st.title('Lab05. Translator')


st.write('Przykładowa aplikacja z wykorzystaniem Streamlit')
st.write('Aplikacja służy do tłumaczenie języka angielskiego na niemiecki oraz oceny czy dane słowo jest pozytywne czy negatywne')

st.write('1. wybierz opcja tłumaczenia lub wydźwięku emocjonalnego')
st.write('2. wpisz słowo lub zdanie')
st.write('3. wciśnij kombinacje ctrl+enter by zatwierdzić')

import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tłumaczenie tekstu (eng to de)",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)

if option == "Tłumaczenie tekstu (eng to de)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        with st.spinner('Tłumaczę...'):
                translator = pipeline("translation_en_to_de")
                answer = translator(text, max_length=512)
                st.success('Tłumaczenie zakończone!')
                st.snow()
                st.write(answer[0]['translation_text'])
            
st.subheader('s22484')
# st.subheader('Zadanie do wykonania')
# st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/docs/transformers/index')
# st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
# st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
# st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
# st.write('🐞 Na końcu umieść swój numer indeksu')
# st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
# st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')

import streamlit as st
import base64
st.set_page_config(
    page_title="DS_club_main",
    page_icon="👋",
)
st.title('Добро пожаловать на сервис от команды REU DS club!')
st.markdown('''С помощью алгоритмов машинного обучения и статистики вы сможете без всякийх 
затруднений легко провести анализ времееного ряда, а также детекцию на аномалии ''')
st.sidebar.success("Выберете интересующий раздел")
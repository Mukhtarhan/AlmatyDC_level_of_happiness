import streamlit as st
import pandas as pd
import base64
import plotly.express as px
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components

#Боковая картина
st.markdown(
    """
    <style>
    .cover-glow {
        width: 180px;
        height: auto;
        padding: 3px;
        box-shadow: 
            0 0 5px #330000,
            0 0 10px #660000,
            0 0 15px #990000,
            0 0 20px #CC0000,
            0 0 25px #FF0000,
            0 0 30px #FF3333,
            0 0 35px #FF6666;
        position: relative;
        z-index: -1;
        border-radius: 30px;  /* Rounded corners */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

#Функция для картины
def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


#Функция для информации сайта
def kz_info_almaty():
    st.sidebar.markdown("---")
    on = st.sidebar.toggle("Сайт туралы ақпарат:", True)
    if on:
        sidebar_text_container = st.sidebar.container()
        with sidebar_text_container:
            st.write("**Алматыға арналған ақпараттық порталға қош келдіңіз!**")
            st.markdown("Біздің сайтта біз Алматыдағы өмірдің келесі аспектілері туралы деректерді беруге ерекше көңіл бөлеміз:")
            st.markdown("**Бақыт деңгейі**: Бақыт индексінің динамикасын қадағалаңыз және оны Алматының басқа аудандарымен салыстырыңыз.")
            st.markdown("**Жұмыссыздық**: жұмыссыздық деңгейін бақылаңыз.")
            st.markdown("**Ластаушы заттардың шығарындылары**: Қаладағы экологиялық жағдайды бақылаңыз және ауаның ластану деңгейінен хабардар болыңыз.")
            st.markdown("**Қылмыс статистикасы**: Қаланың әртүрлі аудандарындағы қылмыс деңгейі туралы хабардар болыңыз және қауіпсіздігіңіз туралы негізделген шешім қабылдаңыз.")
            st.markdown("**Өмір сүру ұзақтығы**: Қаладағы орташа өмір сүру ұзақтығы туралы біліңіз.")
            st.markdown("**Өмір сүру деңгейі**: Алматыда өмір сүруге қажетті өнімдер мен қызметтердің ең аз жиынтығынан хабардар болыңыз.")
            st.markdown("**Тұрғын үй нарығындағы бағалар**: қаланың әртүрлі аудандарындағы жылжымайтын мүлік бағасының динамикасын қадағалаңыз және болашаққа болжам жасаңыз.")
            st.markdown("**Еңбекақы**: Қаланың әртүрлі аймақтарындағы орташа жалақы деңгейі туралы біліңіз.")


#Функция для КЗ главной части
def kz_lang_almaty():
    st.markdown("<h1 style = 'text-align: center;'>Алматы Қаласының Деректері🍎</h1>", unsafe_allow_html=True)
    st.markdown("---")
    df = pd.read_excel("DataBase_for_Project_казак\Алматы_кз.xlsx")
    option = st.selectbox("Параметрді таңдаңыз: ", (
        "Бақыт деңгейі", "Жұмыссыздық", "Ластаушы заттардың шығарындылары", "Қылмыс статистикасы",
        "Өмірдің ұзақтығы", "Күнкөріс деңгейі", "Тұрғын үй бағасы", "Еңбекақы"))
    if option == "Бақыт деңгейі":
        with st.container(height=490, border=True):
            fig_hs = px.line(df, x="Жыл", y="Бақыт деңгейі")
            st.plotly_chart(fig_hs, use_container_width=True)
    elif option == "Жұмыссыздық":
        with st.container(height=490, border=True):
            fig_ur = px.line(df, x="Жыл", y="Жұмыссыздық")
            st.plotly_chart(fig_ur, use_container_width=True)
    elif option == "Ластаушы заттардың шығарындылары":
        with st.container(height=490, border=True):
            fig_pl = px.line(df, "Жыл", "Ластаушы заттардың шығарындылары")
            st.plotly_chart(fig_pl, use_container_width=True)
    elif option == "Қылмыс статистикасы":
        with st.container(height=490, border=True):
            fig_cr = px.pie(df, "Жыл", "Қылмыс статистикасы", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)
    elif option == "Өмірдің ұзақтығы":
        with st.container(height=490, border=True):
            fig_le = px.scatter(df, x="Жыл", y="Өмірдің ұзақтығы")
            st.plotly_chart(fig_le, use_container_width=True)
    elif option == "Күнкөріс деңгейі":
        with st.container(height=490, border=True):
            fig_lw = px.bar(df, x="Күнкөріс деңгейі", y="Жыл", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)
    elif option == "Тұрғын үй бағасы":
        with st.container(height=490, border=True):
            fig_hp = px.bar(df, x="Жыл", y="Тұрғын үй бағасы")
            st.plotly_chart(fig_hp, use_container_width=True)
    elif option == "Еңбекақы":
        with st.container(height=490, border=True):
            fig_in = px.line(df, x="Жыл", y="Еңбекақы")
            st.plotly_chart(fig_in, use_container_width=True)
    #Боковые настройки
    st.sidebar.markdown("---")
    #Нижняя картина боковая
    img_path = "gh7.jpg"  # Replace with the actual image path
    img_base64 = img_to_base64(img_path)
    st.sidebar.markdown(
        f'<img src="data:image/png;base64,{img_base64}" class="cover-glow">',
        unsafe_allow_html=True,
    )
    #Карта Алматы
    st.markdown("<h1 style = 'text-align: center;'>Алматы Картасы 🗺️</h1>", unsafe_allow_html=True)
    with open("webmap.html", "r", encoding="utf-8") as f:
        map_html = f.read()
        components.html(map_html, height=600)
    st.sidebar.markdown("---")
    st.sidebar.markdown('''<small>Практикалық жоба | 2024 жылғы маусым-шілде | Айдарбек, Асан, Мұхтархан</small>''',
                        unsafe_allow_html=True)

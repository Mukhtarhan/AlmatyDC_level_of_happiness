import streamlit as st
import pandas as pd
import base64
import plotly.express as px
import pydeck as pdk
from almaty_lang_function import eng_lang_almaty
from almaty_lang_function import en_info_almaty
from almaty_lang_function_kz import kz_lang_almaty
from almaty_lang_function_kz import kz_info_almaty
import streamlit.components.v1 as components




#Интерфейс языка
language = st.sidebar.selectbox('Язык/Language/Тіл:', ['Русский', 'English', 'Қазақ'])
st.sidebar.markdown("---")


#Дизайн боковых картин
st.markdown(
    """
    <style>
    
    .st-emotion-cache-1gv3huu {
        background-color: bisque;
    }
    .st-emotion-cache-12fmjuu {
        background-color: #fff7ed;
    }
    .st-emotion-cache-bm2z3a {
        background-color: #fff7ed;
    }
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

#Функция для картин
def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

#Вверхняя боковая картина
img_path = "AlmatyDC_level_of_happiness\open.png"
img_base64 = img_to_base64(img_path)
st.sidebar.markdown(
    f'<a href="https://almatydc.kz/"><img src="data:image\png;base64,{img_base64}" class="cover-glow"></a>',
    unsafe_allow_html=True,
)

#Информация о сайте
if language == "Русский":
    st.sidebar.markdown("---")
    on = st.sidebar.toggle("Информация о сайте:", True)
    if on:
        sidebar_text_container = st.sidebar.container()
        with sidebar_text_container:
            st.write("**Добро пожаловать на информационный портал, посвященный Алматы!**")
            st.markdown("На нашем сайте особое внимание мы уделяем предоставлению данных о следующих аспектах жизни в Алматы:")
            st.markdown("**Уровень счастья населения**: Отслеживайте динамику индекса счастья и сравнивайте его с другими районами Алматы.")
            st.markdown("**Безработица**: Отслеживайте уровень безработицы.")
            st.markdown("**Выбросы загрязняющих веществ**: Следите за экологической ситуацией в городе и будьте в курсе уровня загрязнения воздуха.")
            st.markdown("**Статистика преступности**: Будьте в курсе уровня преступности в разных районах города и принимайте осознанные решения о своей безопасности.")
            st.markdown("**Протяженность жизни**: Узнайте о средней продолжительности жизни в городе.")
            st.markdown("**Прожиточный минимум**: Будьте в курсе минимального набора продуктов и услуг, необходимого для жизни в Алматы.")
            st.markdown("**Цены рынка жилья**: Отслеживайте динамику цен на недвижимость в разных районах города и делайте прогнозы на будущее.")
            st.markdown("**Заработная плата**: Узнайте о среднем уровне заработной платы в разных районах города.")

elif language == "English":
    en_info_almaty()
elif language == "Қазақ":
    kz_info_almaty()


#Главная часть
if language == "Русский":
    st.markdown("<h1 style = 'text-align: center;'>Данные Города Алматы 🍎</h1>", unsafe_allow_html=True)
    st.markdown("---")
    df = pd.read_excel("AlmatyDC_level_of_happiness\DataBase_for_Project\Алматы.xlsx")
    option = st.selectbox("Выбрать параметр: ", (
    "Уровень счастья населения", "Безработица", "Выбросы загрязняющих веществ", "Статистика преступности",
    "Протяженность жизни", "Прожиточный минимум", "Цены на рынке жилья", "Заработная плата"))
    if option == "Уровень счастья населения":
        with st.container(height=490, border=True):
            fig_hs = px.line(df, x="Год", y="Уровень счастья")
            st.plotly_chart(fig_hs, use_container_width=True)
    elif option == "Безработица":
        with st.container(height=490, border=True):
            fig_ur = px.line(df, x="Год", y="Безработица")
            st.plotly_chart(fig_ur, use_container_width=True)
    elif option == "Выбросы загрязняющих веществ":
        with st.container(height=490, border=True):
            fig_pl = px.line(df, "Год", "Выбросы загрязняющих веществ")
            st.plotly_chart(fig_pl, use_container_width=True)
    elif option == "Статистика преступности":
        with st.container(height=490, border=True):
            fig_cr = px.pie(df, "Год", "Статистика преступности", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)
    elif option == "Протяженность жизни":
        with st.container(height=490, border=True):
            fig_le = px.scatter(df, x="Год", y="Протяженность жизни")
            st.plotly_chart(fig_le, use_container_width=True)
    elif option == "Прожиточный минимум":
        with st.container(height=490, border=True):
            fig_lw = px.bar(df, x="Прожиточный минимум", y="Год", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)
    elif option == "Цены на рынке жилья":
        with st.container(height=490, border=True):
            fig_hp = px.bar(df, x="Год", y="Цены на рынке жилья")
            st.plotly_chart(fig_hp, use_container_width=True)
    elif option == "Заработная плата":
        with st.container(height=490, border=True):
            fig_in = px.line(df, x="Год", y="Заработная плата")
            st.plotly_chart(fig_in, use_container_width=True)
    #Настройки боковой панели
    st.sidebar.markdown("---")
    #Нижняя картина в боковой панели
    img_path = "AlmatyDC_level_of_happiness\gh7.jpg"  # Replace with the actual image path
    img_base64 = img_to_base64(img_path)
    st.sidebar.markdown(
        f'<a href="https://github.com/aydarbek30/AlmatyDC_happiness_level.git"><img src="data:image\png;base64,{img_base64}" class="cover-glow"></a>',
        unsafe_allow_html=True,
    )
    #Реквезиты
    st.sidebar.markdown("---")
    st.sidebar.markdown('''<small>Практический проект | Июнь-Июль 2024 | Айдарбек, Асан, Мухтархан</small>''',
                                unsafe_allow_html=True)

#Функция для англ интерфейса
elif language == "English":
    eng_lang_almaty()
elif language == "Қазақ":
    kz_lang_almaty()



#карта алматы
if language == "Русский":
    st.markdown("<h1 style = 'text-align: center;'>Карта Районов Алматы 🗺️</h1>", unsafe_allow_html=True)
    with open("AlmatyDC_level_of_happiness\webmap.html", "r", encoding="utf-8") as f:
        map_html = f.read()
        components.html(map_html, height=600)

    
        




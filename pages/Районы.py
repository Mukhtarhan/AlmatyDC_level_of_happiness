import streamlit as st
import pandas as pd
import base64
import plotly.express as px
from districts_lang_function import eng_lang_district
from districts_lang_function_kz import kz_lang_district



#Свитчер языков в боковой панели
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
    f'<a href="https://almatydc.kz/"><img src="data:image/png;base64,{img_base64}" class="cover-glow"></a>',
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")


#Настройки боковой панели
if language == "Русский":
    st.sidebar.subheader("Данные о каждом районе:")
    opt = st.sidebar.radio('Выбрать район: ', options=
    [
        'Алатауский',
        'Алмалинский',
        'Ауэзовский',
        'Бостандыкский',
        'Жетысуский',
        'Медеуский',
        'Наурызбайский',
        'Турксибский'])


    #РАЙОНЫ
    df1 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project\Цены на рынке жилья.xlsx')
    df2 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project\Протяженность жизни.xlsx')
    df3 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project\Безработица.xlsx')
    df4 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project\Заработная плата.xlsx')
    df5 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project\Прожиточный минимум.xlsx')
    df6 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project\Уровень счастья.xlsx')
    df7 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project\Статистика преступности.xlsx')
    df8 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project\Выбросы жидких и газообразных загрязняющих веществ.xlsx')

    #Алатауский район
    if opt == "Алатауский":
        st.markdown("<h1 style = 'text-align: center;'>Алатауский район 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)


        col4.metric("Уровень счастья населения", "5,7", "+0,4")
        col5.metric("Безработица", "4,4%", "-0,7%", delta_color="inverse")
        col6.metric("Выбросы загрязняющих веществ", "29,7", "+0,2", delta_color="inverse")

        with col1:
            st.subheader("Статистика преступности")
            fig_cr = px.pie(df7, "Год", "Алатауский", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Протяженность жизни")
            fig_in = px.scatter(df2, x="Год", y="Алатауский")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Прожиточный минимум")
            fig_lw = px.bar(df5, x="Алатауский", y="Год", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Цены на рынке жилья")
            fig_hp = px.line(df1, "Год", "Алатауский")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Заработная плата")
            fig_in = px.line(df4, x="Год", y="Алатауский")
            st.plotly_chart(fig_in, use_container_width=True)


    #Алмалинский район
    if opt == "Алмалинский":
        st.markdown("<h1 style = 'text-align: center;'>Алмалинский район 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Уровень счастья населения", "5,5", "+0,4")
        col5.metric("Безработица", "4,7%", "-0,1%", delta_color="inverse")
        col6.metric("Выбросы загрязняющих веществ", "0,2", "0", delta_color="off")

        with col1:
            st.subheader("Статистика преступности")
            fig_cr = px.pie(df7, "Год", "Алмалинский", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Протяженность жизни")
            fig_in = px.scatter(df2, x="Год", y="Алмалинский")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Прожиточный минимум")
            fig_lw = px.bar(df5, x="Алмалинский", y="Год", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Цены на рынке жилья")
            fig_hp = px.line(df1, "Год", "Алмалинский")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Заработная плата")
            fig_in = px.line(df4, x="Год", y="Алмалинский")
            st.plotly_chart(fig_in, use_container_width=True)


    #Ауэзовский район
    if opt == "Ауэзовский":
        st.markdown("<h1 style = 'text-align: center;'>Ауэзовский район 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Уровень счастья населения", "5,8", "+0,6")
        col5.metric("Безработица", "4,4%", "-0,7%", delta_color="inverse")
        col6.metric("Выбросы загрязняющих веществ", "0,9", "-0,1", delta_color="inverse")

        with col1:
            st.subheader("Статистика преступности")
            fig_cr = px.pie(df7, "Год", "Ауэзовский", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Протяженность жизни")
            fig_in = px.scatter(df2, x="Год", y="Ауэзовский")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Прожиточный минимум")
            fig_lw = px.bar(df5, x="Ауэзовский", y="Год", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Цены на рынке жилья")
            fig_hp = px.line(df1, "Год", "Ауэзовский")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Заработная плата")
            fig_in = px.line(df4, x="Год", y="Ауэзовский")
            st.plotly_chart(fig_in, use_container_width=True)


    #Бостандыкский район
    if opt == "Бостандыкский":
        st.markdown("<h1 style = 'text-align: center;'>Бостандыкский район 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Уровень счастья населения", "6,1", "+0,6")
        col5.metric("Безработица", "8,3%", "0%", delta_color="off")
        col6.metric("Выбросы загрязняющих веществ", "1,4", "+0,7", delta_color="inverse")

        with col1:
            st.subheader("Статистика преступности")
            fig_cr = px.pie(df7, "Год", "Бостандыкский", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Протяженность жизни")
            fig_in = px.scatter(df2, x="Год", y="Бостандыкский")
            st.plotly_chart(fig_in, use_container_width=True)


        with col3:
            st.subheader("Прожиточный минимум")
            fig_lw = px.bar(df5, x="Бостандыкский", y="Год", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Цены на рынке жилья")
            fig_hp = px.line(df1, "Год", "Бостандыкский")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Заработная плата")
            fig_in = px.line(df4, x="Год", y="Бостандыкский")
            st.plotly_chart(fig_in, use_container_width=True)


    #Жетысуский район
    if opt == "Жетысуский":
        st.markdown("<h1 style = 'text-align: center;'>Жетысуский район 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Уровень счастья населения", "6,4", "+1,1")
        col5.metric("Безработица", "4,8%", "-0,2%", delta_color="inverse")
        col6.metric("Выбросы загрязняющих веществ", "1,7", "+0,2", delta_color="inverse")

        with col1:
            st.subheader("Статистика преступности")
            fig_cr = px.pie(df7, "Год", "Жетысуский", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Протяженность жизни")
            fig_in = px.scatter(df2, x="Год", y="Жетысуский")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Прожиточный минимум")
            fig_lw = px.bar(df5, x="Жетысуский", y="Год", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Цены на рынке жилья")
            fig_hp = px.line(df1, "Год", "Жетысуский")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Заработная плата")
            fig_in = px.line(df4, x="Год", y="Жетысуский")
            st.plotly_chart(fig_in, use_container_width=True)


    #Медеуский район
    if opt == "Медеуский":
        st.markdown("<h1 style = 'text-align: center;'>Медеуский район 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Уровень счастья населения", "6,8", "+0,9")
        col5.metric("Безработица", "6,3%", "0%", delta_color="off")
        col6.metric("Выбросы загрязняющих веществ", "0,2", "-0,1", delta_color="inverse")

        with col1:
            st.subheader("Статистика преступности")
            fig_cr = px.pie(df7, "Год", "Медеуский", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Протяженность жизни")
            fig_in = px.scatter(df2, x="Год", y="Медеуский")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Прожиточный минимум")
            fig_lw = px.bar(df5, x="Медеуский", y="Год", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Цены на рынке жилья")
            fig_hp = px.line(df1, "Год", "Медеуский")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Заработная плата")
            fig_in = px.line(df4, x="Год", y="Медеуский")
            st.plotly_chart(fig_in, use_container_width=True)


    #Наурызбайский район
    if opt == "Наурызбайский":
        st.markdown("<h1 style = 'text-align: center;'>Наурызбайский район 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Уровень счастья населения", "6,3", "+0,5")
        col5.metric("Безработица", "4,7%", "-0,6%", delta_color="inverse")
        col6.metric("Выбросы загрязняющих веществ", "0,3", "0", delta_color="off")

        with col1:
            st.subheader("Статистика преступности")
            fig_cr = px.pie(df7, "Год", "Наурызбайский", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Протяженность жизни")
            fig_in = px.scatter(df2, x="Год", y="Наурызбайский")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Прожиточный минимум")
            fig_lw = px.bar(df5, x="Наурызбайский", y="Год", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Цены на рынке жилья")
            fig_hp = px.line(df1, "Год", "Наурызбайский")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Заработная плата")
            fig_in = px.line(df4, x="Год", y="Наурызбайский")
            st.plotly_chart(fig_in, use_container_width=True)


    #Турксибский район
    if opt == "Турксибский":
        st.markdown("<h1 style = 'text-align: center;'>Турксибский район 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")

        col7, col8 = st.columns(2)

        col4.metric("Уровень счастья населения", "7,3", "+0,5")
        col5.metric("Безработица", "5%", "+0,1%", delta_color="inverse")
        col6.metric("Выбросы загрязняющих веществ", "1,4", "-0,1", delta_color="inverse")

        with col1:
            st.subheader("Статистика преступности")
            fig_cr = px.pie(df7, "Год", "Турксибский", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Протяженность жизни")
            fig_in = px.scatter(df2, x="Год", y="Турксибский")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Прожиточный минимум")
            fig_lw = px.bar(df5, x="Турксибский", y="Год", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Цены на рынке жилья")
            fig_hp = px.line(df1, "Год", "Турксибский")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Заработная плата")
            fig_in = px.line(df4, x="Год", y="Турксибский")
            st.plotly_chart(fig_in, use_container_width=True)
    #Настройки боковой панели
    st.sidebar.markdown("---")
    #Нижняя боковая картина
    img_path = "AlmatyDC_level_of_happiness\gh7.jpg"  # Replace with the actual image path
    img_base64 = img_to_base64(img_path)
    st.sidebar.markdown(
        f'<img src="data:image/png;base64,{img_base64}" class="cover-glow">',
        unsafe_allow_html=True,
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown('''<small>Практический проект | Июнь-Июль 2024 | Айдарбек, Асан, Мухтархан</small>''',
                        unsafe_allow_html=True)


elif language == "English":
    eng_lang_district()
elif language == "Қазақ":
    kz_lang_district()












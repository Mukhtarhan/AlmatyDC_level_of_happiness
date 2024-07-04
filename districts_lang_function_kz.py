import streamlit as st
import pandas as pd
import base64
import plotly.express as px





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


#Функция для основной КЗ части
def kz_lang_district():
    st.sidebar.subheader("Әр аудан бойынша деректер:")
    opt = st.sidebar.radio('Аймақты таңдаңыз: ', options=
    [
        'Алатау',
        'Алмалы',
        'Әуезовский',
        'Бостандық',
        'Жетісу',
        'Медеу',
        'Наурызбай',
        'Түрксіб'])

    #Районы
    df1 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_казак\Цены на рынке жилья_кз.xlsx')
    df2 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_казак\Протяженность жизни_кз.xlsx')
    df3 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_казак\Безработица_кз.xlsx')
    df4 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_казак\Заработная плата_кз.xlsx')
    df5 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_казак\Прожиточный минимум_кз.xlsx')
    df6 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_казак\Уровень счастья_кз.xlsx')
    df7 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_казак\Статистика преступности_кз.xlsx')
    df8 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_казак\Выбросы жидких и газообразных загрязняющих веществ_кз.xlsx')

    #Алатауский район
    if opt == "Алатау":
        st.markdown("<h1 style = 'text-align: center;'>Алатау ауданы 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Бақыт деңгейі", "5,7", "+0,4")
        col5.metric("Жұмыссыздық", "4,4%", "-0,7%", delta_color="inverse")
        col6.metric("Ластаушы заттардың шығарындылары", "29,7", "+0,2", delta_color="inverse")

        with col1:
            st.subheader("Қылмыс статистикасы")
            fig_cr = px.pie(df7, "Жыл", "Алатау", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Өмір сүру ұзақтығы")
            fig_in = px.scatter(df2, x="Жыл", y="Алатау")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Өмір сүру деңгейі")
            fig_lw = px.bar(df5, x="Алатау", y="Жыл", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Тұрғын үй бағасы")
            fig_hp = px.line(df1, "Жыл", "Алатау")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Еңбекақы")
            fig_in = px.line(df4, x="Жыл", y="Алатау")
            st.plotly_chart(fig_in, use_container_width=True)

    #Алмалинский район
    if opt == "Алмалы":
        st.markdown("<h1 style = 'text-align: center;'>Алмалы ауданы 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Бақыт деңгейі", "5,5", "+0,4")
        col5.metric("Жұмыссыздық", "4,7%", "-0,1%", delta_color="inverse")
        col6.metric("Ластаушы заттардың шығарындылары", "0,2", "0", delta_color="off")

        with col1:
            st.subheader("Қылмыс статистикасы")
            fig_cr = px.pie(df7, "Жыл", "Алмалы", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Өмір сүру ұзақтығы")
            fig_in = px.scatter(df2, x="Жыл", y="Алмалы")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Өмір сүру деңгейі")
            fig_lw = px.bar(df5, x="Алмалы", y="Жыл", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Тұрғын үй бағасы")
            fig_hp = px.line(df1, "Жыл", "Алмалы")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Еңбекақы")
            fig_in = px.line(df4, x="Жыл", y="Алмалы")
            st.plotly_chart(fig_in, use_container_width=True)

    #Ауэзовский район
    if opt == "Әуезовский":
        st.markdown("<h1 style = 'text-align: center;'>Әуезов ауданы 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Бақыт деңгейі", "5,8", "+0,6")
        col5.metric("Жұмыссыздық", "4,4%", "-0,7%", delta_color="inverse")
        col6.metric("Ластаушы заттардың шығарындылары", "0,9", "-0,1", delta_color="inverse")

        with col1:
            st.subheader("Қылмыс статистикасы")
            fig_cr = px.pie(df7, "Жыл", "Әуезовский", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Өмір сүру ұзақтығы")
            fig_in = px.scatter(df2, x="Жыл", y="Әуезовский")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Өмір сүру деңгейі")
            fig_lw = px.bar(df5, x="Әуезовский", y="Жыл", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Тұрғын үй бағасы")
            fig_hp = px.line(df1, "Жыл", "Әуезовский")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Еңбекақы")
            fig_in = px.line(df4, x="Жыл", y="Әуезовский")
            st.plotly_chart(fig_in, use_container_width=True)

    #Бостандыкский район
    if opt == "Бостандық":
        st.markdown("<h1 style = 'text-align: center;'>Бостандық ауданы 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Бақыт деңгейі", "6,1", "+0,6")
        col5.metric("Жұмыссыздық", "8,3%", "0%", delta_color="off")
        col6.metric("Ластаушы заттардың шығарындылары", "1,4", "+0,7", delta_color="inverse")

        with col1:
            st.subheader("Қылмыс статистикасы")
            fig_cr = px.pie(df7, "Жыл", "Бостандық", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Өмір сүру ұзақтығы")
            fig_in = px.scatter(df2, x="Жыл", y="Бостандық")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Өмір сүру деңгейі")
            fig_lw = px.bar(df5, x="Бостандық", y="Жыл", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Тұрғын үй бағасы")
            fig_hp = px.line(df1, "Жыл", "Бостандық")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Еңбекақы")
            fig_in = px.line(df4, x="Жыл", y="Бостандық")
            st.plotly_chart(fig_in, use_container_width=True)

    #Жетысуский район
    if opt == "Жетісу":
        st.markdown("<h1 style = 'text-align: center;'>Жетісу ауданы 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Бақыт деңгейі", "6,4", "+1,1")
        col5.metric("Жұмыссыздық", "4,8%", "-0,2%", delta_color="inverse")
        col6.metric("Ластаушы заттардың шығарындылары", "1,7", "+0,2", delta_color="inverse")

        with col1:
            st.subheader("Қылмыс статистикасы")
            fig_cr = px.pie(df7, "Жыл", "Жетісу", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Өмір сүру ұзақтығы")
            fig_in = px.scatter(df2, x="Жыл", y="Жетісу")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Өмір сүру деңгейі")
            fig_lw = px.bar(df5, x="Жетісу", y="Жыл", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Тұрғын үй бағасы")
            fig_hp = px.line(df1, "Жыл", "Жетісу")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Еңбекақы")
            fig_in = px.line(df4, x="Жыл", y="Жетісу")
            st.plotly_chart(fig_in, use_container_width=True)

    #Медеуский район
    if opt == "Медеу":
        st.markdown("<h1 style = 'text-align: center;'>Медеу ауданы 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Бақыт деңгейі", "6,8", "+0,9")
        col5.metric("Жұмыссыздық", "6,3%", "0%", delta_color="off")
        col6.metric("Ластаушы заттардың шығарындылары", "0,2", "-0,1", delta_color="inverse")

        with col1:
            st.subheader("Қылмыс статистикасы")
            fig_cr = px.pie(df7, "Жыл", "Медеу", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Өмір сүру ұзақтығы")
            fig_in = px.scatter(df2, x="Жыл", y="Медеу")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Өмір сүру деңгейі")
            fig_lw = px.bar(df5, x="Медеу", y="Жыл", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Тұрғын үй бағасы")
            fig_hp = px.line(df1, "Жыл", "Медеу")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Еңбекақы")
            fig_in = px.line(df4, x="Жыл", y="Медеу")
            st.plotly_chart(fig_in, use_container_width=True)

    #Наурызбайский район
    if opt == "Наурызбай":
        st.markdown("<h1 style = 'text-align: center;'>Наурызбай ауданы 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Бақыт деңгейі", "6,3", "+0,5")
        col5.metric("Жұмыссыздық", "4,7%", "-0,6%", delta_color="inverse")
        col6.metric("Ластаушы заттардың шығарындылары", "0,3", "0", delta_color="off")

        with col1:
            st.subheader("Қылмыс статистикасы")
            fig_cr = px.pie(df7, "Жыл", "Наурызбай", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Өмір сүру ұзақтығы")
            fig_in = px.scatter(df2, x="Жыл", y="Наурызбай")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Өмір сүру деңгейі")
            fig_lw = px.bar(df5, x="Наурызбай", y="Жыл", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Тұрғын үй бағасы")
            fig_hp = px.line(df1, "Жыл", "Наурызбай")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Еңбекақы")
            fig_in = px.line(df4, x="Жыл", y="Наурызбай")
            st.plotly_chart(fig_in, use_container_width=True)

    #Турксибский район
    if opt == "Түрксіб":
        st.markdown("<h1 style = 'text-align: center;'>Түрксіб ауданы 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")

        col7, col8 = st.columns(2)

        col4.metric("Бақыт деңгейі", "7,3", "+0,5")
        col5.metric("Жұмыссыздық", "5%", "+0,1%", delta_color="inverse")
        col6.metric("Ластаушы заттардың шығарындылары", "1,4", "-0,1", delta_color="inverse")

        with col1:
            st.subheader("Қылмыс статистикасы")
            fig_cr = px.pie(df7, "Жыл", "Түрксіб", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Өмір сүру ұзақтығы")
            fig_in = px.scatter(df2, x="Жыл", y="Түрксіб")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Өмір сүру деңгейі")
            fig_lw = px.bar(df5, x="Түрксіб", y="Жыл", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Тұрғын үй бағасы")
            fig_hp = px.line(df1, "Жыл", "Түрксіб")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Еңбекақы")
            fig_in = px.line(df4, x="Жыл", y="Түрксіб")
            st.plotly_chart(fig_in, use_container_width=True)
    #Боковые настройки
    st.sidebar.markdown("---")
    # Нижняя картина в боковой панели
    img_path = "AlmatyDC_level_of_happiness\gh7.jpg"  # Replace with the actual image path
    img_base64 = img_to_base64(img_path)
    st.sidebar.markdown(
        f'<a href="https://github.com/aydarbek30/AlmatyDC_happiness_level.git"><img src="data:image\png;base64,{img_base64}" class="cover-glow"></a>',
        unsafe_allow_html=True,
    )
    #Реквезиты
    st.sidebar.markdown("---")
    st.sidebar.markdown('''<small>Практикалық жоба | 2024 жылғы маусым-шілде | Айдарбек, Асан, Мұхтархан</small>''',
                        unsafe_allow_html=True)
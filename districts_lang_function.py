import streamlit as st
import pandas as pd
import base64
import plotly.express as px





#Sidebar image
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


#Function for image_eng
def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


#Function of eng main part
def eng_lang_district():
    st.sidebar.subheader("Data about each district:")
    opt = st.sidebar.radio('Select area: ', options=
    [
        'Alatau',
        'Almalinsky',
        'Auezovsky',
        'Bostandyk',
        'Zhetysu',
        'Medeu',
        'Nauryzbay',
        'Turksib'])

    #Districts
    df1 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_ENG\Housing market prices.xlsx')
    df2 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_ENG\Life expectancy.xlsx')
    df3 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_ENG\eUnemployment.xlsx')
    df4 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_ENG\Income.xlsx')
    df5 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_ENG\Living wage.xlsx')
    df6 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_ENG\Happiness level.xlsx')
    df7 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_ENG\Crime statistics.xlsx')
    df8 = pd.read_excel('AlmatyDC_level_of_happiness\DataBase_for_Project_ENG\Emissions of pollutants.xlsx')

    #Alatau district
    if opt == "Alatau":
        st.markdown("<h1 style = 'text-align: center;'>Alatau district 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Happiness level", "5,7", "+0,4")
        col5.metric("Unemployment", "4,4%", "-0,7%", delta_color="inverse")
        col6.metric("Emissions of pollutants", "29,7", "+0,2", delta_color="inverse")

        with col1:
            st.subheader("Crime statistics")
            fig_cr = px.pie(df7, "Year", "Alatau", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Life expectancy")
            fig_in = px.scatter(df2, x="Year", y="Alatau")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Living wage")
            fig_lw = px.bar(df5, x="Alatau", y="Year", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Housing market prices")
            fig_hp = px.line(df1, "Year", "Alatau")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Income")
            fig_in = px.line(df4, x="Year", y="Alatau")
            st.plotly_chart(fig_in, use_container_width=True)

    #Almalinsky district
    if opt == "Almalinsky":
        st.markdown("<h1 style = 'text-align: center;'>Almalinsky district 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Happiness level", "5,5", "+0,4")
        col5.metric("Unemployment", "4,7%", "-0,1%", delta_color="inverse")
        col6.metric("Emissions of pollutants", "0,2", "0", delta_color="off")

        with col1:
            st.subheader("Crime statistics")
            fig_cr = px.pie(df7, "Year", "Almalinsky", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Life expectancy")
            fig_in = px.scatter(df2, x="Year", y="Almalinsky")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Living wage")
            fig_lw = px.bar(df5, x="Almalinsky", y="Year", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Housing market prices")
            fig_hp = px.line(df1, "Year", "Almalinsky")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Income")
            fig_in = px.line(df4, x="Year", y="Almalinsky")
            st.plotly_chart(fig_in, use_container_width=True)

    #Auezovsky district
    if opt == "Auezovsky":
        st.markdown("<h1 style = 'text-align: center;'>Auezovsky district 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Happiness level", "5,8", "+0,6")
        col5.metric("Unemployment", "4,4%", "-0,7%", delta_color="inverse")
        col6.metric("Emissions of pollutants", "0,9", "-0,1", delta_color="inverse")

        with col1:
            st.subheader("Crime statistics")
            fig_cr = px.pie(df7, "Year", "Auezovsky", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Life expectancy")
            fig_in = px.scatter(df2, x="Year", y="Auezovsky")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Living wage")
            fig_lw = px.bar(df5, x="Auezovsky", y="Year", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Housing market prices")
            fig_hp = px.line(df1, "Year", "Auezovsky")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Income")
            fig_in = px.line(df4, x="Year", y="Auezovsky")
            st.plotly_chart(fig_in, use_container_width=True)

    #Bostandyk district
    if opt == "Bostandyk":
        st.markdown("<h1 style = 'text-align: center;'>Bostandyk district 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Happiness level", "6,1", "+0,6")
        col5.metric("Unemployment", "8,3%", "0%", delta_color="off")
        col6.metric("Emissions of pollutants", "1,4", "+0,7", delta_color="inverse")

        with col1:
            st.subheader("Crime statistics")
            fig_cr = px.pie(df7, "Year", "Bostandyk", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Life expectancy")
            fig_in = px.scatter(df2, x="Year", y="Bostandyk")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Living wage")
            fig_lw = px.bar(df5, x="Bostandyk", y="Year", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Housing market prices")
            fig_hp = px.line(df1, "Year", "Bostandyk")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Income")
            fig_in = px.line(df4, x="Year", y="Bostandyk")
            st.plotly_chart(fig_in, use_container_width=True)

    #Zhetysu district
    if opt == "Zhetysu":
        st.markdown("<h1 style = 'text-align: center;'>Zhetysu district 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Happiness level", "6,4", "+1,1")
        col5.metric("Unemployment", "4,8%", "-0,2%", delta_color="inverse")
        col6.metric("Emissions of pollutants", "1,7", "+0,2", delta_color="inverse")

        with col1:
            st.subheader("Crime statistics")
            fig_cr = px.pie(df7, "Year", "Zhetysu", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Life expectancy")
            fig_in = px.scatter(df2, x="Year", y="Zhetysu")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Living wage")
            fig_lw = px.bar(df5, x="Zhetysu", y="Year", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Housing market prices")
            fig_hp = px.line(df1, "Year", "Zhetysu")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Income")
            fig_in = px.line(df4, x="Year", y="Zhetysu")
            st.plotly_chart(fig_in, use_container_width=True)

    #Medeu district
    if opt == "Medeu":
        st.markdown("<h1 style = 'text-align: center;'>Medeu district 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Happiness level", "6,8", "+0,9")
        col5.metric("Unemployment", "6,3%", "0%", delta_color="off")
        col6.metric("Emissions of pollutants", "0,2", "-0,1", delta_color="inverse")

        with col1:
            st.subheader("Crime statistics")
            fig_cr = px.pie(df7, "Year", "Medeu", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Life expectancy")
            fig_in = px.scatter(df2, x="Year", y="Medeu")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Living wage")
            fig_lw = px.bar(df5, x="Medeu", y="Year", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Housing market prices")
            fig_hp = px.line(df1, "Year", "Medeu")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Income")
            fig_in = px.line(df4, x="Year", y="Medeu")
            st.plotly_chart(fig_in, use_container_width=True)

    #Nauryzbay district
    if opt == "Nauryzbay":
        st.markdown("<h1 style = 'text-align: center;'>Nauryzbay district 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")
        col7, col8 = st.columns(2)

        col4.metric("Happiness level", "6,3", "+0,5")
        col5.metric("Unemployment", "4,7%", "-0,6%", delta_color="inverse")
        col6.metric("Emissions of pollutants", "0,3", "0", delta_color="off")

        with col1:
            st.subheader("Crime statistics")
            fig_cr = px.pie(df7, "Year", "Nauryzbay", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Life expectancy")
            fig_in = px.scatter(df2, x="Year", y="Nauryzbay")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Living wage")
            fig_lw = px.bar(df5, x="Nauryzbay", y="Year", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Housing market prices")
            fig_hp = px.line(df1, "Year", "Nauryzbay")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Income")
            fig_in = px.line(df4, x="Year", y="Nauryzbay")
            st.plotly_chart(fig_in, use_container_width=True)

    #Turksib district
    if opt == "Turksib":
        st.markdown("<h1 style = 'text-align: center;'>Turksib district 🏙️</h1>", unsafe_allow_html=True)
        st.markdown("---")
        col4, col5, col6 = st.columns(3)
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        st.markdown("---")

        col7, col8 = st.columns(2)

        col4.metric("Happiness level", "7,3", "+0,5")
        col5.metric("Unemployment", "5%", "+0,1%", delta_color="inverse")
        col6.metric("Emissions of pollutants", "1,4", "-0,1", delta_color="inverse")

        with col1:
            st.subheader("Crime statistics")
            fig_cr = px.pie(df7, "Year", "Turksib", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)

        with col2:
            st.subheader("Life expectancy")
            fig_in = px.scatter(df2, x="Year", y="Turksib")
            st.plotly_chart(fig_in, use_container_width=True)

        with col3:
            st.subheader("Living wage")
            fig_lw = px.bar(df5, x="Turksib", y="Year", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)

        with col7:
            st.subheader("Housing market prices")
            fig_hp = px.line(df1, "Year", "Turksib")
            st.plotly_chart(fig_hp, use_container_width=True)

        with col8:
            st.subheader("Income")
            fig_in = px.line(df4, x="Year", y="Turksib")
            st.plotly_chart(fig_in, use_container_width=True)
    #SIDEBAR SETTINGS_eng
    st.sidebar.markdown("---")
    #Down sidebar image_eng
    img_path = "AlmatyDC_level_of_happiness\gh7.jpg"  # Replace with the actual image path
    img_base64 = img_to_base64(img_path)
    st.sidebar.markdown(
        f'<img src="data:image/png;base64,{img_base64}" class="cover-glow">',
        unsafe_allow_html=True,
    )
    #Rekveziti_eng
    st.sidebar.markdown("---")
    st.sidebar.markdown('''<small>Practice Project  | Jun-July 2024 | Aidarbek, Asan, Muhtarkhan</small>''',
                        unsafe_allow_html=True)
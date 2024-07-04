import streamlit as st
import pandas as pd
import base64
import plotly.express as px
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components


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

#Function for image
def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


#Function for site information
def en_info_almaty():
    st.sidebar.markdown("---")
    on = st.sidebar.toggle("Site Information:", True)
    if on:
        sidebar_text_container = st.sidebar.container()
        with sidebar_text_container:
            st.write("**Welcome to the information portal dedicated to Almaty!**")
            st.markdown("On our site, we pay special attention to providing data on the following aspects of life in Almaty:")
            st.markdown("**Happiness level**: Track the dynamics of the happiness index and compare it with other areas of Almaty.")
            st.markdown("**Unemployment**: Track the unemployment rate.")
            st.markdown("**Emissions of pollutants**: Monitor the environmental situation in the city and be aware of the level of air pollution.")
            st.markdown("**Crime statistics**: Be aware of the crime rate in different areas of the city and make informed decisions about your safety.")
            st.markdown("**Life expectancy**: Find out about the average life expectancy in the city.")
            st.markdown("**Living wage**: Be aware of the minimum set of products and services necessary for life in Almaty.")
            st.markdown("**Housing market prices**: Track the dynamics of real estate prices in different areas of the city and make predictions for the future.")
            st.markdown("**Income**: Find out about the average wage level in different areas of the city.")


#Function for eng lang main part
def eng_lang_almaty():
    st.markdown("<h1 style = 'text-align: center;'>Almaty City Data 🍎</h1>", unsafe_allow_html=True)
    st.markdown("---")
    df = pd.read_excel("AlmatyDC_level_of_happiness\DataBase_for_Project_ENG\Almaty.xlsx")
    option = st.selectbox("Select parameter: ", (
        "Happiness level", "Unemployment", "Emissions of pollutants", "Crime statistics",
        "Life expectancy", "Living wage", "Housing market prices", "Income"))
    if option == "Happiness level":
        with st.container(height=490, border=True):
            fig_hs = px.line(df, x="Year", y="Happiness level")
            st.plotly_chart(fig_hs, use_container_width=True)
    elif option == "Unemployment":
        with st.container(height=490, border=True):
            fig_ur = px.line(df, x="Year", y="Unemployment")
            st.plotly_chart(fig_ur, use_container_width=True)
    elif option == "Emissions of pollutants":
        with st.container(height=490, border=True):
            fig_pl = px.line(df, "Year", "Emissions of pollutants")
            st.plotly_chart(fig_pl, use_container_width=True)
    elif option == "Crime statistics":
        with st.container(height=490, border=True):
            fig_cr = px.pie(df, "Year", "Crime statistics", hole=0.5)
            st.plotly_chart(fig_cr, use_container_width=True)
    elif option == "Life expectancy":
        with st.container(height=490, border=True):
            fig_le = px.scatter(df, x="Year", y="Life expectancy")
            st.plotly_chart(fig_le, use_container_width=True)
    elif option == "Living wage":
        with st.container(height=490, border=True):
            fig_lw = px.bar(df, x="Living wage", y="Year", orientation="h")
            st.plotly_chart(fig_lw, use_container_width=True)
    elif option == "Housing market prices":
        with st.container(height=490, border=True):
            fig_hp = px.bar(df, x="Year", y="Housing market prices")
            st.plotly_chart(fig_hp, use_container_width=True)
    elif option == "Income":
        with st.container(height=490, border=True):
            fig_in = px.line(df, x="Year", y="Income")
            st.plotly_chart(fig_in, use_container_width=True)
    #SIDEBAR SETTINGS
    st.sidebar.markdown("---")
    #Down sidebar image
    img_path = "AlmatyDC_level_of_happiness\gh7.jpg"  # Replace with the actual image path
    img_base64 = img_to_base64(img_path)
    st.sidebar.markdown(
        f'<a href="https://github.com/aydarbek30/AlmatyDC_happiness_level.git"><img src="data:image\png;base64,{img_base64}" class="cover-glow"></a>',
        unsafe_allow_html=True,
    )
    #Map Lamty Disctricts
    st.markdown("<h1 style = 'text-align: center;'>Map of Almaty Districts 🗺️</h1>", unsafe_allow_html=True)
    mapObj = folium.Map(location=[43.238949, 76.889709], zoom_start=10.2)

    with open("AlmatyDC_level_of_happiness\webmap.html", "r", encoding="utf-8") as f:
        map_html = f.read()
        components.html(map_html, height=600)
    #Rekveziti
    st.sidebar.markdown("---")
    st.sidebar.markdown('''<small>Practice Project  | Jun-July 2024 | Aidarbek, Asan, Muhtarkhan</small>''',
                        unsafe_allow_html=True)

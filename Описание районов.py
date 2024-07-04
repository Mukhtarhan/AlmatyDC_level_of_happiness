# import streamlit as st
# from PIL import Image
# import base64
#
# Glow effect for emblem
# st.markdown(
#     """
#     <style>
#     .cover-glow {
#         width: 100%;
#         height: auto;
#         padding: 3px;
#         box-shadow:
#             0 0 5px #330000,
#             0 0 10px #660000,
#             0 0 15px #990000,
#             0 0 20px #CC0000,
#             0 0 25px #FF0000,
#             0 0 30px #FF3333,
#             0 0 35px #FF6666;
#         position: relative;
#         z-index: -1;
#         border-radius: 30px;  /* Rounded corners */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
#
# #Making emblem
# def img_to_base64(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode()
#
# img_path = "pythonProject\open.png"
# img_base64 = img_to_base64(img_path)
# st.sidebar.markdown(
#     f'<a href="https://almatydc.kz/"><img src="data:image/png;base64,{img_base64}" class="cover-glow"></a>',
#     unsafe_allow_html=True,
# )
# st.sidebar.markdown("---")
#
#
#
# #SIDEBAR SETTINGS
# st.sidebar.subheader("Информация о районах")
# opt2 = st.sidebar.radio('Выбрать район: ', options =
#                   ['Алатауский район',
#                   'Алмалинский район',
#                   'Ауэзовский район',
#                   'Бостандыкский район',
#                   'Жетысуский район',
#                   'Медеуский район',
#                   'Наурызбайский район',
#                   'Турксибский район'])
#
# if opt2 == "Алатауский район":
#     st.markdown("<h1 style = 'text-align: center;'></h1>", unsafe_allow_html=True)
#     sc1, sc2 = st.columns(2)
#     hlp_dtl = f"""<span style="font-size: 26px;">
#         <ol>
#         <li style="font-size:15px";>Административно-территориальная единица города Алма-Аты. Образован в 2008 году. Код КАТО kz.75.1210000</li>
#         <li style="font-size:15px";>В 1993-м году Алатауский район был присоединён к Ауэзовскому району и расширил его с южной стороны. В 2008-м году вновь созданный Алатауский район появился в результате разукрупнения Ауэзовского района отделившего от него, его часть севернее проспекта Рыскулова. Административный центр района находится в микрорайоне Шанырак. Географически одноимённые районы (Алатауский до 1993-го и после 2008-го) находятся в разных местах.   </li>
#         <li style="font-size:15px";>Площадь: 104,95 км² (15,39 %, 2-е место)</li>
#         <li style="font-size:15px";>Население (2019): 260 441[2] тыс. чел. (14,04 %, 3-е место)</li>
#         <li style="font-size:15px";>Each of the grid buttons can only be pressed once during the entire game.</li>
#         <li style="font-size:15px";>The game completes when all the grid buttons are pressed.</li>
#         <li style="font-size:15px";>At the end of the game, if you have a positive score, you will have <strong>won</strong>; otherwise, you will have <strong>lost</strong>.</li>
#         </ol></span>"""
#     sc1.subheader('Алатауский район:')
#     sc1.markdown(hlp_dtl, unsafe_allow_html=True)
#
#
#
#
# elif opt2 == "Алмалинский район":
#     st.markdown("<h1 style = 'text-align: center;'>Алмалинский район</h1>", unsafe_allow_html=True)
#     st.subheader("Данные про район")
#
#
# elif opt2 == "Ауэзовский район":
#     st.markdown("<h1 style = 'text-align: center;'>Ауэзовский район</h1>", unsafe_allow_html=True)
#     st.subheader("Данные про район")
#
#
# elif opt2 == "Бостандыкский район":
#     st.markdown("<h1 style = 'text-align: center;'>Бостандыкский район</h1>", unsafe_allow_html=True)
#
# elif opt2 == "Жетысуский район":
#     st.markdown("<h1 style = 'text-align: center;'>Жетысуский район</h1>", unsafe_allow_html=True)
#
# elif opt2 == "Медеуский район":
#     st.markdown("<h1 style = 'text-align: center;'>Медеуский район</h1>", unsafe_allow_html=True)
#
# elif opt2 == "Наурызбайский район":
#     st.markdown("<h1 style = 'text-align: center;'>Наурызбайский район</h1>", unsafe_allow_html=True)
#
# elif opt2 == "Турксибский район":
#     st.markdown("<h1 style = 'text-align: center;'>Турксибский район</h1>", unsafe_allow_html=True)
#
#
#
# st.sidebar.markdown("---")
#
# st.sidebar.markdown('''<small>Practice Project  | Jun-July 2024 | Asan, Aidarbek, Muhtarkhan</small>''', unsafe_allow_html=True)



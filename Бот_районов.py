# import streamlit as st
# from PIL import Image
# import base64
# import time
# import sys
# import os
#
#
# # Glow effect for emblem
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
#
# # Load and display sidebar image with glowing effect
# img_path = "pythonProject/open.png"
# img_base64 = img_to_base64(img_path)
# st.sidebar.markdown(
#     f'<img src="data:image/png;base64,{img_base64}" class="cover-glow">',
#     unsafe_allow_html=True,
# )
# st.sidebar.markdown("---")
#
#
# #Bot interface
# st.title("Задавайте вопросы, я отвечу:robot_face:")
#
# messages = st.container(height=350)
#
# if prompt := st.chat_input("Say something"):
#     messages.chat_message("user").write(prompt)
#     messages.chat_message("assistant").write(f"Echo: {prompt}")
#
#
# #Sidebar interface
# sidebar_toggle = st.sidebar.toggle("Команды", value=False)
#
# if sidebar_toggle:
#     st.sidebar.markdown("""
#             ### ******
#             - **Вопросы по району**: bebebebebeb.
#             - **Вопросы по район**: nenenenenenen.
#             - **Вопросы по район**: kekkekekekekeke.
#             """)
#






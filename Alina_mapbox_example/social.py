import streamlit as st
from streamlit_lottie import st_lottie
import json
import streamlit.components.v1 as components
import math
import json
import time

# Функция для загрузки данных из GeoJSON файла
def load_geojson_data(file_path):
    with open(file_path, "r") as f:
        geojson_data = json.load(f)
    return geojson_data   

def app():

    # Заголовок страницы
    st.title("Анализ по секторам")
    if st.button("Вернуться на главную"):
        st.session_state.current_page = "Главная"

    # Описание приложения
    st.markdown("""
    <div style="text-align: justify;">
    Данное веб-приложение предоставляет удобные инструменты для анализа и прогнозирования
    различных аспектов городской среды в Алматы. Приложение позволяет анализировать 
    распределение инфраструктуры и бизнеса, рассчитывать показатели плотности населения 
    и необходимых инфраструктурных объектов на участке. Оно также позволяет определить 
    привлекательность территории для конкретного типа бизнеса и проводить геоаналитику 
    для более эффективного планирования и развития городской инфраструктуры. 
    Приложение предоставляет интерактивные карты, инструменты для анализа и удобный интерфейс 
    для пользователей, интересующихся инвестициями и принятием решений в области городского развития.
    </div>
    """, unsafe_allow_html=True)

    st.header(" ")

    st.markdown("""#### Шаговая доступность социальных объектов""")

    with open("components/accessibility.html", "r") as f:
        map_html = f.read()
        components.html(map_html, height=600)
         # Создаем и добавляем легенду
        legend_html = """
        <div class="legend">
            <div class="label-left">Минимум</div>
            <div class="gradient"></div>
            <div class="label-right">Максимум</div>
        </div>
        """
        st.markdown(legend_html, unsafe_allow_html=True)
        # CSS стили для легенды
        st.markdown(
            """
            <style>
            .legend {
                position: relative;
                width: 100%; /* Ширина контейнера легенды */
                margin: 0 auto; /* Центрирование контейнера */
                text-align: center;
                background-color: white;
                padding: 10px;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                margin-top: 20px;
            }
            .gradient {
                width: calc(100% - 140px); /* 140px - ширина двух меток и отступов */
                height: 20px;
                background: linear-gradient(to right, rgba(241, 248, 246, 0.45), rgba(17, 87, 171, 0.65), rgba(0, 128, 128, 0.65), rgba(255, 255, 0, 0.65), rgba(126, 177, 16, 0.65), rgba(39, 116, 6, 0.65));
                display: inline-block;
                margin: 0 10px;
            }
            .label-left,
            .label-right {
                display: inline-block;
                width: 50px;
                text-align: center;
            }
            .label-left {
                float: left;
            }
            .label-right {
                float: right;
                margin-right: 20px; /* Отступ справа для слова "Максимум" */
            }
            </style>
            """,
            unsafe_allow_html=True
        )


    st.markdown("""#### Рекомендации по размещению социальных объектов""")


    with open("pythonProject\social_rec.html", "r") as f:
       map_html = f.read()
       components.html(map_html, height=600)
        


########################################################################################################################################

    with st.sidebar:
        with open("data/comp.json", "r", errors='ignore') as f:
            data = json.load(f)
        st_lottie(data)

    st.header(" ")
    # st.markdown("""#### Карта для получения информации по нарисованному полигону""")

    # st.markdown("""
    # <div style="text-align: justify;">
    #     <ul>
    #         <li>По умолчанию на карте показана тепловая карта объектов инфраструктуры</li>
    #         <li>Выберите стиль карты из выпадающего списка для изменения внешнего вида карты</li>
    #         <li>Нажмите на карту для начала рисования полигона на карте</li>
    #         <li>Старайтесь выбирать маленькие участки для получения полее точной информации</li>
    #         <li>После завершения рисования полигона, информация об участке будет отображаться в левой панели</li>
    #         <li>Внизу боковой панели будут также отображены плащадь и периметр участка</li>
    #         <li>Узнав площадь территории, вы можете рассчитать значения показателей в зависимости от количества домов</li>
    #         <li>Для сброса карты и удаления нарисованных полигонов используйте кнопку "Сбросить"</li>
    #         <li>Кнопка "Во весь экран" позволяет перейти в полноэкранный режим для удобства просмотра</li>
    #     </ul>
    # </div>

    #     """, unsafe_allow_html=True)
    

    st.header(" ")

    # Вставляем карту в приложение
    with open("pythonProject\social_combo.html", "r") as f:
        map_html = f.read()
        components.html(map_html, height=600)

        st.markdown("""##### Обеспеченность территорий городской инфраструктурой""")

        # Создаем и добавляем легенду
        legend_html = """
        <div class="legend">
            <div class="label-left">Минимум</div>
            <div class="gradient"></div>
            <div class="label-right">Максимум</div>
        </div>
        """
        st.markdown(legend_html, unsafe_allow_html=True)
        # CSS стили для легенды
        st.markdown(
            """
            <style>
            .legend {
                position: relative;
                width: 100%; /* Ширина контейнера легенды */
                margin: 0 auto; /* Центрирование контейнера */
                text-align: center;
                background-color: white;
                padding: 10px;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                margin-top: 20px;
            }
            .gradient {
                width: calc(100% - 140px); /* 140px - ширина двух меток и отступов */
                height: 20px;
                background: linear-gradient(to right, rgba(241, 248, 246, 0.45), rgba(17, 87, 171, 0.65), rgba(0, 128, 128, 0.65), rgba(255, 255, 0, 0.65), rgba(126, 177, 16, 0.65), rgba(39, 116, 6, 0.65));
                display: inline-block;
                margin: 0 10px;
            }
            .label-left,
            .label-right {
                display: inline-block;
                width: 50px;
                text-align: center;
            }
            .label-left {
                float: left;
            }
            .label-right {
                float: right;
                margin-right: 20px; /* Отступ справа для слова "Максимум" */
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        
    # Кнопка для полноэкранного режима
    # st.markdown('<button onclick="toggleFullscreen()" style="padding: 10px 20px; font-size: 16px; cursor: pointer; border: none; border-radius: 5px; background-color: #ACACAD; color: #ECEBE5;">Полноэкранный режим</button>', unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    /* Стилизация заголовков */
    .stTextInput label {
        font-size: 18px;
    }

    /* Стилизация input fields */
    .stTextInput input {
        font-size: 18px;
        padding: 10px;
        margin: 5px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2); /* Добавление тени */
    }

    /* Стилизация блоков input, включая метки и поля */
    .stTextInput {
        background: #FFFFFF; /* Белый фон */
        border-radius: 5px;
        margin-bottom: 10px; /* Отступ снизу */
    }

    /* Стилизация кнопки */
    .stButton > button {
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 5px;
        border: none;
        color: white;
        background-color: #183F71;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2); /* Добавление тени */
        transition: background-color 0.3s, box-shadow 0.3s, opacity 0.3s;
    }

    .stButton > button:active {
        background-color: transparent; /* Прозрачный фон при нажатии */
        color: #183F71; /* Цвет текста при нажатии */
        box-shadow: none; /* Убрать тень */
        opacity: 0.6; /* Немного прозрачности для визуального отклика */
    }

    /* Стилизация заголовков input */
    .stNumberInput label {
        font-size: 24px;
        font-weight: bold;
        color: #062042; /* Темно-синий цвет текста */
    }

    /* Стилизация контейнера input */
    .stNumberInput > div {
        margin-bottom: 10px; /* Отступ снизу для каждого input */
    }

    /* Стилизация поля input */
    .stNumberInput input {
        font-size: 18px;
        padding: 10px; /* Побольше padding для удобства */
        border-radius: 5px; /* Скругленные углы */
        border: 1px solid #ced4da; /* Светло-серая граница */
        background-color: #f8f9fa; /* Светло-серый фон поля ввода */
    }

    /* Стилизация самого виджета input (может понадобиться дополнительная стилизация) */
    .stNumberInput {
        border: none; /* Убрать рамку, если она есть */
        /* box-shadow: 0px 2px 4px 0px rgba(0,0,0,0.15); /* Небольшая тень для объемности */
    }

    /* Стилизация кнопок управления "+" и "-" */
    .stNumberInput .step-up, .stNumberInput .step-down {
        background-color: #f8f9fa; /* Светло-серый фон кнопок */
    }

    /* Применить стиль ко всем кнопкам внутри виджета number input */
    .stNumberInput button {
        border: 1px solid #ced4da; /* Светло-серая граница */
        background-color: #f8f9fa; /* Светло-серый фон кнопок */
        color: #333; /* Цвет текста */
    }

    /* Указать стиль при наведении */
    .stNumberInput button:hover {
        background-color: #e2e6ea; /* Немного темнее при наведении */
    }
    </style>
    """, unsafe_allow_html=True)

    ######################################################################################

    # st.header("Расчет показателей")

    # # Создаем две колонки
    # col1, col2 = st.columns(2)

    # # Ввод площади участка в первой колонке
    # with col1:
    #     area_km2 = st.number_input("Введите площадь участка (в квадратных километрах):", key="area_km2", min_value=0.1)

    # # Ввод количества домов во второй колонкеs
    # with col2:
    #     number_of_buildings = st.number_input("Введите количество домов:", key="number_of_buildings", min_value=1)


    # calculate_button = st.button("Рассчитать")
    # if calculate_button:
    #     # number_of_buildings = 41
    #     number_of_floor = 9
    #     units_per_floor_per_entrance = 5
    #     entrances_per_building = 3
    #     average_family_size = 3

    #     residential_parking_per_unit = 1.5
    #     commercial_parking_ratio = 3
    #     total_apartments = number_of_buildings * number_of_floor * units_per_floor_per_entrance * entrances_per_building

    #     # Calculate the total population
    #     # total_population = total_apartments * average_family_size

    #     forecasted_population = total_apartments * average_family_size  # 8175

    #     population_density = forecasted_population / (area_km2)  

    #     # Coefficients for infrastructure
    #     parking_space_per_apartment = 1.5
    #     commercial_parking_ratio = 3
    #     daycare_population_coefficient = 0.08
    #     school_population_coefficient = 0.18
    #     green_space_coefficient = 0.10  # use 0.15 for the upper range if needed
    #     streetlight_spacing = 40  # meters
    #     camera_spacing = 45  # meters
    #     commercial_space_coefficient = 0.06
    #     bike_lane_perimeter_multiplier = 0.5  # assuming only the perimeter

    #     # Calculate the perimeter if the area were a square (not accurate for irregular shapes)
    #     perimeter = math.sqrt(area_km2) * 4 * 1000  # converting to meters

    #     # Calculations
    #     daycare_spots_needed = forecasted_population * daycare_population_coefficient
    #     school_spots_needed = forecasted_population * school_population_coefficient
    #     green_space_needed_m2 = area_km2 * green_space_coefficient * 1000000 / 10000  # converting to m² / ga
    #     commercial_space_needed_m2 = area_km2 * commercial_space_coefficient * 1000000  # converting to m²
    #     bike_lane_length_m = perimeter * bike_lane_perimeter_multiplier
    #     streetlights_needed = perimeter / streetlight_spacing
    #     cameras_needed = perimeter / camera_spacing
    #     residential_parking_spaces = total_apartments * residential_parking_per_unit
    #     commercial_parking_spaces = (commercial_space_needed_m2 / 100) * commercial_parking_ratio
    #     total_parking_spaces = residential_parking_spaces + commercial_parking_spaces


    #     # Стилизация текста результатов
    #     st.markdown(
    #         """
    #         <style>
    #         .results-container {
    #             padding: 20px;
    #             border-radius: 5px;
    #             margin-bottom: 20px;
    #             color: #183F71;
    #             display: flex;
    #             flex-direction: column;
    #             align-items: flex-start;
    #             box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); /* Тень вокруг контейнера */
    #             background: #FFFFFF; /* Белый фон для создания объемного вида */
    #         }

    #         .result-item {
    #             width: 100%;
    #             display: flex;
    #             justify-content: space-between;
    #             align-items: center;
    #             margin-bottom: 5px;
    #             border-bottom: 1px solid #E1E1E1; /* Черта под показателем */
    #             padding-bottom: 5px;
    #         }

    #         .result-title {
    #             font-size: 18px;
    #             font-weight: normal; /* Обычный текст */
    #         }

    #         .result-value {
    #             font-size: 18px;
    #             font-weight: bold; /* Жирный текст */
    #             text-align: right;
    #             min-width: 100px;
    #         }
    #         </style>

    #         """,
    #         unsafe_allow_html=True
    #     )

    #     st.markdown(
    #         f"""
    #         <div class="results-container">
    #             <div class="result-item">
    #                 <span class="result-title">Площадь:</span>
    #                 <span class="result-value">{area_km2:.2f} км²</span>
    #             </div>
    #             <div class="result-item">
    #                 <span class="result-title">Прогнозируемое население:</span>
    #                 <span class="result-value">{forecasted_population:.0f} человек</span>
    #             </div>
    #             <div class="result-item">
    #                 <span class="result-title">Плотность населения:</span>
    #                 <span class="result-value">{population_density:.0f} чел./км²</span>
    #             </div>
    #             <div class="result-item">
    #                 <span class="result-title">Общее количество парковочных мест:</span>
    #                 <span class="result-value">{total_parking_spaces:.0f}</span>
    #             </div>
    #             <div class="result-item">
    #                 <span class="result-title">Необходимое количество мест в детских садах:</span>
    #                 <span class="result-value">{daycare_spots_needed:.0f}</span>
    #             </div>
    #             <div class="result-item">
    #                 <span class="result-title">Необходимое количество мест в школах:</span>
    #                 <span class="result-value">{school_spots_needed:.0f}</span>
    #             </div>
    #             <div class="result-item">
    #                 <span class="result-title">Площадь озеленения:</span>
    #                 <span class="result-value">{green_space_needed_m2:.3f} га</span>
    #             </div>
    #             <div class="result-item">
    #                 <span class="result-title">Площадь коммерческих помещений:</span>
    #                 <span class="result-value">{commercial_space_needed_m2:.0f} м²</span>
    #             </div>
    #             <div class="result-item">
    #                 <span class="result-title">Необходимая длина велосипедных дорожек:</span>
    #                 <span class="result-value">{bike_lane_length_m:.0f} м</span>
    #             </div>
    #             <div class="result-item">
    #                 <span class="result-title">Необходимое количество уличных фонарей:</span>
    #                 <span class="result-value">{streetlights_needed:.0f}</span>
    #             </div>
    #             <div class="result-item">
    #                 <span class="result-title">Необходимое количество камер видеонаблюдения:</span>
    #                 <span class="result-value">{cameras_needed:.0f}</span>
    #             </div>
    #         </div>
    #         """,
    #         unsafe_allow_html=True
    #     )



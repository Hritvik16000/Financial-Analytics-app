import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from data_exploration import data_exploration
from data_preprocessing import data_preprocessing
from auto_analysis import auto_analysis

st.set_option('deprecation.showPyplotGlobalUse', False)

custom_css = """
<style>
body {
    background: linear-gradient(45deg, #34495e, #2ecc71, #16a085, #2980b9);
    background-size: 600% 600%;
    animation: gradient 10s ease infinite;
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.title {
    color: white;
    font-size: 48px;
    font-weight: bold;
    text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.7);
}

.subtitle {
    color: white;
    font-size: 24px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.stButton>button {
    background-color: #34495e;
    color: white;
    font-size: 18px;
    padding: 10px 20px;
    border-radius: 5px;
    transition: background-color 0.3s;
}

.stButton>button:hover {
    background-color: #2c3e50;
}

[data-testid="stHorizontalBlock"] > div:first-child {
    border-radius: 10px;
    overflow: hidden;
}

footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    background-color: rgba(240, 242, 246, 0.8);
    color: black;
    font-size: 14px;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
}

footer a {
    color: black;
    text-decoration: none;
    margin-right: 10px;
}

footer a:hover {
    text-decoration: underline;
}

.main-container {
    padding: 20px;
    border-radius: 10px;
    background: rgba(255, 255, 255, 0.8);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
</style>
"""

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main,
[data-testid="stDecoration"],
[data-testid="stHeader"],
footer {
  background: linear-gradient(-45deg, #34495e, #2ecc71, #16a085, #2980b9);
  background-size: 400% 400%;
  animation: gradient 10s ease infinite;
}

@keyframes gradient {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 class='title' style='text-align: center;'>Insight Loom</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle' style='text-align: center;'>Unthread Data Mysteries, One at a Time</p>", unsafe_allow_html=True)

# Main container for content
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# File upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
default_dataset = st.checkbox("Use default Indian_cities.csv dataset")

if default_dataset:
    data = pd.read_csv("Dataset/Indian_cities.csv")
else:
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

if default_dataset or uploaded_file is not None:
    selected = option_menu(
        menu_title=None,
        options=["Info", "Data Exploration", "Data Preprocessing", "Auto Analysis (BETA)"],
        icons=["info-circle", "bar-chart", "wrench", "robot"],
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "rgba(255, 255, 255, 0.8)", "border-radius": "10px", "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)"},
            "icon": {"color": "#34495e", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#ddd", "width": "100%"},
            "nav-link-selected": {"background-color": "#2ecc71", "color": "white"},
        }
    )

    if selected == "Info":
        st.subheader("📚 Introduction")
        st.write("Welcome to the Insight Loom App! This app allows you to perform automated exploratory data analysis (EDA) on your dataset. Simply upload a CSV file or use the default dataset, and explore the various features of the app.")
        st.write("The app provides the following sections:")
        st.write("1. 🔍 Data Exploration: Preview and analyze your dataset, including missing values, data statistics, and visualizations.")
        st.write("2. 🛠️ Data Preprocessing: Preprocess your data by removing unwanted columns, handling missing data, encoding categorical variables, scaling features, and handling outliers.")
        st.write("3. 🤖 Auto Analysis (BETA): Perform automated analysis using OpenAI's language model to generate insights and a summary of your dataset.")
        st.write("Get started by uploading your CSV file or using the default dataset, and explore the different sections of the app!")
    elif selected == "Data Exploration":
        data_exploration(data)
    elif selected == "Data Preprocessing":
        data_preprocessing(data)
    elif selected == "Auto Analysis (BETA)":
        auto_analysis(data, default_dataset)

footer_content = """
<footer>
<div>Created with 🤍 by Hritvik</div>
<div>
    <a href="https://www.linkedin.com/in/hritvik-dadhich" target="_blank">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn" width="20" height="20">
    </a>
    <a href="https://github.com/Hritvik16000" target="_blank">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="20" height="20">
    </a>
</div>
</footer>
"""

st.markdown("</div>", unsafe_allow_html=True)
st.markdown(footer_content, unsafe_allow_html=True)

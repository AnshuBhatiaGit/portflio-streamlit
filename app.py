
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Anshu Bhatia | Portfolio",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Custom styling
st.markdown("""
<style>
.stApp {
    background-color: #050505;
    color: white;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
}

h1, h2, h3, p, label {
    color: white;
}

.gold {
    color: #FBBF24;
    font-weight: bold;
    letter-spacing: 2px;
}

.hero-name {
    font-size: clamp(48px, 6vw, 88px);
    font-weight: 900;
    line-height: 1.05;
    color: white;
}

.hero-title {
    font-size: clamp(22px, 2.5vw, 34px);
    font-weight: 700;
    line-height: 1.3;
    color: white;
}

.skills-line {
    color: #999999;
    font-size: 19px;
}

.location {
    color: #888888;
    text-align: center;
}

button[kind="secondary"] {
    border: none;
    background: transparent;
    color: white;
}

button[kind="secondary"]:hover {
    color: #FBBF24;
}
</style>
""", unsafe_allow_html=True)

# Navigation
logo, navigation = st.columns([1, 2])

with logo:
    st.markdown(
        "<h2 style='color:white;'>Portfolio</h2>",
        unsafe_allow_html=True
    )

with navigation:
    page = st.radio(
        "Navigation",
        ["Home", "Resume", "Projects", "Contact"],
        horizontal=True,
        label_visibility="collapsed"
    )

st.divider()

# Homepage
if page == "Home":

    left, right = st.columns([1.2, 0.9], gap="large")

    with left:
        st.markdown(
            "<p class='gold'>CLOUD SECURITY PORTFOLIO</p>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div class='hero-name'>ANSHU<br>BHATIA</div>",
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            """<div class='hero-title'>
            Cloud Security Engineer | Azure Security |
            Infrastructure as Code
            </div>""",
            unsafe_allow_html=True
        )

        st.markdown(
            """<p class='skills-line'>
            Azure • Terraform • Python • KQL • Security Architecture
            </p>""",
            unsafe_allow_html=True
        )

    with right:
        photo_path = Path("assets/profile.jpg")

        if photo_path.exists():
            st.image(str(photo_path), use_container_width=True)
        else:
            st.markdown(
                """
                <div style="
                    height: 390px;
                    background: #202020;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: #aaaaaa;
                    font-size: 24px;
                ">
                    Add Your Professional Photo
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            "<p class='location'>Colorado, USA</p>",
            unsafe_allow_html=True
        )

elif page == "Resume":
    st.title("My Resume")
    st.write("We will add your professional experience and certifications here.")

elif page == "Projects":
    st.title("My Projects")
    st.write("We will add your Azure security projects here.")

elif page == "Contact":
    st.title("Contact Me")
    st.write("We will add your email and LinkedIn details here.")

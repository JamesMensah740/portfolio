import streamlit as st
from PIL import Image

st.set_page_config(page_title="Welcome", layout="wide")

# === SIDEBAR ===
st.sidebar.title("Navigation")
section = st.sidebar.selectbox("Select Section", ["About Me", "Skills", "Projects", "Contact"])

# === MAIN PAGE ===
if section == "About Me":
    st.title("👋 Hi, I'm James Mensah")
    
    # Profile Picture
    image1 = Image.open("images\picture.jpeg")  # Upload your own image
    st.image(image1, caption="James Mensah", width=250)

    st.markdown("""
    ### About Me
    I'm a data professional who specializes in end-to-end analytics solutions using tools I actually work with—**Pandas, SQL, and Streamlit**.
    
    From cleaning raw data to deploying full dashboards, I believe in _showing_, not telling.
    
    - 💼 Experience: Analytics Engineer with Peepalytics (August 2024 – July 2025)
    - 🔧 Tools I Use: `pandas`, `MySQL`, `Render`, `scrapy`, `streamlit`
    """)
    
    # Second Image (optional)
    image2 = Image.open("images\picture.jpeg")
    st.image(image2, caption="In Action", width=400)

elif section == "Skills":
    st.header("🛠 Skills")
    st.write("""
    - Data Cleaning (Pandas, NumPy)
    - SQL Analysis (MySQL, PostgreSQL)
    - Web Scraping (BeautifulSoup, Scrapy)
    - Dashboarding (Streamlit, Power BI)
    - ETL Automation
    """)

elif section == "Projects":
    st.header("📂 Projects")
    st.write("Interactive dashboards, scraping tools, compensation models, and more (pages coming soon).")

elif section == "Contact":
    st.header("📬 Contact Me")
    st.write("📧 Jamesmensah01789@gmail.com")
    st.write("[🔗 LinkedIn](https://www.linkedin.com/in/YOUR-PROFILE)")
    st.write("[📁 GitHub](https://github.com/YOUR-GITHUB)")


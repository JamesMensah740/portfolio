import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Welcome", layout="wide")

# === SIDEBAR ===
st.sidebar.title("Navigation")
section = st.sidebar.selectbox("Select Section", ["About Me", "Skills", "Projects", "Contact"])

# === MAIN PAGE ===
if section == "About Me":
    st.title("👋 Hi, I'm James Mensah")

    # Correct image path using forward slash
    image_path = os.path.join("images", "picture.jpeg")
    if os.path.exists(image_path):
        image1 = Image.open(image_path)
        st.image(image1, caption="James Mensah", width=250)
    else:
        st.warning("Profile image not found. Please upload to `images/picture.jpeg`")

    st.markdown("""
    ### 👨‍💻 About Me
    I'm **James Mensah**, a results-driven data professional passionate about turning raw data into meaningful business insights.

    With a strong focus on practical tools like **pandas**, **SQL**, and **Streamlit**, I build complete end-to-end analytics solutions — from wrangling messy data to deploying polished dashboards.

    #### 🧩 What Sets Me Apart
    - I use tools I actually work with — no fluff.
    - I prioritize clarity, storytelling, and usability.
    - I believe in _**showing, not telling**_ — every project in this portfolio is interactive and replicable.

    #### 💼 Experience
    **Analytics Engineer at Peepalytics**  
    *August 2024 – July 2025*  
    - Data wrangling and transformation using Python
    - dashboard development
    - Insights generation
    - Analytics pipeline automation

    #### 🧰 Core Stack
    - `pandas` for analysis
    - `MySQL` for querying
    - `streamlit` for dashboards
    - `selenium` for web scraping
    - `PostgreSQL` for data warehousing

    > “Good data tells a story. Great analysts bring it to life.”
    """)


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
    st.write("[🔗 LinkedIn] https://linkedin.com/in/james-mensah-645314248")
    st.write("[📁 GitHub]https://github.com/JamesMensah740")

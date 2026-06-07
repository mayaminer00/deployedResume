import streamlit as st

st.set_page_config(
    page_title="Maya Koushik",
    page_icon="🚀",
    layout="wide"
)

# ---------- SIDEBAR ----------

with st.sidebar:

    st.image("profile.jpg", width=200)

    st.title("🚀 Maya Koushik")

    st.markdown("""
    **AI/ML Undergraduate**
    Backend Developer
    """)

    st.markdown("---")

    st.markdown("""
    📍 Hyderabad, Telangana

    📧 koushikmayaaa@gmail.com

    💻 [GitHub](https://github.com/mayaminer00)

    🔗 [LinkedIn](https://www.linkedin.com/in/koushik-maya-0709742a3)
    """)

    st.markdown("---")

    st.download_button(
        "📄 Download Resume",
        data=open("koushikmaya_resume.pdf", "rb"),
        file_name="Maya_Koushik_Resume.pdf",
        mime="application/pdf"
    )

# ---------- HEADER ----------

st.title("🚀 MAYA KOUSHIK")

st.subheader("AI/ML Undergraduate | Backend Developer")

st.markdown("---")

# ---------- METRICS ----------

col1, col2, col3, col4 = st.columns(4)

col1.metric("LeetCode Problems", "100+")
col2.metric("Projects", "3")
col3.metric("CGPA", "7.6")
col4.metric("Tech Stack", "MERN + AI")

st.markdown("---")

# ---------- ABOUT ----------

st.header("👨‍💻 About Me")

st.write("""
AI/ML undergraduate with hands-on experience in building
machine learning models and full-stack applications.

Skilled in Python, SQL, Java, JavaScript and MERN Stack.
Strong foundation in DSA, Machine Learning,
Deep Learning, NLP and LLMs.

Currently seeking opportunities in
Software Development and AI/ML roles.
""")

# ---------- SKILLS ----------

st.header("🛠 Technical Skills")

skill1, skill2 = st.columns(2)

with skill1:

    st.write("Python")
    st.progress(90)

    st.write("Java")
    st.progress(80)

    st.write("JavaScript")
    st.progress(85)

    st.write("SQL")
    st.progress(85)

with skill2:

    st.write("Node.js")
    st.progress(85)

    st.write("Express.js")
    st.progress(85)

    st.write("MongoDB")
    st.progress(80)

    st.write("Machine Learning")
    st.progress(80)

# ---------- PROJECTS ----------

st.header("📂 Projects")

project1, project2, project3 = st.columns(3)

with project1:
    st.info("🤖 AI Quiz Generator")

    st.write("""
    • MERN Stack

    • Gemini API

    • Dynamic Quiz Generation

    • User Authentication

    • Difficulty Adjustment
    """)

with project2:
    st.success("🔗 URL Shortener")

    st.write("""
    • Node.js

    • Express.js

    • PostgreSQL

    • MVC Architecture

    • REST APIs
    """)

with project3:
    st.warning("🫁 Pneumonia Detection")

    st.write("""
    • CNN

    • TensorFlow

    • Deep Learning

    • Chest X-Ray Classification

    • 92% Accuracy
    """)

# ---------- EDUCATION ----------

st.header("🎓 Education")

st.markdown("""
### B.E Computer Science (AI & ML)
**Keshav Memorial Engineering College**

CGPA: **7.6**

Expected Graduation: **2027**
""")

st.markdown("""
### Intermediate (MPC)

Vaishnavi Junior College

97.3%
""")

st.markdown("""
### SSC

Mother Teresa High School

GPA: 10
""")

# ---------- ACHIEVEMENTS ----------

st.header("🏆 Achievements")

st.success("HackerRank SQL Intermediate Certified")

st.success("Apna College DSA Certificate")

st.success("100+ Problems Solved on LeetCode")

# ---------- CONTACT ----------

st.header("📬 Contact Me")

name = st.text_input("Name")

email = st.text_input("Email")

message = st.text_area("Message")

if st.button("Send Message"):
    st.success("Thank you! Your message has been received.")

# ---------- FOOTER ----------

st.markdown("---")

st.markdown(
    "<center>Made with ❤️ by Koushik</center>",
    unsafe_allow_html=True
)

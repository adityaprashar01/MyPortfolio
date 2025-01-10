import streamlit as st
import webbrowser

# Load Images
# profile_pic = "C:\\Users\\adity\\PycharmProjects\\Myportfolio\\pp.jpeg"



# Function to open links
def open_link(url):
    webbrowser.open_new_tab(url)

# Function to download resume
def download_resume():
    resume_link = "https://drive.google.com/file/d/1Z6jGy1PVEotf2JoMJeRn5CHdC0oASxx8/view?usp=sharing"
    st.markdown(f"[Download Resume]({resume_link})", unsafe_allow_html=True)

# Configure Page
st.set_page_config(page_title="Aditya Prashar", page_icon="🖥️", layout="wide")

# Custom Styling for Aesthetic Design
page_style = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #1a1a2e;
    color: #eaeaea;
    font-family: 'Arial', sans-serif;
}
[data-testid="stSidebar"] {
    background-color: #16213e;
    color: #eaeaea;
}
h1, h2, h3 {
    color: #eaeaea;
}
a {
    color: #00aaff;
    text-decoration: none;
}
a:hover {
    color: #ffaa00;
}
img.circular {
    display: block;
    margin: 0 auto;
    border-radius: 50%;
    border: 5px solid #ffaa00;
    box-shadow: 0px 0px 15px rgba(255, 170, 0, 0.6);
}
.section {
    margin-bottom: 40px;
    padding: 20px;
    background-color: #0f3460;
    border-radius: 10px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
}
.section h2 {
    margin-bottom: 10px;
    border-bottom: 2px solid #00aaff;
    padding-bottom: 5px;
}
button {
    background-color: #00aaff;
    color: #ffffff;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}
button:hover {
    background-color: #ffaa00;
    color: #000000;
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# Sidebar Section
with st.sidebar:
    # st.image(profile_pic, width=250, caption="Aditya Prashar", use_container_width=True)
    st.title("Contact Me")
    st.write("📞 +91 7783858607")
    st.write("✉️ adityaprashar03@gmail.com")
    st.markdown("---")
    if st.button("💼 LinkedIn"):
        open_link("https://www.linkedin.com/in/aditya-prashar-69885a219")
    if st.button("🐙 GitHub"):
        open_link("https://www.github.com/adityaprashar01")

# Header Section with Image
# st.markdown(
#     f"""
#     <div style="
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         margin-bottom: 20px;">
#         <img src="file:///{profile_pic}"
#              alt="Aditya Prashar"
#              style="
#                 width: 150px;
#                 height: 150px;
#                 border-radius: 50%;
#                 border: 5px solid #ffaa00;
#                 box-shadow: 0px 0px 15px rgba(255, 170, 0, 0.6);
#              ">
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

st.title("Welcome to My Portfolio")
st.markdown("---")

# Education Section
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🎓 Education")
st.write(
    "**Vellore Institute of Technology (B.Tech, Computer Science Engineering)** - CGPA: 8.34/10\n\n"
    "**Parkmount Public School (Senior Secondary)** - Percentage: 73.4%\n\n"
    "**Patna Central School (Matriculation)** - Percentage: 79.4%"
)
st.markdown("</div>", unsafe_allow_html=True)

# Experience Section
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("💼 Experience")
st.write(
    "**LingoLeap (Software Engineering Intern)**\n"
    "- Developed an AI-driven platform for TOEFL and IELTS preparation.\n\n"
    "**ISAN Data Systems (App Developer)**\n"
    "- Developed \"Internshipgate\" bridging students and employers.\n\n"
    "**PwC India (CTDP 2.0 Trainee)**\n"
    "- Hands-on experience with Salesforce App Builder and flow automation.\n\n"
    "**Medide (App Developer)**\n"
    "- Integrated Google Maps API for locating healthcare facilities."
)
st.markdown("</div>", unsafe_allow_html=True)

# Projects Section
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🚀 Projects")
st.write(
    "**[Internshipgate](https://play.google.com/store/apps/details?id=com.internshipgate.igapp)**\n"
    "- Core features include user profiles, internship listings, and in-app messaging using Flutter and Dart.\n\n"
    "**[LingoLeap](https://apps.apple.com/us/app/lingoleap-ai-toefl-prep/id6480381514)**\n"
    "- Implemented WebSocket for real-time data retrieval.\n\n"
    "**[Vasudev- Virtual Voice Assistant](https://github.com/adityaprashar01/vasudev/tree/main/vasudeva)**\n"
    "- Integrated ChatGPT and Dall-E APIs for advanced natural language processing and image generation."
)
st.markdown("</div>", unsafe_allow_html=True)

# Technical Skills Section
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🛠️ Technical Skills")
st.write(
    "- **Proficient in:** Java, OOP, SQL, Flutter, Dart, Git, Postman\n"
    "- **Tools:** VS Code, IntelliJ, Figma, Canva"
)
st.markdown("</div>", unsafe_allow_html=True)

# Extracurricular Activities Section
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("🎉 Extracurricular Activities")
st.write(
    "- Secured 1st position in \"Think Equity Stock Picking Challenge\" with a 20.6% portfolio return in 5 days.\n"
    "- Volunteer at Riviera for International Event Infusion 5.0."
)
st.markdown("</div>", unsafe_allow_html=True)

# Footer Section
st.markdown("---")
st.write("💡 Developed using Streamlit. Feel free to connect with me!")
st.write(" Made with ❤️ by Aditya ✨")

# Download Resume Section
download_resume()

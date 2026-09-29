import streamlit as st
from dotenv import load_dotenv
import os
from google import genai
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #fff176,
        #ffb3e6,
        #80deea,
        #b388ff
    );
}

/* Main container */
.block-container {
    max-width: 850px;
    padding-top: 50px;
}

/* Title */
h1 {
    text-align: center;
    color: #7200ff;
    font-size: 45px;
    font-weight: bold;
    text-shadow: 2px 2px 5px white;
}

/* Description */
p {
    color: #4a148c !important;
    font-size: 18px;
    font-weight: 600;
}

/* Text area label */
label {
    color: #4a148c !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

/* Text area */
.stTextArea textarea {
    background-color: white !important;
    color: #222222 !important;
    border: 3px solid #9c27b0 !important;
    border-radius: 15px !important;
    padding: 15px !important;
    font-size: 17px !important;
}

/* Text area focus */
.stTextArea textarea:focus {
    border: 3px solid #ff1493 !important;
    box-shadow: 0 0 15px #ff69b4 !important;
}

/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(
        90deg,
        #ff1493,
        #8a2be2,
        #007bff
    );
    color: white !important;
    border: none;
    border-radius: 30px;
    padding: 14px;
    font-size: 19px;
    font-weight: bold;
}

/* Button hover */
.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 20px #ff1493;
}

/* Success message */
.stSuccess {
    border-radius: 15px;
    font-weight: bold;
}

/* Warning message */
.stWarning {
    border-radius: 15px;
    font-weight: bold;
}

/* Response heading */
h3 {
    color: #7200ff;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# =========================
# GEMINI AI CHATBOT
# =========================

st.title("🤖 Gemini AI Chatbot")

st.write("✨ Ask Gemini anything!")

prompt = st.text_area(
    "💬 Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words..."
)


# =========================
# GENERATE RESPONSE
# =========================

if st.button("🚀 Generate Response"):

    if prompt:

        with st.spinner("🧠 Gemini is thinking..."):

            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

        st.success("🎉 Response generated!")

        st.markdown("### 💡 Gemini's Response")

        st.write(response.text)

    else:

        st.warning("⚠️ Please enter a prompt.")

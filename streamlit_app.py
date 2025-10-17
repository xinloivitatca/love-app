import streamlit as st
import random
import time

st.set_page_config(page_title="Ứng dụng tỏ tình 💖", page_icon="💘", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #ffe6f0;
        color: #ff4d6d;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
    }
    .big-text {
        font-size: 40px;
        font-weight: bold;
        color: #ff1a75;
        text-shadow: 2px 2px 10px #ff99cc;
    }
    .heart {
        font-size: 24px;
        animation: float 1.5s infinite ease-in-out;
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 50px;
        margin-top: 40px;
    }
    button {
        border-radius: 12px;
        font-size: 22px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-text'>💞 Làm người yêu tớ nhé 💞</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
yes = col1.button("💘 YES 💘")
no = col2.button("💔 NO 💔")

if yes:
    st.balloons()
    st.success("Tớ biết mà 🥰 Tớ yêu cậu nhiều lắm 💖💖💖")
    for _ in range(30):
        hearts = "".join(random.choice(["💖", "💞", "💘", "💕", "💓", "💗", "💝"]) for _ in range(10))
        st.markdown(f"<div class='heart'>{hearts}</div>", unsafe_allow_html=True)
        time.sleep(0.05)

if no:
    st.warning("😢 Nút này không bấm được đâu, thử lại đi 🥺💞")

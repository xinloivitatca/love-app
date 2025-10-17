import streamlit as st

st.set_page_config(page_title="Những Kẻ Xà Lơ", layout="centered")

# ===== CSS hiệu ứng nâng cấp =====
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

        body {
            background: linear-gradient(45deg, #ff4b1f, #ff9068, #ff4b1f);
            background-size: 400% 400%;
            animation: fire 8s ease infinite;
            color: white;
            font-family: 'Poppins', sans-serif;
        }

        @keyframes fire {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        .title {
            text-align: center;
            font-size: 46px;
            font-weight: 800;
            margin-top: 40px;
            margin-bottom: 50px;
            color: #fff;
            text-shadow: 0 0 20px #ff4b1f, 0 0 40px #ff9068;
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { text-shadow: 0 0 10px #ff4b1f, 0 0 20px #ff9068; }
            to { text-shadow: 0 0 25px #ffd700, 0 0 45px #ff4b1f; }
        }

        .fade-in {
            animation: fadeIn 1s ease-in-out;
        }

        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }

        /* Hiệu ứng phóng to ảnh Phong */
        .zoom-img {
            animation: zoomIn 1.2s ease-in-out;
        }

        @keyframes zoomIn {
            0% {opacity: 0; transform: scale(0.6);}
            100% {opacity: 1; transform: scale(1);}
        }

        img {
            border-radius: 20px;
            box-shadow: 0 0 25px rgba(255, 200, 100, 0.7);
            margin-top: 15px;
        }

        .footer {
            text-align: center;
            margin-top: 60px;
            font-size: 20px;
            font-weight: bold;
            color: #fff;
            text-shadow: 0 0 10px #ffd700, 0 0 20px #ff6b6b;
            animation: sparkle 2s infinite alternate;
        }

        @keyframes sparkle {
            from { opacity: 0.8; text-shadow: 0 0 10px #ffd700; }
            to { opacity: 1; text-shadow: 0 0 25px #ffcc33, 0 0 40px #ff6b6b; }
        }
    </style>
""", unsafe_allow_html=True)

# ===== Tiêu đề =====
st.markdown("<div class='title'>🔥 Chủ đề: Câu chuyện về những kẻ xà lơ 🔥</div>", unsafe_allow_html=True)

# ===== Phong =====
with st.expander("💙 Phong: biệt danh kẻ hay khịa và không thích người khác khịa lại"):
    st.markdown("<div class='zoom-img'>", unsafe_allow_html=True)
    st.image("https://files.catbox.moe/nhrwjk.jpg", caption="Phong 💙", use_column_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ===== Nhi =====
with st.expander("💛 Nhi: kẻ bị khịa và cũng hay đi khịa"):
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image("https://files.catbox.moe/lv1xij.jpg", caption="Nhi 💛", use_column_width=True)
    st.image("https://files.catbox.moe/1b6nm5.jpg", caption="Nhi 💛", use_column_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ===== Châu =====
with st.expander("💗 Châu: kẻ nhận tội j cũng nhận j cũng khót"):
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image("https://files.catbox.moe/s4ukx5.jpg", caption="Châu 💗", use_column_width=True)
    st.image("https://files.catbox.moe/6zdd08.jpg", caption="Châu 💗", use_column_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ===== Credit =====
st.markdown("<div class='footer'>💫 Cre by Philong 💫</div>", unsafe_allow_html=True)

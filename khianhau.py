import streamlit as st

st.set_page_config(page_title="Những Kẻ Xà Lơ", layout="centered")

# CSS hiệu ứng nâng cấp
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

        .character {
            font-size: 22px;
            margin-bottom: 25px;
            padding: 18px;
            border-radius: 16px;
            background: rgba(255, 255, 255, 0.1);
            box-shadow: 0 0 15px rgba(255,255,255,0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .character:hover {
            transform: translateY(-6px);
            box-shadow: 0 0 25px rgba(255,255,255,0.4);
        }

        .phong { color: #00e5ff; text-shadow: 0 0 10px #00e5ff; }
        .nhi { color: #ffeb3b; text-shadow: 0 0 10px #ffeb3b; }
        .chau { color: #ffb3ec; text-shadow: 0 0 10px #ffb3ec; }

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

# Nội dung người dùng
st.markdown("<div class='title'>🔥 Chủ đề: Câu chuyện về những kẻ xà lơ 🔥</div>", unsafe_allow_html=True)

st.markdown("""
<div class='character phong'>
    <b>Phong:</b> biệt danh kẻ hay khịa và không thích người khác khịa lại
</div>

<div class='character nhi'>
    <b>Nhi:</b> kẻ bị khịa và cũng hay đi khịa
</div>

<div class='character chau'>
    <b>Châu:</b> kẻ nhận tội j cũng nhận j cũng khót
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='footer'>💫 Cre by Philong 💫</div>", unsafe_allow_html=True)

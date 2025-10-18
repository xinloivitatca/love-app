# -*- coding: utf-8 -*-
import streamlit as st

# --- Cấu hình trang ---
st.set_page_config(page_title="Những Kẻ Xà Lơ", layout="centered")

# --- CSS nền Cyber + hiệu ứng neon (không dùng JS để tránh lỗi “Oh no”) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&display=swap');

[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #0a0a1f, #000000 90%);
    color: white;
    font-family: 'Orbitron', sans-serif;
}

h1 {
    text-align: center;
    font-size: 50px;
    background: linear-gradient(90deg, #00fff7, #ff00c8, #00fff7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 3s infinite linear;
}

@keyframes glow {
    0% { filter: drop-shadow(0 0 10px #00fff7); }
    50% { filter: drop-shadow(0 0 25px #ff00c8); }
    100% { filter: drop-shadow(0 0 10px #00fff7); }
}

h3 {
    text-align: center;
    color: #ccc;
    margin-bottom: 20px;
}

.expander-header {
    font-size: 22px;
    color: #00fff7;
    font-weight: bold;
}

img {
    border-radius: 15px;
    transition: transform 0.6s ease, box-shadow 0.6s ease;
}
img:hover {
    transform: scale(1.05);
    box-shadow: 0 0 30px #00fff7;
}

.desc {
    font-size: 17px;
    line-height: 1.6em;
    margin-bottom: 15px;
    color: #f2f2f2;
}

.footer {
    text-align: center;
    font-size: 20px;
    margin-top: 50px;
    background: linear-gradient(90deg, #ff00c8, #00fff7, #ff00c8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 2s infinite linear;
}
</style>
""", unsafe_allow_html=True)

# --- Tiêu đề ---
st.markdown("<h1>💫 NHỮNG KẺ XÀ LƠ 💫</h1>", unsafe_allow_html=True)
st.markdown("<h3>Bộ sưu tập huyền thoại của nhóm 💀</h3>", unsafe_allow_html=True)

# --- Dữ liệu nhân vật ---
characters = {
    "🔥 Phong (aka SyBau)": {
        "desc": "Kẻ biến thái pỏn nhất nhóm, chuyên gia kể chuyện ài ố sì mà kẻ hay khịa nhưng lại không muốn người khác khịa. Xuất thân từ một nam nhân phàm trần bước vào cõi tu luyện không giữ được bản chất, sa đọa vào lầm than.",
        "imgs": [
            "https://raw.githubusercontent.com/xinloivitatca/love-app/main/images/Screenshot_2025-10-17-22-54-58-63.jpg",
        ],
        "color": "#00fff7"
    },
    "🌸 Nhi (aka Skibidi + Ếch)": {
        "desc": "Học cao hiểu rộng khoảng 1 gang, người có trí tuệ cao siêu đã bước vào giới kết đan kỳ nhưng vẫn vướng víu phàm trần. Đem lòng si mê 1 nam nhân SV, vì quá mê muội để rồi cuối cùng ân hận tự trách bản thân.",
        "imgs": [
            "https://raw.githubusercontent.com/xinloivitatca/love-app/main/images/Messenger_creation_790543723732506.jpg",
            "https://raw.githubusercontent.com/xinloivitatca/love-app/main/images/Messenger_creation_1225944009554639.jpg"
        ],
        "color": "#ff00c8"
    },
    "💫 Châu (aka Kẻ nhận lội)": {
        "desc": "Giống như Phong — hai người này cùng một bậc nhưng tính cách khác nhau. Châu rất thích nhận lỗi và tự tin rằng bất cứ điều gì trên đời nếu không tốt đẹp đều là do bản thân hiện tại.",
        "imgs": [
            "https://raw.githubusercontent.com/xinloivitatca/love-app/main/images/received_1147283250829739.jpg",
            "https://raw.githubusercontent.com/xinloivitatca/love-app/main/images/received_1089987166321962.jpg"
        ],
        "color": "#00ffaa"
    },
    "😎 Tôi (aka PhiLong)": {
        "desc": "Là tôi đây — đzai, không có gì để nói hihi 😎",
        "imgs": [],
        "color": "#ffffff"
    }
}

# --- Hiển thị từng nhân vật ---
for name, info in characters.items():
    with st.expander(f"{name}", expanded=False):
        st.markdown(f"<p class='desc' style='color:{info['color']}'>{info['desc']}</p>", unsafe_allow_html=True)
        for img_url in info["imgs"]:
            st.image(img_url, use_container_width=True)

# --- Footer ---
st.markdown("<div class='footer'>💻 Code by PhiLong 💻</div>", unsafe_allow_html=True)

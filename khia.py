import streamlit as st
from PIL import Image
import os
import time

# --- Cấu hình trang ---
st.set_page_config(page_title="Những Kẻ Xà Lơ", layout="centered")

# --- CSS nền Cyber + hiệu ứng fade-in & neon ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&display=swap');
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #0a0a1f, #000000 90%);
    color: white;
    font-family: 'Orbitron', sans-serif;
    overflow-x: hidden;
}
@keyframes fadeIn {
    0% {opacity: 0; transform: translateY(20px);}
    100% {opacity: 1; transform: translateY(0);}
}
.fade-in {
    animation: fadeIn 1s ease forwards;
}
h1 {
    text-align: center;
    font-size: 45px;
    background: linear-gradient(90deg, #00fff7, #ff00c8, #00fff7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 3s infinite linear;
}
@keyframes glow {
    0% { filter: drop-shadow(0 0 10px #00fff7); }
    50% { filter: drop-shadow(0 0 20px #ff00c8); }
    100% { filter: drop-shadow(0 0 10px #00fff7); }
}
.expander-header {
    font-size: 22px;
    color: #00fff7;
    font-weight: bold;
}
img {
    border-radius: 15px;
    opacity: 0;
    animation: fadeIn 1.5s ease forwards;
    transition: transform 0.6s ease, box-shadow 0.6s ease;
}
img:hover {
    transform: scale(1.05);
    box-shadow: 0 0 30px #00fff7;
}
.desc {
    font-size: 17px;
    line-height: 1.5em;
    margin-bottom: 15px;
}
.footer {
    text-align: center;
    font-size: 20px;
    margin-top: 40px;
    background: linear-gradient(90deg, #ff00c8, #00fff7, #ff00c8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 2s infinite linear;
}
</style>
""", unsafe_allow_html=True)

# --- Tiêu đề ---
st.markdown("<h1>💫 NHỮNG KẺ XÀ LƠ 💫</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#ccc;'>Bộ sưu tập huyền thoại của nhóm 💀</h3>", unsafe_allow_html=True)

# --- Đường dẫn ảnh ---
img_dir = "/mnt/data/xalo_images"

# --- Danh sách nhân vật (theo nội dung bạn soạn) ---
characters = {
    "🔥 Phong (aka SyBau)": {
        "desc": "Kẻ biến thái pỏn nhất nhóm, chuyên gia kể chuyện ài ố sì mà kẻ hay khịa nhưng lại không muốn người khác khịa. Xuất thân từ 1 nam nhân phàm trần bước vào cõi tu luyện không dữ được bản chất, sa đọa vào lầm than.",
        "imgs": ["Screenshot_2025-10-17-22-54-58-63.jpg"],
    },
    "🌸 Nhi (aka Skibidi + Ếch)": {
        "desc": "Học cao hiểu rộng khoảng 1 gang, người có trí tuệ cao siêu đã bước vào giới kết đan kỳ nhưng vẫn vướng víu phàm trần. Đem lòng si mê 1 nam nhân SV, vì quá mê muội để rồi cuối cùng ân hận tự trách bản thân.",
        "imgs": [
            "Messenger_creation_1225944009554639.jpg",
            "Messenger_creation_790543723732506.jpg",
        ],
    },
    "💫 Châu (aka Kẻ nhận lội)": {
        "desc": "Giống như Phong — hai người này cùng một bậc nhưng tính cách khác nhau. Châu rất thích nhận lỗi và tự tin rằng bất cứ điều gì trên đời nếu không tốt đẹp đều là do bản thân hiện tại.",
        "imgs": [
            "received_1089987166321962.jpg",
            "received_1147283250829739.jpg",
        ],
    },
    "😎 Tôi (aka PhiLong)": {
        "desc": "Là tôi đây — đzai, không có gì để nói hihi 😎",
        "imgs": [],
    },
}

# --- Hiển thị từng nhân vật ---
for name, info in characters.items():
    with st.expander(name, expanded=False):
        st.markdown(f"<p class='desc fade-in'>{info['desc']}</p>", unsafe_allow_html=True)
        for img_file in info["imgs"]:
            img_path = os.path.join(img_dir, img_file)
            if os.path.exists(img_path):
                image = Image.open(img_path)
                st.image(image, use_container_width=True)
                time.sleep(0.2)
            else:
                st.warning(f"⚠️ Không tìm thấy ảnh: {img_file}")

# --- Footer ---
st.markdown("<div class='footer'>💻 Code by PhiLong 💻</div>", unsafe_allow_html=True)

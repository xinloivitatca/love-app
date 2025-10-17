import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="Những Kẻ Xà Lơ", layout="centered")

# ===== CSS =====
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
            font-size: 42px;
            font-weight: 800;
            margin-top: 24px;
            margin-bottom: 30px;
            color: #fff;
            text-shadow: 0 0 16px #ff4b1f, 0 0 28px #ff9068;
        }

        .fade-in { animation: fadeIn 0.9s ease-in-out; }
        @keyframes fadeIn { from {opacity:0} to {opacity:1} }

        .zoom-img { animation: zoomIn 1s ease-in-out; }
        @keyframes zoomIn { 0% {opacity:0; transform:scale(0.7)} 100% {opacity:1; transform:scale(1)} }

        img { border-radius: 12px; box-shadow: 0 0 20px rgba(0,0,0,0.4); margin-top:10px; }

        .footer {
            text-align: center;
            margin-top: 40px;
            font-size: 16px;
            font-weight: 600;
        }
        .hint {
            background: rgba(0,0,0,0.2);
            padding: 10px;
            border-radius: 8px;
            margin-top: 8px;
            color: #fff;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🔥 Chủ đề: Câu chuyện về những kẻ xà lơ 🔥</div>", unsafe_allow_html=True)

st.markdown("""
**Hướng dẫn nhanh:**  
- Bạn có thể **upload ảnh từ máy** (khuyến nghị) hoặc **dán link ảnh trực tiếp** (link phải kết thúc bằng .jpg/.png/.jpeg/.gif).
- Nếu ảnh không hiện, thử upload thay vì dùng link.
""")

# ---------- helper load image ----------
def load_image_from_url(url: str):
    try:
        resp = requests.get(url, timeout=8)
        resp.raise_for_status()
        return Image.open(BytesIO(resp.content))
    except Exception as e:
        return None

def display_image(obj, caption="", styles=""):
    """
    obj: can be PIL.Image or file-like or URL string
    """
    if isinstance(obj, Image.Image):
        st.image(obj, caption=caption, use_container_width=True)
        return True
    if isinstance(obj, str):
        # treat as URL
        img = load_image_from_url(obj)
        if img:
            st.image(img, caption=caption, use_container_width=True)
            return True
    # if file-like (UploadedFile)
    try:
        st.image(obj, caption=caption, use_container_width=True)
        return True
    except Exception:
        return False

# ---------- Phong section (zoom effect) ----------
with st.expander("💙 Phong: biệt danh kẻ hay khịa và không thích người khác khịa lại", expanded=False):
    st.write("")  # spacing
    st.markdown("<div class='hint'>Tải lên ảnh Phong (tốt nhất) hoặc dán link trực tiếp.</div>", unsafe_allow_html=True)
    phong_file = st.file_uploader("Upload ảnh Phong (jpg/png)", type=["png","jpg","jpeg","gif"], key="up_phong")
    phong_url = st.text_input("Hoặc dán link ảnh Phong (direct link)", key="url_phong", placeholder="https://...")
    displayed = False
    if phong_file is not None:
        displayed = display_image(phong_file, caption="Phong 💙")
    elif phong_url:
        displayed = display_image(phong_url, caption="Phong 💙")
    if displayed:
        # thêm class zoom (unsafe html wrapper)
        st.markdown("<div class='zoom-img'></div>", unsafe_allow_html=True)
    else:
        st.warning("Chưa có ảnh hợp lệ cho Phong. Hãy upload file hoặc dán link direct image (kết thúc bằng .jpg/.png).")

# ---------- Nhi section ----------
with st.expander("💛 Nhi: kẻ bị khịa và cũng hay đi khịa", expanded=False):
    st.markdown("<div class='hint'>Tải lên 1 hoặc nhiều ảnh cho Nhi (bạn có thể upload 2 ảnh). Nếu dùng link, phải là direct image link.</div>", unsafe_allow_html=True)
    nhi_files = st.file_uploader("Upload ảnh Nhi (có thể chọn nhiều)", type=["png","jpg","jpeg","gif"], accept_multiple_files=True, key="up_nhi")
    nhi_url = st.text_input("Hoặc dán link ảnh Nhi (cách 1 link)", key="url_nhi", placeholder="https://...")
    shown = False
    if nhi_files:
        for f in nhi_files:
            display_image(f, caption="Nhi 💛")
            shown = True
    elif nhi_url:
        if display_image(nhi_url, caption="Nhi 💛"):
            shown = True
    if not shown:
        st.info("Chưa có ảnh Nhi. Upload ảnh hoặc dán link.")

# ---------- Châu section ----------
with st.expander("💗 Châu: kẻ nhận tội j cũng nhận j cũng khót", expanded=False):
    st.markdown("<div class='hint'>Upload ảnh cho Châu hoặc dán link direct image.</div>", unsafe_allow_html=True)
    chau_files = st.file_uploader("Upload ảnh Châu (có thể chọn nhiều)", type=["png","jpg","jpeg","gif"], accept_multiple_files=True, key="up_chau")
    chau_url = st.text_input("Hoặc dán link ảnh Châu (cách 1 link)", key="url_chau", placeholder="https://...")
    shown_c = False
    if chau_files:
        for f in chau_files:
            display_image(f, caption="Châu 💗")
            shown_c = True
    elif chau_url:
        if display_image(chau_url, caption="Châu 💗"):
            shown_c = True
    if not shown_c:
        st.info("Chưa có ảnh Châu. Upload ảnh hoặc dán link.")

st.markdown("<div class='footer'>💫 Cre by Philong 💫</div>", unsafe_allow_html=True)

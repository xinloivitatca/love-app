# khia.py
import streamlit as st

st.set_page_config(page_title="Những Kẻ Xà Lơ — Cyber Edition", layout="wide")

# -------------------------
# Raw image URLs (your uploaded files)
# -------------------------
IMAGES = {
    "Phong": [
        "https://raw.githubusercontent.com/xinloivitatca/love-app/refs/heads/main/images/Screenshot_2025-10-17-22-54-58-63.jpg"
    ],
    "Nhi": [
        "https://raw.githubusercontent.com/xinloivitatca/love-app/refs/heads/main/images/Messenger_creation_790543723732506.jpg",
        "https://raw.githubusercontent.com/xinloivitatca/love-app/refs/heads/main/images/Messenger_creation_1225944009554639.jpg"
    ],
    "Châu": [
        "https://raw.githubusercontent.com/xinloivitatca/love-app/refs/heads/main/images/received_1147283250829739.jpg",
        "https://raw.githubusercontent.com/xinloivitatca/love-app/refs/heads/main/images/received_1089987166321962.jpg"
    ],
}

# -------------------------
# Content (keeps your original text)
# -------------------------
CHAR_CONTENT = {
    "🔥 Phong (aka SyBau)": "Kẻ biến thái pỏn nhất nhóm, chuyên gia kể chuyện ài ố sì mà kẻ hay khịa nhưng lại không muốn người khác khịa. Xuất thân từ 1 nam nhân phàm trần bước vào cõi tu luyện không dữ được bản chất, sa đọa vào lầm than.",
    "🌸 Nhi (aka Skibidi + Ếch)": "Học cao hiểu rộng khoảng 1 gang, người có trí tuệ cao siêu đã bước vào giới kết đan kỳ nhưng vẫn vướng víu phàm trần. Đem lòng si mê 1 nam nhân SV, vì quá mê muội để rồi cuối cùng ân hận tự trách bản thân.",
    "💫 Châu (aka Kẻ nhận lội)": "Giống như Phong — hai người này cùng một bậc nhưng tính cách khác nhau. Châu rất thích nhận lỗi và tự tin rằng bất cứ điều gì trên đời nếu không tốt đẹp đều là do bản thân hiện tại.",
    "😎 Tôi (aka PhiLong)": "Là tôi đây — đzai, không có gì để nói hihi 😎",
}

# -------------------------
# Optional background music URL
# (Leave as "" to disable by default or replace with your own raw link / mp3 url)
# -------------------------
BACKGROUND_MUSIC = ""  # e.g. "https://raw.githubusercontent.com/....../cyber-chill.mp3"

# -------------------------
# CSS (cyber background, modal, animations)
# -------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    :root{
        --neon1: #00fff7;
        --neon2: #ff00c8;
        --bg-dark: #050514;
        --panel: rgba(255,255,255,0.03);
    }

    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at 20% 10%, rgba(20,16,40,0.6), rgba(2,2,8,1) 60%), linear-gradient(180deg, rgba(0,0,0,0.2), rgba(0,0,0,1));
        color: #e6f4ff;
        font-family: 'Orbitron', sans-serif;
    }

    /* Heading */
    .cyber-title {
        font-size: 44px;
        text-align: center;
        margin-bottom: 0;
        letter-spacing: 1px;
        background: linear-gradient(90deg, var(--neon1), var(--neon2), var(--neon1));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: neonGlow 3s ease-in-out infinite;
    }
    @keyframes neonGlow {
        0% { filter: drop-shadow(0 0 6px rgba(0,255,247,0.6)); }
        50% { filter: drop-shadow(0 0 18px rgba(255,0,200,0.8)); }
        100% { filter: drop-shadow(0 0 6px rgba(0,255,247,0.6)); }
    }

    .subtitle { text-align:center; color: #bfc9d9; margin-top: 2px; margin-bottom: 24px; }

    /* Layout cards */
    .card {
        background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 14px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.6);
        border: 1px solid rgba(255,255,255,0.03);
    }
    .card .name {
        font-weight:700;
        font-size:20px;
        color: var(--neon1);
        cursor: pointer;
        display:flex;
        align-items:center;
        gap:10px;
    }
    .desc { color: #d7e9ff; margin-top:8px; font-size:15px; line-height:1.45; }

    /* image styling */
    .gallery-img {
        width:100%;
        border-radius:12px;
        transform-origin:center center;
        transition: transform 0.6s cubic-bezier(.2,.9,.2,1), box-shadow 0.4s ease, opacity 0.6s ease;
        box-shadow: 0 8px 30px rgba(0,0,0,0.6);
        opacity: 0;
    }
    .gallery-img.visible {
        transform: scale(1) rotate(0deg);
        opacity: 1;
    }
    .gallery-img:hover {
        transform: scale(1.03);
        box-shadow: 0 12px 40px rgba(0,255,247,0.12);
    }

    /* Modal using :target trick */
    .modal {
        display:none;
        position: fixed;
        z-index: 9999;
        left:0; top:0;
        width:100%; height:100%;
        background: radial-gradient(circle at center, rgba(2,6,23,0.6), rgba(0,0,0,0.9));
        align-items:center;
        justify-content:center;
        padding: 30px;
    }
    .modal:target { display:flex; animation: modalIn 0.35s ease; }
    @keyframes modalIn {
        from { opacity: 0; transform: translateY(12px) scale(0.98); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }
    .modal .panel {
        width: min(1100px, 95%);
        background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.015));
        padding: 18px;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.04);
    }
    .modal .close {
        display:block;
        text-align:right;
        color:#cfefff;
        text-decoration:none;
        font-size:18px;
        margin-bottom:8px;
    }

    /* footer rainbow */
    .rainbow {
        text-align:center;
        font-weight:700;
        font-size:18px;
        margin-top:30px;
        background: linear-gradient(90deg, #ff004b, #ff8a00, #ffd300, #2affc6, #2b8bff);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        animation: rainbow 4s linear infinite;
    }
    @keyframes rainbow {
        0%{filter:drop-shadow(0 0 6px rgba(255,0,75,0.6));}
        50%{filter:drop-shadow(0 0 10px rgba(43,139,255,0.6));}
        100%{filter:drop-shadow(0 0 6px rgba(255,0,75,0.6));}
    }

    /* small helpers */
    .small-muted { color:#9fb3cc; font-size:13px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Top controls: music toggle (if BACKGROUND_MUSIC provided)
# -------------------------
left, right = st.columns([3, 1])
with left:
    st.markdown('<div class="cyber-title">💫 NHỮNG KẺ XÀ LƠ 💫</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Bộ sưu tập huyền thoại — bấm vào người để mở gallery</div>', unsafe_allow_html=True)

with right:
    if BACKGROUND_MUSIC:
        # show audio player (user can play/pause)
        st.markdown("<div style='text-align:right'>🎧 Nhạc nền:</div>", unsafe_allow_html=True)
        st.audio(BACKGROUND_MUSIC, format='audio/mp3')
    else:
        st.markdown("<div style='text-align:right' class='small-muted'>Nhạc nền: (chưa chọn)</div>", unsafe_allow_html=True)

st.write("")  # spacing

# -------------------------
# Layout: left column shows cards
# -------------------------
col1, col2 = st.columns([1, 2])

with col1:
    # show each character card and a link to open modal via anchor (target)
    for idx, (title, desc) in enumerate(CHAR_CONTENT.items()):
        # Skip if you want different ordering - but keep content
        with st.container():
            st.markdown(f"<div class='card'>", unsafe_allow_html=True)
            # create a target anchor id for modal (use safe id)
            anchor_id = f"modal-{idx}"
            # Show name as clickable link that anchors to modal
            st.markdown(f"<a href='#{anchor_id}' class='name' style='text-decoration:none;'><div class='name'>{title}</div></a>", unsafe_allow_html=True)
            st.markdown(f"<div class='desc'>{desc}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # show quick gallery preview (small thumbnails)
    st.markdown("<div class='card'><div style='font-weight:700;color:var(--neon2);'>Gallery Preview</div>", unsafe_allow_html=True)
    # show small montage of thumbnails (first image of each person)
    for person, imgs in IMAGES.items():
        if imgs:
            url = imgs[0]
            st.markdown(f"<div style='margin-top:10px'><strong style='color:#9feef8'>{person}</strong></div>", unsafe_allow_html=True)
            st.markdown(f"<img src='{url}' style='width:100%;border-radius:10px;box-shadow:0 8px 30px rgba(0,0,0,0.6);margin-top:6px'/>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Create a modal block for each character using :target anchors
# -------------------------
modal_html_parts = []
for idx, (name, imgs) in enumerate(IMAGES.items()):
    anchor = f"modal-{idx}"
    # Prepare gallery HTML inside panel
    imgs_html = ""
    for uidx, u in enumerate(imgs):
        # each image will have class gallery-img; we add '?raw=true' not needed because using raw path already
        imgs_html += f"<div style='margin-bottom:12px'><img class='gallery-img' src='{u}' alt='' /></div>"
    if not imgs:
        imgs_html = "<div class='small-muted'>Chưa có ảnh.</div>"

    panel_html = f"""
    <div id="{anchor}" class="modal">
      <div class="panel">
        <a class="close" href="#">✕ Close</a>
        <div style="display:flex;gap:18px;align-items:flex-start;flex-wrap:wrap;">
          <div style="flex:1 1 40%;">
            <h2 style="margin:0;padding:0">{list(CHAR_CONTENT.keys())[idx]}</h2>
            <p class="small-muted" style="margin-top:10px;">{list(CHAR_CONTENT.values())[idx]}</p>
            <div style="margin-top:12px;">
              <a href="#" style="text-decoration:none;padding:8px 12px;border-radius:8px;background:linear-gradient(90deg,var(--neon1),var(--neon2));color:#001; font-weight:700;">Close</a>
            </div>
          </div>
          <div style="flex:1 1 55%;">{imgs_html}</div>
        </div>
      </div>
    </div>
    """
    modal_html_parts.append(panel_html)

# render modals HTML
full_modals_html = "\n".join(modal_html_parts)
st.markdown(full_modals_html, unsafe_allow_html=True)

# -------------------------
# Small script to add 'visible' class to images after load (makes fade-in effect)
# We use a little JS inserted via components (safe as no external requests)
# -------------------------
js = """
<script>
(() => {
  // find images in modals and add 'visible' class after slight delay
  function revealImgs() {
    const imgs = document.querySelectorAll('.gallery-img');
    imgs.forEach((img, i) => {
      // ensure we wait until image is loaded
      if (img.complete) {
        setTimeout(() => img.classList.add('visible'), 50 + i*120);
      } else {
        img.addEventListener('load', () => {
          setTimeout(() => img.classList.add('visible'), 50 + i*120);
        });
      }
    });
  }
  // run on initial load
  document.addEventListener('DOMContentLoaded', revealImgs);
  // also run when hash changes (modal opened)
  window.addEventListener('hashchange', revealImgs);
})();
</script>
"""
st.components.v1.html(js, height=0)

# -------------------------
# Footer: Code by PhiLong
# -------------------------
st.markdown("<div class='rainbow'>💻 Code by PhiLong 💻</div>", unsafe_allow_html=True)

# -------------------------
# NOTE to user (in-app guidance)
# -------------------------
st.markdown(
    """
    <div style="margin-top:14px;color:#9fb3cc;font-size:13px">
    Hướng dẫn: bấm vào tên (ở cột trái) để mở gallery từng người — ảnh sẽ hiển thị trong modal mượt (nhấn ✕ hoặc 'Close' để đóng).<br>
    Nếu muốn thêm nhạc nền tự động, upload file mp3 vào repo và gán đường dẫn vào biến <code>BACKGROUND_MUSIC</code> ở đầu file.
    </div>
    """,
    unsafe_allow_html=True,
        )

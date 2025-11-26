# -*- coding: utf-8 -*-
"""
Streamlit app: Web-key emulator (symbolic)
Features:
 - Show/generate keys like plongdzai_XXXXXXXXXXXX
 - Accept key via URL query param ?key=...
 - Validate against an in-memory list (you can extend to DB/file)
 - Admin sidebar to change site-name and key-prefix in-session
 - Buttons/links to Zalo / Telegram
 - Exportable URL to share (user can copy)
"""
import streamlit as st
import secrets
import string
import urllib.parse

st.set_page_config(page_title="plongdzai Key Hub", layout="centered")

# ---------- Helper functions ----------
def generate_key(prefix="plongdzai", length=16):
    """Generate a random URL-safe key suffix (letters+digits)."""
    alphabet = string.ascii_letters + string.digits
    suffix = ''.join(secrets.choice(alphabet) for _ in range(length))
    return f"{prefix}_{suffix}"

def make_share_url(base_url, key_value):
    """Construct a shareable URL with ?key=..."""
    q = {"key": key_value}
    return f"{base_url}?{urllib.parse.urlencode(q)}"

def is_valid_key(k, valid_list):
    return k in valid_list

# ---------- Session state initialization ----------
if "site_name" not in st.session_state:
    st.session_state.site_name = "plongdzai"

if "key_prefix" not in st.session_state:
    st.session_state.key_prefix = "plongdzai"

if "valid_keys" not in st.session_state:
    # default valid sample key
    st.session_state.valid_keys = [
        "plongdzai_7UEaHodEefNk4Vs"  # your original example
    ]

# ---------- UI: header ----------
st.markdown(
    "<div style='text-align:center; padding:6px 0 0 0;'>"
    f"<h1 style='margin:0 0 4px; font-family:Orbitron,monospace;'>🔑 {st.session_state.site_name} Key Hub</h1>"
    "<div style='color:#aebfd6;'>Mô phỏng web-key — tạo/kiểm tra/chia sẻ</div>"
    "</div>",
    unsafe_allow_html=True,
)

st.write("---")

# ---------- Read key from URL (query param) ----------
qp = st.experimental_get_query_params()
incoming_key = qp.get("key", [""])[0] if qp else ""

col1, col2 = st.columns([2,1])

with col1:
    st.subheader("🔐 Key actions")
    # show current key field (prefill with incoming_key or blank)
    current_key = st.text_input("Key (nhập hoặc dán vào):", value=incoming_key, key="key_input")

    btn_col1, btn_col2, btn_col3 = st.columns([1,1,1])
    with btn_col1:
        if st.button("Generate mới"):
            new_k = generate_key(st.session_state.key_prefix, length=16)
            # show new key in text input by setting session state
            st.session_state.key_input = new_k
            current_key = new_k
            st.success("Đã tạo key mới")
    with btn_col2:
        if st.button("Kiểm tra key"):
            if current_key.strip() == "":
                st.warning("Vui lòng nhập key để kiểm tra.")
            else:
                if is_valid_key(current_key.strip(), st.session_state.valid_keys):
                    st.success("✅ Key hợp lệ (VALID)")
                else:
                    st.error("❌ Key không hợp lệ (INVALID)")

    with btn_col3:
        if st.button("Thêm key vào danh sách hợp lệ"):
            if current_key.strip() == "":
                st.warning("Nhập key trước khi thêm.")
            else:
                if current_key.strip() in st.session_state.valid_keys:
                    st.info("Key đã tồn tại trong danh sách hợp lệ.")
                else:
                    st.session_state.valid_keys.append(current_key.strip())
                    st.success("Đã thêm key vào danh sách hợp lệ.")

    st.markdown("**URL chia sẻ (copy & gửi):**")
    # base url auto detect
    try:
        base = st.experimental_get_url()  # returns full current URL
    except Exception:
        # fallback: streamlit cloud will provide actual URL; local dev use http://localhost:8501
        base = "https://<your-streamlit-app>.streamlit.app"
    share_url = make_share_url(base.split("?")[0], current_key) if current_key else ""
    if share_url:
        st.code(share_url)
        # provide quick open link
        st.markdown(f"[🔗 Mở link này]({share_url})")
    else:
        st.info("Tạo/nhập key rồi app sẽ hiển thị URL chia sẻ ở đây.")

with col2:
    st.subheader("📇 Thông tin nhanh")
    st.markdown(f"- **Site name:** `{st.session_state.site_name}`")
    st.markdown(f"- **Key prefix:** `{st.session_state.key_prefix}`")
    st.markdown(f"- **Số key hợp lệ hiện tại:** **{len(st.session_state.valid_keys)}**")
    if st.button("Xem danh sách key hợp lệ"):
        st.write(st.session_state.valid_keys)

st.write("---")

# ---------- Details / result panel ----------
st.subheader("Kết quả kiểm tra & Demo")
if current_key:
    if is_valid_key(current_key.strip(), st.session_state.valid_keys):
        st.success(f"Key `{current_key}` là **HỢP LỆ** ✅")
    else:
        st.error(f"Key `{current_key}` **KHÔNG HỢP LỆ** ❌")
else:
    st.info("Hãy tạo hoặc dán key để kiểm tra/chia sẻ.")

# ---------- Contact buttons (Zalo & Telegram) ----------
st.write("")
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### Liên hệ nhanh")
contact_col1, contact_col2, contact_col3 = st.columns([1,1,1])
with contact_col1:
    # Zalo web link (thay bằng link của bạn)
    zalo_link = "https://zalo.me/0123456789"  # <--- thay số bằng số của bạn
    st.markdown(f"<a href='{zalo_link}' target='_blank'><div style='padding:10px;border-radius:8px;background:linear-gradient(90deg,#ff7ab6,#6ef6ff);text-align:center;color:#001;font-weight:700;'>💬 Zalo</div></a>", unsafe_allow_html=True)

with contact_col2:
    telegram_link = "https://t.me/yourusername"  # <--- thay bằng username telegram của bạn
    st.markdown(f"<a href='{telegram_link}' target='_blank'><div style='padding:10px;border-radius:8px;background:linear-gradient(90deg,#ffd36e,#ff7a7a);text-align:center;color:#001;font-weight:700;'>📲 Telegram</div></a>", unsafe_allow_html=True)

with contact_col3:
    st.markdown(f"<a href='mailto:youremail@example.com' target='_blank'><div style='padding:10px;border-radius:8px;background:linear-gradient(90deg,#9be6a8,#6ec6ff);text-align:center;color:#001;font-weight:700;'>✉️ Email</div></a>", unsafe_allow_html=True)

st.write("---")

# ---------- Admin settings (sidebar) ----------
st.sidebar.header("⚙️ Admin (session)")
site_name = st.sidebar.text_input("Site name", value=st.session_state.site_name)
key_prefix = st.sidebar.text_input("Key prefix", value=st.session_state.key_prefix)
if st.sidebar.button("Apply"):
    st.session_state.site_name = site_name.strip() or st.session_state.site_name
    st.session_state.key_prefix = key_prefix.strip() or st.session_state.key_prefix
    st.sidebar.success("Applied (session only)")

st.sidebar.markdown("---")
st.sidebar.markdown("**Ghi chú:** danh sách key hợp lệ và cài đặt sẽ được lưu trong session (tạm thời). Nếu muốn lưu lâu dài, bạn có thể: ")
st.sidebar.markdown("- Lưu file CSV/JSON trên repo (không an toàn nếu public).")
st.sidebar.markdown("- Lưu vào Google Sheet / database / S3 / Supabase (mình có thể hướng dẫn).")

# ---------- Footer ----------
st.write("")
st.markdown("<div style='text-align:center;color:#9fb3cc;margin-top:16px;'>Plongdzai Key Hub • demo by PhiLong</div>", unsafe_allow_html=True)

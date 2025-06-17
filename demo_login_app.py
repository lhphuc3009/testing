
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title="Demo Login", page_icon="🔐")

with open("auth_config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    cookie_settings=None,
    hashed_passwords=True
)

authenticator.login()

if st.session_state.get("authentication_status"):
    st.success(f"Chào mừng {st.session_state['name']}!")
    authenticator.logout("Đăng xuất", "sidebar")
elif st.session_state.get("authentication_status") is False:
    st.error("Sai tên đăng nhập hoặc mật khẩu")
elif st.session_state.get("authentication_status") is None:
    st.warning("Vui lòng nhập thông tin đăng nhập")

import streamlit as st

users = {
    "admin": "admin123",
    "aditya": "aws@123",
    "student": "cloud2025"
}

def login():
    st.sidebar.markdown("### 🔐 Login to Continue")

    # If already logged in, show logout option
    if st.session_state.get("logged_in", False):
        st.sidebar.success(f"✅ Logged in as: **{st.session_state['username']}**")
        if st.sidebar.button("🚪 Logout"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            #st.experimental_rerun()
        return True, st.session_state["username"]

    # If not logged in, show login form
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_btn = st.sidebar.button("Login")

    if login_btn:
        if username in users and users[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success(f"✅ Logged in as **{username}**")
            #st.experimental_rerun()
        else:
            st.error("❌ Invalid username or password")

    return st.session_state.get("logged_in", False), st.session_state.get("username", "")

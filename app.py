import streamlit as st
from dotenv import load_dotenv
import os
import sys

# Add subfolders to path
sys.path.append(os.path.join(os.path.dirname(__file__), "EC2"))
sys.path.append(os.path.join(os.path.dirname(__file__), "RDS"))
sys.path.append(os.path.join(os.path.dirname(__file__), "S3"))

# Load environment variables
load_dotenv()

# Import custom modules
from EC2.create_ec2_instance_file import create_ec2_instance
from EC2.delete_ec2_instance_file import delete_ec2_instance
from RDS.create_rds_instance_file import create_rds_instance
from RDS.delete_rds_instance_file import delete_rds_instance
from RDS.create_snapshot_file import create_snapshot
from RDS.modify_rds_instance_file import modify_rds_instance
from RDS.restore_from_snapshot_file import restore_from_snapshot
from S3.upload_to_s3_file import upload_to_s3
from auth import login




st.markdown("""
    <style>
    /* === Global Styles === */
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f3f6f4;
        scroll-behavior: smooth;
    }

    body.dark-mode {
        background-color: #121212;
        color: #f5f5f5;
    }

    .main-title {
        text-align: center;
        color: white;
        background: linear-gradient(to right, #4CAF90, #2E7D32);
        padding: 20px;
        border-radius: 10px;
        font-size: 40px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.25);
        animation: fadeIn 1.5s ease-in-out;
    }

    .section-header {
        font-size: 28px;
        margin-top: 30px;
        color: #2E7D32;
        font-weight: 600;
        border-bottom: 2px solid #C8E6C9;
        padding-bottom: 5px;
        margin-bottom: 20px;
    }

    /* === Responsive Layout === */
    @media screen and (max-width: 768px) {
        .main-title {
            font-size: 28px;
        }
        .section-header {
            font-size: 20px;
        }
        .stButton > button {
            font-size: 14px;
            padding: 6px 12px !important;
        }
    }

    /* === Light/Dark Theme Toggle === */
    .theme-toggle {
        position: fixed;
        top: 10px;
        right: 20px;
        z-index: 1000;
    }
    .theme-toggle button {
        background-color: #fff;
        border: none;
        padding: 8px 14px;
        border-radius: 20px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        font-weight: bold;
        color: #333;
        cursor: pointer;
    }

    /* === Spinner Animation === */
    .spinner {
        border: 4px solid #f3f3f3;
        border-top: 4px solid #4CAF50;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: spin 2s linear infinite;
        margin: 20px auto;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    /* === Navbar Animations === */
    .navbar {
        display: flex;
        justify-content: space-around;
        background: linear-gradient(to right, #388E3C, #66BB6A);
        padding: 12px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        position: sticky;
        top: 0;
        z-index: 999;
        animation: slideDown 0.8s ease-in-out;
    }

    .navbar a {
        color: white;
        font-weight: bold;
        text-decoration: none;
        transition: color 0.3s ease;
        padding: 8px 16px;
        border-radius: 5px;
    }

    .navbar a:hover {
        background-color: rgba(255,255,255,0.2);
        color: #f1f1f1;
    }

    @keyframes slideDown {
        0% {
            transform: translateY(-100%);
            opacity: 0;
        }
        100% {
            transform: translateY(0);
            opacity: 1;
        }
    }

    footer {
        visibility: hidden;
    }

    hr {
        border: none;
        height: 2px;
        background-color: #C8E6C9;
        margin: 20px 0;
    }
            
        /* === Custom Cards === */
    .info-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
        transition: transform 0.2s;
    }

    .info-card:hover {
        transform: translateY(-4px);
    }

    .info-title {
        color: #2E7D32;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .info-description {
        color: #555;
        font-size: 16px;
        line-height: 1.5;
    }

    /* === Notification Boxes === */
    .notice {
        border-left: 6px solid #4CAF50;
        background-color: #E8F5E9;
        color: #2E7D32;
        padding: 12px 20px;
        border-radius: 10px;
        margin: 15px 0;
    }

    .warning {
        border-left: 6px solid #FFB300;
        background-color: #FFFDE7;
        color: #F57F17;
        padding: 12px 20px;
        border-radius: 10px;
        margin: 15px 0;
    }

    .danger {
        border-left: 6px solid #E53935;
        background-color: #FFEBEE;
        color: #C62828;
        padding: 12px 20px;
        border-radius: 10px;
        margin: 15px 0;
    }

    /* === Dashboard Grid === */
    .dashboard-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin-top: 20px;
    }

    .dashboard-item {
        background-color: #F1F8E9;
        border: 1px solid #C5E1A5;
        padding: 20px;
        border-radius: 10px;
        transition: box-shadow 0.3s;
    }

    .dashboard-item:hover {
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
    }

    /* === Table Styling === */
    .stTable td, .stTable th {
        border: 1px solid #ddd;
        padding: 8px;
    }

    .stTable tr:nth-child(even){background-color: #f9f9f9;}
    .stTable tr:hover {background-color: #f1f1f1;}
    .stTable th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
        background-color: #4CAF50;
        color: white;
    }

    /* === Modal Popup === */
    .modal {
        display: none;
        position: fixed;
        z-index: 1001;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0,0,0,0.5);
    }

    .modal-content {
        background-color: #fefefe;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 60%;
        border-radius: 10px;
    }
    /* === Navigation Menu Animation === */
    .nav-bar {
        display: flex;
        justify-content: space-around;
        background-color: #4CAF50;
        padding: 14px 0;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        animation: slideDown 0.5s ease-in-out;
    }

    .nav-bar a {
        color: white;
        font-weight: bold;
        text-decoration: none;
        padding: 8px 16px;
        border-radius: 4px;
        transition: background 0.3s;
    }

    .nav-bar a:hover {
        background-color: #388E3C;
    }

    @keyframes slideDown {
        from { transform: translateY(-100%); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    /* === Spinner Loader === */
    .spinner {
        border: 4px solid #f3f3f3;
        border-top: 4px solid #4CAF50;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: spin 1s linear infinite;
        margin: auto;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    /* === Light/Dark Mode Toggle === */
    .toggle-wrapper {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        margin: 10px 0;
    }

    .toggle-button {
        appearance: none;
        width: 50px;
        height: 26px;
        background: #ccc;
        border-radius: 50px;
        position: relative;
        cursor: pointer;
        outline: none;
        transition: background 0.3s ease;
    }

    .toggle-button:checked {
        background: #4CAF50;
    }

    .toggle-button::before {
        content: "";
        position: absolute;
        top: 3px;
        left: 3px;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: white;
        transition: transform 0.3s ease;
    }

    .toggle-button:checked::before {
        transform: translateX(24px);
    }

    .dark-theme {
        background-color: #1e1e1e;
        color: #eeeeee;
    }

    .dark-theme .info-card,
    .dark-theme .dashboard-item,
    .dark-theme .modal-content {
        background-color: #2c2c2c;
        color: #e0e0e0;
    }

    .dark-theme .nav-bar {
        background-color: #2e7d32;
    }

    .dark-theme .nav-bar a:hover {
        background-color: #1b5e20;
    }

    .dark-theme .section-header {
        color: #a5d6a7;
        border-bottom: 2px solid #81c784;
    }

    /* === Badges === */
    .badge {
        display: inline-block;
        padding: 5px 10px;
        font-size: 12px;
        font-weight: bold;
        color: white;
        background-color: #4CAF50;
        border-radius: 10px;
        margin-left: 8px;
    }
    /* === Notification Toasts === */
    .toast {
        position: fixed;
        top: 20px;
        right: 20px;
        background: #4CAF50;
        color: white;
        padding: 15px 25px;
        border-radius: 8px;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.2);
        z-index: 9999;
        animation: fadeInUp 0.5s ease-out forwards;
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* === Custom Cards With Icons === */
    .feature-box {
        display: flex;
        align-items: center;
        background: #ffffff;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin: 15px 0;
    }

    .feature-box .icon {
        font-size: 32px;
        color: #4CAF50;
        margin-right: 15px;
    }

    .feature-box .content h4 {
        margin: 0;
        font-size: 20px;
        color: #2E7D32;
    }

    .feature-box .content p {
        margin: 5px 0 0 0;
        color: #555;
        font-size: 14px;
    }

    /* === Accordion/Expand === */
    .accordion {
        background-color: #f1f1f1;
        color: #444;
        cursor: pointer;
        padding: 18px;
        width: 100%;
        border: none;
        text-align: left;
        outline: none;
        font-size: 15px;
        transition: 0.4s;
    }

    .accordion:hover {
        background-color: #e0f2f1;
    }

    .panel {
        padding: 0 18px;
        display: none;
        background-color: white;
        overflow: hidden;
    }

    /* === Progress Bars === */
    .progress-container {
        width: 100%;
        background-color: #e0e0e0;
        border-radius: 13px;
        padding: 3px;
    }

    .progress-bar {
        height: 20px;
        border-radius: 10px;
        background-color: #4CAF50;
        width: 0%;
        transition: width 0.6s ease;
    }

    /* === Tags / Chips === */
    .chip {
        display: inline-block;
        padding: 0 15px;
        height: 32px;
        font-size: 14px;
        line-height: 32px;
        border-radius: 16px;
        background-color: #E0F2F1;
        color: #00796B;
        margin: 5px;
    }

    /* === Floating Action Button === */
    .fab {
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 56px;
        height: 56px;
        background-color: #4CAF50;
        border-radius: 50%;
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.2);
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 24px;
        cursor: pointer;
        z-index: 999;
    }
            /* === Section Dividers === */
    .divider {
        height: 2px;
        width: 100%;
        background: linear-gradient(to right, #4CAF50, #81C784);
        margin: 30px 0;
        border-radius: 2px;
    }

    /* === Info Cards === */
    .info-card {
        padding: 15px 25px;
        background-color: #ffffff;
        border-left: 5px solid #4CAF50;
        border-radius: 8px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }

    .info-card h4 {
        margin-top: 0;
        color: #2E7D32;
    }

    .info-card p {
        margin: 5px 0;
        color: #666;
    }

    /* === Tooltips === */
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: pointer;
    }

    .tooltip .tooltiptext {
        visibility: hidden;
        width: 140px;
        background-color: #4CAF50;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px 0;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -70px;
        opacity: 0;
        transition: opacity 0.3s;
    }

    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }

    /* === Timeline Component === */
    .timeline {
        position: relative;
        max-width: 800px;
        margin: 20px auto;
    }

    .timeline::after {
        content: '';
        position: absolute;
        width: 6px;
        background-color: #4CAF50;
        top: 0;
        bottom: 0;
        left: 50%;
        margin-left: -3px;
    }

    .timeline-item {
        padding: 10px 40px;
        position: relative;
        background-color: inherit;
        width: 50%;
    }

    .timeline-item::after {
        content: ' ';
        position: absolute;
        width: 25px;
        height: 25px;
        right: -17px;
        background-color: white;
        border: 4px solid #4CAF50;
        top: 15px;
        border-radius: 50%;
        z-index: 1;
    }

    .left {
        left: 0;
    }

    .right {
        left: 50%;
    }

    .timeline-content {
        padding: 20px;
        background-color: #e8f5e9;
        position: relative;
        border-radius: 6px;
    }

    /* === Status Labels === */
    .label-success {
        background-color: #4CAF50;
        color: white;
        padding: 3px 10px;
        font-size: 13px;
        border-radius: 4px;
        display: inline-block;
    }

    .label-warning {
        background-color: #FFB300;
        color: white;
        padding: 3px 10px;
        font-size: 13px;
        border-radius: 4px;
        display: inline-block;
    }

    .label-error {
        background-color: #C62828;
        color: white;
        padding: 3px 10px;
        font-size: 13px;
        border-radius: 4px;
        display: inline-block;
    }
    
    /* === Global Modal === */
    .modal {
        display: none;
        position: fixed;
        z-index: 9999;
        padding-top: 100px;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0,0,0,0.4);
    }

    .modal-content {
        background-color: #fefefe;
        margin: auto;
        padding: 20px;
        border: 1px solid #888;
        width: 60%;
        border-radius: 10px;
        animation-name: animatetop;
        animation-duration: 0.4s;
    }

    @keyframes animatetop {
        from {top:-300px; opacity:0}
        to {top:0; opacity:1}
    }

    .close {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
    }

    .close:hover,
    .close:focus {
        color: black;
        text-decoration: none;
        cursor: pointer;
    }

    /* === Animated Spinner === */
    .lds-ring {
        display: inline-block;
        position: relative;
        width: 64px;
        height: 64px;
    }

    .lds-ring div {
        box-sizing: border-box;
        display: block;
        position: absolute;
        width: 51px;
        height: 51px;
        margin: 6px;
        border: 6px solid #4CAF50;
        border-radius: 50%;
        animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
        border-color: #4CAF50 transparent transparent transparent;
    }

    .lds-ring div:nth-child(1) {
        animation-delay: -0.45s;
    }

    .lds-ring div:nth-child(2) {
        animation-delay: -0.3s;
    }

    .lds-ring div:nth-child(3) {
        animation-delay: -0.15s;
    }

    @keyframes lds-ring {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }

    /* === Mobile Responsive Adjustments === */
    @media screen and (max-width: 768px) {
        .main-title {
            font-size: 26px;
            padding: 15px;
        }

        .section-header {
            font-size: 20px;
        }

        .timeline-item, .timeline::after {
            left: 20px !important;
        }

        .timeline-item {
            width: 90% !important;
            padding-left: 20px !important;
        }
    }

    /* === Fade Button Entry === */
    .fade-in-button {
        animation: fadeInBtn 1.2s ease-in;
    }

    @keyframes fadeInBtn {
        0% {opacity: 0; transform: translateY(20px);}
        100% {opacity: 1; transform: translateY(0);}
    }
            /* === GLOBAL STYLES (Light/Dark Toggle + More) === */
    :root {
        --bg-light: #f3f6f4;
        --bg-dark: #1e1e1e;
        --text-light: #2E7D32;
        --text-dark: #ffffff;
        --accent: #4CAF50;
    }

    body.light-mode {
        background-color: var(--bg-light);
        color: var(--text-light);
    }

    body.dark-mode {
        background-color: var(--bg-dark);
        color: var(--text-dark);
    }

    .main-title, .section-header {
        transition: all 0.4s ease-in-out;
    }

    .mode-toggle {
        position: fixed;
        top: 20px;
        right: 30px;
        background-color: var(--accent);
        color: Black;
        padding: 10px 16px;
        border-radius: 20px;
        font-size: 14px;
        cursor: pointer;
        z-index: 100;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    }

    .mode-toggle:hover {
        background-color: #388Y9C;
        align-items: center;
        justify-content: center;
    }

    /* === Login Form Styling === */
    .login-form {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        margin-top: 50px;
    }

    .login-form input {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #4CAF50;
        border-radius: 8px;
    }

    .login-form button {
        width: 100%;
        padding: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-weight: bold;
    }

    .login-form button:hover {
        background-color: #388E3C;
    }

    /* === Sidebar Enhancements === */
    .block-container .sidebar-content {
        background-color: #E8F5E9;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #C8E6C9;
        margin-top: 10px;
        animation: fadeInSidebar 1s ease-in-out;
    }

    @keyframes fadeInSidebar {
        from {opacity: 0; transform: translateX(-10px);}
        to {opacity: 1; transform: translateX(0);}
    }

    .sidebar-content h2, .sidebar-content h3 {
        color: #2E7D32;
    }

    /* === Tooltip Styling === */
    .tooltip {
        position: relative;
        display: inline-block;
    }

    .tooltip .tooltiptext {
        visibility: hidden;
        width: 160px;
        background-color: #4CAF50;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 6px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -80px;
        opacity: 0;
        transition: opacity 0.3s;
    }

    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    </style>
""", unsafe_allow_html=True)
# ======================= Dark Mode Toggle =======================
# Dark Mode Toggle
dark_mode = st.sidebar.toggle("🌗 Toggle Dark Mode", value=False)
st.markdown('<div class="mode-toggle" onclick="document.body.classList.toggle(\'dark-mode\')">🌓 Toggle Mode</div>', unsafe_allow_html=True)
if dark_mode:
    st.markdown("""
        <style>
        html, body, [class*="css"] {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        .main-title, .section-header {
            color: #ffffff;
        }
        .stButton>button {
            background-color: #555 !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        html, body, [class*="css"] {
            background-color: #f3f6f4;
            color: #2E7D32;
        }
        </style>
    """, unsafe_allow_html=True)


# ======================= User Login =======================
logged_in, username = login()
if not logged_in:
    st.stop()

# ======================= Navigation Bar =======================
st.markdown('<div class="main-title">🚀 AWS Automation Dashboard</div>', unsafe_allow_html=True)

st.sidebar.image("https://tse4.mm.bing.net/th/id/OIP.DLBFfleSngfziGnJZmJDtAHaHa?w=626&h=626&rs=1&pid=ImgDetMain&o=7&rm=3", width=150)
st.sidebar.markdown(f"### 👋 Welcome, {username}")

selected_page = st.sidebar.selectbox("📂 Navigate to", ["🏠 Home", "📖 Guidelines", "🧠 Project Applications"])

# ======================= Page: Home =======================
if selected_page == "🏠 Home":
    tab1, tab2, tab3 = st.tabs(["🖥️ EC2", "🛢️ RDS", "🗂️ S3"])

    with tab1:
        st.markdown('<div class="section-header">EC2 Instance Management 🖥️</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🚀 Launch EC2 Instance"):
                st.success(create_ec2_instance())
        with col2:
            instance_id = st.text_input("Enter EC2 Instance ID to delete: ex. i-1234567890abcdef0", placeholder="i-xxxxxxxxxxxxxxxxx")
            if st.button("❌ Terminate EC2 Instance"):
                if instance_id:
                    result = delete_ec2_instance(instance_id)
                    if result:
                        st.success(f"✅ Terminated: {instance_id}")
                    else:
                        st.error("❌ Failed to terminate instance.")
                else:
                    st.warning("⚠️ Please enter a valid instance ID.")

    with tab2:
        st.markdown('<div class="section-header">RDS Service Management 🛢️ (after each task it will take 5 minutes of time)</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📦 Create RDS Instance:"):
                st.success(create_rds_instance())
            if st.button("🗑️ Delete RDS Instance"):
                st.success(delete_rds_instance())
        with col2:
            if st.button("📸 Create Snapshot"):
                st.success(create_snapshot())
            db_class = st.selectbox("Modify DB Size", ["db.t3.small", "db.t3.medium", "db.t3.micro"])
            if st.button("⚙️ Modify DB Instance"):
                st.success(modify_rds_instance(db_class))
        with col3:
            if st.button("🔁 Restore from Snapshot"):
                st.success(restore_from_snapshot())

    with tab3:
        st.markdown('<div class="section-header">📁 Upload Files to S3 Bucket (only for existing s3buckets)</div>', unsafe_allow_html=True)
        bucket = st.text_input(" **Enter S3 Bucket Name:** (ex. mys3-bucket-2025-automation-with-boto3)")
        file = st.file_uploader("📁 Choose a File")
        if st.button("⬆️ Upload to S3"):
            if file and bucket:
                with open(file.name, "wb") as f:
                    f.write(file.getbuffer())
                st.success(upload_to_s3(bucket, file.name))
            else:
                st.warning("⚠️ File and bucket name required.")

# ======================= Page: Guidelines =======================
elif selected_page == "📖 Guidelines":
    st.markdown("## 📖 Guidelines - How to Use This Web App")
    st.markdown("---")
    st.markdown("""
    Welcome to the **AWS Automation Dashboard** 👋  
    This tool helps you manage essential AWS services (EC2, RDS, S3) through a user-friendly interface.

    ---

    ### 🧾 Prerequisites
    - ✅ You must have a valid AWS account.
    - ✅ IAM credentials with permissions for EC2, RDS, and S3.
    - ✅ `.env` file set up with `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_DEFAULT_REGION`.

    ---

    ### 🔐 Step 1: Login
    - Enter your **username and password** in the sidebar.
    - On successful login, you’ll be redirected to the main dashboard.

    ---

    ### 🧭 Step 2: Navigate Sections
    Use the left sidebar menu to explore:
    - 🏠 Home (Main EC2, RDS, and S3 interface)
    - 📖 Guidelines (This help section)
    - 🧠 Project Applications (Use cases for this tool)

    ---

    ### 🖥️ EC2 (Elastic Compute Cloud)
    - **Launch EC2 Instance**: Automatically creates a t2.micro instance with pre-configured settings.
    - **Terminate Instance**: Requires you to input the instance ID (e.g., `i-xxxxxxxxxxxxxxxxx`) to delete.

    **💡 Tip**: Use AWS Console or CLI to get the instance ID if needed.

    ---

    ### 🛢️ RDS (Relational Database Service)
    - **Create DB Instance**: Launches a MySQL instance.
    - **Delete DB Instance**: Removes the running database.
    - **Create Snapshot**: Takes a backup (snapshot) of the RDS instance.
    - **Modify DB Class**: Upgrade/downgrade database size (e.g., t3.micro → t3.medium).
    - **Restore Snapshot**: Recreate DB from snapshot if needed.

    **⚠️ Note**: Some changes may take a few minutes due to AWS provisioning time.

    ---

    ### 🗂️ S3 (Simple Storage Service)
    - **Upload Files**: Choose an existing S3 bucket and upload any file from your computer.
    - Use this for storing:
      - Images
      - PDFs or Docs
      - Backups
      - Dataset files

    ---

    ### 🛡️ Best Practices
    - Always delete unused instances to avoid charges.
    - Store IAM credentials securely and never push them to GitHub.
    - Periodically create RDS snapshots if working on a live DB.

    ---

    📌 *This dashboard simplifies repetitive cloud management tasks and enhances learning and development experience.*
    """)

# ======================= Page: Project Applications =======================
elif selected_page == "🧠 Project Applications":
    st.markdown("## 🧠 Project Applications - Where This Web App Can Be Used")
    st.markdown("---")
    st.markdown("""
    The **AWS Automation Dashboard** is a powerful platform that integrates multiple AWS services into one web interface. Below are areas where it can be applied effectively.

    ---

    ### 🎓 Academic Applications

    - ✅ **Face Recognition Attendance Systems**
      - Upload face datasets to S3
      - Use AWS Rekognition to match and log
      - Store attendance logs in RDS

    - ✅ **Deploying Machine Learning Projects**
      - Host ML model APIs (Flask, FastAPI) on EC2
      - Store inference results or logs in RDS

    - ✅ **Database Projects**
      - Build relational DB-backed applications
      - Connect external apps to your RDS MySQL DB

    - ✅ **Cloud-Based Data Pipelines**
      - Automate data collection, backup and snapshot using RDS
      - Visualize input/output files via S3 dashboard

    ---

    ### 🏢 Industry / Enterprise Use

    - ✅ **Automated Cloud Backup Solutions**
      - Daily/Weekly snapshots of RDS DBs
      - Restore in case of crash/failure

    - ✅ **Dev/Test Environments on EC2**
      - Quickly create/terminate test servers
      - Ideal for QA teams and internal testing

    - ✅ **S3 File-Based Applications**
      - Store design assets, reports, or code archives
      - Use versioning, permissions via AWS Console if needed

    - ✅ **Team-Based Infrastructure Management**
      - Multiple teams can share dashboard access
      - Ideal for startups and mid-sized cloud projects

    ---

    ### 🧑‍💻 Developer & Learner Use Cases

    - ✅ **AWS Certification Preparation**
      - Practice Boto3 scripting without CLI
      - Understand IAM, EC2, S3, RDS relationships

    - ✅ **Cloud Automation Projects**
      - Build and deploy serverless/automated tasks
      - Integrate with CI/CD pipelines for cloud workflows

    - ✅ **Portfolio Projects**
      - Showcase how to deploy apps using EC2
      - Display DB design, snapshot recovery in RDS

    - ✅ **Hackathons / Cloud Bootcamps**
      - Rapid development with minimal AWS Console usage

    ---

    🔧 *This tool supports learners, professionals, and teams aiming to build scalable and manageable cloud-based applications efficiently.*
    """)
# ======================= Footer =======================
st.markdown("---")
st.markdown("""
    © 2025 AWS Automation with Boto3. All rights reserved for educational purposes.
""")
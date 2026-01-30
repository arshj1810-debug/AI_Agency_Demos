import streamlit as st
import csv
import pandas as pd
import os
from datetime import datetime

# ------------------------------
# Page Setup
# ------------------------------
st.set_page_config(page_title="AI Lead Capture System", page_icon="📋")

st.title("📋 AI Lead Capture System")
st.markdown("Powered by **AI Automation Agency**")
st.markdown("Enter your details below — our team will contact you shortly.")

file_name = "leads.csv"

# ------------------------------
# Create CSV if not exists
# ------------------------------
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Full Name", "Email", "Phone", "Business"])

# ------------------------------
# Lead Form
# ------------------------------
with st.form("lead_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    business = st.text_input("Business Type")

    submitted = st.form_submit_button("Submit Lead")

    if submitted:
        # Validation
        if not name or not email or not phone:
            st.error("❌ Please fill all required fields.")
        elif "@" not in email:
            st.error("❌ Enter a valid email address.")
        elif len(phone) < 10:
            st.error("❌ Enter a valid phone number.")
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(file_name, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, name, email, phone, business])

            st.success(f"✅ Thank you {name}! Our team will contact you soon.")

# ------------------------------
# Secure Admin Panel (PRIVATE)
# ------------------------------
st.markdown("---")
st.markdown("### 🔒 Admin Login")

admin_pass = st.text_input("Enter Admin Password", type="password")

if admin_pass == "agency@123":  # Change later for security
    st.success("Admin Access Granted")

    df = pd.read_csv(file_name)

    st.markdown("### 📊 All Leads (Private CRM View)")
    st.dataframe(df, use_container_width=True)

    st.download_button(
        "📥 Download Leads CSV",
        data=df.to_csv(index=False),
        file_name="leads_export.csv"
    )


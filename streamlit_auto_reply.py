import streamlit as st
import random

st.set_page_config(page_title="AI Auto-Reply Bot")
st.title("💬 AI Instagram / WhatsApp Auto-Reply Bot")
st.markdown("Powered by **AI Automation Agency**")
st.markdown("Simulating real Instagram / WhatsApp business replies")

# Smart reply database
auto_replies = {
    "price": [
        "Our plans start at ₹999/month with full AI automation. Want a free demo?",
        "Pricing starts from ₹999/month — affordable & powerful. Want details?",
        "We offer budget-friendly AI automation starting ₹999/month. Interested?"
    ],
    "demo": [
        "We’d love to schedule a demo! What time works best for you?",
        "Sure — want the demo today or tomorrow?",
        "Let’s set up your free demo. Tell me your preferred time."
    ],
    "services": [
        "We automate customer replies, lead capture, and sales using AI.",
        "Our services include auto-reply bots, lead capture, and sales automation.",
        "We help businesses grow with AI customer support and automation."
    ],
    "hello": [
        "Hey! Thanks for messaging us 😊 How can we help today?",
        "Hi there! Welcome — how can we assist your business?",
        "Hello! Want to see how AI can automate your customer replies?"
    ],
    "yes": [
        "Great! Want me to schedule a free demo for you?",
        "Awesome — let’s book your demo. What time suits you?",
        "Perfect! When should we show you the demo?"
    ],
    "time": [
        "Got it! Our team will confirm your demo shortly.",
        "Demo scheduled — we’ll send you details soon.",
        "Awesome! We’ll lock in that demo time for you."
    ]
}

default_replies = [
    "Thanks for reaching out! Want a free demo?",
    "Happy to help 😊 What are you looking for?",
    "Tell me a little about your business, and I’ll guide you.",
    "We help businesses automate customer replies — want to try a demo?",
    "Would you like us to set up a free trial?"
]

# Save chat history
if "history" not in st.session_state:
    st.session_state.history = []

if "last_reply" not in st.session_state:
    st.session_state.last_reply = ""

# Chat input (Enter works)
user_msg = st.chat_input("Type your message and press Enter")

if user_msg:
    st.session_state.history.append(("Customer", user_msg))

    msg_lower = user_msg.lower()
    reply_list = None

    # Detect keywords
    for keyword, replies in auto_replies.items():
        if keyword in msg_lower:
            reply_list = replies
            break

    if not reply_list:
        reply_list = default_replies

    # Prevent repeating same reply
    reply = random.choice(reply_list)
    while reply == st.session_state.last_reply:
        reply = random.choice(reply_list)

    st.session_state.last_reply = reply
    st.session_state.history.append(("AI", reply))

# Display chat
for role, msg in st.session_state.history:
    if role == "Customer":
        st.markdown(f"**👤 Customer:** {msg}")
    else:
        st.markdown(f"**🤖 AI:** {msg}")


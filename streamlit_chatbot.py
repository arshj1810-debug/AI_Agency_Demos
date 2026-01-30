import streamlit as st
import subprocess
import re

st.set_page_config(page_title="AI Customer Support Bot", page_icon="🤖")

st.title("🤖 AI Customer Support Bot")
st.markdown("Powered by **AI Automation Agency**")
st.markdown("Ask about pricing, demos, services, or automation.")

# ---------------------------
# Session Memory
# ---------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "demo_booked" not in st.session_state:
    st.session_state.demo_booked = False

# ---------------------------
# System Prompt
# ---------------------------
SYSTEM_PROMPT = """
You are a fast, professional AI sales assistant for an automation agency.

Tone:
- Friendly
- Clear
- Confident
- Business-focused

Rules:
- Keep replies under 3 lines
- Never repeat previous answers
- Push demo bookings when relevant
- Sound human and helpful
- If demo booked, confirm politely
"""

# ---------------------------
# Chat Input
# ---------------------------
user_input = st.chat_input("Type your message and press Enter...")

if user_input:
    st.session_state.history.append(f"Customer: {user_input}")

    # Keep memory short (FAST MODE)
    memory_context = "\n".join(st.session_state.history[-4:])

    # ---------------------------
    # DEMO BOOKING LOGIC
    # ---------------------------
    demo_keywords = ["demo", "book", "schedule", "meeting"]

    if any(word in user_input.lower() for word in demo_keywords):
        if not st.session_state.demo_booked:
            bot_reply = (
                "✅ Demo booked successfully!\n\n"
                "Our team will contact you shortly to confirm time.\n"
                "Excited to show you how AI can grow your business 🚀"
            )
            st.session_state.demo_booked = True
        else:
            bot_reply = (
                "📅 Your demo is already scheduled.\n"
                "Looking forward to speaking with you soon!"
            )

    else:
        # ---------------------------
        # AI RESPONSE ENGINE
        # ---------------------------
        prompt = f"""
{SYSTEM_PROMPT}

Conversation History:
{memory_context}

Customer: {user_input}
Reply as AI sales assistant:
"""

        result = subprocess.run(
            ["ollama", "run", "llama3", prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8"
        )

        bot_reply = result.stdout.strip()

        # Clean formatting
        bot_reply = re.sub(r"\n{3,}", "\n", bot_reply)
        bot_reply = bot_reply[:500]

    st.session_state.history.append(f"AI: {bot_reply}")

# ---------------------------
# DISPLAY CHAT UI
# ---------------------------
for msg in st.session_state.history:
    if msg.startswith("Customer:"):
        st.markdown(f"👤 **{msg.replace('Customer:', '').strip()}**")
    else:
        st.markdown(f"🤖 **{msg.replace('AI:', '').strip()}**")


import streamlit as st
import json
import anthropic
import os

# =========================
# 🔑 Claude API Key (from Streamlit secrets or local env)
# =========================
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# =========================
# 📚 Load Knowledge Base
# =========================
with open("it_helpdesk.json") as f:
    data = json.load(f)

# =========================
# 🎯 Page Setup
# =========================
st.set_page_config(page_title="AI IT Helpdesk", layout="centered")

st.title("🤖 AI IT Helpdesk Assistant")
st.write("Get instant help for common IT issues")

# =========================
# 🔍 SMART Matching Function
# =========================
def find_solution(query):
    query = query.lower()

    for item in data:
        # Match exact issue
        if item["issue"] in query:
            return item

        # Match keywords
        for keyword in item.get("keywords", []):
            if keyword in query:
                return item

    return None

# =========================
# 🧠 Claude AI Response
# =========================
def claude_response(query, context):
    try:
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=300,
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    You are a helpful IT helpdesk assistant.

                    User issue: {query}

                    Known solution: {context}

                    Give a clear, step-by-step answer in simple language.
                    """
                }
            ]
        )
        return message.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"

# =========================
# 🔽 Dropdown + Manual Input
# =========================
st.subheader("📌 Select or Describe Your Issue")

options = [
    "Select an issue",
    "WiFi not connecting",
    "VPN not working",
    "Password reset",
    "Laptop slow",
    "Email not syncing",
    "Software not installing",
    "Printer not working",
    "System not booting",
    "Other (type manually)"
]

selected_issue = st.selectbox("Choose your issue:", options)

query = None

if selected_issue != "Select an issue" and selected_issue != "Other (type manually)":
    query = selected_issue.lower()

elif selected_issue == "Other (type manually)":
    query = st.text_input("Describe your issue:")

# =========================
# 🤖 Chatbot Logic
# =========================
if query:
    result = find_solution(query)

    if result:
        st.info(f"✅ Category: {result.get('category', 'General')}")
        answer = claude_response(query, result["solution"])
        st.success(answer)
    else:
        st.info("⚠️ No exact match found. Using AI...")
        answer = claude_response(query, "General IT troubleshooting steps")
        st.warning(answer)

# =========================
# 🎟️ Ticket Option
# =========================
if st.button("📩Assistance"):
    st.success("Kindly contact the IT agent.")

# =========================
# 📌 Sidebar
# =========================
st.sidebar.title("🛠️ Helpdesk Menu")
st.sidebar.write("""
**Categories:**
- Network  
- System  
- Email  
- Software  
- Hardware  

**Tips:**
- Use dropdown for quick help  
- Use manual input for custom issues  
""")
